import dataclasses
from typing import Any, Callable

from xformula.arch.meta import Options
from xformula.syntax.grammar.definitions.abc.definition_type import DefinitionType

__all__ = [
    "DefinitionOptions",
]


@dataclasses.dataclass()
class DefinitionOptions(Options):

    definition_name: str = dataclasses.field(
        kw_only=True,
        default=str(),
    )

    atomic: bool = dataclasses.field(
        kw_only=True,
        default=False,
    )

    retain_anonymous_literals: bool = dataclasses.field(
        kw_only=True,
        default=False,
    )

    type: DefinitionType = dataclasses.field(
        kw_only=True,
        default=DefinitionType.UNDEFINED,
    )

    arguments: list[str] = dataclasses.field(
        kw_only=True,
        default_factory=list,
    )

    priority: int = dataclasses.field(
        kw_only=True,
        default=int(),
    )

    tags: dict[str, int | float] = dataclasses.field(
        kw_only=True,
        default_factory=dict,
    )

    transform: str | Callable[..., Any] = dataclasses.field(
        kw_only=True,
        default="transform",
    )
