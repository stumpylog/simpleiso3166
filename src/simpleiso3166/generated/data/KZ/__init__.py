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

KZSubdivisionCodeType = Literal[
    "KZ-10",  # Abay oblysy
    "KZ-11",  # Aqmola oblysy
    "KZ-15",  # Aqtöbe oblysy
    "KZ-19",  # Almaty oblysy
    "KZ-23",  # Atyraū oblysy
    "KZ-27",  # Batys Qazaqstan oblysy
    "KZ-31",  # Zhambyl oblysy
    "KZ-33",  # Zhetisū oblysy
    "KZ-35",  # Qaraghandy oblysy
    "KZ-39",  # Qostanay oblysy
    "KZ-43",  # Qyzylorda oblysy
    "KZ-47",  # Mangghystaū oblysy
    "KZ-55",  # Pavlodar oblysy
    "KZ-59",  # Soltüstik Qazaqstan oblysy
    "KZ-61",  # Türkistan oblysy
    "KZ-62",  # Ulytaū oblysy
    "KZ-63",  # Shyghys Qazaqstan oblysy
    "KZ-71",  # Astana
    "KZ-75",  # Almaty
    "KZ-79",  # Shymkent
]


@dataclasses.dataclass(**DATACLASS_BASE_ARGS)
class KZSubdivision(Subdivision):
    code: KZSubdivisionCodeType


KZ: Final[Country] = Country(
    alpha2="KZ",
    alpha3="KAZ",
    name="Kazakhstan",
    common_name=None,
    official_name="Republic of Kazakhstan",
    subdivisions=[
        KZSubdivision(code="KZ-10", name="Abay oblysy", type_="Region"),
        KZSubdivision(code="KZ-11", name="Aqmola oblysy", type_="Region"),
        KZSubdivision(code="KZ-15", name="Aqtöbe oblysy", type_="Region"),
        KZSubdivision(code="KZ-19", name="Almaty oblysy", type_="Region"),
        KZSubdivision(code="KZ-23", name="Atyraū oblysy", type_="Region"),
        KZSubdivision(code="KZ-27", name="Batys Qazaqstan oblysy", type_="Region"),
        KZSubdivision(code="KZ-31", name="Zhambyl oblysy", type_="Region"),
        KZSubdivision(code="KZ-33", name="Zhetisū oblysy", type_="Region"),
        KZSubdivision(code="KZ-35", name="Qaraghandy oblysy", type_="Region"),
        KZSubdivision(code="KZ-39", name="Qostanay oblysy", type_="Region"),
        KZSubdivision(code="KZ-43", name="Qyzylorda oblysy", type_="Region"),
        KZSubdivision(code="KZ-47", name="Mangghystaū oblysy", type_="Region"),
        KZSubdivision(code="KZ-55", name="Pavlodar oblysy", type_="Region"),
        KZSubdivision(code="KZ-59", name="Soltüstik Qazaqstan oblysy", type_="Region"),
        KZSubdivision(code="KZ-61", name="Türkistan oblysy", type_="Region"),
        KZSubdivision(code="KZ-62", name="Ulytaū oblysy", type_="Region"),
        KZSubdivision(code="KZ-63", name="Shyghys Qazaqstan oblysy", type_="Region"),
        KZSubdivision(code="KZ-71", name="Astana", type_="City"),
        KZSubdivision(code="KZ-75", name="Almaty", type_="City"),
        KZSubdivision(code="KZ-79", name="Shymkent", type_="City"),
    ],
)
