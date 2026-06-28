# Source Review Notes

## Project

Used Car Market Analysis: Toyota Camry Hybrid Pricing in Australia

## Purpose

Before collecting any vehicle listing data, this document records the ethical and legal checks completed for potential data sources.

The goal is to avoid unsafe or unethical scraping and choose a collection method that is suitable for a junior data analyst portfolio project.

## Candidate Sources Reviewed

| Source                         |       Publicly Accessible? |    Terms Checked? | robots.txt Checked? | Personal Info Risk? | Decision                                 |
| ------------------------------ | -------------------------: | ----------------: | ------------------: | ------------------: | ---------------------------------------- |
| Carsales                       | Yes, some pages are public |               Yes |                 Yes |              Medium | Do not scrape                            |
| Gumtree Cars                   | Yes, some pages are public |               Yes |                 Yes |              Medium | Do not scrape unless permission is clear |
| Facebook Marketplace           | No, login usually required |          Not used |            Not used |                High | Avoid                                    |
| Manual anonymised sample       |                        Yes |    Not applicable |      Not applicable |   Low if anonymised | Preferred fallback                       |
| Open/public dataset supplement |          Yes, if available | Depends on source |   Depends on source |       Low to medium | Optional supplement                      |

## Source Review Summary

Carsales was reviewed as a possible data source. The decision is not to scrape Carsales because its terms restrict automated scraping, data mining, copying, and compiling databases from its material without prior written approval.

Gumtree Cars was also reviewed. The decision is not to build an automated scraper because scraping permission is not clearly established. The project will avoid automated access unless permission is clear.

Facebook Marketplace will not be used because it commonly requires login and may expose personal seller information.

## Data Collection Rules for This Project

This project will only collect a small educational sample.

The project will not collect or publish:

- Seller names
- Phone numbers
- Email addresses
- Exact street addresses
- Full source URLs in the public dataset

The public GitHub repository will include only cleaned, anonymised, or sample data suitable for portfolio demonstration.

## Preferred Collection Strategy

Preferred strategy at this stage:

- [ ] Permitted web scraping
- [x] Manual anonymised sample collection
- [ ] Open data/API supplement
- [ ] Not decided yet

## Notes

The project will prioritise ethical data handling over scraping. If scraping is not clearly allowed, the project will use a manually collected and anonymised sample or an open dataset instead.

This decision still allows the project to demonstrate important junior data analyst skills, including data cleaning, pandas transformations, SQL analysis, Power BI reporting, business insights, and GitHub documentation.
