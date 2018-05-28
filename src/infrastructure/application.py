# coding: utf-8
import fire

from domain.usecases.find_by_tag import FindByTagUseCase
from domain.usecases.import_links import ImportLinksUseCase
from infrastructure.cli.cli_app import CLI

from infrastructure.config.base import EnvironmentConfig
from infrastructure.db.mock.daos import MockLinksDAO, MockImportStatisticsDAO
from infrastructure.db.mongoengine.storage import Storage
from infrastructure.external.pocket.service import PocketLinkSource
from infrastructure.services.notification import MockNotificationService


class Toshokan:

    def __init__(self):

        self.config = EnvironmentConfig()

        # self.links_dao = MockLinksDAO()
        # self.statistics_dao = MockImportStatisticsDAO()

        self.storage = Storage(self.config.MONGO_DB_NAME, self.config.MONGO_URI)
        self.links_dao = self.storage.links_dao
        self.statistics_dao = self.storage.import_statistics_dao

        self.notification_service = MockNotificationService()

        self.pocket_source = PocketLinkSource(
            self.config.POCKET_CONSUMER_KEY, self.config.POCKET_ACCESS_TOKEN
        )

        self.import_from_pocket_usecase = ImportLinksUseCase(
            links_dao=self.links_dao,
            link_source=self.pocket_source,
            statistics_dao=self.statistics_dao,
            user_notification_service=self.notification_service,
        )

        self.find_by_tag_usecase = FindByTagUseCase(links_dao=self.links_dao)

        self.cli = CLI(
            import_pocket_use_case=self.import_from_pocket_usecase,
            find_by_tag_use_case=self.find_by_tag_usecase,
        )

    def run_cli(self):
        fire.Fire(self.cli)
