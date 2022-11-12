from typing import TYPE_CHECKING, Iterable, Protocol, overload, runtime_checkable

if TYPE_CHECKING:
    from xformula.syntax.grammar.definitions.abc.definition import Definition

__all__ = [
    "RegexExpressionBuilderProtocol",
]


@runtime_checkable
class RegexExpressionBuilderProtocol(Protocol):

    _definition: "Definition"

    def __init__(
        self,
        definition: "Definition",
    ) -> None:
        self._definition = definition

    def any_char(self) -> str:
        ...

    def any_char_except(
        self,
        *chars: str,
    ) -> str:
        ...

    def any_char_of(
        self,
        *chars: str,
    ) -> str:
        ...

    def any_of(
        self,
        *expressions: str,
    ) -> str:
        ...

    def bound(
        self,
        *expressions: str,
    ) -> str:
        ...

    def chars_between(
        self,
        lower: str,
        upper: str,
    ) -> str:
        ...

    def escape_char(
        self,
        char: str,
    ) -> str:
        ...

    def flat(
        self,
        *expressions: str,
    ) -> str:
        ...

    def flat_join(
        self,
        separator: str,
        expressions: Iterable[str],
    ) -> str:
        ...

    def flat_one_or_more_of(
        self,
        expression: str,
    ) -> str:
        ...

    def flat_optional(
        self,
        expression: str,
    ) -> str:
        ...

    def flat_zero_or_more_of(
        self,
        expression: str,
    ) -> str:
        ...

    def non_capturing_group(
        self,
        *expressions: str,
    ) -> str:
        ...

    def one_or_more_of(
        self,
        *expressions: str,
    ) -> str:
        ...

    def whitespace(self) -> str:
        ...

    def word(
        self,
        chars: str,
    ) -> str:
        ...

    @overload
    def wrap(
        self,
        outer: str,
        inner: str,
    ) -> str:
        ...

    @overload
    def wrap(
        self,
        left: str,
        right: str,
        inner: str,
    ) -> str:
        ...

    @overload
    def wrap(
        self,
        left: str,
        right: str,
        *inner: str,
    ) -> str:
        ...

    def wrap(
        self,
        *args,
    ):
        ...

    def zero_or_more_of(
        self,
        *expressions: str,
    ) -> str:
        ...
