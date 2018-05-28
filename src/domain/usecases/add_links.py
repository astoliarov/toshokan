# coding: utf-8
import uuid
from typing import List

from domain.constants import LinkSourceEnum
from domain.entities import Link
from domain.requests import AddLinksRequest
from domain.responses import AddLinksResponse

from domain.interfaces import IAddLinksUseCase, ILinksDAO


class AddLinksUseCase(IAddLinksUseCase):

    def __init__(self, links_dao: ILinksDAO) -> None:
        self.links_dao = links_dao

    def execute(self, req: AddLinksRequest) -> AddLinksResponse:

        self.mark_links_as_internal(req.links)
        self.links_dao.insert_many(req.links)

        return AddLinksResponse(count_of_added=len(req.links))

    def generate_identifier(self) -> str:
        return uuid.uuid4().hex

    def mark_links_as_internal(self, links: List[Link]):
        for link in links:
            link.source = LinkSourceEnum.CUSTOM
            link.internal_id = Link.generate_id(link.source, self.generate_identifier())
