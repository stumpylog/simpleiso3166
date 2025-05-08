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

VUSubdivisionCodeType = Literal[
    "VU-MAP",  # Malampa
    "VU-PAM",  # Pénama
    "VU-SAM",  # Sanma
    "VU-SEE",  # Shéfa
    "VU-TAE",  # Taféa
    "VU-TOB",  # Torba
]


class VUSubdivision(Subdivision):
    code: VUSubdivisionCodeType
    name: str
    type_: SubdivisionTypeType


VU: Final[Country] = Country(
    alpha2="VU",
    alpha3="VUT",
    name="Vanuatu",
    common_name=None,
    official_name="Republic of Vanuatu",
    subdivisions=[
        VUSubdivision(code="VU-MAP", name="Malampa", type_="Province"),
        VUSubdivision(code="VU-PAM", name="Pénama", type_="Province"),
        VUSubdivision(code="VU-SAM", name="Sanma", type_="Province"),
        VUSubdivision(code="VU-SEE", name="Shéfa", type_="Province"),
        VUSubdivision(code="VU-TAE", name="Taféa", type_="Province"),
        VUSubdivision(code="VU-TOB", name="Torba", type_="Province"),
    ],
)
