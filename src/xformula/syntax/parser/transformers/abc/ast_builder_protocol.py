from abc import ABC

from xformula.syntax.parser.transformers.abc.transformer import Transformer

__all__ = [
    "ASTBuilderProtocol",
]


class ASTBuilderProtocol(
    Transformer,
    ABC,
):
    ...
