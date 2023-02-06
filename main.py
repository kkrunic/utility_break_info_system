from address_orm import Address, PowerShutdownPoi, Base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, select, func
from scrapper import ShutdownScrapper
from street_refactoring import street_name_parsing, reformat_street_numbers
from address_orm import Address, AddressScrapped
import logging
# import csv

logging.basicConfig(filename='data_processing.log', filemode='w', level=logging.INFO, format='%(name)s - %(levelname)s - %(message)s', encoding='utf-8')

engine = create_engine("postgresql://postgres:postgres@localhost:5432/mydb")
Base.metadata.create_all(engine)

# Base.metadata.reflect(bind=engine)

#Scrape data
url_eps = "https://www.epsdistribucija.rs/Dan_0_Iskljucenja.htm"
s = ShutdownScrapper(url=url_eps)
s.scrape()
scrapeed_df = s.scrape_2_df()
# print(scrapeed_df)

df_rows = len(scrapeed_df)
street_col = "Улице"
time_col = "Време"
# shape_list = []

session = Session(engine)

for i in range(df_rows):

    municipality_name = scrapeed_df.at[i,"Општина"]
    
    # Handlovanje palilula
    # TODO:

    if municipality_name == 'Палилула':
        municipality_name = 'Палилула (БЕОГРАД)'
    
    logging.info(f"Procesiraju se podaci za opstinu: {municipality_name}")

    shutdown_time = scrapeed_df.at[i,time_col]
    logging.info(f"Planirani nestanak struje u periodu: {shutdown_time}")
    try:
        dict_list = street_name_parsing(str(scrapeed_df.at[i,street_col]))
        dict_list = reformat_street_numbers(dict_list)
    except AttributeError:
        # FIXME:
        continue

    for street_dict in dict_list:
        # if "Naselje" in street_dict:
        #     neighborhood = street_dict["Naselje"]
        
        street_name = street_dict["Ulica"]
        # print(street_name)

        for num in street_dict["Broj"]:

            scrapped_street = AddressScrapped(scrapped_street_numb=num, scrapped_street_name=street_name, scrapped_municipality_name=municipality_name)
            session.add(scrapped_street)

            logging.info("Uparivanje skrejpovanig podataka")
            logging.info(f"{num} {street_name}")

            matched_address = session.scalars(select(Address).where(Address.opstina_ime == municipality_name.upper(), Address.ulica_ime == street_name, Address.kucni_broj == num)).first()

            if matched_address != None:

                logging.info("Uspesno upareni podaci!")
                psp = PowerShutdownPoi(scrapped_house_numb=num, scrapped_street_name=street_name, matched_kucni_broj=matched_address.kucni_broj, matched_kucni_broj_lat=matched_address.kucni_broj_lat,
                matched_ulica_ime=matched_address.ulica_ime, matched_ulica_ime_lat=matched_address.ulica_ime_lat, match_percentage=100,
                geom= matched_address.wkb_geometry)
                
                session.add(psp)

            else:
                logging.info("Neuspesno upareni podaci!")
                # See what is the problem
                # Is it street numb?
                # Is it street name?
                street_name_check = session.scalars(select(Address).where(Address.opstina_ime == municipality_name.upper(), Address.ulica_ime == street_name)).first()
                if street_name_check != None:
                    logging.info(f"Postoji ulica sa ovim nazivom: {street_name}")
                    logging.info("Pretpostavlja se da broj ne postoji u bazi")
                else:
                    logging.info(f"Postoji ulica sa ovim nazivom: {street_name}")
                    logging.info("Potrebno je videti da li ulica ne postoji ili postoji pod drugim slicnim nazivom (skracenim npr)")

            # g = Geocoder()
            # try:
            #     # g.geocode(street=street_full_name ,city= "Belgrade", country= "Serbia", format="json", return_geometry=1)
            #     # shape_list.append(g.geometry)
            # except IndexError:
            #     # FIXME:
            #     continue
            
            # del g
    del dict_list

session.flush()
session.commit()

logging.info("Proces obrade obrade i uparivanja podataka se gotov")