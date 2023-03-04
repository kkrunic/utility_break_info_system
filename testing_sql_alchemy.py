from sqlalchemy import create_engine, text, literal_column
from address_orm import Address, Base
from sqlalchemy import select, desc
from sqlalchemy.orm import Session
from sqlalchemy import func

engine = create_engine("postgresql://postgres:postgres@localhost:5432/mydb")
Base.metadata.create_all(engine)

session = Session(engine)


street_dict1 = {
    "municipality_name": "ЗВЕЗДАРА",
    "street_name": "БАТУТОВА",
    "street_numb": "11",
}
street_dict2 = {
    "municipality_name": "ЗВЕЗДАРА",
    "street_name": "БАТУТОВА",
    "street_numb": "18А",
}
street_dict3 = {
    "municipality_name": "ЗЕМУН",
    "street_name": "БАТАЈНИЧКИ ДРУМ",
    "street_numb": "12",
}
street_dict4 = {
    "municipality_name": "САВСКИ ВЕНАЦ",
    "street_name": "КНЕЗА МИЛОША",
    "street_numb": "37",
}
street_dict5 = {
    "municipality_name": "Палилула (БЕОГРАД)",
    "street_name": "РАНКА МИЉИЋА",
    "street_numb": "17А",
}

street_list = [street_dict1, street_dict2, street_dict3, street_dict4, street_dict5]

# for i in street_list:
#     matched = session.execute(select(Address).where(Address.opstina_ime == i["municipality_name"], Address.ulica_ime == i["street_name"], Address.kucni_broj == i["street_numb"])).first()
#     print(matched)
#     matched_l = session.execute(select(Address, func.levenshtein(Address.kucni_broj+ " " +Address.ulica_ime, i["street_numb"] + " " + i["street_name"]).label("leven")).where(Address.opstina_ime==i["municipality_name"]).order_by("leven")).first()
#     print(matched_l.leven)
#     print(matched_l)

res = session.scalars(
    select(Address).where(
        Address.opstina_ime == street_dict5["municipality_name"].upper(),
        Address.ulica_ime == street_dict5["street_name"],
    )
).first()
print("aa")
