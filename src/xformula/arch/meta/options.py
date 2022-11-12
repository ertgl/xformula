import dataclasses

__all__ = [
    "Options",
]


@dataclasses.dataclass()
class Options:

    name: str = dataclasses.field(
        kw_only=True,
        default=str(),
    )

    abstract: bool = dataclasses.field(
        kw_only=True,
        default=bool(),
    )
