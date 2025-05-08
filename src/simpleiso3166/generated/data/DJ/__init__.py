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

DJSubdivisionCodeType = Literal[
    "DJ-AR",  # Arta
    "DJ-AS",  # Ali Sabieh
    "DJ-DI",  # Dikhil
    "DJ-DJ",  # Djibouti
    "DJ-OB",  # Obock
    "DJ-TA",  # Tadjourah
]


class DJSubdivision(Subdivision):
    code: DJSubdivisionCodeType
    name: str
    type_: SubdivisionTypeType


DJ: Final[Country] = Country(
    alpha2="DJ",
    alpha3="DJI",
    name="Djibouti",
    common_name=None,
    official_name="Republic of Djibouti",
    subdivisions=[
        DJSubdivision(code="DJ-AR", name="Arta", type_="Region"),
        DJSubdivision(code="DJ-AS", name="Ali Sabieh", type_="Region"),
        DJSubdivision(code="DJ-DI", name="Dikhil", type_="Region"),
        DJSubdivision(code="DJ-DJ", name="Djibouti", type_="City"),
        DJSubdivision(code="DJ-OB", name="Obock", type_="Region"),
        DJSubdivision(code="DJ-TA", name="Tadjourah", type_="Region"),
    ],
)
