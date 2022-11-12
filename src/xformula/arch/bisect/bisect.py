from functools import partial
from typing import Any, Callable, TypeVar

__all__ = [
    "Bisect",
]


T = TypeVar("T", bound=Any)

V = TypeVar("V", bound=Any)


class Bisect:
    @staticmethod
    def pure(x: T) -> T:
        return x

    @staticmethod
    def left(rhs: V, lhs: V) -> bool:
        return lhs >= rhs

    @staticmethod
    def right(rhs: V, lhs: V) -> bool:
        return lhs > rhs

    @classmethod
    def search(
        cls,
        predict: Callable[[V], bool],
        list_: list[T],
        low: int = 0,
        high: int | None = None,
        key: Callable[[T], V] = pure,
    ) -> int:
        if high is None:
            high = len(list_)
        while low < high:
            middle = (low + high) >> 0x1
            lhs = key(list_[middle])
            if predict(lhs):
                high = middle
            else:
                low = middle + 1
        return low

    @classmethod
    def find_left_index(
        cls,
        list_: list[T],
        x: V,
        low: int = 0,
        high: int | None = None,
        lhs_key: Callable[[T], V] = pure,
        rhs_key: Callable[[T], V] = pure,
    ) -> int:
        rhs = rhs_key(x)
        return cls.search(
            partial(cls.left, rhs),
            list_,
            low=low,
            high=high,
            key=lhs_key,
        )

    @classmethod
    def find_right_index(
        cls,
        list_: list[T],
        x: V,
        low: int = 0,
        high: int | None = None,
        lhs_key: Callable[[T], V] = pure,
        rhs_key: Callable[[T], V] = pure,
    ) -> int:
        rhs = rhs_key(x)
        return cls.search(
            partial(cls.right, rhs),
            list_,
            low=low,
            high=high,
            key=lhs_key,
        )

    @classmethod
    def insert_left(
        cls,
        list_: list[T],
        x: T,
        low: int = 0,
        high: int | None = None,
        lhs_key: Callable[[T], V] = pure,
        rhs_key: Callable[[T], V] = pure,
    ) -> list[T]:
        index = cls.find_left_index(
            list_,
            x,
            low=low,
            high=high,
            lhs_key=lhs_key,
            rhs_key=rhs_key,
        )
        list_.insert(index, x)
        return list_

    @classmethod
    def insert_right(
        cls,
        list_: list[T],
        x: T,
        low: int = 0,
        high: int | None = None,
        lhs_key: Callable[[T], V] = pure,
        rhs_key: Callable[[T], V] = pure,
    ) -> list[T]:
        index = cls.find_right_index(
            list_,
            x,
            low=low,
            high=high,
            lhs_key=lhs_key,
            rhs_key=rhs_key,
        )
        list_.insert(index, x)
        return list_
