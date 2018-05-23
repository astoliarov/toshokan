# coding: utf-8
import datetime

from domain.constants import LinkSourceEnum


class ImportStatistics:

    def __init__(self, source: LinkSourceEnum, count: int, dt: datetime.datetime) -> None:
        self.source = source
        self.count = count
        self.dt = dt
