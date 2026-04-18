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

RUSubdivisionCodeType = Literal[
    "RU-AD",  # Adygeya, Respublika
    "RU-AL",  # Altay, Respublika
    "RU-ALT",  # Altayskiy kray
    "RU-AMU",  # Amurskaya oblast'
    "RU-ARK",  # Arkhangel'skaya oblast'
    "RU-AST",  # Astrakhanskaya oblast'
    "RU-BA",  # Bashkortostan, Respublika
    "RU-BEL",  # Belgorodskaya oblast'
    "RU-BRY",  # Bryanskaya oblast'
    "RU-BU",  # Buryatiya, Respublika
    "RU-CE",  # Chechenskaya Respublika
    "RU-CHE",  # Chelyabinskaya oblast'
    "RU-CHU",  # Chukotskiy avtonomnyy okrug
    "RU-CU",  # Chuvashskaya Respublika
    "RU-DA",  # Dagestan, Respublika
    "RU-IN",  # Ingushetiya, Respublika
    "RU-IRK",  # Irkutskaya oblast'
    "RU-IVA",  # Ivanovskaya oblast'
    "RU-KAM",  # Kamchatskiy kray
    "RU-KB",  # Kabardino-Balkarskaya Respublika
    "RU-KC",  # Karachayevo-Cherkesskaya Respublika
    "RU-KDA",  # Krasnodarskiy kray
    "RU-KEM",  # Kemerovskaya oblast'
    "RU-KGD",  # Kaliningradskaya oblast'
    "RU-KGN",  # Kurganskaya oblast'
    "RU-KHA",  # Khabarovskiy kray
    "RU-KHM",  # Khanty-Mansiyskiy avtonomnyy okrug
    "RU-KIR",  # Kirovskaya oblast'
    "RU-KK",  # Khakasiya, Respublika
    "RU-KL",  # Kalmykiya, Respublika
    "RU-KLU",  # Kaluzhskaya oblast'
    "RU-KO",  # Komi, Respublika
    "RU-KOS",  # Kostromskaya oblast'
    "RU-KR",  # Kareliya, Respublika
    "RU-KRS",  # Kurskaya oblast'
    "RU-KYA",  # Krasnoyarskiy kray
    "RU-LEN",  # Leningradskaya oblast'
    "RU-LIP",  # Lipetskaya oblast'
    "RU-MAG",  # Magadanskaya oblast'
    "RU-ME",  # Mariy El, Respublika
    "RU-MO",  # Mordoviya, Respublika
    "RU-MOS",  # Moskovskaya oblast'
    "RU-MOW",  # Moskva
    "RU-MUR",  # Murmanskaya oblast'
    "RU-NEN",  # Nenetskiy avtonomnyy okrug
    "RU-NGR",  # Novgorodskaya oblast'
    "RU-NIZ",  # Nizhegorodskaya oblast'
    "RU-NVS",  # Novosibirskaya oblast'
    "RU-OMS",  # Omskaya oblast'
    "RU-ORE",  # Orenburgskaya oblast'
    "RU-ORL",  # Orlovskaya oblast'
    "RU-PER",  # Permskiy kray
    "RU-PNZ",  # Penzenskaya oblast'
    "RU-PRI",  # Primorskiy kray
    "RU-PSK",  # Pskovskaya oblast'
    "RU-ROS",  # Rostovskaya oblast'
    "RU-RYA",  # Ryazanskaya oblast'
    "RU-SA",  # Saha, Respublika
    "RU-SAK",  # Sakhalinskaya oblast'
    "RU-SAM",  # Samarskaya oblast'
    "RU-SAR",  # Saratovskaya oblast'
    "RU-SE",  # Severnaya Osetiya, Respublika
    "RU-SMO",  # Smolenskaya oblast'
    "RU-SPE",  # Sankt-Peterburg
    "RU-STA",  # Stavropol'skiy kray
    "RU-SVE",  # Sverdlovskaya oblast'
    "RU-TA",  # Tatarstan, Respublika
    "RU-TAM",  # Tambovskaya oblast'
    "RU-TOM",  # Tomskaya oblast'
    "RU-TUL",  # Tul'skaya oblast'
    "RU-TVE",  # Tverskaya oblast'
    "RU-TY",  # Tyva, Respublika
    "RU-TYU",  # Tyumenskaya oblast'
    "RU-UD",  # Udmurtskaya Respublika
    "RU-ULY",  # Ul'yanovskaya oblast'
    "RU-VGG",  # Volgogradskaya oblast'
    "RU-VLA",  # Vladimirskaya oblast'
    "RU-VLG",  # Vologodskaya oblast'
    "RU-VOR",  # Voronezhskaya oblast'
    "RU-YAN",  # Yamalo-Nenetskiy avtonomnyy okrug
    "RU-YAR",  # Yaroslavskaya oblast'
    "RU-YEV",  # Yevreyskaya avtonomnaya oblast'
    "RU-ZAB",  # Zabaykal'skiy kray
]


@dataclasses.dataclass(**DATACLASS_BASE_ARGS)
class RUSubdivision(Subdivision):
    code: RUSubdivisionCodeType


RU: Final[Country] = Country(
    alpha2="RU",
    alpha3="RUS",
    name="Russian Federation",
    common_name=None,
    official_name=None,
    subdivisions=[
        RUSubdivision(code="RU-AD", name="Adygeya, Respublika", type_="Republic"),
        RUSubdivision(code="RU-AL", name="Altay, Respublika", type_="Republic"),
        RUSubdivision(code="RU-ALT", name="Altayskiy kray", type_="Administrative territory"),
        RUSubdivision(code="RU-AMU", name="Amurskaya oblast'", type_="Administrative region"),
        RUSubdivision(code="RU-ARK", name="Arkhangel'skaya oblast'", type_="Administrative region"),
        RUSubdivision(code="RU-AST", name="Astrakhanskaya oblast'", type_="Administrative region"),
        RUSubdivision(code="RU-BA", name="Bashkortostan, Respublika", type_="Republic"),
        RUSubdivision(code="RU-BEL", name="Belgorodskaya oblast'", type_="Administrative region"),
        RUSubdivision(code="RU-BRY", name="Bryanskaya oblast'", type_="Administrative region"),
        RUSubdivision(code="RU-BU", name="Buryatiya, Respublika", type_="Republic"),
        RUSubdivision(code="RU-CE", name="Chechenskaya Respublika", type_="Republic"),
        RUSubdivision(code="RU-CHE", name="Chelyabinskaya oblast'", type_="Administrative region"),
        RUSubdivision(code="RU-CHU", name="Chukotskiy avtonomnyy okrug", type_="Autonomous district"),
        RUSubdivision(code="RU-CU", name="Chuvashskaya Respublika", type_="Republic"),
        RUSubdivision(code="RU-DA", name="Dagestan, Respublika", type_="Republic"),
        RUSubdivision(code="RU-IN", name="Ingushetiya, Respublika", type_="Republic"),
        RUSubdivision(code="RU-IRK", name="Irkutskaya oblast'", type_="Administrative region"),
        RUSubdivision(code="RU-IVA", name="Ivanovskaya oblast'", type_="Administrative region"),
        RUSubdivision(code="RU-KAM", name="Kamchatskiy kray", type_="Administrative territory"),
        RUSubdivision(code="RU-KB", name="Kabardino-Balkarskaya Respublika", type_="Republic"),
        RUSubdivision(code="RU-KC", name="Karachayevo-Cherkesskaya Respublika", type_="Republic"),
        RUSubdivision(code="RU-KDA", name="Krasnodarskiy kray", type_="Administrative territory"),
        RUSubdivision(code="RU-KEM", name="Kemerovskaya oblast'", type_="Administrative region"),
        RUSubdivision(code="RU-KGD", name="Kaliningradskaya oblast'", type_="Administrative region"),
        RUSubdivision(code="RU-KGN", name="Kurganskaya oblast'", type_="Administrative region"),
        RUSubdivision(code="RU-KHA", name="Khabarovskiy kray", type_="Administrative territory"),
        RUSubdivision(code="RU-KHM", name="Khanty-Mansiyskiy avtonomnyy okrug", type_="Autonomous district"),
        RUSubdivision(code="RU-KIR", name="Kirovskaya oblast'", type_="Administrative region"),
        RUSubdivision(code="RU-KK", name="Khakasiya, Respublika", type_="Republic"),
        RUSubdivision(code="RU-KL", name="Kalmykiya, Respublika", type_="Republic"),
        RUSubdivision(code="RU-KLU", name="Kaluzhskaya oblast'", type_="Administrative region"),
        RUSubdivision(code="RU-KO", name="Komi, Respublika", type_="Republic"),
        RUSubdivision(code="RU-KOS", name="Kostromskaya oblast'", type_="Administrative region"),
        RUSubdivision(code="RU-KR", name="Kareliya, Respublika", type_="Republic"),
        RUSubdivision(code="RU-KRS", name="Kurskaya oblast'", type_="Administrative region"),
        RUSubdivision(code="RU-KYA", name="Krasnoyarskiy kray", type_="Administrative territory"),
        RUSubdivision(code="RU-LEN", name="Leningradskaya oblast'", type_="Administrative region"),
        RUSubdivision(code="RU-LIP", name="Lipetskaya oblast'", type_="Administrative region"),
        RUSubdivision(code="RU-MAG", name="Magadanskaya oblast'", type_="Administrative region"),
        RUSubdivision(code="RU-ME", name="Mariy El, Respublika", type_="Republic"),
        RUSubdivision(code="RU-MO", name="Mordoviya, Respublika", type_="Republic"),
        RUSubdivision(code="RU-MOS", name="Moskovskaya oblast'", type_="Administrative region"),
        RUSubdivision(code="RU-MOW", name="Moskva", type_="Autonomous city"),
        RUSubdivision(code="RU-MUR", name="Murmanskaya oblast'", type_="Administrative region"),
        RUSubdivision(code="RU-NEN", name="Nenetskiy avtonomnyy okrug", type_="Autonomous district"),
        RUSubdivision(code="RU-NGR", name="Novgorodskaya oblast'", type_="Administrative region"),
        RUSubdivision(code="RU-NIZ", name="Nizhegorodskaya oblast'", type_="Administrative region"),
        RUSubdivision(code="RU-NVS", name="Novosibirskaya oblast'", type_="Administrative region"),
        RUSubdivision(code="RU-OMS", name="Omskaya oblast'", type_="Administrative region"),
        RUSubdivision(code="RU-ORE", name="Orenburgskaya oblast'", type_="Administrative region"),
        RUSubdivision(code="RU-ORL", name="Orlovskaya oblast'", type_="Administrative region"),
        RUSubdivision(code="RU-PER", name="Permskiy kray", type_="Administrative territory"),
        RUSubdivision(code="RU-PNZ", name="Penzenskaya oblast'", type_="Administrative region"),
        RUSubdivision(code="RU-PRI", name="Primorskiy kray", type_="Administrative territory"),
        RUSubdivision(code="RU-PSK", name="Pskovskaya oblast'", type_="Administrative region"),
        RUSubdivision(code="RU-ROS", name="Rostovskaya oblast'", type_="Administrative region"),
        RUSubdivision(code="RU-RYA", name="Ryazanskaya oblast'", type_="Administrative region"),
        RUSubdivision(code="RU-SA", name="Saha, Respublika", type_="Republic"),
        RUSubdivision(code="RU-SAK", name="Sakhalinskaya oblast'", type_="Administrative region"),
        RUSubdivision(code="RU-SAM", name="Samarskaya oblast'", type_="Administrative region"),
        RUSubdivision(code="RU-SAR", name="Saratovskaya oblast'", type_="Administrative region"),
        RUSubdivision(code="RU-SE", name="Severnaya Osetiya, Respublika", type_="Republic"),
        RUSubdivision(code="RU-SMO", name="Smolenskaya oblast'", type_="Administrative region"),
        RUSubdivision(code="RU-SPE", name="Sankt-Peterburg", type_="Autonomous city"),
        RUSubdivision(code="RU-STA", name="Stavropol'skiy kray", type_="Administrative territory"),
        RUSubdivision(code="RU-SVE", name="Sverdlovskaya oblast'", type_="Administrative region"),
        RUSubdivision(code="RU-TA", name="Tatarstan, Respublika", type_="Republic"),
        RUSubdivision(code="RU-TAM", name="Tambovskaya oblast'", type_="Administrative region"),
        RUSubdivision(code="RU-TOM", name="Tomskaya oblast'", type_="Administrative region"),
        RUSubdivision(code="RU-TUL", name="Tul'skaya oblast'", type_="Administrative region"),
        RUSubdivision(code="RU-TVE", name="Tverskaya oblast'", type_="Administrative region"),
        RUSubdivision(code="RU-TY", name="Tyva, Respublika", type_="Republic"),
        RUSubdivision(code="RU-TYU", name="Tyumenskaya oblast'", type_="Administrative region"),
        RUSubdivision(code="RU-UD", name="Udmurtskaya Respublika", type_="Republic"),
        RUSubdivision(code="RU-ULY", name="Ul'yanovskaya oblast'", type_="Administrative region"),
        RUSubdivision(code="RU-VGG", name="Volgogradskaya oblast'", type_="Administrative region"),
        RUSubdivision(code="RU-VLA", name="Vladimirskaya oblast'", type_="Administrative region"),
        RUSubdivision(code="RU-VLG", name="Vologodskaya oblast'", type_="Administrative region"),
        RUSubdivision(code="RU-VOR", name="Voronezhskaya oblast'", type_="Administrative region"),
        RUSubdivision(code="RU-YAN", name="Yamalo-Nenetskiy avtonomnyy okrug", type_="Autonomous district"),
        RUSubdivision(code="RU-YAR", name="Yaroslavskaya oblast'", type_="Administrative region"),
        RUSubdivision(code="RU-YEV", name="Yevreyskaya avtonomnaya oblast'", type_="Autonomous region"),
        RUSubdivision(code="RU-ZAB", name="Zabaykal'skiy kray", type_="Administrative territory"),
    ],
)
