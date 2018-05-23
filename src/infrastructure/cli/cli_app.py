# coding: utf-8
from domain.interfaces import IImportLinksUseCase
from infrastructure.cli.commands.import_command import ImportCommand


class CLI:

    def __init__(self, import_pocket_use_case: IImportLinksUseCase) -> None:
        self._import_from_pocket_command = ImportCommand(import_pocket_use_case)

    def import_from_pocket(self):
        self._import_from_pocket_command.execute()
