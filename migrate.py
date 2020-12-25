# imports
import os
import dotenv
import data
import pandas as pd

# environment variables
dotenv.load_dotenv()
username = os.getenv("GCP_SQL_USER")
password = os.getenv("GCP_SQL_PASS")
hostname = os.getenv("GCP_SQL_HOST")


# processing census_age.csv
def dataset_age():
    df_age = pd.read_csv("resources/data/censusindia.gov.in/census_age.csv")

    # separating states and districts
    area_district = []
    area_state = []
    for x in list(df_age["Area Name"].unique()):
        if x[:8] == "State - ":
            area_state.append(x)
        elif x[:8] == "District":
            area_district.append(x)
        else:
            pass

    # district wise age distribution
    df_processed_district = df_age[df_age["Area Name"].isin(area_district)][["District Code", "Age Group", "Total Persons"]]
    df_processed_district = df_processed_district.reset_index().drop(["index"], axis = 1)
    print(df_processed_district.head())
    df_processed_district.to_csv("resources/processed_data/census_age_district.csv")

    # district wise age distribution
    df_processed_state = df_age[df_age["Area Name"].isin(area_state)][["State Code", "Age Group", "Total Persons"]]
    df_processed_state = df_processed_state.reset_index().drop(["index"], axis = 1)
    print(df_processed_state.head())
    df_processed_state.to_csv("resources/processed_data/census_age_state.csv")

# processing census_occupation.csv
def dataset_occupation():
    df_occupation = pd.read_csv("resources/data/censusindia.gov.in/census_occupation.csv")

    # separating states and districts
    area_district = []
    area_state = []
    for x in list(df_occupation["Area Name"].unique()):
        if x[:8] == "STATE - ":
            area_state.append(x)
        elif x[:8] == "District":
            area_district.append(x)
        else:
            pass

    # district wise occupation distribution
    df_occupation = df_occupation[df_occupation["Residence"] == "Total"]
    df_processed_district = df_occupation[df_occupation["Area Name"].isin(area_district)][["District Code", "Occupation", "Total Main Worker (Person)"]]
    df_processed_district = df_processed_district.reset_index().drop(["index"], axis = 1)
    print(df_processed_district.head())
    df_processed_district.to_csv("resources/processed_data/census_occupation_district.csv")

    # state wise occupation distribution
    df_occupation = df_occupation[df_occupation["Residence"] == "Total"]
    df_processed_state = df_occupation[df_occupation["Area Name"].isin(area_district)][["State Code", "Occupation", "Total Main Worker (Person)"]]
    df_processed_state = df_processed_state.reset_index().drop(["index"], axis = 1)
    print(df_processed_state.head())
    df_processed_state.to_csv("resources/processed_data/census_occupation_state.csv")


# processing census_population.csv
def dataset_population():
    df_district = pd.read_csv("resources/data/censusindia.gov.in/census_population.csv")
    
    # state & district wise population distribution
    df_district = df_district[df_district["Residence"] == "Total"]
    df_processed_district = df_district[df_district["Category"].isin(["STATE", "DISTRICT"])]
    df_processed_district = df_processed_district[["State Code", "District Code", "Name", "Population (Person)", "Area", "Population Density"]]
    print(df_processed_district.head())
    df_processed_district.to_csv("resources/processed_data/census_population.csv")


dataset_age()
dataset_occupation()
dataset_population()
