# SPDX-FileCopyrightText: 2024-present Trenton H <rda0128ou@mozmail.com>
#
# SPDX-License-Identifier: MPL-2.0
# Generated from:
#  Country Data: d055275324963c9bce5882eaaa93024cf2bf7ed0
#  Subdivision Data: 4f5658fa63afce8cd121d41444b28c2294e6b513
import dataclasses
from typing import Final
from typing import Literal

from simpleiso3166.base import DATACLASS_BASE_ARGS
from simpleiso3166.base import Country
from simpleiso3166.base import Subdivision

ERSubdivisionCodeType = Literal[
    "ER-AN",  # Ansabā
    "ER-DK",  # Janūbī al Baḩrī al Aḩmar
    "ER-DU",  # Al Janūbī
    "ER-GB",  # Qāsh-Barkah
    "ER-MA",  # Al Awsaţ
    "ER-SK",  # Shimālī al Baḩrī al Aḩmar
]


@dataclasses.dataclass(**DATACLASS_BASE_ARGS)
class ERSubdivision(Subdivision):
    code: ERSubdivisionCodeType


ER: Final[Country] = Country(
    alpha2="ER",
    alpha3="ERI",
    name="Eritrea",
    common_name=None,
    official_name="the State of Eritrea",
    subdivisions=[
        ERSubdivision(code="ER-AN", name="Ansabā", type_="Region"),
        ERSubdivision(code="ER-DK", name="Janūbī al Baḩrī al Aḩmar", type_="Region"),
        ERSubdivision(code="ER-DU", name="Al Janūbī", type_="Region"),
        ERSubdivision(code="ER-GB", name="Qāsh-Barkah", type_="Region"),
        ERSubdivision(code="ER-MA", name="Al Awsaţ", type_="Region"),
        ERSubdivision(code="ER-SK", name="Shimālī al Baḩrī al Aḩmar", type_="Region"),
    ],
)
