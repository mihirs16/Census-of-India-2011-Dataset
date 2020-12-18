# imports
import pandas as pd
import requests
from bs4 import BeautifulSoup
import wget
import concurrent.futures
import ssl

# setup
requests.packages.urllib3.disable_warnings()
ssl._create_default_https_context = ssl._create_unverified_context

# template for fetching census dataset
class dataset:

    # URL to fetch as parameter
    def __init__(self, url, max_threads = 4):
        self.url = url
        self.max_threads = max_threads

    # fetch all links from the webpage
    def fetch_links(self):
        page = requests.request("GET", self.url, verify=False).text
        soup = BeautifulSoup(page, features="html.parser")

        all_rows = soup.find("table").find("table").find_all("tr")[5:-2]
        all_labels = [x.find_all("td")[0] for x in all_rows]
        
        all_links_total = [x.find_all("td")[1].find('a')['href'] for x in all_rows]
        all_links_sc = [x.find_all("td")[2].find('a')['href'] if x.find_all("td")[2].find('a') else "NA" for x in all_rows]
        all_links_st = [x.find_all("td")[3].find('a')['href'] if x.find_all("td")[3].find('a') else "NA" for x in all_rows]
        all_labels = [x.get_text() for x in all_labels]

        return pd.DataFrame(data = {
            "State": all_labels,
            "Total": all_links_total,
            "SC": all_links_sc,
            "ST": all_links_st
        })

    # download data from fetched links
    def download_files(self):
        
        # getting download links
        try:
            print("[-]Fetching download links...") 
            df_links = self.fetch_links()
            print("[-]Building download URLs")
            all_links_total = ['/'.join(self.url.split('/')[:-1] + [x]) for x in df_links['Total'].values]
            all_links_sc = ['/'.join(self.url.split('/')[:-1] + [x]) for x in df_links['SC'].values]
            all_links_st = ['/'.join(self.url.split('/')[:-1] + [x]) for x in df_links['ST'].values]
        except: 
            print("[!]Links couldn't be fetched")
            return False
        
        filenames = []
        try:
            print("[-]Downloading data")
            with concurrent.futures.ThreadPoolExecutor(max_workers = self.max_threads) as executor:
                futures = []
                for url in all_links_total:
                    futures.append(executor.submit(wget.download, url=url, bar=None, out=f"censusindia.gov.in/demographic/{url.split('/')[-1]}"))
                for future in concurrent.futures.as_completed(futures):
                    filenames.append(future.result())
        except:
            print("[!]Download failed")
            return False
        
        print(f"[+]Downloaded {len(filenames)} files")
        return filenames

    # build the dataset from downloaded files
    def build_dataset(self):
        df = pd.DataFrame(columns=["Table Name", "State Code", "District Code", "Area Name", "Age Group", "Total Persons", "Total Males", "Total Females", "Rural Persons", "Rural Males", "Rural Females", "Urban Persons", "Urban Males", "Urban Females"])

        xls_files = self.download_files()
        if xls_files != False:
            for file in xls_files:
                this_df = pd.read_excel(file, skiprows = range(0, 6), names=df.columns.values)
                df = df.append(this_df)
        
        df.to_csv("census_age.csv")
        return True