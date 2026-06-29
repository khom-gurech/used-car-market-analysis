"""
 Validate the manually collected raw used-car listing data.
 This script checks:   
 1.Whether the raw csv can be loaded
 2. Row and column counts
 3. Column names
 4. Missing values
 5. Duplicate listing IDs
 6. Basic price and odemeter formatting   
        
"""
from pathlib import Path
import pandas as pd

RAW_DATA_PATH = Path("data/raw/listings_manual_raw.csv")
EXPECTED_COLUMNS = [
    "scrape_date",
    "source_site",
    "listing_id_hash",
    "title",
    "price_aud",
    "year",
    "make",
    "model",
    "variant",
    "fuel_type",
    "transmission",
    "odometer_km",
    "state",
    "suburb_or_region",
    "seller_type",
    "listing_age_days",
]
def main() -> None:
    if not RAW_DATA_PATH.exists():
        raise FileExistsError(f"Raw data file not found: {RAW_DATA_PATH}")
    df = pd.read_csv(RAW_DATA_PATH)
    print("\n RAW DATA VALIDATION")
    print("="* 50)
    print(f"\n File loaded: {RAW_DATA_PATH}")
    print(f"Rows: {df.shape[0]}")
    print(f"Columns: {df.shape[1]}")
    print("\n COLUMN CHECK")
    print("-" * 50)
    actual_columns = list(df.columns)
    missing_columns = [col for col in EXPECTED_COLUMNS if col not in actual_columns]
    extra_columns = [col for col in actual_columns if col not in EXPECTED_COLUMNS]

    if not missing_columns and not extra_columns:
        print("PASS: All expected columns are present.")
    else:
        print(f"WARNING: Column mismatch found.")
        print(f"Missing columns: {missing_columns}")
        print(f"Extra columns: {extra_columns}")
    print("\nMISSING VALUES")
    print("-" * 50)
    print(df.isna().sum())
    print("\nDUPLICATE LISTING IDS")
    print("-"* 50)
    duplicated_count = df["listing_id_hash"].duplicated().sum()
    print(f"Duplicated listing_id_hash values:{duplicated_count}")
    
    print("\nRAW PRICE VALUES")
    print("-"* 50)
    print(df["price_aud"].head())
    

    
    
    print("\nPRICE CLEANING PREVIEW")
    print("-"* 50)
    
    price_clean = (df["price_aud"]
                   .astype(str)
                   .str.replace("$","",regex=False)
                    .str.replace(",","",regex=False)
                    .astype(float))
    
    print(price_clean.head())
    print("\nODOMETER CHECK")
    print(df['odometer_km'].describe())
    
    print("\nFUEL TYPE VALUES")
    print("-"* 50)
    print(df["fuel_type"].value_counts(dropna=False))
    
    print("\n VARIANT VALUES")
    print("-"* 50)
    print(df["variant"].value_counts(dropna=False))
    
    print("VALIDATION COMPLETE")
    
    
if __name__ == "__main__":
    main()


