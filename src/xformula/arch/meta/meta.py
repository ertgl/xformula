import dataclasses
from abc import ABCMeta
from typing import Any, Generic, NoReturn, Optional, TypeVar, cast

from xformula.arch.meta.options import Options

__all__ = [
    "Meta",
]


C = TypeVar("C", bound="Meta")

O = TypeVar("O", bound=Options)


class Meta(
    ABCMeta,
    Generic[O],
):

    options_class: type[O] = cast(type[O], Options)

    options: O

    __XF__META_ATTNAME__: str = "Meta"

    def __new__(
        mcs: type[C],
        name: str,
        bases: tuple[type, ...],
        namespace: dict[str, Any],
        **kwargs: Any,
    ) -> C:
        meta_attname = mcs.get_meta_attname(
            name,
            bases,
            namespace,
            **kwargs,
        )
        meta = mcs.get_meta(
            name,
            bases,
            namespace,
            **kwargs,
        )

        options_kwargs = mcs.get_super_options_kwargs(
            name,
            bases,
            namespace,
            **kwargs,
        )

        options_kwargs["name"] = name

        mcs.populate_options_kwargs(
            name,
            bases,
            namespace,
            meta,
            options_kwargs,
            **kwargs,
        )

        if not options_kwargs.get("name"):
            options_kwargs["name"] = name

        options_class = mcs.get_options_class()
        options = options_class(**options_kwargs)

        mcs.validate_options(
            name,
            bases,
            namespace,
            options,
            **kwargs,
        )

        namespace["options"] = options
        if not options.abstract:
            namespace.pop(meta_attname, None)

        generated_type = super(Meta, mcs).__new__(
            mcs,
            name,
            bases,
            namespace,
            **kwargs,
        )

        mcs.post_generate(
            name,
            bases,
            namespace,
            meta,
            generated_type,
            **kwargs,
        )

        return generated_type

    @classmethod
    def get_meta_attname(
        mcs,
        name: str,
        bases: tuple[type, ...],
        namespace: dict[str, Any],
        **kwargs: Any,
    ) -> str:
        return mcs.__XF__META_ATTNAME__

    @classmethod
    def get_meta(
        mcs,
        name: str,
        bases: tuple[type, ...],
        namespace: dict[str, Any],
        **kwargs: Any,
    ) -> Any | None:
        return namespace.get(
            mcs.get_meta_attname(
                name,
                bases,
                namespace,
                **kwargs,
            ),
            None,
        )

    @classmethod
    def get_options_class(mcs) -> type[O]:
        return mcs.options_class

    @classmethod
    def get_excluded_super_options_attnames(
        mcs,
        name: str,
        bases: tuple[type, ...],
        namespace: dict[str, Any],
        **kwargs: Any,
    ) -> set[str]:
        return {"abstract", "name"}

    @classmethod
    def get_super_options_kwargs(
        mcs,
        name: str,
        bases: tuple[type, ...],
        namespace: dict[str, Any],
        **kwargs: Any,
    ) -> dict[str, Any]:
        options_kwargs: dict[str, Any] = dict()
        excluded_att_names = mcs.get_excluded_super_options_attnames(
            name,
            bases,
            namespace,
            **kwargs,
        )
        for super_type in bases[::-1]:
            super_options = cast(Optional[O], getattr(super_type, "options", None))
            if super_options is None:
                continue
            for field in dataclasses.fields(mcs.options_class):
                if field.name in excluded_att_names or field.name in options_kwargs:
                    continue
                if hasattr(super_options, field.name):
                    options_kwargs[field.name] = getattr(super_options, field.name)
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
        if meta is None:
            return
        for field in dataclasses.fields(mcs.options_class):
            if hasattr(meta, field.name):
                options_kwargs[field.name] = getattr(meta, field.name)

    @classmethod
    def post_generate(
        mcs: type[C],
        name: str,
        bases: tuple[type, ...],
        namespace: dict[str, Any],
        meta: Any | None,
        generated_type: C,
        **kwargs: Any,
    ) -> None:
        return None

    @classmethod
    def validate_options(
        mcs,
        name: str,
        bases: tuple[type, ...],
        namespace: dict[str, Any],
        options: O,
        **kwargs: Any,
    ) -> NoReturn | None:
        return None
