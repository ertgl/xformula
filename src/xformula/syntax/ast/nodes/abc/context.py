from enum import IntEnum

from xformula.arch.enumeration import Iota

__all__ = [
    "Context",
]


__xf__context_iota__ = Iota()


class Context(IntEnum):

    UNDEFINED = __xf__context_iota__()

    __XF__START__ = __xf__context_iota__()

    ATTRIBUTE = __xf__context_iota__()

    DELETE = __xf__context_iota__()

    KEYWORD_ARGUMENT = __xf__context_iota__()

    LOAD = __xf__context_iota__()

    REGISTER = __xf__context_iota__()

    __XF__END__ = __xf__context_iota__()


del __xf__context_iota__
