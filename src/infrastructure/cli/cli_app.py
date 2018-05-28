# coding: utf-8
from domain.interfaces import IImportLinksUseCase, IFindByTagUseCase
from infrastructure.cli.commands.import_command import ImportCommand
from infrastructure.cli.commands.find_by_tag import FindByTagCommand


class CLI:

    def __init__(self, import_pocket_use_case: IImportLinksUseCase, find_by_tag_use_case: IFindByTagUseCase) -> None:
        self._import_from_pocket_command = ImportCommand(import_pocket_use_case)
        self._find_by_tag_command = FindByTagCommand(find_by_tag_use_case)

    def import_from_pocket(self) -> None:
        self._import_from_pocket_command.execute()

    def find_by_tag(self, tag: str) -> None:
        self._find_by_tag_command.execute(tag)

