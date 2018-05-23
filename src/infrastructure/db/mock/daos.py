# coding: utf-8
from typing import List, Optional

from domain.constants import LinkSourceEnum
from domain.entities import Link, ImportStatistics
from domain.interfaces import ILinksDAO, IImportStatisticsDAO


class MockLinksDAO(ILinksDAO):

    def insert_many(self, links: List[Link]) -> None:
        pass

    def find_by_tag(self, tag: str) -> List[Link]:
        return []


class MockImportStatisticsDAO(IImportStatisticsDAO):

    def insert(self, statistics: ImportStatistics) -> None:
        pass

    def get_last_by_source(self, source: LinkSourceEnum) -> Optional[ImportStatistics]:
        return None
