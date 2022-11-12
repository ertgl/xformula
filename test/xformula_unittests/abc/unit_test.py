from unittest import TestCase as _TestCase

__all__ = [
    "UnitTest",
]


class UnitTest(_TestCase):
    def setUp(self) -> None:
        self.set_up()

    def set_up(self) -> None:
        ...

    def tearDown(self) -> None:
        self.tear_down()

    def tear_down(self) -> None:
        ...
