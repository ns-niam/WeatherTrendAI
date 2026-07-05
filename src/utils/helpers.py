from __future__ import annotations

from pathlib import Path
from time import perf_counter


def ensure_directory(path: str | Path) -> Path:

    path = Path(path)

    path.mkdir(
        parents=True,
        exist_ok=True,
    )

    return path


def file_exists(path: str | Path) -> bool:

    return Path(path).exists()


def format_number(value: float, digits: int = 3) -> float:

    return round(value, digits)


class Timer:

    def __init__(self):
        self.start = None

    def __enter__(self):

        self.start = perf_counter()

        return self

    def __exit__(
        self,
        exc_type,
        exc_value,
        traceback,
    ):

        self.elapsed = perf_counter() - self.start


def print_section(title: str):

    line = "=" * 60

    print(line)

    print(title)

    print(line)