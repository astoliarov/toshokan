# coding: utf-8
from mongoengine import connect

from .dao import MongoengineLinkDAO, MongoengineImportStatisticsDAO


CONNECTION_TIMEOUT = 5000
SERVER_SELECTION_TIMEOUT = 5000


class Storage:

    def __init__(self, db_name: str, mongo_uri: str) -> None:

        self.mongo_conn = connect(
            db_name,
            host=mongo_uri,
            connecttimeoutms=CONNECTION_TIMEOUT,
            serverselectiontimeoutms=SERVER_SELECTION_TIMEOUT,
        )

        self.links_dao = MongoengineLinkDAO()
        self.import_statistics_dao = MongoengineImportStatisticsDAO()
