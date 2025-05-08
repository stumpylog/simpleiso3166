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

GQSubdivisionCodeType = Literal[
    "GQ-AN",  # Annobon
    "GQ-BN",  # Bioko Nord
    "GQ-BS",  # Bioko Sud
    "GQ-C",  # Région Continentale
    "GQ-CS",  # Centro Sud
    "GQ-DJ",  # Djibloho
    "GQ-I",  # Région Insulaire
    "GQ-KN",  # Kié-Ntem
    "GQ-LI",  # Littoral
    "GQ-WN",  # Wele-Nzas
]


class GQSubdivision(Subdivision):
    code: GQSubdivisionCodeType
    name: str
    type_: SubdivisionTypeType


GQ: Final[Country] = Country(
    alpha2="GQ",
    alpha3="GNQ",
    name="Equatorial Guinea",
    common_name=None,
    official_name="Republic of Equatorial Guinea",
    subdivisions=[
        GQSubdivision(code="GQ-AN", name="Annobon", type_="Province"),
        GQSubdivision(code="GQ-BN", name="Bioko Nord", type_="Province"),
        GQSubdivision(code="GQ-BS", name="Bioko Sud", type_="Province"),
        GQSubdivision(code="GQ-C", name="Région Continentale", type_="Region"),
        GQSubdivision(code="GQ-CS", name="Centro Sud", type_="Province"),
        GQSubdivision(code="GQ-DJ", name="Djibloho", type_="Province"),
        GQSubdivision(code="GQ-I", name="Région Insulaire", type_="Region"),
        GQSubdivision(code="GQ-KN", name="Kié-Ntem", type_="Province"),
        GQSubdivision(code="GQ-LI", name="Littoral", type_="Province"),
        GQSubdivision(code="GQ-WN", name="Wele-Nzas", type_="Province"),
    ],
)
