"""
Clean the manually collected Toyota Camry Hybrid listing dat.
This script:
1. Loads the raw manually csv
2.Clean price and odometer fields
3.Standardizes text fields
4. Creates vehicle age and kilometer bands.
5. Saves a cleaned csv SQL and Power BI

"""

from pathlib import Path
import pandas as pd

RAW_DATA_PATH = Path("data/raw/listings_manual_raw.csv")
PROCESS_DATA_PATH = Path("data/processed/listings_clean.csv")


def clean_price(price_value):
    if pd.isna(price_value):
        return None
    clean_value = str(price_value).replace("$", "").replace(",", "").strip()
    return float(clean_value)


# print(clean_price("$45,000 "))


def standard_fuel_type(fuel_value):
    """Standardize fuel labels into one consistent category"""
    if pd.isna(fuel_value):
        return None
    fuel_text = str(fuel_value).lower()
    if "electric" in fuel_text or "hybrid" in fuel_text:
        return "Hybrid"

    return str(fuel_value).strip()


# print(standard_fuel_type("Premium Unleaded/Electric"))


def standardize_variant(variant_value):
    """Standardize Camry Variant names."""
    if pd.isna(variant_value):
        return None

    variant_text = str(variant_value).lower()
    if "ascent sport" in variant_value:
        return "Ascent Sport"

    if "ascent " in variant_value:
        return "Ascent"

    if "sx" in variant_value:
        return "SL"

    if "sl" in variant_value:
        return "SL"

    if "hybrid" in variant_value:
        return "Hybrid"

    return str(variant_value).strip()


def create_km_band(odometer_km):
    """Group odometer readings into kilometers bands."""
    if pd.isna(odometer_km):
        return None
    if odometer_km < 50000:
        return "0-50k"
    if odometer_km < 100000:
        return "50-100k"

    if odometer_km < 150000:
        return "100-150k"

    if odometer_km < 200000:
        return "150-200k"

    return "200k+"


# Add the main cleaning functio


def main() -> None:
    if not RAW_DATA_PATH.exists():
        raise FileNotFoundError(f"Raw data file not found: {RAW_DATA_PATH}")
    df = pd.read_csv(RAW_DATA_PATH)
    print("Cleaning raw listing data...")
    print(f"Raw rows loaded: {len(df)}")
    # clean numeric columns
    df["price_aud"] = df["price_aud"].apply(clean_price)
    df["odometer_km"] = pd.to_numeric(df["odometer_km"], errors="coerce")
    df["year"] = pd.to_numeric(df["year"], errors="coerce")

    # standardise text columns
    df["make"] = df["make"].str.strip().str.title()
    df["model"] = df["model"].str.strip().str.title()
    df["seller_type"] = df["seller_type"].str.strip().str.title()
    df["fuel_type"] = df["fuel_type"].apply(standard_fuel_type)
    df["variant"] = df["variant"].apply(standardize_variant)

    # create derived columns
    scrape_year = pd.to_datetime(df["scrape_date"]).dt.year
    df["vehicle_age"] = scrape_year - df["year"]
    df["km_band"] = df["odometer_km"].apply(create_km_band)
    # remove duplicated listing ids
    df = df.drop_duplicates(subset=["listing_id_hash"])
    # save cleaned data
    PROCESS_DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(PROCESS_DATA_PATH, index=False)

    print(f"Clean rows save: {len(df)}")
    print(f"Clean file created: {PROCESS_DATA_PATH}")


if __name__ == "__main__":
    main()
