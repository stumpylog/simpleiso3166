# SPDX-FileCopyrightText: 2024-present Trenton H <rda0128ou@mozmail.com>
#
# SPDX-License-Identifier: MPL-2.0
from __future__ import annotations

import importlib
import sys
from dataclasses import dataclass
from functools import cached_property
from functools import lru_cache
from typing import TYPE_CHECKING
from typing import get_args

from simpleiso3166.countries.data.types import CountryCodeAlpha2Type

if TYPE_CHECKING:
    from collections.abc import Generator

    from simpleiso3166.subdivisions.types import SubdivisionCodeType
    from simpleiso3166.subdivisions.types import SubdivisionType

dataclass_args = {"frozen": True}

# Add slots=True if the Python version is 3.10 or higher
if sys.version_info >= (3, 10):
    dataclass_args["slots"] = True


@lru_cache(maxsize=1)
def _all_subdivisions() -> list[Subdivision]:
    subdivisions = []
    for country_code in get_args(CountryCodeAlpha2Type):  # type: ignore[misc]
        subdivisions.extend(Subdivision.from_country_alpha2(country_code))  # type: ignore[misc]
    return subdivisions


@dataclass(**dataclass_args)
class Subdivision:
    code: SubdivisionCodeType
    name: str
    type_: SubdivisionType

    @cached_property
    def country(self) -> CountryCodeAlpha2Type:
        code = self.code.split("-")[0]
        return code  # type: ignore[return-value]

    @staticmethod
    def from_country_alpha2(code: CountryCodeAlpha2Type) -> list[Subdivision]:
        module = importlib.import_module(f"simpleiso3166.subdivisions.data.{code}")
        return module.SUBDIVISIONS  # type: ignore[misc]

    @staticmethod
    def from_code(code: SubdivisionCodeType) -> Subdivision | None:
        for x in Subdivision.from_country_alpha2(code.split("-")[0]):
            if x.code == code:
                return x
        return None

    @staticmethod
    def search_by_name(
        subdivision_name: str,
        *,
        ratio: float | int | None = 80.0,
        limit: int = 10,
    ) -> Generator[Subdivision, None, None]:
        from rapidfuzz import fuzz
        from rapidfuzz import process
        from rapidfuzz.utils import default_process

        processed_name = default_process(subdivision_name)

        sent = 0
        for _, _, result in process.extract(
            processed_name,
            {x: default_process(x.name) for x in _all_subdivisions()},
            scorer=fuzz.WRatio,
            score_cutoff=ratio,
            limit=None,
        ):
            yield result
            sent += 1  # noqa: SIM113
            if sent >= limit:
                return
