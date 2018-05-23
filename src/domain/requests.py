# coding: utf-8
from typing import List

from domain.entities import Link


class ImportLinksRequest:

    def __init__(self, send_results: bool = False) -> None:
        self.send_results = send_results


class AddLinksRequest:

    def __init__(self, links: List[Link]) -> None:
        self.links = links
