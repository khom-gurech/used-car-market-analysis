/*
 Used Car Market Analysis
 Starter SQL analysis queries
 
 These queries will be completed after data is collected, cleaned,
 and loaded into PostgreSQL.
 */
-- 1. Check total number of cleaned listings
-- SELECT COUNT(*) AS total_listings
-- FROM clean_listings;
-- 2. Average price by vehicle year
-- SELECT
--     year,
--     COUNT(*) AS listings,
--     ROUND(AVG(price_aud), 0) AS avg_price
-- FROM clean_listings
-- GROUP BY year
-- ORDER BY year;
-- 3. Average price by kilometre band
-- SELECT
--     km_band,
--     COUNT(*) AS listings,
--     ROUND(AVG(price_aud), 0) AS avg_price
-- FROM clean_listings
-- GROUP BY km_band;
-- 4. Average price by variant
-- SELECT
--     variant,
--     COUNT(*) AS listings,
--     ROUND(AVG(price_aud), 0) AS avg_price
-- FROM clean_listings
-- GROUP BY variant
-- ORDER BY avg_price DESC;
-- 5. Dealer vs private seller comparison
-- SELECT
--     seller_type,
--     COUNT(*) AS listings,
--     ROUND(AVG(price_aud), 0) AS avg_price
-- FROM clean_listings
-- GROUP BY seller_type;
-- 6. Comparable listings for a 2020 Camry Ascent Hybrid
-- SELECT
--     COUNT(*) AS comparable_listings,
--     MIN(price_aud) AS min_price,
--     ROUND(AVG(price_aud), 0) AS avg_price,
--     MAX(price_aud) AS max_price
-- FROM clean_listings
-- WHERE year = 2020
--   AND variant = 'Ascent'
--   AND odometer_km BETWEEN 60000 AND 90000;