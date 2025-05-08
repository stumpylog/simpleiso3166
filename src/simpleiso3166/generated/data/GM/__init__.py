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

GMSubdivisionCodeType = Literal[
    "GM-B",  # Banjul
    "GM-L",  # Lower River
    "GM-M",  # Central River
    "GM-N",  # North Bank
    "GM-U",  # Upper River
    "GM-W",  # Western
]


class GMSubdivision(Subdivision):
    code: GMSubdivisionCodeType
    name: str
    type_: SubdivisionTypeType


GM: Final[Country] = Country(
    alpha2="GM",
    alpha3="GMB",
    name="Gambia",
    common_name=None,
    official_name="Republic of the Gambia",
    subdivisions=[
        GMSubdivision(code="GM-B", name="Banjul", type_="City"),
        GMSubdivision(code="GM-L", name="Lower River", type_="Division"),
        GMSubdivision(code="GM-M", name="Central River", type_="Division"),
        GMSubdivision(code="GM-N", name="North Bank", type_="Division"),
        GMSubdivision(code="GM-U", name="Upper River", type_="Division"),
        GMSubdivision(code="GM-W", name="Western", type_="Division"),
    ],
)
