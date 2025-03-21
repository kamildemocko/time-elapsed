from typing import Protocol
from dataclasses import dataclass


@dataclass(frozen=True)
class DBItem:
    created: float
    title: str
    description: str
    datetime: float
    precise_time: bool
    color: str
    index: int | None

class DBInterface(Protocol):
    def add_item(self, item: DBItem) -> None: ...
    def delete_item(self, index: int) -> None: ...
    def edit_item(self, index: int) -> None: ...
    def get_all_items(self) -> list[DBItem]: ...
