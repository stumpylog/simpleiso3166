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

ATSubdivisionCodeType = Literal[
    "AT-1",  # Burgenland
    "AT-2",  # Kärnten
    "AT-3",  # Niederösterreich
    "AT-4",  # Oberösterreich
    "AT-5",  # Salzburg
    "AT-6",  # Steiermark
    "AT-7",  # Tirol
    "AT-8",  # Vorarlberg
    "AT-9",  # Wien
]


class ATSubdivision(Subdivision):
    code: ATSubdivisionCodeType
    name: str
    type_: SubdivisionTypeType


AT: Final[Country] = Country(
    alpha2="AT",
    alpha3="AUT",
    name="Austria",
    common_name=None,
    official_name="Republic of Austria",
    subdivisions=[
        ATSubdivision(code="AT-1", name="Burgenland", type_="State"),
        ATSubdivision(code="AT-2", name="Kärnten", type_="State"),
        ATSubdivision(code="AT-3", name="Niederösterreich", type_="State"),
        ATSubdivision(code="AT-4", name="Oberösterreich", type_="State"),
        ATSubdivision(code="AT-5", name="Salzburg", type_="State"),
        ATSubdivision(code="AT-6", name="Steiermark", type_="State"),
        ATSubdivision(code="AT-7", name="Tirol", type_="State"),
        ATSubdivision(code="AT-8", name="Vorarlberg", type_="State"),
        ATSubdivision(code="AT-9", name="Wien", type_="State"),
    ],
)
