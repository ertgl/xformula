from xformula.syntax.core.features.abc import Feature

__all__ = [
    "PolyfillFeature",
]


class PolyfillFeature(Feature):
    class Meta:
        fqn = "xformula.core.Polyfill"

    def post_setup(self) -> None:
        from xformula.syntax.core.features.polyfill.generators import (
            NonTerminalTypeGenerator,
        )
        from xformula.syntax.core.features.validation.detectors import (
            MissingNonTerminalDetector,
        )

        missing_non_terminal_definitions = MissingNonTerminalDetector.detect(
            self.context,
        )

        generated_non_terminal_types = NonTerminalTypeGenerator.generate(
            self.context,
            missing_non_terminal_definitions,
        )

        self.non_terminal_types.extend(generated_non_terminal_types)

        self.context.register_feature_definitions(self)
