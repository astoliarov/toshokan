# coding: utf-8
from domain.constants import ResponsesTypesEnum
from domain.interfaces import IResponse


class SuccessResponse(IResponse):

    def get_type(self) -> ResponsesTypesEnum:
        return ResponsesTypesEnum.SUCCESS


class AddLinksResponse(SuccessResponse):

    def __init__(self, count_of_added: int) -> None:
        self.count_of_added = count_of_added
