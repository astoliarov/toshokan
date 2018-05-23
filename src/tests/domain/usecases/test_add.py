# coding: utf-8

from unittest import TestCase, mock

from domain.constants import LinkSourceEnum
from domain.requests import AddLinksRequest
from domain.usecases.add_links import AddLinksUseCase


from tests.utils.factories import LinkFactory


class AddLinksTestCase(TestCase):

    def setUp(self):

        self.links_dao_mock = mock.Mock()
        self.usecase = AddLinksUseCase(links_dao=self.links_dao_mock)

    def test__execute__links_ids_updated(self):
        self.usecase.generate_identifier = mock.Mock()
        self.usecase.generate_identifier.return_value = "test"
        link = LinkFactory()
        link.internal_id = ""

        req = AddLinksRequest(links=[link])
        self.usecase.execute(req)

        self.assertEqual(link.internal_id, f"{LinkSourceEnum.CUSTOM}__test")

    def test__execute__links_inserted(self):
        link = LinkFactory()
        link.internal_id = ""
        links = [link]

        req = AddLinksRequest(links=links)
        self.usecase.execute(req)

        self.links_dao_mock.insert_many.assert_called_once_with(links)
