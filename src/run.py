# coding: utf-8
import datetime

from infrastructure.application import Toshokan
from infrastructure.db.mock.daos import MockLinksDAO
from infrastructure.external.pocket.service import PocketLinkSource

if __name__ == "__main__":
    toshokan = Toshokan()
    toshokan.run_cli()
