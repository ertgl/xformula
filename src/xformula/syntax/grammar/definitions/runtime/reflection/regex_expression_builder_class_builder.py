from typing import Any, Callable, Concatenate, ParamSpec, TypeVar

from xformula.arch.runtime.reflection import ClassBuilder
from xformula.syntax.grammar.definitions.abc import RegexExpressionBuilderProtocol

__all__ = [
    "RegexExpressionBuilderClassBuilder",
]


P = ParamSpec("P")

R = TypeVar("R")


class RegexExpressionBuilderClassBuilder(
    ClassBuilder[RegexExpressionBuilderProtocol],
):
    @classmethod
    def get_name(
        cls,
        *args: Any,
        **kwargs: Any,
    ) -> str:
        return "RegexExpressionBuilder"

    @classmethod
    def get_bases(
        cls,
        *args: Any,
        **kwargs: Any,
    ) -> tuple[type, ...]:
        return (RegexExpressionBuilderProtocol,)

    @classmethod
    def get_namespace(
        cls,
        *args: Any,
        **kwargs: Any,
    ) -> dict[str, Any]:
        from xformula.syntax.grammar import regex

        namespace: dict[str, Any] = dict()

        for attname in dir(regex):
            if attname.startswith("_"):
                continue
            value = getattr(regex, attname)
            if not callable(value):
                continue
            delegate = cls.build_regex_function_delegator(
                attname,
                value,
            )
            namespace[attname] = delegate

        return namespace

    @classmethod
    def build_regex_function_delegator(
        cls,
        regex_function_name: str,
        regex_function: Callable[P, R],
    ) -> Callable[Concatenate[RegexExpressionBuilderProtocol, P], R]:
        def delegate(
            protocol: RegexExpressionBuilderProtocol,
            *args: P.args,
            **kwargs: P.kwargs,
        ) -> R:
            pre_handler_function_name = f"pre_call_regex_{regex_function_name}"
            pre_handler_function = getattr(protocol, pre_handler_function_name, None)
            post_handler_function_name = f"post_call_regex_{regex_function_name}"
            post_handler_function = getattr(protocol, post_handler_function_name, None)
            if callable(pre_handler_function):
                args, kwargs = pre_handler_function(args, kwargs)
            result = regex_function(*args, **kwargs)
            if callable(post_handler_function):
                post_handler_function(args, kwargs, result)
            return result

        if hasattr(regex_function, "__name__"):
            delegate.__name__ = getattr(regex_function, "__name__")

        return delegate
