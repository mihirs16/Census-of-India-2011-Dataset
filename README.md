# Project-MAY

Dashboard for monitoring distribution of the COVID-19 vaccine. ML-driven decision making and prioritization of candidates for the same.

## Contents

### Data

* [Demographic Data](resources/data/censusindia.gov.in/census_age.csv) from [Census of India: C-14](https://censusindia.gov.in/2011census/C-series/C-14.html)

* [Occupation Data](resources/data/censusindia.gov.in/census_occupation.csv) from [Census of India: B-24](https://censusindia.gov.in/2011census/B-series/B_24.html)

* [State, District & Town Data](resources/data/censusindia.gov.in/census_district.csv) from [Census of India: A-1](http://censusindia.gov.in/2011census/A-1_NO_OF_VILLAGES_TOWNS_HOUSEHOLDS_POPULATION_AND_AREA.xlsx)

* COVID Data from [MyGov Website](https://www.mygov.in/covid-19)

### API

* Fork the repository and clone it.

```bash
git clone https://github.com/:username/Project-MAY
```

* Installed the required packages.

```bash
pip install -r requirements.txt
```

* Run the server.

```bash
python app.py
```

* You can view the dashboard at `http://localhost:5000/`
