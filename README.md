# Project-MAY

Dashboard for monitoring distribution of the COVID-19 vaccine. ML-driven decision making and prioritization of candidates for the same.

## Data

* [Demographic Data](resources/data/censusindia.gov.in/census_age.csv) from [Census of India: C-14](https://censusindia.gov.in/2011census/C-series/C-14.html)

* [Occupation Data](resources/data/censusindia.gov.in/census_occupation.csv) from [Census of India: B-24](https://censusindia.gov.in/2011census/B-series/B_24.html)

* [State, District & Town Data](resources/data/censusindia.gov.in/census_district.csv) from [Census of India: A-1](http://censusindia.gov.in/2011census/A-1_NO_OF_VILLAGES_TOWNS_HOUSEHOLDS_POPULATION_AND_AREA.xlsx)

* COVID Data from [MyGov Website](https://www.mygov.in/covid-19)

## Development

* Fork the repository and clone it.

```bash
git clone https://github.com/:username/Project-MAY
```

* Installed the required packages.

```bash
pip install -r requirements.txt
```

* Add credentials for MY_SQL database to `.env` as follows.

```text
SQL_USER=example
SQL_PASS=Example#123
SQL_HOST=ex.am.pl.es:eg
```

### Backend (Flask)

* Run the server.

```bash
python main.py
```

* Local server will be available at `http://localhost:5000/`.

### Frontend (React.js)

* Change directory to client app.

```bash
cd dashboard
```

* Run the full-stack application.

```bash
npm install
npm run build
cd ..
python main.py
```

* \[OPTIONAL\] Run the React development Server.

```bash
npm install
npm start
```
