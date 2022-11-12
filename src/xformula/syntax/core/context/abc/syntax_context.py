import dataclasses
from functools import partial
from itertools import chain
from typing import TYPE_CHECKING, Optional, TypeVar, cast

from xformula.arch.bisect import Bisect

if TYPE_CHECKING:
    from xformula.runtime.core.context.abc.runtime_context import RuntimeContext
    from xformula.syntax.core.features.abc.feature import Feature
    from xformula.syntax.core.operations.abc.operator_precedence import (
        OperatorPrecedence,
    )
    from xformula.syntax.grammar.definitions.abc.definition import Definition
    from xformula.syntax.grammar.definitions.abc.definition_type import DefinitionType
    from xformula.syntax.grammar.definitions.abc.ebnf_expression_builder_protocol import (
        EBNFExpressionBuilderProtocol,
    )
    from xformula.syntax.grammar.definitions.abc.regex_expression_builder_protocol import (
        RegexExpressionBuilderProtocol,
    )
    from xformula.syntax.grammar.directives.abc.directive import Directive
    from xformula.syntax.grammar.non_terminals.abc.non_terminal import NonTerminal
    from xformula.syntax.grammar.templates.abc.template import Template
    from xformula.syntax.grammar.terminals.abc.terminal import Terminal
    from xformula.syntax.parser.transformers.abc.ast_builder_protocol import (
        ASTBuilderProtocol,
    )

__all__ = [
    "SyntaxContext",
]


C = TypeVar("C", bound="SyntaxContext")


@dataclasses.dataclass()
class SyntaxContext:
    @staticmethod
    def build_ebnf_expression_builder_class() -> type[
        "EBNFExpressionBuilderProtocol",
    ]:
        from xformula.syntax.grammar.definitions.runtime.reflection import (
            EBNFExpressionBuilderClassBuilder,
        )

        return EBNFExpressionBuilderClassBuilder.build()

    @staticmethod
    def build_regex_expression_builder_class() -> type[
        "RegexExpressionBuilderProtocol",
    ]:
        from xformula.syntax.grammar.definitions.runtime.reflection import (
            RegexExpressionBuilderClassBuilder,
        )

        return RegexExpressionBuilderClassBuilder.build()

    feature_types: dataclasses.InitVar[
        list[type["Feature"]] | None
    ] = dataclasses.field(
        kw_only=True,
        default=None,
    )

    ebnf_expression_builder_class: type[
        "EBNFExpressionBuilderProtocol",
    ] = dataclasses.field(
        default_factory=build_ebnf_expression_builder_class,
    )

    regex_expression_builder_class: type[
        "RegexExpressionBuilderProtocol",
    ] = dataclasses.field(
        default_factory=build_regex_expression_builder_class,
    )

    features: dict[str, "Feature"] = dataclasses.field(
        kw_only=True,
        default_factory=dict,
    )

    directives: list["Directive"] = dataclasses.field(
        kw_only=True,
        default_factory=list,
    )

    non_terminals: list["NonTerminal"] = dataclasses.field(
        kw_only=True,
        default_factory=list,
    )

    templates: list["Template"] = dataclasses.field(
        kw_only=True,
        default_factory=list,
    )

    terminals: list["Terminal"] = dataclasses.field(
        kw_only=True,
        default_factory=list,
    )

    tagged_definitions: dict[str, list["Definition"]] = dataclasses.field(
        kw_only=True,
        default_factory=dict,
    )

    operator_precedences: list["OperatorPrecedence"] = dataclasses.field(
        kw_only=True,
        default_factory=list,
    )

    def __post_init__(
        self,
        feature_types: list[type["Feature"]] | None,
    ) -> None:
        if feature_types is not None:
            for feature_type in feature_types:
                self.register_feature_type(feature_type)
        self.setup()

    def get_feature(
        self,
        fqn: str,
    ) -> Optional["Feature"]:
        return self.features.get(fqn)

    def f(
        self,
        fqn: str,
    ) -> "Feature":
        return self.features[fqn]

    def register_feature_type(
        self,
        feature_type: type["Feature"],
    ) -> None:
        feature = feature_type(self)
        self.register_feature(feature)

    def register_feature(
        self,
        feature: "Feature",
    ) -> None:
        self.features[feature.__class__.options.fqn] = feature

    def register_feature_definitions(
        self,
        feature: "Feature",
    ) -> None:
        definition_types = chain(
            feature.directive_types,
            feature.non_terminal_types,
            feature.template_types,
            feature.terminal_types,
        )
        for definition_type in definition_types:
            definition = definition_type(self)
            definitions = self.get_definitions_by_type(definition_type.options.type)
            definitions.append(definition)
            for tag, priority in definition_type.options.tags.items():
                if tag not in self.tagged_definitions:
                    self.tagged_definitions[tag] = []
                bisect_key = partial(self.get_definition_tag_priority, tag)
                Bisect.insert_right(
                    self.tagged_definitions[tag],
                    definition,
                    lhs_key=bisect_key,
                    rhs_key=bisect_key,
                )

    @staticmethod
    def get_definition_tag_priority(
        tag: str,
        definition: "Definition",
    ) -> int | float:
        return definition.__class__.options.tags.get(tag, 0)

    def get_definitions_by_type(
        self,
        definition_type: "DefinitionType",
    ) -> list["Definition"]:
        from xformula.syntax.grammar import DefinitionType

        if definition_type == DefinitionType.DIRECTIVE:
            return cast(list["Definition"], self.directives)
        if definition_type == DefinitionType.NON_TERMINAL:
            return cast(list["Definition"], self.non_terminals)
        if definition_type == DefinitionType.TEMPLATE:
            return cast(list["Definition"], self.templates)
        if definition_type == DefinitionType.TERMINAL:
            return cast(list["Definition"], self.terminals)

        raise TypeError(f"invalid definition type: {definition_type!r}")

    def setup_features(self) -> None:
        # todo: These get done before runtime, we still need a signal-handling mechanism.
        for feature in self.features.values():
            feature.pre_setup()
        for feature in self.features.values():
            feature.setup()
        for feature in self.features.values():
            self.register_feature_definitions(feature)
        for feature in self.features.values():
            feature.post_setup()
        for feature in self.features.values():
            feature.on_ready()

    def setup(self) -> None:
        self.setup_features()

    def build_ast_builder_class(
        self,
        runtime_context: "RuntimeContext",
    ) -> type["ASTBuilderProtocol"]:
        from xformula.syntax.parser.transformers.runtime.reflection import (
            ASTBuilderClassBuilder,
        )

        return ASTBuilderClassBuilder.build(
            self,
            runtime_context,
        )
