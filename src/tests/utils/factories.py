# coding: utf-8
import datetime

import factory
import faker

from domain.constants import LinkSourceEnum
from domain.entities import Link, ImportStatistics

fake = faker.Faker()


class LinkFactory(factory.Factory):

    class Meta:
        model = Link

    internal_id = '0__test'
    url = factory.lazy_attribute(lambda o: fake.url(schemes=None))
    image_url = factory.lazy_attribute(lambda o: fake.url(schemes=None))
    name = factory.lazy_attribute(lambda o: fake.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None))
    tags = ['test', 'test2']
    source = LinkSourceEnum.POCKET


class ImportStatisticsFactory(factory.Factory):

    class Meta:
        model = ImportStatistics

    source = LinkSourceEnum.POCKET
    count = 10
    dt = factory.lazy_attribute(lambda o: datetime.datetime.now())
