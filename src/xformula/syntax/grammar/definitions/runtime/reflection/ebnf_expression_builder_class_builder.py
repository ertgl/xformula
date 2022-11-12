from typing import Any, Callable, Concatenate, ParamSpec, TypeVar

from xformula.arch.runtime.reflection import ClassBuilder
from xformula.syntax.grammar.definitions.abc import EBNFExpressionBuilderProtocol

__all__ = [
    "EBNFExpressionBuilderClassBuilder",
]


P = ParamSpec("P")

R = TypeVar("R")


class EBNFExpressionBuilderClassBuilder(
    ClassBuilder[EBNFExpressionBuilderProtocol],
):
    @classmethod
    def get_name(
        cls,
        *args: Any,
        **kwargs: Any,
    ) -> str:
        return "EBNFExpressionBuilder"

    @classmethod
    def get_bases(
        cls,
        *args: Any,
        **kwargs: Any,
    ) -> tuple[type, ...]:
        return (EBNFExpressionBuilderProtocol,)

    @classmethod
    def get_namespace(
        cls,
        *args: Any,
        **kwargs: Any,
    ) -> dict[str, Any]:
        from xformula.syntax.grammar import ebnf

        namespace: dict[str, Any] = dict()

        for attname in dir(ebnf):
            if attname.startswith("_"):
                continue
            value = getattr(ebnf, attname)
            if not callable(value):
                continue
            delegate = cls.build_ebnf_function_delegator(
                attname,
                value,
            )
            namespace[attname] = delegate

        return namespace

    @classmethod
    def build_ebnf_function_delegator(
        cls,
        ebnf_function_name: str,
        ebnf_function: Callable[P, R],
    ) -> Callable[Concatenate[EBNFExpressionBuilderProtocol, P], R]:
        def delegate(
            protocol: EBNFExpressionBuilderProtocol,
            *args: P.args,
            **kwargs: P.kwargs,
        ) -> R:
            pre_handler_function_name = f"pre_call_ebnf_{ebnf_function_name}"
            pre_handler_function = getattr(protocol, pre_handler_function_name, None)
            post_handler_function_name = f"post_call_ebnf_{ebnf_function_name}"
            post_handler_function = getattr(protocol, post_handler_function_name, None)
            if callable(pre_handler_function):
                args, kwargs = pre_handler_function(args, kwargs)
            result = ebnf_function(*args, **kwargs)
            if callable(post_handler_function):
                post_handler_function(args, kwargs, result)
            return result

        if hasattr(ebnf_function, "__name__"):
            delegate.__name__ = getattr(ebnf_function, "__name__")

        return delegate
