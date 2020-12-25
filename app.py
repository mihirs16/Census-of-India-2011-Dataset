# imports
import data
import os
import dotenv

# setup
dotenv.load_dotenv()
username = os.getenv("GCP_SQL_USER")
password = os.getenv("GCP_SQL_PASS")
hostname = os.getenv("GCP_SQL_HOST")
db = data.Database("may_db", username, password, hostname)

print(db.fetch(
    table_name = "AGE_STATE", 
    filter_column = "Age Group",
    filter_values = ["50-54", "55-59", "60-64", "65-69", "70-74", "75-79", "80+"],
).head())

print(db.fetch(
    table_name = "OCCUPATION_STATE", 
    filter_column = "Occupation",
    filter_values = ["Life Science and Health Professionals", "Teaching Associate Professionals"],
).head())
