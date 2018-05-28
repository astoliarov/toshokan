# coding: utf-8

import abc
import datetime
from typing import List, Optional

from domain.constants import LinkSourceEnum, ResponsesTypesEnum
from domain.entities import ImportStatistics, Link
from domain.requests import ImportLinksRequest, AddLinksRequest, FindByTagRequest
from domain.responses import FindByTagResponse, ImportLinksResponse, AddLinksResponse


class ILinkSource(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_links(self, since: Optional[datetime.datetime]) -> List[Link]:
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
    def execute(self, req: AddLinksRequest) -> AddLinksResponse:
        pass


class IImportLinksUseCase(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def execute(self, req: ImportLinksRequest) -> ImportLinksResponse:
        pass


class IFindByTagUseCase(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def execute(self, req: FindByTagRequest) -> FindByTagResponse:
        pass
