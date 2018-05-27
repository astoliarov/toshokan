# coding: utf-8
import datetime
import time
from typing import Optional, Dict, Any, List

import pocket

from domain.constants import LinkSourceEnum
from domain.entities import ImportStatistics, Link
from domain.interfaces import ILinkSource, ILinksDAO


class PocketLinkSource(ILinkSource):

    def __init__(self, links_dao: ILinksDAO, consumer_key: str, access_token: str) -> None:
        self.links_dao = links_dao
        self.client = pocket.Pocket(consumer_key, access_token)

    def get_source(self) -> LinkSourceEnum:
        return LinkSourceEnum.POCKET

    def get_links(self, since: Optional[datetime.datetime]) -> List[Link]:
        data = self._get_raw_data(since)
        links = []
        for item in data:
            link = self._convert_raw_to_entity(item)
            if not link:
                continue

            links.append(link)

        return links

    def _get_raw_data(self, last_import_dt: Optional[datetime.datetime]) -> List[Dict[str, Any]]:
        since = time.mktime(last_import_dt.timetuple()) if last_import_dt else None
        data = self.client.get(detailType="complete", since=since)
        return [value for _, value in data[0]["list"].items()]

    def _convert_raw_to_entity(self, data: Dict[str, Any]) -> Optional[Link]:
        source = self.get_source()
        internal_id = Link.generate_id(source, data["item_id"])

        if data.get("tags"):
            tags = list(data["tags"].keys())
        else:
            tags = []

        resolved_url = data.get("resolved_url", "")
        if not resolved_url:
            return None

        return Link(
            internal_id=internal_id,
            url=data["resolved_url"],
            image_url=data.get("top_image_url", ""),
            tags=tags,
            source=self.get_source(),
            name=data["resolved_title"],
        )
