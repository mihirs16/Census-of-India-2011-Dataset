# imports
import pandas as pd
import wget
import ssl
import os

# setup
ssl._create_default_https_context = ssl._create_unverified_context

# download data from census of india
filename = f"{os.path.dirname(os.path.realpath(__file__))}/censusindia.gov.in/district.xlsx" 
wget.download("http://censusindia.gov.in/2011census/A-1_NO_OF_VILLAGES_TOWNS_HOUSEHOLDS_POPULATION_AND_AREA.xlsx", out=filename)
print()

# clean and build dataset
columns = [
    "State Code",
    "District Code",
    "Sub District Code",
    "Category",
    "Name",
    "Residence",
    "Inhabited Villages",
    "Uninhabited Villages",
    "Towns",
    "Households",
    "Population (Person)",
    "Population (Male)",
    "Population (Female)",
    "Area",
    "Population Density"
]
df = pd.read_excel(filename, skiprows = 3, skipfooter = 28, names = columns)
df.replace("INDIA @&", "INDIA", inplace = True)
df.replace("INDIA $", "INDIA", inplace = True)
df.replace("JAMMU & KASHMIR @&", "JAMMU & KASHMIR", inplace = True)
df.to_csv(f"{os.path.dirname(os.path.realpath(__file__))}/censusindia.gov.in/census_district.csv")

# clean directory
os.remove(filename)