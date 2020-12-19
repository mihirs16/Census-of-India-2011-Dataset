# imports
import census_scraper

# fetching links from censusindia.gov.in
url = "https://censusindia.gov.in/2011census/C-series/C-14.html"
columns = [
    "Table Name", 
    "State Code", 
    "District Code", 
    "Area Name", 
    "Age Group", 
    "Total Persons", 
    "Total Males", 
    "Total Females", 
    "Rural Persons", 
    "Rural Males", 
    "Rural Females", 
    "Urban Persons", 
    "Urban Males", 
    "Urban Females"
]
outfile = f"{census_scraper.os.path.dirname(census_scraper.os.path.realpath(__file__))}/censusindia.gov.in/census_age.csv"
age_grp = census_scraper.dataset(url = url, max_threads = 8)
age_grp.get_data(columns = columns, outfile = outfile)