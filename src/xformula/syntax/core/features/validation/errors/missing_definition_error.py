__all__ = [
    "MissingDefinitionError",
]


class MissingDefinitionError(Exception):

    missing_definitions: dict[str, dict[str, set[str]]]

    @classmethod
    def build_message(
        cls,
        missing_definitions: dict[str, dict[str, set[str]]],
    ) -> str:
        message = "\n".join(
            [
                f"Missing {definition_type} definitions:\n"
                f"\t⧃ {missing_name} : ({' | '.join(alternation)})"
                for definition_type, detected in missing_definitions.items()
                for missing_name, alternation in detected.items()
            ],
        )
        return message

    def __init__(
        self,
        missing_definitions: dict[str, dict[str, set[str]]],
    ) -> None:
        self.missing_definitions = missing_definitions
        super(MissingDefinitionError, self).__init__(
            f"\n\n{self.__class__.build_message(self.missing_definitions)}",
        )
