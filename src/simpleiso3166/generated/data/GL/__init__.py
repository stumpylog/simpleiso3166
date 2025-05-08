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

GLSubdivisionCodeType = Literal[
    "GL-AV",  # Avannaata Kommunia
    "GL-KU",  # Kommune Kujalleq
    "GL-QE",  # Qeqqata Kommunia
    "GL-QT",  # Kommune Qeqertalik
    "GL-SM",  # Kommuneqarfik Sermersooq
]


class GLSubdivision(Subdivision):
    code: GLSubdivisionCodeType
    name: str
    type_: SubdivisionTypeType


GL: Final[Country] = Country(
    alpha2="GL",
    alpha3="GRL",
    name="Greenland",
    common_name=None,
    official_name=None,
    subdivisions=[
        GLSubdivision(code="GL-AV", name="Avannaata Kommunia", type_="Municipality"),
        GLSubdivision(code="GL-KU", name="Kommune Kujalleq", type_="Municipality"),
        GLSubdivision(code="GL-QE", name="Qeqqata Kommunia", type_="Municipality"),
        GLSubdivision(code="GL-QT", name="Kommune Qeqertalik", type_="Municipality"),
        GLSubdivision(code="GL-SM", name="Kommuneqarfik Sermersooq", type_="Municipality"),
    ],
)
