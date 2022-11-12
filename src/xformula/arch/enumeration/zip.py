from collections import deque
from enum import IntEnum
from itertools import zip_longest
from typing import Any, Callable, Iterable, Literal, Optional, TypeVar, overload

from xformula.arch.enumeration.iota import Iota

__all__ = [
    "Zip",
]


S = TypeVar("S")

T = TypeVar("T")

V = TypeVar("V", bound=Optional[Any])

X = TypeVar("X")


__xf__zip_separator_placement_iota__ = Iota()


class Zip:
    class SeparatorPlacement(IntEnum):

        UNDEFINED = __xf__zip_separator_placement_iota__()

        __XF__START__ = __xf__zip_separator_placement_iota__()

        LEFT = __xf__zip_separator_placement_iota__()

        RIGHT = __xf__zip_separator_placement_iota__()

        __XF__END__ = __xf__zip_separator_placement_iota__()

    @classmethod
    @overload
    def join(
        cls,
        separators: Iterable[S],
        elements: Iterable[T],
        separator_placement: Literal[SeparatorPlacement.LEFT] = SeparatorPlacement.LEFT,
    ) -> Iterable[tuple[S | None, T | None]]:
        ...

    @classmethod
    @overload
    def join(
        cls,
        separators: Iterable[S],
        elements: Iterable[T],
        separator_placement: Literal[SeparatorPlacement.LEFT] = SeparatorPlacement.LEFT,
        default_value: V = None,
    ) -> Iterable[tuple[S | V, T | V]]:
        ...

    @classmethod
    @overload
    def join(
        cls,
        separators: Iterable[S],
        elements: Iterable[T],
        separator_placement: Literal[
            SeparatorPlacement.RIGHT
        ] = SeparatorPlacement.RIGHT,
    ) -> Iterable[tuple[T | None, S | None]]:
        ...

    @classmethod
    @overload
    def join(
        cls,
        separators: Iterable[S],
        elements: Iterable[T],
        separator_placement: Literal[
            SeparatorPlacement.RIGHT
        ] = SeparatorPlacement.RIGHT,
        default_value: V = None,
    ) -> Iterable[tuple[T | V, S | V]]:
        ...

    @classmethod
    def join(
        cls,
        separators,
        elements,
        separator_placement=SeparatorPlacement.RIGHT,
        default_value=None,
    ):
        if not (
            cls.SeparatorPlacement.__XF__START__
            < separator_placement
            < cls.SeparatorPlacement.__XF__END__
        ):
            raise TypeError(f"invalid separator placement: {separator_placement!r}")

        iterator = zip_longest(
            separators,
            elements,
            fillvalue=default_value,
        )

        for s, x in iterator:
            if separator_placement == cls.SeparatorPlacement.LEFT:
                yield s, x
            elif separator_placement == cls.SeparatorPlacement.RIGHT:
                yield x, s
            else:
                raise NotImplementedError(
                    f"{cls.__qualname__}.join is not implemented for"
                    f" separator placement: {separator_placement!r}"
                )

    @classmethod
    @overload
    def split(
        cls,
        iterable: Iterable[T | S],
    ) -> tuple[Iterable[S], Iterable[T]]:
        ...

    @classmethod
    @overload
    def split(
        cls,
        iterable: Iterable[T | S],
        separator_placement: SeparatorPlacement,
    ) -> tuple[Iterable[S], Iterable[T]]:
        ...

    @classmethod
    @overload
    def split(
        cls,
        iterable: Iterable[S | T],
        separator_placement: Literal[SeparatorPlacement.LEFT] = SeparatorPlacement.LEFT,
    ) -> tuple[Iterable[S], Iterable[T]]:
        ...

    @classmethod
    @overload
    def split(
        cls,
        iterable: Iterable[T | S],
        separator_placement: Literal[
            SeparatorPlacement.RIGHT
        ] = SeparatorPlacement.RIGHT,
    ) -> tuple[Iterable[S], Iterable[T]]:
        ...

    @classmethod
    def split(
        cls,
        iterable,
        separator_placement=SeparatorPlacement.RIGHT,
    ):
        if not (
            cls.SeparatorPlacement.__XF__START__
            < separator_placement
            < cls.SeparatorPlacement.__XF__END__
        ):
            raise TypeError(f"invalid separator placement: {separator_placement!r}")

        iterator = iter(iterable)

        separator_channel: deque[S] = deque()
        element_channel: deque[T] = deque()

        def filter_channel(
            channel: deque[X],
            is_separator: Callable[[int], bool],
        ) -> Iterable[X]:
            nonlocal separator_channel
            nonlocal element_channel

            i = 0
            while True:
                if not channel:
                    try:
                        x = next(iterator)
                    except StopIteration:
                        return

                    if is_separator(i):
                        separator_channel.append(x)
                    else:
                        element_channel.append(x)

                if channel:
                    yield channel.popleft()
                i += 1

        if separator_placement == cls.SeparatorPlacement.LEFT:
            return (
                filter_channel(
                    separator_channel,
                    lambda j: j % 2 == 0,
                ),
                filter_channel(
                    element_channel,
                    lambda j: j % 2 != 0,
                ),
            )

        elif separator_placement == cls.SeparatorPlacement.RIGHT:
            return (
                filter_channel(
                    separator_channel,
                    lambda j: j % 2 != 0,
                ),
                filter_channel(
                    element_channel,
                    lambda j: j % 2 == 0,
                ),
            )

        else:
            raise NotImplementedError(
                f"{cls.__qualname__}.split is not implemented for"
                f" separator placement: {separator_placement!r}"
            )


del __xf__zip_separator_placement_iota__
