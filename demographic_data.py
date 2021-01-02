# imports
import census_downloader

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
outfile = f"{census_downloader.os.path.dirname(census_downloader.os.path.realpath(__file__))}/censusindia.gov.in/census_age.csv"
age_grp = census_downloader.dataset(url = url, max_threads = 8)
age_grp.get_data(columns = columns, outfile = outfile)