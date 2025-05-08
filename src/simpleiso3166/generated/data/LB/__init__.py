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

LBSubdivisionCodeType = Literal[
    "LB-AK",  # Aakkâr
    "LB-AS",  # Ash Shimāl
    "LB-BA",  # Bayrūt
    "LB-BH",  # Baalbek-Hermel
    "LB-BI",  # Al Biqā‘
    "LB-JA",  # Al Janūb
    "LB-JL",  # Jabal Lubnān
    "LB-NA",  # An Nabaţīyah
]


class LBSubdivision(Subdivision):
    code: LBSubdivisionCodeType
    name: str
    type_: SubdivisionTypeType


LB: Final[Country] = Country(
    alpha2="LB",
    alpha3="LBN",
    name="Lebanon",
    common_name=None,
    official_name="Lebanese Republic",
    subdivisions=[
        LBSubdivision(code="LB-AK", name="Aakkâr", type_="Governorate"),
        LBSubdivision(code="LB-AS", name="Ash Shimāl", type_="Governorate"),
        LBSubdivision(code="LB-BA", name="Bayrūt", type_="Governorate"),
        LBSubdivision(code="LB-BH", name="Baalbek-Hermel", type_="Governorate"),
        LBSubdivision(code="LB-BI", name="Al Biqā‘", type_="Governorate"),
        LBSubdivision(code="LB-JA", name="Al Janūb", type_="Governorate"),
        LBSubdivision(code="LB-JL", name="Jabal Lubnān", type_="Governorate"),
        LBSubdivision(code="LB-NA", name="An Nabaţīyah", type_="Governorate"),
    ],
)
