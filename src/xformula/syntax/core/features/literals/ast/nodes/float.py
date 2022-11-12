import dataclasses

from xformula.syntax.ast.nodes import Literal

__all__ = [
    "Float",
]


@dataclasses.dataclass()
class Float(
    Literal[float],
):

    value: float = dataclasses.field(
        kw_only=True,
        default=float(),
    )
