# coding: utf-8
from typing import List, Optional

from domain.constants import LinkSourceEnum
from domain.entities import Link, ImportStatistics
from domain.interfaces import ILinksDAO, IImportStatisticsDAO

from .models import LinkModel, ImportStatisticsModel


class MongoengineLinkDAO(ILinksDAO):

    def find_by_tag(self, tag: str) -> List[Link]:
        entities = []

        models = LinkModel.objects.filter(tag=tag)
        for model in models:
            entities.append(model.to_entity())

        return entities

    def insert_many(self, links: List[Link]) -> None:

        models = []
        for entity in links:
            models.append(LinkModel.from_entity(entity))

        LinkModel.objects.insert(models)


class MongoengineImportStatisticsDAO(IImportStatisticsDAO):

    def insert(self, entity: ImportStatistics) -> None:
        model = ImportStatisticsModel.from_entity(entity)
        model.save()

    def get_last_by_source(self, source: LinkSourceEnum) -> Optional[ImportStatistics]:

        try:
            statistics = ImportStatisticsModel.objects.filter(source=source).order_by('-dt')[0]
            return statistics
        except IndexError:
            return None
