# Data Dictionary

## Project

Used Car Market Analysis: Toyota Camry Hybrid Pricing in Australia

## Dataset Level

Each row represents one Toyota Camry Hybrid used-car listing at the time the listing was recorded.

## Fields

| Column           | Type   | Description                            | Example                         |
| ---------------- | ------ | -------------------------------------- | ------------------------------- |
| scrape_date      | Date   | Date the listing was recorded          | 2026-06-28                      |
| source_site      | Text   | Generic source label, not full URL     | manual_sample                   |
| listing_id_hash  | Text   | Anonymous listing identifier           | listing_001                     |
| title            | Text   | Listing title                          | 2020 Toyota Camry Ascent Hybrid |
| price_aud        | Number | Listed price in Australian dollars     | 28990                           |
| year             | Number | Vehicle year                           | 2020                            |
| make             | Text   | Vehicle make                           | Toyota                          |
| model            | Text   | Vehicle model                          | Camry                           |
| variant          | Text   | Vehicle variant                        | Ascent                          |
| fuel_type        | Text   | Fuel type                              | Hybrid                          |
| transmission     | Text   | Transmission type                      | CVT                             |
| odometer_km      | Number | Odometer reading in kilometres         | 72400                           |
| state            | Text   | Australian state or territory          | NSW                             |
| suburb_or_region | Text   | General region only, not exact address | Sydney                          |
| seller_type      | Text   | Dealer or Private                      | Dealer                          |
| listing_age_days | Number | Number of days listed, if available    | 12                              |

## Privacy Rules

This project will not collect or publish:

- Seller names
- Phone numbers
- Email addresses
- Exact street addresses
- Full listing URLs

## Notes

The dataset is a small educational sample and should be interpreted as a snapshot of asking prices, not confirmed sale prices.
