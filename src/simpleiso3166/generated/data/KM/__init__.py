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

KMSubdivisionCodeType = Literal[
    "KM-A",  # Anjouan
    "KM-G",  # Grande Comore
    "KM-M",  # Mohéli
]


class KMSubdivision(Subdivision):
    code: KMSubdivisionCodeType
    name: str
    type_: SubdivisionTypeType


KM: Final[Country] = Country(
    alpha2="KM",
    alpha3="COM",
    name="Comoros",
    common_name=None,
    official_name="Union of the Comoros",
    subdivisions=[
        KMSubdivision(code="KM-A", name="Anjouan", type_="Island"),
        KMSubdivision(code="KM-G", name="Grande Comore", type_="Island"),
        KMSubdivision(code="KM-M", name="Mohéli", type_="Island"),
    ],
)
