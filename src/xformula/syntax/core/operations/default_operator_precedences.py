from xformula.arch.enumeration import Iota
from xformula.syntax.ast.nodes.abc import Associativity, Placement, SymbolType
from xformula.syntax.core.operations.abc import OperatorPrecedence

__all__ = [
    "DEFAULT_OPERATOR_PRECEDENCES",
]


__xf__operator_precedence_iota__ = Iota(
    value=0,
    step=1000,
)


DEFAULT_OPERATOR_PRECEDENCES: list[OperatorPrecedence] = [
    OperatorPrecedence(
        arity=2,
        associativity=Associativity.LEFT_TO_RIGHT,
        level=__xf__operator_precedence_iota__(),
        placement=Placement.RIGHT,
        symbols=[
            (SymbolType.OPERATOR, "**"),
        ],
    ),
    OperatorPrecedence(
        arity=1,
        associativity=Associativity.RIGHT_TO_LEFT,
        level=__xf__operator_precedence_iota__(),
        placement=Placement.LEFT,
        symbols=[
            (SymbolType.OPERATOR, "+"),
        ],
    ),
    OperatorPrecedence(
        arity=1,
        associativity=Associativity.RIGHT_TO_LEFT,
        level=__xf__operator_precedence_iota__(),
        placement=Placement.LEFT,
        symbols=[
            (SymbolType.OPERATOR, "-"),
        ],
    ),
    OperatorPrecedence(
        arity=1,
        associativity=Associativity.RIGHT_TO_LEFT,
        level=__xf__operator_precedence_iota__(),
        placement=Placement.LEFT,
        symbols=[
            (SymbolType.OPERATOR, "!"),
        ],
    ),
    OperatorPrecedence(
        arity=1,
        associativity=Associativity.RIGHT_TO_LEFT,
        level=__xf__operator_precedence_iota__(),
        placement=Placement.LEFT,
        symbols=[
            (SymbolType.OPERATOR, "~"),
        ],
    ),
    OperatorPrecedence(
        arity=2,
        associativity=Associativity.LEFT_TO_RIGHT,
        level=__xf__operator_precedence_iota__(),
        placement=Placement.RIGHT,
        symbols=[
            (SymbolType.OPERATOR, "*"),
        ],
    ),
    OperatorPrecedence(
        arity=2,
        associativity=Associativity.LEFT_TO_RIGHT,
        level=__xf__operator_precedence_iota__(),
        placement=Placement.RIGHT,
        symbols=[
            (SymbolType.OPERATOR, "@"),
        ],
    ),
    OperatorPrecedence(
        arity=2,
        associativity=Associativity.LEFT_TO_RIGHT,
        level=__xf__operator_precedence_iota__(),
        placement=Placement.RIGHT,
        symbols=[
            (SymbolType.OPERATOR, "/"),
        ],
    ),
    OperatorPrecedence(
        arity=2,
        associativity=Associativity.LEFT_TO_RIGHT,
        level=__xf__operator_precedence_iota__(),
        placement=Placement.RIGHT,
        symbols=[
            (SymbolType.OPERATOR, "//"),
        ],
    ),
    OperatorPrecedence(
        arity=2,
        associativity=Associativity.LEFT_TO_RIGHT,
        level=__xf__operator_precedence_iota__(),
        placement=Placement.RIGHT,
        symbols=[
            (SymbolType.OPERATOR, "%"),
        ],
    ),
    OperatorPrecedence(
        arity=2,
        associativity=Associativity.LEFT_TO_RIGHT,
        level=__xf__operator_precedence_iota__(),
        placement=Placement.RIGHT,
        symbols=[
            (SymbolType.OPERATOR, "+"),
        ],
    ),
    OperatorPrecedence(
        arity=2,
        associativity=Associativity.LEFT_TO_RIGHT,
        level=__xf__operator_precedence_iota__(),
        placement=Placement.RIGHT,
        symbols=[
            (SymbolType.OPERATOR, "-"),
        ],
    ),
    OperatorPrecedence(
        arity=2,
        associativity=Associativity.LEFT_TO_RIGHT,
        level=__xf__operator_precedence_iota__(),
        placement=Placement.RIGHT,
        symbols=[
            (SymbolType.OPERATOR, "<<"),
        ],
    ),
    OperatorPrecedence(
        arity=2,
        associativity=Associativity.LEFT_TO_RIGHT,
        level=__xf__operator_precedence_iota__(),
        placement=Placement.RIGHT,
        symbols=[
            (SymbolType.OPERATOR, ">>"),
        ],
    ),
    OperatorPrecedence(
        arity=2,
        associativity=Associativity.LEFT_TO_RIGHT,
        level=__xf__operator_precedence_iota__(),
        placement=Placement.RIGHT,
        symbols=[
            (SymbolType.OPERATOR, "&"),
        ],
    ),
    OperatorPrecedence(
        arity=2,
        associativity=Associativity.LEFT_TO_RIGHT,
        level=__xf__operator_precedence_iota__(),
        placement=Placement.RIGHT,
        symbols=[
            (SymbolType.OPERATOR, "^"),
        ],
    ),
    OperatorPrecedence(
        arity=2,
        associativity=Associativity.LEFT_TO_RIGHT,
        level=__xf__operator_precedence_iota__(),
        placement=Placement.RIGHT,
        symbols=[
            (SymbolType.OPERATOR, "|"),
        ],
    ),
    OperatorPrecedence(
        arity=2,
        associativity=Associativity.LEFT_TO_RIGHT,
        level=__xf__operator_precedence_iota__(),
        placement=Placement.RIGHT,
        symbols=[
            (SymbolType.OPERATOR, "not in"),
        ],
    ),
    OperatorPrecedence(
        arity=2,
        associativity=Associativity.LEFT_TO_RIGHT,
        level=__xf__operator_precedence_iota__(),
        placement=Placement.RIGHT,
        symbols=[
            (SymbolType.OPERATOR, "!in"),
        ],
    ),
    OperatorPrecedence(
        arity=2,
        associativity=Associativity.LEFT_TO_RIGHT,
        level=__xf__operator_precedence_iota__(),
        placement=Placement.RIGHT,
        symbols=[
            (SymbolType.KEYWORD, "in"),
        ],
    ),
    OperatorPrecedence(
        arity=2,
        associativity=Associativity.LEFT_TO_RIGHT,
        level=__xf__operator_precedence_iota__(),
        placement=Placement.RIGHT,
        symbols=[
            (SymbolType.KEYWORD, "is not"),
        ],
    ),
    OperatorPrecedence(
        arity=2,
        associativity=Associativity.LEFT_TO_RIGHT,
        level=__xf__operator_precedence_iota__(),
        placement=Placement.RIGHT,
        symbols=[
            (SymbolType.OPERATOR, "!is"),
        ],
    ),
    OperatorPrecedence(
        arity=2,
        associativity=Associativity.LEFT_TO_RIGHT,
        level=__xf__operator_precedence_iota__(),
        placement=Placement.RIGHT,
        symbols=[
            (SymbolType.KEYWORD, "is"),
        ],
    ),
    OperatorPrecedence(
        arity=2,
        associativity=Associativity.LEFT_TO_RIGHT,
        level=__xf__operator_precedence_iota__(),
        placement=Placement.RIGHT,
        symbols=[
            (SymbolType.OPERATOR, "!<"),
        ],
    ),
    OperatorPrecedence(
        arity=2,
        associativity=Associativity.LEFT_TO_RIGHT,
        level=__xf__operator_precedence_iota__(),
        placement=Placement.RIGHT,
        symbols=[
            (SymbolType.OPERATOR, "!<="),
        ],
    ),
    OperatorPrecedence(
        arity=2,
        associativity=Associativity.LEFT_TO_RIGHT,
        level=__xf__operator_precedence_iota__(),
        placement=Placement.RIGHT,
        symbols=[
            (SymbolType.OPERATOR, "<="),
        ],
    ),
    OperatorPrecedence(
        arity=2,
        associativity=Associativity.LEFT_TO_RIGHT,
        level=__xf__operator_precedence_iota__(),
        placement=Placement.RIGHT,
        symbols=[
            (SymbolType.OPERATOR, "<"),
        ],
    ),
    OperatorPrecedence(
        arity=2,
        associativity=Associativity.LEFT_TO_RIGHT,
        level=__xf__operator_precedence_iota__(),
        placement=Placement.RIGHT,
        symbols=[
            (SymbolType.OPERATOR, "!>"),
        ],
    ),
    OperatorPrecedence(
        arity=2,
        associativity=Associativity.LEFT_TO_RIGHT,
        level=__xf__operator_precedence_iota__(),
        placement=Placement.RIGHT,
        symbols=[
            (SymbolType.OPERATOR, "!>="),
        ],
    ),
    OperatorPrecedence(
        arity=2,
        associativity=Associativity.LEFT_TO_RIGHT,
        level=__xf__operator_precedence_iota__(),
        placement=Placement.RIGHT,
        symbols=[
            (SymbolType.OPERATOR, ">="),
        ],
    ),
    OperatorPrecedence(
        arity=2,
        associativity=Associativity.LEFT_TO_RIGHT,
        level=__xf__operator_precedence_iota__(),
        placement=Placement.RIGHT,
        symbols=[
            (SymbolType.OPERATOR, ">"),
        ],
    ),
    OperatorPrecedence(
        arity=2,
        associativity=Associativity.LEFT_TO_RIGHT,
        level=__xf__operator_precedence_iota__(),
        placement=Placement.RIGHT,
        symbols=[
            (SymbolType.OPERATOR, "!="),
        ],
    ),
    OperatorPrecedence(
        arity=2,
        associativity=Associativity.LEFT_TO_RIGHT,
        level=__xf__operator_precedence_iota__(),
        placement=Placement.RIGHT,
        symbols=[
            (SymbolType.OPERATOR, "=="),
        ],
    ),
    OperatorPrecedence(
        arity=3,
        associativity=Associativity.RIGHT_TO_LEFT,
        level=__xf__operator_precedence_iota__(),
        placement=Placement.LEFT,
        symbols=[
            (SymbolType.OPERATOR, "?"),
            (SymbolType.OPERATOR, ":"),
        ],
    ),
    OperatorPrecedence(
        arity=2,
        associativity=Associativity.LEFT_TO_RIGHT,
        level=__xf__operator_precedence_iota__(),
        placement=Placement.RIGHT,
        symbols=[
            (SymbolType.OPERATOR, "??"),
        ],
    ),
    OperatorPrecedence(
        arity=1,
        associativity=Associativity.RIGHT_TO_LEFT,
        level=__xf__operator_precedence_iota__(),
        placement=Placement.LEFT,
        symbols=[
            (SymbolType.KEYWORD, "not"),
        ],
    ),
    OperatorPrecedence(
        arity=2,
        associativity=Associativity.LEFT_TO_RIGHT,
        level=__xf__operator_precedence_iota__(),
        placement=Placement.RIGHT,
        symbols=[
            (SymbolType.OPERATOR, "&&"),
        ],
    ),
    OperatorPrecedence(
        arity=2,
        associativity=Associativity.LEFT_TO_RIGHT,
        level=__xf__operator_precedence_iota__(),
        placement=Placement.RIGHT,
        symbols=[
            (SymbolType.OPERATOR, "||"),
        ],
    ),
    OperatorPrecedence(
        arity=2,
        associativity=Associativity.LEFT_TO_RIGHT,
        level=__xf__operator_precedence_iota__(),
        placement=Placement.RIGHT,
        symbols=[
            (SymbolType.KEYWORD, "and"),
        ],
    ),
    OperatorPrecedence(
        arity=2,
        associativity=Associativity.LEFT_TO_RIGHT,
        level=__xf__operator_precedence_iota__(),
        placement=Placement.RIGHT,
        symbols=[
            (SymbolType.KEYWORD, "or"),
        ],
    ),
]


del __xf__operator_precedence_iota__
