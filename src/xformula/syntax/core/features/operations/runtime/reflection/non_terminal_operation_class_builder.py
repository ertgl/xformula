from itertools import chain, repeat
from typing import Any, Callable, Iterable, Literal, Union, cast

from xformula.arch.enumeration import Zip
from xformula.arch.runtime.reflection import ClassBuilder
from xformula.runtime.core.context.abc import RuntimeContext
from xformula.syntax.ast.nodes.abc import Associativity, Operand, Placement
from xformula.syntax.core.features.operations.ast.nodes import (
    Operation,
    Operator,
    Symbol,
)
from xformula.syntax.core.operations.abc import OperatorPrecedence
from xformula.syntax.grammar.non_terminals.abc import NonTerminal
from xformula.syntax.lexer.tokens.abc import Token
from xformula.syntax.parser.trees.abc import ParseTree

__all__ = [
    "NonTerminalOperationClassBuilder",
]


class NonTerminalOperationClassBuilder(
    ClassBuilder[NonTerminal],
):
    @classmethod
    def get_name(
        cls,
        name: str,
        *args: Any,
        **kwargs: Any,
    ) -> str:
        return name

    @classmethod
    def get_bases(
        cls,
        *args: Any,
        **kwargs: Any,
    ) -> tuple[type, ...]:
        return (NonTerminal,)

    @classmethod
    def get_namespace(
        cls,
        name: str,
        operator_precedence: OperatorPrecedence,
        operand: str,
        *args: Any,
        tags: dict[str, int] | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        namespace: dict[str, Any] = dict()

        meta_kwargs = dict(tags=tags) if tags is not None else dict()
        namespace["Meta"] = cls.get_meta_class(operator_precedence, **meta_kwargs)

        namespace["build_grammar"] = cls.get_grammar_builder_function(
            operator_precedence,
            operand,
        )

        namespace["transform_parse_tree"] = cls.get_parse_tree_transformer_function(
            operator_precedence,
            operand,
        )

        return namespace

    @classmethod
    def get_meta_class(
        cls,
        operator_precedence: OperatorPrecedence,
        tags: dict[str, int] | None = None,
    ) -> type:
        if tags is None:
            tags = dict()
        meta_namespace = dict(
            atomic=False,
            priority=operator_precedence.level,
            retain_anonymous_literals=True,
            tags=tags,
        )
        return type("Meta", (), meta_namespace)

    @classmethod
    def cast_zip_join_separator_placement(
        cls,
        placement: Placement,
    ) -> Union[
        Literal[Zip.SeparatorPlacement.LEFT],
        Literal[Zip.SeparatorPlacement.RIGHT],
    ]:
        if placement == Placement.LEFT:
            return Zip.SeparatorPlacement.LEFT
        if placement == Placement.RIGHT:
            return Zip.SeparatorPlacement.RIGHT
        raise TypeError(f"invalid operator placement: {placement!r}")

    @classmethod
    def get_grammar_builder_function(
        cls,
        operator_precedence: OperatorPrecedence,
        operand: str,
    ) -> Callable[[NonTerminal], str]:
        args = (operator_precedence, operand)
        if operator_precedence.arity == 1:
            return cls.get_arity_1_grammar_builder_function(*args)
        return cls.get_arity_n_grammar_builder_function(*args)

    @classmethod
    def get_arity_1_grammar_builder_function(
        cls,
        operator_precedence: OperatorPrecedence,
        operand: str,
    ) -> Callable[[NonTerminal], str]:

        separator_placement = cls.cast_zip_join_separator_placement(
            operator_precedence.placement,
        )

        def build_grammar(self: NonTerminal) -> str:
            recursive_part = self.ebnf.concat(
                chain.from_iterable(
                    Zip.join(
                        [self.ebnf.sym(operator_precedence.symbols[0])],
                        [self.__class__.options.definition_name],
                        separator_placement=separator_placement,
                        default_value="",
                    ),
                ),
            )

            suite = self.ebnf.suite
            define = self.ebnf.define
            orelse = self.ebnf.orelse

            return suite(
                define(recursive_part),
                orelse(operand),
            )

        return build_grammar

    @classmethod
    def get_arity_n_grammar_builder_function(
        cls,
        operator_precedence: OperatorPrecedence,
        operand: str,
    ) -> Callable[[NonTerminal], str]:
        args = (operator_precedence, operand)
        if operator_precedence.associativity == Associativity.LEFT_TO_RIGHT:
            return cls.get_arity_n_ltr_grammar_builder_function(*args)
        if operator_precedence.associativity == Associativity.RIGHT_TO_LEFT:
            return cls.get_arity_n_rtl_grammar_builder_function(*args)
        raise TypeError(
            f"invalid operation associativity: {operator_precedence.associativity!r}"
        )

    @classmethod
    def get_arity_n_ltr_grammar_builder_function(
        cls,
        operator_precedence: OperatorPrecedence,
        operand: str,
    ) -> Callable[[NonTerminal], str]:

        separator_placement = cls.cast_zip_join_separator_placement(
            operator_precedence.placement,
        )

        def build_grammar(self: NonTerminal) -> str:
            left_recursive_part = self.ebnf.concat(
                chain.from_iterable(
                    Zip.join(
                        map(self.ebnf.sym, operator_precedence.symbols),
                        repeat(
                            self.__class__.options.definition_name,
                            times=operator_precedence.arity - 1,
                        ),
                        separator_placement=separator_placement,
                        default_value="",
                    ),
                ),
            )

            define = self.ebnf.define
            optional = self.ebnf.optional

            return define(
                optional(left_recursive_part),
                operand,
            )

        return build_grammar

    @classmethod
    def get_arity_n_rtl_grammar_builder_function(
        cls,
        operator_precedence: OperatorPrecedence,
        operand: str,
    ) -> Callable[[NonTerminal], str]:

        separator_placement = cls.cast_zip_join_separator_placement(
            operator_precedence.placement,
        )

        def build_grammar(self: NonTerminal) -> str:
            left_recursive_part = self.ebnf.concat(
                chain.from_iterable(
                    Zip.join(
                        map(self.ebnf.sym, operator_precedence.symbols),
                        chain(
                            repeat(
                                operand,
                                times=operator_precedence.arity - 2,
                            ),
                            [self.__class__.options.definition_name],
                        ),
                        separator_placement=separator_placement,
                        default_value="",
                    ),
                ),
            )

            define = self.ebnf.define
            optional = self.ebnf.optional

            return define(
                operand,
                optional(left_recursive_part),
            )

        return build_grammar

    @classmethod
    def get_parse_tree_transformer_function(
        cls,
        operator_precedence: OperatorPrecedence,
        operand: str,
    ) -> Callable[[NonTerminal, RuntimeContext, ParseTree], Operation]:
        separator_placement = cls.cast_zip_join_separator_placement(
            operator_precedence.placement,
        )

        if operator_precedence.arity > 1:
            separator_placement = Zip.SeparatorPlacement.RIGHT

        symbol_to_symbol_type_dispatcher = {
            symbol[1]: symbol[0] for symbol in operator_precedence.symbols
        }

        def transform_parse_tree(
            self: NonTerminal,
            runtime_context: RuntimeContext,
            tree: ParseTree,
        ) -> Operation:
            channels = cast(
                tuple[Iterable[Token], Iterable[Operand]],
                Zip.split(
                    cast(Iterable[Token | Operand], tree.children),
                    separator_placement=separator_placement,
                ),
            )
            operator_channel = channels[0]
            operand_channel = channels[1]
            operator = Operator(
                arity=operator_precedence.arity,
                associativity=operator_precedence.associativity,
                placement=operator_precedence.placement,
                precedence_level=operator_precedence.level,
                symbols=[
                    Symbol(
                        type=symbol_to_symbol_type_dispatcher[operator.value],
                        value=operator.value,
                    )
                    for operator in operator_channel
                ],
            )
            return Operation(
                operator=operator,
                operands=cast(list[Operand], list(operand_channel)),
            )

        return transform_parse_tree
