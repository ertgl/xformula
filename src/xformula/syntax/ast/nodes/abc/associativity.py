from enum import IntEnum

from xformula.arch.enumeration import Iota

__all__ = [
    "Associativity",
]


__xf__associativity_iota__ = Iota()


class Associativity(IntEnum):

    UNDEFINED = __xf__associativity_iota__()

    __XF__START__ = __xf__associativity_iota__()

    LEFT_TO_RIGHT = __xf__associativity_iota__()

    RIGHT_TO_LEFT = __xf__associativity_iota__()

    __XF__END__ = __xf__associativity_iota__()


del __xf__associativity_iota__
