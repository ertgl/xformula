from enum import IntEnum

from xformula.arch.enumeration import Iota

__all__ = [
    "Placement",
]


__xf__placement_iota__ = Iota()


class Placement(IntEnum):

    UNDEFINED = __xf__placement_iota__()

    __XF__START__ = __xf__placement_iota__()

    LEFT = __xf__placement_iota__()

    RIGHT = __xf__placement_iota__()

    __XF__END__ = __xf__placement_iota__()


del __xf__placement_iota__
