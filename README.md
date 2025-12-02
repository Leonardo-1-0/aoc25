# Repository for the 2025 Advent of Code

## Setup

### AOC helper CLI

Install [uv](https://docs.astral.sh/uv/) with

```shell
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Install the packages for the `aoc_helper.py` cli

```shell
uv sync --group cli
```

Call the cli from everywhere with [poe](https://poethepoet.natn.io/)

```shell
uv run poe aoc
# or, if the venv is already active
poe aoc
```

Rename `.env.example` to `.env` and add your `AOC_COOKIE` to the file.
You can find it by logging into your AOC account and cheking the
browser cookie storage (f12) for the value.

## CLI / POE

- aoc init

  > create a file tree for the given day and year (defaults to today if no
  > parameters are given). The file tree root is src/aoc25/ by default but
  > can be overwritten. The script will create the files `part1.py`, `part2.py`
  > and `test.txt` for the test input.

- aoc pull

  > Download the puzzle input for a given day and year and save it into a
  > specified directory in the `full.txt` file.

- other poe tasks like `poe test1 | test2 | full1 | full2`

  Input is meant to be fed from the terminal to the python scripts like so

  ```shell
  part1.py < test.txt
  ```

  with the python file reading the input e.g.,

  ```python
  input_ = open(0).read()
  # or
  import sys
  input_ = sys.stdin.read()
  ```
