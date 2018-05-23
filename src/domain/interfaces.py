# coding: utf-8

import abc
import datetime
from typing import List, Optional

from domain.constants import LinkSourceEnum
from domain.entities import ImportStatistics
from domain.requests import ImportLinksRequest


class ILinkSource(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_and_store_links_since(self, last_import_dt: Optional[datetime.datetime]) -> ImportStatistics:
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


class IImportLinksUseCase(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def execute(self, req: ImportLinksRequest) -> None:
        pass
