"""
Placeholder cleaning script.

This script will later clean raw Toyota Camry Hybrid listing data.
No cleaning is performed yet because no data has been collected.
"""

from pathlib import Path


RAW_DATA_PATH = Path("data/raw/listings_raw.csv")
PROCESSED_DATA_PATH = Path("data/processed/listings_clean.csv")


def main() -> None:
    """Placeholder entry point for future cleaning code."""
    print("Cleaning script placeholder.")
    print(f"Expected raw data path: {RAW_DATA_PATH}")
    print(f"Expected processed data path: {PROCESSED_DATA_PATH}")


if __name__ == "__main__":
    main()