# coding: utf-8

import abc

from domain.constants import LinkSourceEnum
from domain.entities import ImportStatistics


class ILinkSource(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def import_links(self, last_statistics: ImportStatistics) -> ImportStatistics:
        pass

    @abc.abstractmethod
    def get_source(self) -> LinkSourceEnum:
        pass


class IImportStatisticsDAO(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def insert(self, statistics: ImportStatistics):
        pass

    @abc.abstractmethod
    def get_last_by_source(self, source: LinkSourceEnum) -> ImportStatistics:
        pass


class IUserNotificationService(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def send_import_result_notification(self, statistics: ImportStatistics):
        pass
