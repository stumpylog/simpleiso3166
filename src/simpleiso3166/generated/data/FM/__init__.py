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

FMSubdivisionCodeType = Literal[
    "FM-KSA",  # Kosrae
    "FM-PNI",  # Pohnpei
    "FM-TRK",  # Chuuk
    "FM-YAP",  # Yap
]


class FMSubdivision(Subdivision):
    code: FMSubdivisionCodeType
    name: str
    type_: SubdivisionTypeType


FM: Final[Country] = Country(
    alpha2="FM",
    alpha3="FSM",
    name="Micronesia, Federated States of",
    common_name=None,
    official_name="Federated States of Micronesia",
    subdivisions=[
        FMSubdivision(code="FM-KSA", name="Kosrae", type_="State"),
        FMSubdivision(code="FM-PNI", name="Pohnpei", type_="State"),
        FMSubdivision(code="FM-TRK", name="Chuuk", type_="State"),
        FMSubdivision(code="FM-YAP", name="Yap", type_="State"),
    ],
)
