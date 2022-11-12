from abc import ABC
from typing import Any, Generic, TypeVar, cast

__all__ = [
    "ClassBuilder",
]


T = TypeVar("T")


class ClassBuilder(
    Generic[T],
    ABC,
):
    @classmethod
    def get_name(
        cls,
        *args: Any,
        **kwargs: Any,
    ) -> str:
        raise NotImplementedError(f"{cls.__qualname__}.get_name is not implemented")

    @classmethod
    def get_base_qualname(
        cls,
        *args: Any,
        **kwargs: Any,
    ) -> str:
        return cls.__qualname__

    @classmethod
    def get_bases(
        cls,
        *args: Any,
        **kwargs: Any,
    ) -> tuple[type, ...]:
        return ()

    @classmethod
    def get_namespace(
        cls,
        *args: Any,
        **kwargs: Any,
    ) -> dict[str, Any]:
        return dict()

    @classmethod
    def build(
        cls,
        *args: Any,
        **kwargs: Any,
    ) -> type[T]:
        name = cls.get_name(*args, **kwargs)
        base_qualname = cls.get_base_qualname(*args, **kwargs)
        bases = cls.get_bases(*args, **kwargs)
        namespace = cls.get_namespace(*args, **kwargs)
        built_type = cast(type[T], type(name, bases, namespace))
        built_type.__qualname__ = ".".join([base_qualname, name])
        return built_type
