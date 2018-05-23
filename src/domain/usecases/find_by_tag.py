# coding: utf-8
from domain.interfaces import ILinksDAO
from domain.requests import FindByTagRequest
from domain.responses import FindByTagResponse


class FindByTagUseCase:

    def __init__(self, links_dao: ILinksDAO) -> None:
        self.links_dao = links_dao

    def execute(self, req: FindByTagRequest) -> FindByTagResponse:
        links = self.links_dao.find_by_tag(req.tag)
        return FindByTagResponse(links=links)
