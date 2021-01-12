# imports
import census_downloader

# fetching links from censusindia.gov.in
url = "https://censusindia.gov.in/2011census/C-series/c-20.html"
columns = [
    "Table Name", 
    "State Code", 
    "District Code", 
    "Area Name",
    "Residence", 
    "Age Group", 
    "Disabled Persons", 
    "Disabled Males", 
    "Disabled Females", 
    "In Seeing Persons", 
    "In Seeing Males", 
    "In Seeing Females",
    "In Hearing Persons", 
    "In Hearing Males", 
    "In Hearing Females", 
    "In Speech Persons", 
    "In Speech Males", 
    "In Speech Females", 
    "In Movement Persons", 
    "In Movement Males", 
    "In Movement Females",
    "In Mental Retardation Persons",
    "In Mental Retardation Males", 
    "In Mental Retardation Females",
    "In Mental Illness Persons", 
    "In Mental Illness Males", 
    "In Mental Illness Females",
    "In Any Other Persons",
    "In Any Other Males", 
    "In Any Other Females",
    "In Multiple Disability Persons",
    "In Multiple Disability Males", 
    "In Multiple Disability Females", 
]
outfile = f"{census_downloader.os.path.dirname(census_downloader.os.path.realpath(__file__))}/censusindia.gov.in/census_disability.csv"
age_grp = census_downloader.dataset(url = url, max_threads = 8)
age_grp.get_data(columns = columns, outfile = outfile)