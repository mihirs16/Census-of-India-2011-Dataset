# imports
import census_scraper

# fetching links from censusindia.gov.in
age_grp = census_scraper.dataset(url = "https://censusindia.gov.in/2011census/C-series/C-14.html", max_threads = 8)
print("Success") if age_grp.build_dataset() else print("Failed")