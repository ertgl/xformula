import dataclasses

__all__ = [
    "Iota",
]


@dataclasses.dataclass()
class Iota:

    value: int = dataclasses.field(
        default=-1,
    )

    step: int = dataclasses.field(
        default=1,
    )

    def incr(self) -> int:
        self.value += self.step
        return self.value

    def reset(self) -> int:
        self.value = 0
        return self.value

    def __call__(
        self,
        reset: bool = False,
    ) -> int:
        if reset:
            return self.reset()
        return self.incr()
