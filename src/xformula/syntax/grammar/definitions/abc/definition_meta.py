from typing import Any, NoReturn, TypeVar

from xformula.arch.meta import Meta
from xformula.syntax.grammar.definitions.abc.definition_options import DefinitionOptions

__all__ = [
    "DefinitionMeta",
]


C = TypeVar("C", bound="DefinitionMeta")


class DefinitionMeta(
    Meta[DefinitionOptions],
):

    options_class = DefinitionOptions

    options: DefinitionOptions

    @classmethod
    def get_excluded_super_options_attnames(
        mcs,
        name: str,
        bases: tuple[type, ...],
        namespace: dict[str, Any],
        **kwargs: Any,
    ) -> set[str]:
        excluded = super(DefinitionMeta, mcs).get_excluded_super_options_attnames(
            name,
            bases,
            namespace,
            **kwargs,
        )
        excluded.add("definition_name")
        return excluded

    @classmethod
    def get_super_options_kwargs(
        mcs,
        name: str,
        bases: tuple[type, ...],
        namespace: dict[str, Any],
        **kwargs: Any,
    ) -> dict[str, Any]:
        options_kwargs = super(DefinitionMeta, mcs).get_super_options_kwargs(
            name,
            bases,
            namespace,
            **kwargs,
        )
        if "arguments" in options_kwargs:
            options_kwargs["arguments"] = options_kwargs["arguments"].copy()
        if "tags" in options_kwargs:
            options_kwargs["tags"] = options_kwargs["tags"].copy()
        return options_kwargs

    @classmethod
    def populate_options_kwargs(
        mcs,
        name: str,
        bases: tuple[type, ...],
        namespace: dict[str, Any],
        meta: Any | None,
        options_kwargs: dict[str, Any],
        **kwargs: Any,
    ) -> None:
        from xformula.syntax.grammar.ebnf import normalize_name_by_type

        super(DefinitionMeta, mcs).populate_options_kwargs(
            name,
            bases,
            namespace,
            meta,
            options_kwargs,
            **kwargs,
        )

        abstract = options_kwargs.get("abstract", False)

        if not abstract:

            if not options_kwargs.get("definition_name", ""):
                options_kwargs["definition_name"] = options_kwargs["name"]

            if not abstract and "type" in options_kwargs:
                options_kwargs["definition_name"] = normalize_name_by_type(
                    options_kwargs["type"],
                    options_kwargs["definition_name"],
                )

    @classmethod
    def validate_options(
        mcs,
        name: str,
        bases: tuple[type, ...],
        namespace: dict[str, Any],
        options: DefinitionOptions,
        **kwargs: Any,
    ) -> NoReturn | None:
        super(DefinitionMeta, mcs).validate_options(
            name,
            bases,
            namespace,
            options,
            **kwargs,
        )

        if options.abstract:
            return None

        from xformula.syntax.grammar.definitions.abc.definition_type import (
            DefinitionType,
        )

        if not (
            DefinitionType.__XF__START__ < options.type < DefinitionType.__XF__END__
        ):
            raise TypeError(f"invalid rule type: {options.type!r}")

        return None
