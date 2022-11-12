from xformula.arch.enumeration import Iota
from xformula_unittests.abc import UnitTest

__all__ = [
    "IotaUnitTest",
]


class IotaUnitTest(UnitTest):
    def test__init(self) -> None:
        iota = Iota()
        self.assertEqual(iota.value, -1)

    def test__incr(self) -> None:
        iota = Iota()
        self.assertEqual(iota.incr(), 0)
        self.assertEqual(iota.incr(), 1)
        self.assertEqual(iota.incr(), 2)

    def test__reset(self) -> None:
        iota = Iota()
        self.assertEqual(iota.incr(), 0)
        self.assertEqual(iota.incr(), 1)
        self.assertEqual(iota.reset(), 0)
        self.assertEqual(iota.incr(), 1)

    def test__magic_call(self) -> None:
        iota = Iota()
        self.assertEqual(iota(), 0)
        self.assertEqual(iota(), 1)
        self.assertEqual(iota(reset=True), 0)
        self.assertEqual(iota(), 1)
