from enum import IntEnum

from xformula.arch.enumeration import Iota

__all__ = [
    "SymbolType",
]


__xf__symbol_type_iota__ = Iota()


class SymbolType(IntEnum):

    UNDEFINED = __xf__symbol_type_iota__()

    __XF__START__ = __xf__symbol_type_iota__()

    KEYWORD = __xf__symbol_type_iota__()

    OPERATOR = __xf__symbol_type_iota__()

    __XF__END__ = __xf__symbol_type_iota__()


del __xf__symbol_type_iota__
