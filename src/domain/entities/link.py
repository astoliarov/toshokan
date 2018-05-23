# coding: utf-8
from typing import List, Optional

from domain.constants import LinkSourceEnum


class Link:

    def __init__(
        self, internal_id: Optional[str], url: str, name: str, image_url: str, tags: List[str], source: LinkSourceEnum
    ) -> None:
        self.internal_id = internal_id

        self.url = url
        self.name = name
        self.image_url = image_url
        self.tags = tags

        self.source = source

    @staticmethod
    def generate_id(source: LinkSourceEnum, _id: str) -> str:
        return f"{source}__{_id}"
