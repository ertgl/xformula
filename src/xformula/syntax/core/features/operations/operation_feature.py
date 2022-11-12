from xformula.syntax.core.features.abc import Feature

__all__ = [
    "OperationFeature",
]


class OperationFeature(Feature):
    class Meta:
        fqn = "xformula.core.Operation"

    def setup(self) -> None:
        from xformula.syntax.core.features.operations.definitions.non_terminals import (
            Operand,
            Operation,
        )
        from xformula.syntax.core.features.operations.generators import (
            NonTerminalOperationTypeGenerator,
        )

        non_terminal_operation_types = NonTerminalOperationTypeGenerator.generate(
            self.context,
        )

        self.non_terminal_types.append(Operand)
        self.non_terminal_types.extend(non_terminal_operation_types)
        self.non_terminal_types.append(Operation)
