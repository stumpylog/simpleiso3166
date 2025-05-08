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

TGSubdivisionCodeType = Literal[
    "TG-C",  # Centrale
    "TG-K",  # Kara
    "TG-M",  # Maritime (Région)
    "TG-P",  # Plateaux
    "TG-S",  # Savanes
]


class TGSubdivision(Subdivision):
    code: TGSubdivisionCodeType
    name: str
    type_: SubdivisionTypeType


TG: Final[Country] = Country(
    alpha2="TG",
    alpha3="TGO",
    name="Togo",
    common_name=None,
    official_name="Togolese Republic",
    subdivisions=[
        TGSubdivision(code="TG-C", name="Centrale", type_="Region"),
        TGSubdivision(code="TG-K", name="Kara", type_="Region"),
        TGSubdivision(code="TG-M", name="Maritime (Région)", type_="Region"),
        TGSubdivision(code="TG-P", name="Plateaux", type_="Region"),
        TGSubdivision(code="TG-S", name="Savanes", type_="Region"),
    ],
)
