# coding: utf-8
from typing import List

from domain.constants import ResponsesTypesEnum, LinkSourceEnum
from domain.entities import Link


class SuccessResponse:

    def get_type(self) -> ResponsesTypesEnum:
        return ResponsesTypesEnum.SUCCESS


class AddLinksResponse(SuccessResponse):

    def __init__(self, count_of_added: int) -> None:
        self.count_of_added = count_of_added


class FindByTagResponse(SuccessResponse):

    def __init__(self, links: List[Link]) -> None:
        self.links = links


class ImportLinksResponse(SuccessResponse):

    def __init__(self, count: int, source: LinkSourceEnum) -> None:
        self.count = count
        self.source = source
