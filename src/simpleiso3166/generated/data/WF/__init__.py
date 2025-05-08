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

WFSubdivisionCodeType = Literal[
    "WF-AL",  # Alo
    "WF-SG",  # Sigave
    "WF-UV",  # Uvea
]


class WFSubdivision(Subdivision):
    code: WFSubdivisionCodeType
    name: str
    type_: SubdivisionTypeType


WF: Final[Country] = Country(
    alpha2="WF",
    alpha3="WLF",
    name="Wallis and Futuna",
    common_name=None,
    official_name=None,
    subdivisions=[
        WFSubdivision(code="WF-AL", name="Alo", type_="Administrative precinct"),
        WFSubdivision(code="WF-SG", name="Sigave", type_="Administrative precinct"),
        WFSubdivision(code="WF-UV", name="Uvea", type_="Administrative precinct"),
    ],
)
