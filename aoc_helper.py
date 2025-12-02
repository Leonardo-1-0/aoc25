import requests
import os
from datetime import date
from pathlib import Path
from typing import Annotated, Optional

import rich
import typer
from rich.tree import Tree
from typer import Argument, Typer
from dotenv import load_dotenv


def get_year() -> int:
    return date.today().year


def get_day() -> int:
    return date.today().day


def init(
    day: Annotated[Optional[int], Argument()] = None,
    root: Annotated[
        Path, Argument(help="Parent dir of the generated structure")
    ] = Path(__file__).parent / "src/aoc25",
) -> None:
    day = day or get_day()
    new_dir = root / f"{day:02d}"

    files = ["part1.py", "part2.py", "test.txt"]
    tree = Tree(f"[blue]{new_dir}")
    for file in files:
        tree.add(file)
    print("The follwing file tree will be created:")
    rich.print(tree)

    typer.confirm("Would you like to continue?", default=True, abort=True)
    new_dir.mkdir(parents=True)
    for file in files:
        file = (new_dir / file).touch()


def pull(
    day: Annotated[Optional[int], Argument()] = None,
    year: Annotated[Optional[int], Argument()] = None,
    out: Annotated[
        Optional[Path],
        Argument(
            help="Path to write the downloaded input file to (defaults to 'src/aoc25/day' if left empty)."
        ),
    ] = None,
) -> None:
    year = year or get_year()
    day = day or get_day()
    out = out or Path(__file__).parent / "src/aoc25" / f"{day:02d}"

    load_dotenv(Path(__file__).parent / ".env")
    AOC_COOKIE = os.environ.get("AOC_COOKIE")
    if not AOC_COOKIE:
        raise ValueError(
            "This command requires the AOC_COOKIE environment variable to be set.\n"
            + "Log into your advent of code account and go to the network tab of the "
            + "developer console in the 'storage' menue to find your session cookie."
        )

    response = requests.get(
        f"https://adventofcode.com/{year}/day/{day}/input",
        cookies={"session": AOC_COOKIE},
    )
    if not response.ok:
        response.raise_for_status()

    with open(out / "full.txt", "w") as outfile:
        outfile.write(response.text)


app = Typer(no_args_is_help=True, add_completion=False)

app.command(help="Creat aoc files for a given day", rich_help_panel="Setup")(init)
app.command(help="Download the input file for a given day", rich_help_panel="Setup")(
    pull
)


if __name__ == "__main__":
    app()
