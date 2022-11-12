import re
from typing import cast

from lark import Lark

from xformula.runtime.core.context.abc import RuntimeContext
from xformula.syntax.ast.nodes.abc import Node
from xformula.syntax.core.context import SyntaxContext
from xformula.syntax.core.features import DEFAULT_FEATURE_TYPES, Feature
from xformula.syntax.core.operations import (
    DEFAULT_OPERATOR_PRECEDENCES,
    OperatorPrecedence,
)
from xformula.syntax.grammar.ebnf import document
from xformula.syntax.parser.transformers import ASTBuilderProtocol

__all__ = [
    "Parser",
]


DEBUG = False


class Parser:

    _ebnf_document: str

    _grammar: Lark

    ast_builder: ASTBuilderProtocol

    syntax_context: SyntaxContext

    runtime_context: RuntimeContext

    @classmethod
    def get_default_feature_types(cls) -> list[type[Feature]]:
        return DEFAULT_FEATURE_TYPES

    @classmethod
    def get_default_operator_precedences(cls) -> list[OperatorPrecedence]:
        return DEFAULT_OPERATOR_PRECEDENCES

    def __init__(
        self,
        ast_builder: ASTBuilderProtocol | None = None,
        runtime_context: RuntimeContext | None = None,
        syntax_context: SyntaxContext | None = None,
    ) -> None:
        if runtime_context is None:
            runtime_context = RuntimeContext()
        self.runtime_context = runtime_context
        if syntax_context is None:
            syntax_context = SyntaxContext(
                feature_types=self.__class__.get_default_feature_types(),
                operator_precedences=self.__class__.get_default_operator_precedences(),
            )
        self.syntax_context = syntax_context
        self._ebnf_document = document(syntax_context)
        if DEBUG:
            print("*" * 100)
            print(self._ebnf_document)
            print("*" * 100)
            print()
        self._grammar = Lark(
            self._ebnf_document,
            lexer="contextual",
            parser="lalr",
            g_regex_flags=re.UNICODE | re.IGNORECASE,
            propagate_positions=True,
            maybe_placeholders=False,
        )
        if ast_builder is None:
            ast_builder_class = syntax_context.build_ast_builder_class(runtime_context)
            ast_builder = ast_builder_class()
        self.ast_builder = ast_builder

    @property
    def ebnf_document(self) -> str:
        return self._ebnf_document

    @property
    def grammar(self) -> Lark:
        return self._grammar

    def parse(
        self,
        source: str,
    ) -> Node:
        parse_tree = self.grammar.parse(source)
        ast = cast(Node, self.ast_builder.transform(parse_tree))
        return ast
