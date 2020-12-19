# Project-MAY

Dashboard for monitoring distribution of the COVID-19 vaccine. ML-driven decision making and prioritization of candidates for the same.

## Contents

### Data

* [Demographic Data](resources/data/censusindia.gov.in/census_age.csv) from [Census of India: C-14](https://censusindia.gov.in/2011census/C-series/C-14.html)

* [Occupation Data](resources/data/censusindia.gov.in/census_occupation.csv) from [Census of India: B-24](https://censusindia.gov.in/2011census/B-series/B_24.html)

### Web Scrapers

* Install the required packages

```bash
pip install -r requirements.txt
```

* Run the scraper

```bash
python resources/data/demographic_data.py
python resources/data/occupation_data.py
```
