# coding: utf-8

from mongoengine import DynamicDocument, fields

from domain.entities import Link, ImportStatistics


class LinkModel(DynamicDocument):

    internal_id = fields.StringField(required=True)

    url = fields.StringField()
    name = fields.StringField()
    image_url = fields.StringField()
    tags = fields.ListField(field=fields.StringField())

    source = fields.IntField()

    def to_entity(self) -> Link:
        return Link(
            internal_id=self.internal_id,
            url=self.url,
            name=self.name,
            image_url=self.image_url,
            tags=self.tags,
            source=self.source,
        )

    @classmethod
    def from_entity(cls, entity: Link):
        return LinkModel(
            internal_id=entity.internal_id,
            url=entity.url,
            name=entity.name,
            image_url=entity.image_url,
            tags=entity.tags,
            source=entity.source,
        )


class ImportStatisticsModel(DynamicDocument):
    source = fields.IntField()
    count = fields.IntField()
    dt = fields.DateTimeField()

    def to_entity(self) -> ImportStatistics:
        return ImportStatistics(
            source=self.source,
            count=self.count,
            dt=self.dt,
        )

    @classmethod
    def from_entity(cls, entity: ImportStatistics):
        return ImportStatisticsModel(
            source=entity.source,
            count=entity.count,
            dt=entity.dt,
        )
