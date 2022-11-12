from xformula.arch.meta import Configurable
from xformula.syntax.ast.nodes.abc.node_meta import NodeMeta

__all__ = [
    "Node",
]


class Node(
    Configurable,
    metaclass=NodeMeta,
):
    class Meta(Configurable.Meta):

        abstract: bool = True

        is_start_point: bool = False

        is_expression: bool = False

        is_simple_expression: bool = False

        is_operation: bool = False

        is_operator: bool = False

        is_symbol: bool = True

        is_operand: bool = False

        is_primary: bool = False

        is_mapping: bool = False

        is_pair: bool = False

        is_container: bool = False

        is_term: bool = False

        is_call: bool = False

        is_attribute: bool = False

        is_identifier: bool = False

        is_literal: bool = False

        has_associativity_attribute: bool = False

        has_arity_attribute: bool = False

        has_arguments_attribute: bool = False

        has_callee_attribute: bool = False

        has_context_attribute: bool = False

        has_elements_attribute: bool = False

        has_name_attribute: bool = False

        has_owner_attribute: bool = False

        has_placement_attribute: bool = False

        has_precedence_level_attribute: bool = False

        has_type_attribute: bool = False

        has_operands_attribute: bool = False

        has_operator_attribute: bool = False

        has_symbols_attribute: bool = False

        has_value_attribute: bool = False
