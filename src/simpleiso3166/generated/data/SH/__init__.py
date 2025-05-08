# SPDX-FileCopyrightText: 2024-present Trenton H <rda0128ou@mozmail.com>
#
# SPDX-License-Identifier: MPL-2.0
# Generated from:
#  Country Data: d055275324963c9bce5882eaaa93024cf2bf7ed0
#  Subdivision Data: 4f5658fa63afce8cd121d41444b28c2294e6b513
from typing import Final
from typing import Literal

from simpleiso3166.base import Country
from simpleiso3166.base import Subdivision
from simpleiso3166.generated.types import SubdivisionTypeType

SHSubdivisionCodeType = Literal[
    "SH-AC",  # Ascension
    "SH-HL",  # Saint Helena
    "SH-TA",  # Tristan da Cunha
]


class SHSubdivision(Subdivision):
    code: SHSubdivisionCodeType
    name: str
    type_: SubdivisionTypeType


SH: Final[Country] = Country(
    alpha2="SH",
    alpha3="SHN",
    name="Saint Helena, Ascension and Tristan da Cunha",
    common_name=None,
    official_name=None,
    subdivisions=[
        SHSubdivision(code="SH-AC", name="Ascension", type_="Geographical entity"),
        SHSubdivision(code="SH-HL", name="Saint Helena", type_="Geographical entity"),
        SHSubdivision(code="SH-TA", name="Tristan da Cunha", type_="Geographical entity"),
    ],
)
