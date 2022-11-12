from abc import ABC
from typing import Generic, TypeVar

from xformula.runtime.core.context.abc import RuntimeContext
from xformula.syntax.grammar.definitions.abc import Definition, DefinitionType
from xformula.syntax.lexer.tokens.abc import Token

__all__ = [
    "Terminal",
]


T = TypeVar("T")


class Terminal(
    Definition,
    Generic[T],
    ABC,
):
    class Meta(Definition.Meta):

        abstract = True

        atomic = True

        type = DefinitionType.TERMINAL

        transform = "transform_token"

    def transform_token(
        self,
        runtime_context: RuntimeContext,
        token: Token,
    ) -> T:
        raise NotImplementedError(
            f"{self.__class__.__qualname__}.transform_token is not implemented",
        )
