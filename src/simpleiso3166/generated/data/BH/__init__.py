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

BHSubdivisionCodeType = Literal[
    "BH-13",  # Al ‘Āşimah
    "BH-14",  # Al Janūbīyah
    "BH-15",  # Al Muḩarraq
    "BH-17",  # Ash Shamālīyah
]


class BHSubdivision(Subdivision):
    code: BHSubdivisionCodeType
    name: str
    type_: SubdivisionTypeType


BH: Final[Country] = Country(
    alpha2="BH",
    alpha3="BHR",
    name="Bahrain",
    common_name=None,
    official_name="Kingdom of Bahrain",
    subdivisions=[
        BHSubdivision(code="BH-13", name="Al ‘Āşimah", type_="Governorate"),
        BHSubdivision(code="BH-14", name="Al Janūbīyah", type_="Governorate"),
        BHSubdivision(code="BH-15", name="Al Muḩarraq", type_="Governorate"),
        BHSubdivision(code="BH-17", name="Ash Shamālīyah", type_="Governorate"),
    ],
)
