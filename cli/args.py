from dataclasses import dataclass


@dataclass
class Args:
    command: str
    title: str | None
    content: str | None
    identifier: str | None
    query: str | None