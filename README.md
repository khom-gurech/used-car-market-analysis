# Used Car Market Analysis: Toyota Camry Hybrid Pricing in Australia

## Project Overview

This project analyses used Toyota Camry Hybrid listings in Australia to understand the main factors that influence resale price.

The goal is to build a junior data analyst portfolio project that demonstrates practical skills in:

- Python data collection and cleaning
- pandas data transformation
- PostgreSQL / SQL analysis
- Power BI dashboard reporting
- GitHub project documentation

## Business Question

**What factors most influence the resale price of Toyota Camry Hybrid vehicles in Australia?**

The project will investigate how listing price changes based on:

- Vehicle year
- Odometer kilometres
- Variant
- State or region
- Seller type
- Listing age, if available

## Tools Used

- Windows
- VS Code
- Python
- pandas
- PostgreSQL
- SQL
- Power BI
- GitHub

## Project Structure

```text
used-car-market-analysis/
│
├── data/
│   ├── raw/              # Raw collected data. Do not edit manually.
│   └── processed/        # Cleaned data ready for SQL and Power BI.
│
├── docs/                 # Project notes, source review, and methodology notes.
│
├── notebooks/            # Exploratory analysis and cleaning notebooks.
│
├── powerbi/              # Power BI dashboard file and screenshots.
│
├── sql/                  # SQL table creation and analysis queries.
│
├── src/                  # Reusable Python scripts.
│
├── README.md             # Project explanation and findings.
├── requirements.txt      # Python packages required for the project.
└── .gitignore            # Files and folders excluded from GitHub.
```

## Data Collection Status

Data has not been collected yet.

Before collecting any data, this project will check:

- Website Terms of Use
- robots.txt rules
- Whether the pages are publicly accessible
- Whether personal seller information can be avoided
- Whether a small manual sample is safer than scraping

No personal seller names, phone numbers, emails, or exact street addresses will be collected or published.

## Planned Dataset Fields

Each row will represent one used Toyota Camry Hybrid listing at the time it was collected.

| Column           | Description                                            |
| ---------------- | ------------------------------------------------------ |
| scrape_date      | Date the listing was collected                         |
| source_site      | Generic source label                                   |
| listing_id_hash  | Hashed listing identifier                              |
| title            | Listing title                                          |
| price_aud        | Listed price in Australian dollars                     |
| year             | Vehicle year                                           |
| make             | Vehicle make                                           |
| model            | Vehicle model                                          |
| variant          | Camry variant, such as Ascent, Ascent Sport, SX, or SL |
| fuel_type        | Fuel type, expected to be Hybrid                       |
| transmission     | Transmission type                                      |
| odometer_km      | Odometer reading in kilometres                         |
| state            | Australian state                                       |
| suburb_or_region | General region only, not exact address                 |
| seller_type      | Dealer or private seller                               |
| listing_age_days | Listing age, if available                              |

## Planned Workflow

1. Review ethical and legal data collection options.
2. Collect a small educational sample of listings.
3. Save raw data in `data/raw/`.
4. Clean and standardise the data using Python and pandas.
5. Save cleaned data in `data/processed/`.
6. Load cleaned data into PostgreSQL.
7. Write SQL queries to analyse price patterns.
8. Build a Power BI dashboard.
9. Summarise insights and limitations in this README.

## Current Project Status

- [x] Project folder created
- [x] GitHub repository structure prepared
- [x] README skeleton created
- [ ] Data source reviewed
- [ ] Data collected
- [ ] Data cleaned
- [ ] SQL analysis completed
- [ ] Power BI dashboard created
- [ ] Final insights written

## Limitations

This project will use a small snapshot of used-car listing data. Listing prices are not final sale prices, so the results should be interpreted as market asking-price trends rather than confirmed transaction prices.

## Author

Khom Gurech
