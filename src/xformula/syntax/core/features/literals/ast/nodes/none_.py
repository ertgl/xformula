import dataclasses

from xformula.syntax.ast.nodes import Literal

__all__ = [
    "None_",
]


@dataclasses.dataclass()
class None_(  # NOSONAR
    Literal[None],
):

    value: None = dataclasses.field(
        kw_only=True,
        init=False,
        default=None,
    )
