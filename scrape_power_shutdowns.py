from bs4 import BeautifulSoup
import requests 
import pandas as pd
from geocoder_nominatum import Geocoder
from street_refactoring import street_name_parsing, reformat_street_numbers
import geopandas as gpd

url_eps = "https://www.epsdistribucija.rs/Dan_0_Iskljucenja.htm"

headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }

res = requests.get(url=url_eps, headers=headers)

soup = BeautifulSoup(res.content, "html.parser")

date_string = soup.table.text
date = date_string.split(":")[1]
date = date.strip()

all_t = soup.find_all('table')
tbl = all_t[1]
print(type(tbl))
# print(soup.prettify())

column_names = []
data_row = []
data_list = []

for idx,child in enumerate(tbl.children):
    # print(f"####{idx}")
    # print(child.text)
    # print(type(child))

    if idx == 0:
        print("zaglavlje")
        [column_names.append(c.text) for c in child.children]
    
    else:
        print("Podaci")
        # print(child.prettify())
        # print(child.text)
        [data_row.append(td.text) for td in child.children]
        data_list.append(data_row)
        data_row = []
        

df = pd.DataFrame(columns=column_names, data=data_list)
# print(df)
df.to_csv("table.csv")
del df
df_2 = pd.read_csv("table.csv")


print(df_2["Улице"])
print(str(df_2.at[0,"Улице"]))

# dict_list = street_name_parsing(str(df_2.iloc[0,3]))
# dict_list = reformat_street_numbers(dict_list)

df_rows = len(df_2)
street_col = "Улице"
shape_list = []

for i in range(df_rows):

    print(df_2.at[i,"Општина"])
    try:
        dict_list = street_name_parsing(str(df_2.at[i,street_col]))
        dict_list = reformat_street_numbers(dict_list)
    except AttributeError:
        # FIXME:
        continue

    for street_dict in dict_list:
        # if "Naselje" in street_dict:
        #     neighborhood = street_dict["Naselje"]
        
        street_name = street_dict["Ulica"]
        print(street_name)

        for num in street_dict["Broj"]:
            
            street_full_name =  num + " " + street_name
            print(street_full_name)
            g = Geocoder()
            try:
                g.geocode(street=street_full_name ,city= "Belgrade", country= "Serbia", format="json", return_geometry=1)
                shape_list.append(g.geometry)
            except IndexError:
                # FIXME:
                continue
            
            del g
    del dict_list

gdf = gpd.GeoDataFrame(geometry=shape_list)
gdf.crs = {'init': 'epsg:4326'}
gdf.to_file('shapes.gpkg', driver='GPKG')

# def naselje_cleaning(input_street_txt):
#     input_street_list = input_street_txt.split(":")
#     for i in input_street_list:
#         if "Насеље" in i:
#             input_street_txt.replace(i,"")
#             input_street_list.remove(i)
            
#     return input_street_txt, input_street_list

# def resolve_street_name():

# def resovle_street_numbers(

