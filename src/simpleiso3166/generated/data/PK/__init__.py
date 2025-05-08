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

PKSubdivisionCodeType = Literal[
    "PK-BA",  # Balochistan
    "PK-GB",  # Gilgit-Baltistan
    "PK-IS",  # Islamabad
    "PK-JK",  # Azad Jammu and Kashmir
    "PK-KP",  # Khyber Pakhtunkhwa
    "PK-PB",  # Punjab
    "PK-SD",  # Sindh
]


class PKSubdivision(Subdivision):
    code: PKSubdivisionCodeType
    name: str
    type_: SubdivisionTypeType


PK: Final[Country] = Country(
    alpha2="PK",
    alpha3="PAK",
    name="Pakistan",
    common_name=None,
    official_name="Islamic Republic of Pakistan",
    subdivisions=[
        PKSubdivision(code="PK-BA", name="Balochistan", type_="Province"),
        PKSubdivision(code="PK-GB", name="Gilgit-Baltistan", type_="Pakistan administered area"),
        PKSubdivision(code="PK-IS", name="Islamabad", type_="Federal capital territory"),
        PKSubdivision(code="PK-JK", name="Azad Jammu and Kashmir", type_="Pakistan administered area"),
        PKSubdivision(code="PK-KP", name="Khyber Pakhtunkhwa", type_="Province"),
        PKSubdivision(code="PK-PB", name="Punjab", type_="Province"),
        PKSubdivision(code="PK-SD", name="Sindh", type_="Province"),
    ],
)
