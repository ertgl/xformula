import dataclasses

from xformula.arch.meta import Options

__all__ = [
    "NodeOptions",
]


@dataclasses.dataclass()
class NodeOptions(Options):

    is_start_point: bool = dataclasses.field(
        kw_only=True,
        default=bool(),
    )

    is_expression: bool = dataclasses.field(
        kw_only=True,
        default=bool(),
    )

    is_simple_expression: bool = dataclasses.field(
        kw_only=True,
        default=bool(),
    )

    is_operation: bool = dataclasses.field(
        kw_only=True,
        default=bool(),
    )

    is_operator: bool = dataclasses.field(
        kw_only=True,
        default=bool(),
    )

    is_symbol: bool = dataclasses.field(
        kw_only=True,
        default=bool(),
    )

    is_operand: bool = dataclasses.field(
        kw_only=True,
        default=bool(),
    )

    is_primary: bool = dataclasses.field(
        kw_only=True,
        default=bool(),
    )

    is_mapping: bool = dataclasses.field(
        kw_only=True,
        default=bool(),
    )

    is_dict: bool = dataclasses.field(
        kw_only=True,
        default=bool(),
    )

    is_pair: bool = dataclasses.field(
        kw_only=True,
        default=bool(),
    )

    is_container: bool = dataclasses.field(
        kw_only=True,
        default=bool(),
    )

    is_set: bool = dataclasses.field(
        kw_only=True,
        default=bool(),
    )

    is_tuple: bool = dataclasses.field(
        kw_only=True,
        default=bool(),
    )

    is_list: bool = dataclasses.field(
        kw_only=True,
        default=bool(),
    )

    is_term: bool = dataclasses.field(
        kw_only=True,
        default=bool(),
    )

    is_call: bool = dataclasses.field(
        kw_only=True,
        default=bool(),
    )

    is_attribute: bool = dataclasses.field(
        kw_only=True,
        default=bool(),
    )

    is_identifier: bool = dataclasses.field(
        kw_only=True,
        default=bool(),
    )

    is_literal: bool = dataclasses.field(
        kw_only=True,
        default=bool(),
    )

    has_associativity_attribute: bool = dataclasses.field(
        kw_only=True,
        default=bool(),
    )

    has_arity_attribute: bool = dataclasses.field(
        kw_only=True,
        default=bool(),
    )

    has_arguments_attribute: bool = dataclasses.field(
        kw_only=True,
        default=bool(),
    )

    has_callee_attribute: bool = dataclasses.field(
        kw_only=True,
        default=bool(),
    )

    has_context_attribute: bool = dataclasses.field(
        kw_only=True,
        default=bool(),
    )

    has_elements_attribute: bool = dataclasses.field(
        kw_only=True,
        default=bool(),
    )

    has_name_attribute: bool = dataclasses.field(
        kw_only=True,
        default=bool(),
    )

    has_owner_attribute: bool = dataclasses.field(
        kw_only=True,
        default=bool(),
    )

    has_placement_attribute: bool = dataclasses.field(
        kw_only=True,
        default=bool(),
    )

    has_precedence_level_attribute: bool = dataclasses.field(
        kw_only=True,
        default=bool(),
    )

    has_type_attribute: bool = dataclasses.field(
        kw_only=True,
        default=bool(),
    )

    has_operands_attribute: bool = dataclasses.field(
        kw_only=True,
        default=bool(),
    )

    has_operator_attribute: bool = dataclasses.field(
        kw_only=True,
        default=bool(),
    )

    has_symbols_attribute: bool = dataclasses.field(
        kw_only=True,
        default=bool(),
    )

    has_value_attribute: bool = dataclasses.field(
        kw_only=True,
        default=bool(),
    )
