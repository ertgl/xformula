import dataclasses

from xformula.syntax.ast.nodes import Literal

__all__ = [
    "Complex",
]


@dataclasses.dataclass()
class Complex(
    Literal[complex],
):

    value: complex = dataclasses.field(
        kw_only=True,
        default=complex(),
    )
