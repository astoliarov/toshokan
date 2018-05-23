# coding: utf-8

import abc
import datetime
from typing import List, Optional

from domain.constants import LinkSourceEnum, ResponsesTypesEnum
from domain.entities import ImportStatistics, Link
from domain.requests import ImportLinksRequest, AddLinksRequest, FindByTagRequest


class ILinkSource(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_and_store_links_since(self, last_import_dt: Optional[datetime.datetime]) -> ImportStatistics:
        pass

    @abc.abstractmethod
    def get_source(self) -> LinkSourceEnum:
        pass


class ILinksDAO(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def insert_many(self, links: List[Link]) -> None:
        pass

    @abc.abstractmethod
    def find_by_tag(self, tag: str) -> List[Link]:
        pass


class IImportStatisticsDAO(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def insert(self, statistics: ImportStatistics) -> None:
        pass

    @abc.abstractmethod
    def get_last_by_source(self, source: LinkSourceEnum) -> Optional[ImportStatistics]:
        pass


class IUserNotificationService(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def send_import_result_notification(self, statistics: ImportStatistics):
        pass


class IResponse(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_type(self) -> ResponsesTypesEnum:
        pass


class IAddLinksUseCase(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def execute(self, req: AddLinksRequest) -> IResponse:
        pass


class IImportLinksUseCase(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def execute(self, req: ImportLinksRequest) -> None:
        pass


class IFindByTagUseCase(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def execute(self, req: FindByTagRequest) -> IResponse:
        pass
