from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


class ModelEvaluator:

    def __init__(
        self,
        leaderboard: pd.DataFrame,
        output_dir: str = "outputs/results",
    ):
        self.leaderboard = leaderboard.copy()
        self.output_dir = Path(output_dir)

        self.output_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

    def save(self):

        csv_path = self.output_dir / "leaderboard.csv"

        json_path = self.output_dir / "leaderboard.json"

        from src.utils.io import save_csv

        save_csv(
            self.leaderboard,
            csv_path,
        )

        self.leaderboard.to_json(
            json_path,
        )

        return self

    def plot(self):

        plt.figure(figsize=(8,5))

        plt.bar(
            self.leaderboard["Model"],
            self.leaderboard["R2"],
        )

        plt.ylabel("R² Score")

        plt.title("Model Comparison")

        plt.tight_layout()

        plt.savefig(
            self.output_dir / "model_comparison.png",
            dpi=300,
        )

        plt.close()

        return self

    def best_model(self):

        return self.leaderboard.iloc[0]