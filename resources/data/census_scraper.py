# imports
from bs4 import BeautifulSoup
from numpy.core.numeric import NaN
import pandas as pd
import requests
import wget
import concurrent.futures
import ssl
import os

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
        all_labels = [x.get_text() for x in all_labels]

        return pd.DataFrame(data = {
            "State": all_labels,
            "Total": all_links_total,
        })

    # download data from fetched links
    def download_files(self):
        
        # getting download links
        try:
            print("[-]Fetching download links...") 
            df_links = self.fetch_links()
            print("[-]Building download URLs")
            all_links_total = ['/'.join(self.url.split('/')[:-1] + [x]) for x in df_links['Total'].values]
        except: 
            print("[!]Links couldn't be fetched")
            return False
        
        # downloading all excel files
        filenames = []
        try:
            print("[-]Downloading data")
            with concurrent.futures.ThreadPoolExecutor(max_workers = self.max_threads) as executor:
                futures = []
                for url in all_links_total:
                    futures.append(executor.submit(wget.download, url=url, bar=None, out=f"{os.path.dirname(os.path.realpath(__file__))}/censusindia.gov.in/{url.split('/')[-1]}"))
                for future in concurrent.futures.as_completed(futures):
                    filenames.append(future.result())
        except:
            print("[!]Download failed")
            return False
        
        print(f"[+]Downloaded {len(filenames)} files")
        return filenames

    # clean excel files
    def clean_files(self, filenames):
        try:
            for x in filenames:
                os.remove(x)
        except:
            print("[-]Couldn't clean directory")
            return None
        
        print("[+]Directory cleaned")
        return None

    # build the dataset from downloaded files
    def get_data(self, columns, outfile, skiprows = range(0, 6)):
        df = pd.DataFrame(columns = columns)

        xls_files = self.download_files()
        if xls_files != False:
            for file in xls_files:
                this_df = pd.read_excel(file, skiprows = skiprows, names = df.columns.values)
                df = df.append(this_df)
            
            df.to_csv(outfile)
            print("[+]Dataset Built")
            self.clean_files(xls_files)
            return True

        else: 
            print("[!]Couldn't Download files")
            return False