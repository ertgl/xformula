from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from xformula.syntax.core.context.abc.syntax_context import SyntaxContext

__all__ = [
    "MissingNonTerminalDetector",
]


class MissingNonTerminalDetector:

    syntax_context: "SyntaxContext"

    @classmethod
    def detect(
        cls,
        syntax_context: "SyntaxContext",
    ) -> dict[str, set[str]]:
        detector = cls(syntax_context)
        return detector.find_tags_have_no_definition()

    def __init__(self, syntax_context: "SyntaxContext") -> None:
        self.syntax_context = syntax_context

    def find_tags_have_no_definition(self) -> dict[str, set[str]]:
        detected: dict[str, set[str]] = dict()
        defined_tags = {
            definition.__class__.options.definition_name
            for definition in self.syntax_context.non_terminals
        }
        for tag, alternation in self.syntax_context.tagged_definitions.items():
            if tag not in defined_tags:
                detected[tag] = {
                    wanted_by_definition.__class__.options.definition_name
                    for wanted_by_definition in alternation
                }
        return detected
