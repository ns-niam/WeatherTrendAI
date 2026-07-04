from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import joblib
import pandas as pd


def ensure_dir(path: str | Path) -> Path:
    path = Path(path)
    path.mkdir(parents=True, exist_ok=True)
    return path


def save_csv(
    dataframe: pd.DataFrame,
    path: str | Path,
) -> Path:

    path = Path(path)
    ensure_dir(path.parent)

    dataframe.to_csv(
        path,
        index=False,
    )

    return path


def load_csv(
    path: str | Path,
) -> pd.DataFrame:

    return pd.read_csv(path)


def save_json(
    data: Any,
    path: str | Path,
) -> Path:

    path = Path(path)
    ensure_dir(path.parent)

    with open(
        path,
        "w",
        encoding="utf-8",
    ) as file:

        json.dump(
            data,
            file,
            indent=4,
            ensure_ascii=False,
        )

    return path


def load_json(
    path: str | Path,
) -> Any:

    with open(
        path,
        "r",
        encoding="utf-8",
    ) as file:

        return json.load(file)


def save_model(
    model: Any,
    path: str | Path,
) -> Path:

    path = Path(path)
    ensure_dir(path.parent)

    joblib.dump(
        model,
        path,
    )

    return path


def load_model(
    path: str | Path,
) -> Any:

    return joblib.load(path)