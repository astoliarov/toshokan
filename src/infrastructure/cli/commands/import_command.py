# coding: utf-8
from typing import cast

from domain.constants import ResponsesTypesEnum, LinkSourceEnum
from domain.interfaces import IImportLinksUseCase
from domain.requests import ImportLinksRequest
from domain.responses import ImportLinksResponse


class ImportCommand:

    def __init__(self, usecase: IImportLinksUseCase) -> None:
        self.usecase = usecase

    def execute(self):

        req = ImportLinksRequest(send_results=False)
        resp = self.usecase.execute(req)

        if resp.get_type() != ResponsesTypesEnum.SUCCESS:
            print("Oh no. Something goes wrong")
            return

        resp = cast(ImportLinksResponse, resp)

        if resp.source == LinkSourceEnum.POCKET:
            source = "Pocket"
        else:
            source = "Custom"

        print(f"Import {resp.count} from {source}")

        return
