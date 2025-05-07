# SPDX-FileCopyrightText: 2024-present Trenton H <rda0128ou@mozmail.com>
#
# SPDX-License-Identifier: MPL-2.0
from __future__ import annotations

import importlib
import sys
from dataclasses import dataclass
from functools import cached_property
from typing import TYPE_CHECKING
from typing import get_args

from simpleiso3166.countries.types import CountryCodeAlpha2Type

if TYPE_CHECKING:
    from collections.abc import Generator

    from simpleiso3166.subdivisions.types import SubdivisionCodeType
    from simpleiso3166.subdivisions.types import SubdivisionType

dataclass_args = {}

# Add slots=True if the Python version is 3.10 or higher
if sys.version_info >= (3, 10):
    dataclass_args["slots"] = True


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
        ratio: float | int = 80.0,
    ) -> Generator[Subdivision, None, None]:
        from rapidfuzz.fuzz import token_set_ratio
        from rapidfuzz.utils import default_process

        processed_name = default_process(subdivision_name)

        results: list[tuple[float, SubdivisionCodeType]] = []

        for country_code in get_args(CountryCodeAlpha2Type):  # type: ignore[misc]
            subdivisions = Subdivision.from_country_alpha2(country_code)  # type: ignore[misc]
            for subdivision in subdivisions:
                similarity = token_set_ratio(processed_name, default_process(subdivision.name))
                if similarity >= ratio:
                    results.append((similarity, subdivision))  # type: ignore[misc]

        sent = set()

        for result in sorted(results, key=lambda x: x[0], reverse=True):  # type: ignore[misc]
            if result[1] not in sent:
                yield result[1]
                sent.add(result[1])
