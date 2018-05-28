# coding: utf-8
import datetime
from typing import List

from domain.entities import ImportStatistics, Link
from domain.interfaces import (
    ILinkSource,
    IImportStatisticsDAO,
    IUserNotificationService,
    IImportLinksUseCase,
    IResponse,
    ILinksDAO,
)
from domain.requests import ImportLinksRequest
from domain.responses import ImportLinksResponse


class ImportLinksUseCase(IImportLinksUseCase):

    def __init__(
        self,
        link_source: ILinkSource,
        links_dao: ILinksDAO,
        statistics_dao: IImportStatisticsDAO,
        user_notification_service: IUserNotificationService,
    ) -> None:
        self.links_dao = links_dao
        self.links_source = link_source
        self.statistics_dao = statistics_dao
        self.user_notification_service = user_notification_service

    def execute(self, req: ImportLinksRequest) -> IResponse:

        source = self.links_source.get_source()
        last_statistics = self.statistics_dao.get_last_by_source(source)
        last_import_dt = last_statistics.dt if last_statistics else None

        links = self.links_source.get_links(last_import_dt)
        self.links_dao.insert_many(links)

        current_statistics = self.prepare_statistics(links)

        self.statistics_dao.insert(current_statistics)

        if req.send_results:
            self.user_notification_service.send_import_result_notification(current_statistics)

        return ImportLinksResponse(count=current_statistics.count, source=current_statistics.source)

    def prepare_statistics(self, links: List[Link]) -> ImportStatistics:
        return ImportStatistics(
            source=self.links_source.get_source(),
            count=len(links),
            dt=datetime.datetime.now(),
        )
