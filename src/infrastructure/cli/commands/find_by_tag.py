# coding: utf-8
import json
from pprint import pprint

from domain.interfaces import IFindByTagUseCase
from domain.requests import FindByTagRequest


class FindByTagCommand:

    def __init__(self, usecase: IFindByTagUseCase) -> None:
        self.usecase = usecase

    def execute(self, tag: str):

        req = FindByTagRequest(tag=tag)
        resp = self.usecase.execute(req)

        data = []
        for item in resp.links:
            data.append({
                'name': item.name,
                'url': item.url,
                'image_url': item.image_url,
                'internal_id': item.internal_id,
                'tags': item.tags,
                'source': item.source,
            })

        print(f"Results by: {tag}")
        print(json.dumps(data, indent=4, sort_keys=True))
