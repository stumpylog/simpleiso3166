import json
import sys
from collections import defaultdict
from io import TextIOWrapper
from itertools import zip_longest
from pathlib import Path
from shutil import rmtree
from typing import Final

from rich.progress import track

if sys.version_info < (3, 11):
    from typing_extensions import NotRequired
    from typing_extensions import TypedDict

else:
    from typing import NotRequired
    from typing import TypedDict


from httpx import Client

COUNTRY_REVISION: Final[str] = "d055275324963c9bce5882eaaa93024cf2bf7ed0"
SUBDIVISION_REVISION: Final[str] = "4f5658fa63afce8cd121d41444b28c2294e6b513"

ISO_3166_1_JSON_URL = (
    f"https://salsa.debian.org/iso-codes-team/iso-codes/-/raw/main/data/iso_3166-1.json?ref={COUNTRY_REVISION}"
)
ISO_3166_2_JSON_URL = (
    f"https://salsa.debian.org/iso-codes-team/iso-codes/-/raw/main/data/iso_3166-2.json?ref={SUBDIVISION_REVISION}"
)


class Iso3116TypeOneEntry(TypedDict):
    alpha_2: str
    alpha_3: str
    flag: str
    common_name: NotRequired[str]
    official_name: NotRequired[str]
    name: NotRequired[str]
    numeric: NotRequired[str]


class Iso3116TypeTwoEntry(TypedDict):
    code: str
    name: str
    type: str


class CombinedData(TypedDict):
    name: str | None
    common_name: str | None
    official_name: str | None
    alpha_2: str
    alpha_3: str
    subdivisions: list[Iso3116TypeTwoEntry]


def common_header(f: TextIOWrapper) -> None:
    f.writelines(
        [
            "# SPDX-FileCopyrightText: 2024-present Trenton H <rda0128ou@mozmail.com>\n",
            "#\n",
            "# SPDX-License-Identifier: MPL-2.0\n",
            "# Generated from:\n",
            f"#  Country Data: {COUNTRY_REVISION}\n",
            f"#  Subdivision Data: {SUBDIVISION_REVISION}\n",
        ],
    )


def make_literal_from_list(name: str, items: list[str], comments: list[str]) -> list[str]:
    data = [f"{name} = Literal[\n"]
    for item, comment in zip_longest(items, comments, fillvalue=None):
        if comment:
            data.append(f'    "{item}",  # {comment}\n')
        else:
            data.append(f'    "{item}",\n')
    data.append("]\n\n")
    return data


def get_country_comment_name(country_data: CombinedData) -> str:
    if country_data["common_name"] is not None:
        return country_data["common_name"]
    else:
        assert country_data["name"] is not None  # noqa: S101
        return country_data["name"]


def output_data(module_dir: Path, combined_data: dict[str, CombinedData]) -> None:
    if module_dir.exists():
        rmtree(module_dir)

    module_dir.mkdir(parents=True, exist_ok=True)

    types_module = module_dir / "types"
    mapping_module = module_dir / "mapping"
    data_module = module_dir / "data"

    types_file = types_module / "__init__.py"
    mapping_file = mapping_module / "__init__.py"

    data_module.mkdir(parents=True, exist_ok=True)
    types_module.mkdir(parents=True, exist_ok=True)
    mapping_module.mkdir(parents=True, exist_ok=True)

    # 1 - Ensure we are a proper Python module
    with (module_dir / "__init__.py").open("w", encoding="utf-8", newline="\n") as f:
        common_header(f)
    with (data_module / "__init__.py").open("w", encoding="utf-8", newline="\n") as f:
        common_header(f)

    # 2 - Generate the alpha2, alpha3 and subdivision type types
    with types_file.open("w", encoding="utf-8", newline="\n") as f:
        common_header(f)
        f.writelines("from typing import Literal\n\n")

        alpha2_type: list[str] = []
        alpha3_type: list[str] = []
        alphas_comment_strs: list[str] = []

        subdivision_types: set[str] = set()
        for country_code in sorted(combined_data):
            country_data = combined_data[country_code]
            comment_name = get_country_comment_name(country_data)
            alpha2_type.append(country_data["alpha_2"])
            alpha3_type.append(country_data["alpha_3"])
            alphas_comment_strs.append(comment_name)
            for subdivision in country_data["subdivisions"]:
                subdivision_types.add(subdivision["type"])
        f.writelines(
            [
                *make_literal_from_list("CountryCodeAlpha2Type", alpha2_type, alphas_comment_strs),
                *make_literal_from_list("CountryCodeAlpha3Type", alpha3_type, alphas_comment_strs),
                *make_literal_from_list("SubdivisionTypeType", sorted(subdivision_types), []),
            ],
        )

    # 3 - Make the country and subdivision information
    for country_code, country_data in combined_data.items():
        country_module = data_module / f"{country_code.upper()}"

        country_module.mkdir(parents=True, exist_ok=True)
        country_init = country_module / "__init__.py"

        with country_init.open("w", encoding="utf-8", newline="\n") as f:
            common_header(f)
            import_lines = ["from typing import Final\n"]

            if country_data["subdivisions"]:
                subdivision_lines = ["[\n"]
                subdivision_literal = make_literal_from_list(
                    f"{country_code.upper()}SubdivisionCodeType",
                    [subdivision["code"] for subdivision in country_data["subdivisions"]],
                    [subdivision["name"] for subdivision in country_data["subdivisions"]],
                )
                import_lines.append("from typing import Literal\n\n")
                import_lines.append("from simpleiso3166.base import Country\n")
                import_lines.append("from simpleiso3166.base import Subdivision\n")
                import_lines.append("from simpleiso3166.generated.types import SubdivisionTypeType\n\n")
                for subdivision in country_data["subdivisions"]:
                    subdivision_lines.extend(
                        [
                            f'        {country_code.upper()}Subdivision(code="{subdivision["code"]}",',
                            f' name="{subdivision["name"]}",',
                            f' type_="{subdivision["type"]}"),\n',
                        ],
                    )
                subdivision_class_lines = [
                    f"class {country_code.upper()}Subdivision(Subdivision):\n",
                    f"    code: {country_code.upper()}SubdivisionCodeType\n",
                    "    name: str\n",
                    "    type_: SubdivisionTypeType\n\n",
                ]
                subdivision_lines.append("    ],\n")
            else:
                subdivision_literal = []
                subdivision_class_lines = []
                subdivision_lines = ["[],\n"]
                import_lines.append("\n")
                import_lines.append("from simpleiso3166.base import Country\n\n")
            common_name_str = f'"{country_data["common_name"]}"' if country_data["common_name"] else "None"
            official_name_str = f'"{country_data["official_name"]}"' if country_data["official_name"] else "None"
            f.writelines(
                [
                    *import_lines,
                    *subdivision_literal,
                    *subdivision_class_lines,
                    f"{country_code.upper()}: Final[Country] = Country(\n",
                    f'    alpha2="{country_data["alpha_2"]}",\n',
                    f'    alpha3="{country_data["alpha_3"]}",\n'
                    f'    name="{country_data["name"]}",\n'
                    f"    common_name={common_name_str},\n"
                    f"    official_name={official_name_str},\n"
                    f"    subdivisions=",
                    *subdivision_lines,
                    ")\n",
                ],
            )

    with mapping_file.open("w", encoding="utf-8", newline="\n") as f:
        common_header(f)
        import_lines = [
            "from typing import Final\n\n",
            "from simpleiso3166.base import Country\n",
        ]
        for country_code in sorted(combined_data.keys()):
            import_lines.append(
                f"from simpleiso3166.generated.data.{country_code.upper()} import {country_code.upper()}\n",
            )

        import_lines.extend(
            [
                "from simpleiso3166.generated.types import CountryCodeAlpha2Type\n",
                "from simpleiso3166.generated.types import CountryCodeAlpha3Type\n",
            ],
        )

        f.writelines([*import_lines, "\n"])

        f.write("ALPHA2_CODE_TO_COUNTRIES: Final[dict[CountryCodeAlpha2Type, Country]] = {\n")
        for country_code in sorted(combined_data):
            comment_name = get_country_comment_name(combined_data[country_code])
            f.write(f'    "{country_code}": {country_code},  # {comment_name}\n')
        f.write("}\n\n")

        f.write("ALPHA3_CODE_TO_COUNTRIES: Final[dict[CountryCodeAlpha3Type, Country]] = {\n")
        for country_code in sorted(combined_data):
            comment_name = get_country_comment_name(combined_data[country_code])
            country_data = combined_data[country_code]
            f.write(f'    "{country_data["alpha_3"]}": {country_code},  # {comment_name}\n')
        f.write("}\n")


def main(
    data_dir: Path = Path(),
    module_dir: Path = Path("src") / "simpleiso3166" / "generated",
    *,
    force_update: bool = False,
) -> None:
    country_json = data_dir / "iso_3166-1.json"
    subdivision_json = data_dir / "iso_3166-2.json"
    for output_file, url in zip(
        [country_json, subdivision_json],
        [ISO_3166_1_JSON_URL, ISO_3166_2_JSON_URL],
        strict=True,
    ):
        if force_update or not output_file.exists():
            with Client() as client:
                response = client.get(url)
                response.raise_for_status()
                output_file.write_bytes(response.content)

    subdivision_data: list[Iso3116TypeTwoEntry] = json.loads(subdivision_json.read_text(encoding="utf-8"))["3166-2"]  # type: ignore[misc]
    country_data: list[Iso3116TypeOneEntry] = json.loads(country_json.read_text(encoding="utf-8"))["3166-1"]  # type: ignore[misc]

    country_code_to_subdivision: dict[str, list[Iso3116TypeTwoEntry]] = defaultdict(list)

    for subdivision in subdivision_data:
        subdivision_code: str = subdivision["code"]
        country_alpha_2 = subdivision_code.split("-")[0]
        country_code_to_subdivision[country_alpha_2].append(subdivision)

    combined_data: dict[str, CombinedData] = {}

    for country in track(country_data, description="Combining data...            "):
        combined_data[country["alpha_2"]] = {
            "alpha_2": country["alpha_2"],
            "alpha_3": country["alpha_3"],
            "name": country.get("name"),
            "common_name": country.get("common_name"),
            "official_name": country.get("official_name"),
            "subdivisions": country_code_to_subdivision.get(country["alpha_2"], []),
        }

    output_data(module_dir, combined_data)


if __name__ == "__main__":
    import typer

    typer.run(main)
