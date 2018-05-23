# coding: utf-8
from domain.entities import ImportStatistics
from domain.interfaces import IUserNotificationService


class MockNotificationService(IUserNotificationService):

    def send_import_result_notification(self, statistics: ImportStatistics):
        pass
