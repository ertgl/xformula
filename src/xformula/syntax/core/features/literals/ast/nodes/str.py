import dataclasses

from xformula.syntax.ast.nodes import Literal

__all__ = [
    "Str",
]


@dataclasses.dataclass()
class Str(
    Literal[str],
):

    value: str = dataclasses.field(
        kw_only=True,
        default=str(),
    )
