# coding: utf-8
from domain.interfaces import ILinkSource, IImportStatisticsDAO, IUserNotificationService


class ImportDataUseCase:

    def __init__(
        self,
        link_source: ILinkSource,
        statistics_dao: IImportStatisticsDAO,
        user_notification_service: IUserNotificationService,
    ) -> None:
        self.links_source = link_source
        self.statistics_dao = statistics_dao
        self.user_notification_service = user_notification_service

    def execute(self, send_results: bool = True):

        source = self.links_source.get_source()
        last_statistics = self.statistics_dao.get_last_by_source(source)

        current_statistics = self.links_source.import_links(last_statistics)

        self.statistics_dao.insert(current_statistics)

        if send_results:
            self.user_notification_service.send_import_result_notification(current_statistics)
