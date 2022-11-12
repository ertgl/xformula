import dataclasses

from xformula.arch.meta import Options

__all__ = [
    "FeatureOptions",
]


@dataclasses.dataclass()
class FeatureOptions(Options):

    fqn: str = dataclasses.field(
        kw_only=True,
        default=str(),
    )
