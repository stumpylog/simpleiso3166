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

SOSubdivisionCodeType = Literal[
    "SO-AW",  # Awdal
    "SO-BK",  # Bakool
    "SO-BN",  # Banaadir
    "SO-BR",  # Bari
    "SO-BY",  # Bay
    "SO-GA",  # Galguduud
    "SO-GE",  # Gedo
    "SO-HI",  # Hiiraan
    "SO-JD",  # Jubbada Dhexe
    "SO-JH",  # Jubbada Hoose
    "SO-MU",  # Mudug
    "SO-NU",  # Nugaal
    "SO-SA",  # Sanaag
    "SO-SD",  # Shabeellaha Dhexe
    "SO-SH",  # Shabeellaha Hoose
    "SO-SO",  # Sool
    "SO-TO",  # Togdheer
    "SO-WO",  # Woqooyi Galbeed
]


class SOSubdivision(Subdivision):
    code: SOSubdivisionCodeType
    name: str
    type_: SubdivisionTypeType


SO: Final[Country] = Country(
    alpha2="SO",
    alpha3="SOM",
    name="Somalia",
    common_name=None,
    official_name="Federal Republic of Somalia",
    subdivisions=[
        SOSubdivision(code="SO-AW", name="Awdal", type_="Region"),
        SOSubdivision(code="SO-BK", name="Bakool", type_="Region"),
        SOSubdivision(code="SO-BN", name="Banaadir", type_="Region"),
        SOSubdivision(code="SO-BR", name="Bari", type_="Region"),
        SOSubdivision(code="SO-BY", name="Bay", type_="Region"),
        SOSubdivision(code="SO-GA", name="Galguduud", type_="Region"),
        SOSubdivision(code="SO-GE", name="Gedo", type_="Region"),
        SOSubdivision(code="SO-HI", name="Hiiraan", type_="Region"),
        SOSubdivision(code="SO-JD", name="Jubbada Dhexe", type_="Region"),
        SOSubdivision(code="SO-JH", name="Jubbada Hoose", type_="Region"),
        SOSubdivision(code="SO-MU", name="Mudug", type_="Region"),
        SOSubdivision(code="SO-NU", name="Nugaal", type_="Region"),
        SOSubdivision(code="SO-SA", name="Sanaag", type_="Region"),
        SOSubdivision(code="SO-SD", name="Shabeellaha Dhexe", type_="Region"),
        SOSubdivision(code="SO-SH", name="Shabeellaha Hoose", type_="Region"),
        SOSubdivision(code="SO-SO", name="Sool", type_="Region"),
        SOSubdivision(code="SO-TO", name="Togdheer", type_="Region"),
        SOSubdivision(code="SO-WO", name="Woqooyi Galbeed", type_="Region"),
    ],
)
