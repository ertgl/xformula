from enum import IntEnum

from xformula.arch.enumeration import Iota

__all__ = [
    "DefinitionType",
]


__xf__definition_type__iota__ = Iota()


class DefinitionType(IntEnum):

    UNDEFINED = __xf__definition_type__iota__.value

    __XF__START__ = __xf__definition_type__iota__()

    DIRECTIVE = __xf__definition_type__iota__()

    NON_TERMINAL = __xf__definition_type__iota__()

    TEMPLATE = __xf__definition_type__iota__()

    TERMINAL = __xf__definition_type__iota__()

    __XF__END__ = __xf__definition_type__iota__()


del __xf__definition_type__iota__
