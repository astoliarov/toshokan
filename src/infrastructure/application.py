# coding: utf-8
from unittest import mock

from domain.usecases.find_by_tag import FindByTagUseCase
from domain.usecases.import_links import ImportLinksUseCase
from infrastructure.config.base import Config
from infrastructure.db.mock.daos import MockLinksDAO, MockImportStatisticsDAO
from infrastructure.external.pocket.service import PocketLinkSource
from infrastructure.services.notification import MockNotificationService


class Toshokan:

    def __init__(self):

        self.config = Config()

        self.links_dao = MockLinksDAO()
        self.statistics_dao = MockImportStatisticsDAO()

        self.notification_service = MockNotificationService()

        self.pocket_source = PocketLinkSource(
            self.links_dao, self.config.POCKET_CONSUMER_KEY, self.config.POCKET_ACCESS_TOKEN
        )

        self.import_from_pocket_usecase = ImportLinksUseCase(
            link_source=self.pocket_source,
            statistics_dao=self.statistics_dao,
            user_notification_service=self.notification_service,
        )

        self.find_by_tag_usecase = FindByTagUseCase(links_dao=self.links_dao)
