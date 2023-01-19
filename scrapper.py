from bs4 import BeautifulSoup
import requests 
import pandas as pd

class ShutdownScrapper():
    def __init__(self, url) -> None:
        self.base_url = url
        self.date = None
        self.scrapped_data = None
        self.headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }

    def scrape(self):
        base_url = self.base_url
        res = requests.get(url=base_url, headers=self.headers)
        soup = BeautifulSoup(res.content, "html.parser")
        # Grab second table, its where the data is.
        self.scrapped_data = soup.find_all('table')[1]
        
    
    def scrape_2_df(self):
        scrapped_data = self.scrapped_data
        if scrapped_data:
            column_names = []
            data_row = []
            data_list = []
            for idx,child in enumerate(scrapped_data.children):
                # print(f"####{idx}")
                # print(child.text)
                # print(type(child))
                if idx == 0:
                    # print("header")
                    [column_names.append(c.text) for c in child.children]
                
                else:
                    print("Podaci")
                    # print(child.prettify())
                    # print(child.text)
                    [data_row.append(td.text) for td in child.children]
                    # print(data_row)
                    data_list.append(data_row)
                    data_row = []

        scrapped_df = pd.DataFrame(columns=column_names, data=data_list)
        return scrapped_df

# If you want to test
# url_eps = "https://www.epsdistribucija.rs/Dan_0_Iskljucenja.htm"
# s=ShutdownScrapper(url_eps)
# s.scrape()
# scrapeed_df = s.scrape_2_df()
# print(type(scrapeed_df))
# scrapeed_df.to_excel("test.xlsx", sheet_name='Sheet1', index=False)