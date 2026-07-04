"""
============================================================
WeatherTrendAI
Data Loader Module
============================================================

Author: Md Sha Niamatullah
Project: WeatherTrendAI
Description:
    Utility functions for loading and validating datasets.

============================================================
"""

from pathlib import Path
import pandas as pd


class DataLoader:
    """
    Handles loading weather datasets.
    """

    def __init__(self, data_path: str):
        self.data_path = Path(data_path)

    def exists(self) -> bool:
        """
        Check whether dataset exists.
        """
        return self.data_path.exists()

    def load(self) -> pd.DataFrame:
        """
        Load dataset into pandas DataFrame.
        """

        if not self.exists():
            raise FileNotFoundError(
                f"Dataset not found:\n{self.data_path}"
            )

        df = pd.read_csv(self.data_path)

        print("=" * 60)
        print("Dataset Loaded Successfully")
        print("=" * 60)
        print(f"Rows    : {df.shape[0]:,}")
        print(f"Columns : {df.shape[1]}")
        print("=" * 60)

        return df

    @staticmethod
    def summary(df: pd.DataFrame):
        """
        Print dataset summary.
        """

        print("\nDataset Summary")
        print("-" * 60)

        print(f"Rows      : {df.shape[0]:,}")
        print(f"Columns   : {df.shape[1]}")
        print(f"Memory    : {round(df.memory_usage().sum()/1024**2,2)} MB")
        print(f"Missing   : {df.isnull().sum().sum()}")
        print(f"Duplicates: {df.duplicated().sum()}")

        print("-" * 60)

    @staticmethod
    def column_info(df: pd.DataFrame):
        """
        Display column names and data types.
        """

        info = pd.DataFrame({
            "Column": df.columns,
            "Data Type": df.dtypes.astype(str)
        })

        return info