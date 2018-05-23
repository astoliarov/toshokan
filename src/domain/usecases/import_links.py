# coding: utf-8
from domain.interfaces import (
    ILinkSource,
    IImportStatisticsDAO,
    IUserNotificationService,
    IImportLinksUseCase,
    IResponse,
)
from domain.requests import ImportLinksRequest
from domain.responses import ImportLinksResponse


class ImportLinksUseCase(IImportLinksUseCase):

    def __init__(
        self,
        link_source: ILinkSource,
        statistics_dao: IImportStatisticsDAO,
        user_notification_service: IUserNotificationService,
    ) -> None:
        self.links_source = link_source
        self.statistics_dao = statistics_dao
        self.user_notification_service = user_notification_service

    def execute(self, req: ImportLinksRequest) -> IResponse:

        source = self.links_source.get_source()
        last_statistics = self.statistics_dao.get_last_by_source(source)
        last_import_dt = last_statistics.dt if last_statistics else None

        # NOTE: Different link sources (like Pocket or Instapaper) have different API's with different limitations
        # so for now the best way to prepare code for it
        # is to make Interface for this type of services as common as it can be
        # So for now, this services will contain instances of DAO inside
        # and will store data in the most efficient way as they can
        current_statistics = self.links_source.get_and_store_links_since(last_import_dt)

        self.statistics_dao.insert(current_statistics)

        if req.send_results:
            self.user_notification_service.send_import_result_notification(current_statistics)

        return ImportLinksResponse(count=current_statistics.count, source=current_statistics.source)
