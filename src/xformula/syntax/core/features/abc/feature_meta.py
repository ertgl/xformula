from typing import Any, TypeVar

from xformula.arch.meta import Meta
from xformula.syntax.core.features.abc.feature_options import FeatureOptions

__all__ = [
    "FeatureMeta",
]


C = TypeVar("C", bound="FeatureMeta")


class FeatureMeta(
    Meta[FeatureOptions],
):

    options_class = FeatureOptions

    options: FeatureOptions

    @classmethod
    def get_excluded_super_options_attnames(
        mcs,
        name: str,
        bases: tuple[type, ...],
        namespace: dict[str, Any],
        **kwargs: Any,
    ) -> set[str]:
        excluded = super(FeatureMeta, mcs).get_excluded_super_options_attnames(
            name,
            bases,
            namespace,
            **kwargs,
        )
        excluded.add("fqn")
        return excluded

    @classmethod
    def post_generate(
        mcs: type[C],
        name: str,
        bases: tuple[type, ...],
        namespace: dict[str, Any],
        meta: Any | None,
        generated_type: C,
        **kwargs: Any,
    ) -> None:
        if not generated_type.options.fqn:
            generated_type.options.fqn = ".".join(
                [
                    generated_type.__module__,
                    generated_type.__qualname__,
                ],
            )
