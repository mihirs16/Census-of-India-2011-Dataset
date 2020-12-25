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

# testing SQL DB
print(db.read("AGE_DISTRICT").shape)
