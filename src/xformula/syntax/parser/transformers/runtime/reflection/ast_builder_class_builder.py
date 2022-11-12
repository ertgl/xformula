from itertools import chain
from typing import Any, Callable, Concatenate, Optional, ParamSpec, TypeVar, cast

from lark import v_args

from xformula.arch.runtime.reflection import ClassBuilder
from xformula.runtime.core.context.abc import RuntimeContext
from xformula.syntax.core.context.abc import SyntaxContext
from xformula.syntax.parser.transformers.abc import ASTBuilderProtocol

__all__ = [
    "ASTBuilderClassBuilder",
]


P = ParamSpec("P")

R = TypeVar("R")


class ASTBuilderClassBuilder(
    ClassBuilder[ASTBuilderProtocol],
):
    @classmethod
    def get_name(
        cls,
        *args: Any,
        **kwargs: Any,
    ) -> str:
        return "ASTBuilder"

    @classmethod
    def get_bases(
        cls,
        *args: Any,
        **kwargs: Any,
    ) -> tuple[type, ...]:
        return (ASTBuilderProtocol,)

    @classmethod
    def get_namespace(
        cls,
        syntax_context: SyntaxContext,
        runtime_context: RuntimeContext,
        *args: Any,
        **kwargs: Any,
    ) -> dict[str, Any]:
        namespace: dict[str, Any] = dict()
        definitions = chain(
            chain(
                syntax_context.non_terminals,
                syntax_context.terminals,
            ),
        )
        for definition in definitions:
            transformer_function: Optional[Callable]
            if isinstance(definition.__class__.options.transform, str):
                transformer_function = getattr(
                    definition,
                    definition.__class__.options.transform,
                    None,
                )
            else:
                transformer_function = definition.__class__.options.transform
            if not callable(transformer_function):
                raise RuntimeError(
                    f"invalid transformer function:"
                    f" {definition.__class__.__qualname__}.{transformer_function!r}"
                    " is not a callable"
                )
            delegate = cls.build_transformer_function_delegator(
                runtime_context,
                definition.__class__.options.definition_name,
                transformer_function,
            )
            namespace[definition.__class__.options.definition_name] = delegate
        return namespace

    @classmethod
    def build_transformer_function_delegator(
        cls,
        runtime_context: RuntimeContext,
        transformer_function_name: str,
        transformer_function: Callable[Concatenate[RuntimeContext, P], R],
    ) -> Callable[Concatenate[ASTBuilderProtocol, P], R]:
        def delegate(
            transformer: ASTBuilderProtocol,
            *args: P.args,
            **kwargs: P.kwargs,
        ) -> R:
            return transformer_function(runtime_context, *args, **kwargs)

        delegate.__name__ = transformer_function_name

        return delegate

    @classmethod
    def build(
        cls,
        syntax_context: SyntaxContext,
        runtime_context: RuntimeContext,
        *args: Any,
        **kwargs: Any,
    ) -> type[ASTBuilderProtocol]:
        built_type = super(ASTBuilderClassBuilder, cls).build(
            syntax_context,
            runtime_context,
            *args,
            **kwargs,
        )
        v_args_kwargs = kwargs.get(
            "v_args_kwargs",
            dict(
                tree=True,
            ),
        )
        if v_args_kwargs:
            built_type = cast(
                type[ASTBuilderProtocol],
                v_args(**v_args_kwargs)(built_type),
            )
        return built_type
