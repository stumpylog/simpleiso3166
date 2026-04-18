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

BYSubdivisionCodeType = Literal[
    "BY-BR",  # Bresckaja voblasć
    "BY-HM",  # Horad Minsk
    "BY-HO",  # Homieĺskaja voblasć
    "BY-HR",  # Hrodzienskaja voblasć
    "BY-MA",  # Mahilioŭskaja voblasć
    "BY-MI",  # Minskaja voblasć
    "BY-VI",  # Viciebskaja voblasć
]


@dataclasses.dataclass(**DATACLASS_BASE_ARGS)
class BYSubdivision(Subdivision):
    code: BYSubdivisionCodeType


BY: Final[Country] = Country(
    alpha2="BY",
    alpha3="BLR",
    name="Belarus",
    common_name=None,
    official_name="Republic of Belarus",
    subdivisions=[
        BYSubdivision(code="BY-BR", name="Bresckaja voblasć", type_="Oblast"),
        BYSubdivision(code="BY-HM", name="Horad Minsk", type_="City"),
        BYSubdivision(code="BY-HO", name="Homieĺskaja voblasć", type_="Oblast"),
        BYSubdivision(code="BY-HR", name="Hrodzienskaja voblasć", type_="Oblast"),
        BYSubdivision(code="BY-MA", name="Mahilioŭskaja voblasć", type_="Oblast"),
        BYSubdivision(code="BY-MI", name="Minskaja voblasć", type_="Oblast"),
        BYSubdivision(code="BY-VI", name="Viciebskaja voblasć", type_="Oblast"),
    ],
)
