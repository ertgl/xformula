from abc import ABC
from typing import Protocol, runtime_checkable

from xformula.arch.meta.meta import Meta

__all__ = [
    "Configurable",
]


class Configurable(
    ABC,
    metaclass=Meta,
):
    @runtime_checkable
    class Meta(Protocol):

        abstract: bool = True

        name: str = ""
