/*
 Used Car Market Analysis
 Starter SQL schema
 
 This table structure is a draft.
 It will be updated after the cleaned dataset is finalised.
 */
DROP TABLE IF EXISTS clean_listings;
CREATE TABLE clean_listings (
    listing_id_hash TEXT PRIMARY KEY,
    scrape_date DATE,
    source_site TEXT,
    title TEXT,
    price_aud NUMERIC,
    year INTEGER,
    make TEXT,
    model TEXT,
    variant TEXT,
    fuel_type TEXT,
    transmission TEXT,
    odometer_km INTEGER,
    state TEXT,
    suburb_or_region TEXT,
    seller_type TEXT,
    listing_age_days INTEGER,
    vehicle_age INTEGER,
    km_band TEXT
);