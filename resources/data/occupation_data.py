# imports
import census_scraper

# fetching links from censusindia.gov.in
url = "https://censusindia.gov.in/2011census/B-series/B_24.html"
columns = [
    "Table Name", 
    "State Code", 
    "District Code", 
    "Area Name", 
    "Division",
    "Sub-division",
    "Occupation",
    "Residence",
    "Total Main Worker (Person)",
    "Total Main Worker (Male)",
    "Total Main Worker (Female)",
    "Employer (Person)",
    "Employer (Male)",
    "Employer (Female)",
    "Employee (Person)",
    "Employee (Male)",
    "Employee (Female)",
    "Single Worker (Person)",
    "Single Worker (Male)",
    "Single Worker (Female)",
    "Family Worker (Person)",
    "Family Worker (Male)",
    "Family Worker (Female)",
]
outfile = f"{census_scraper.os.path.dirname(census_scraper.os.path.realpath(__file__))}/censusindia.gov.in/census_occupation.csv"
age_grp = census_scraper.dataset(url = url, max_threads = 8)
age_grp.get_data(columns = columns, outfile = outfile, skiprows = range(0, 7), droprows = 2) 