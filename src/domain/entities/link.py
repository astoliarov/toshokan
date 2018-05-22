# coding: utf-8
from typing import List, Optional


class Link:

    def __init__(
        self, internal_id: Optional[str], url: str, name: str, image_url: str, tags: List[str], pocket_id: Optional[str]
    ):
        self.internal_id = internal_id

        self.url = url
        self.name = name
        self.image_url = image_url
        self.tags = tags

        self.pocket_id = pocket_id
