from sqlalchemy import Column, Integer, Date, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from geoalchemy2 import Geometry
from sqlalchemy.orm import sessionmaker


Base = declarative_base()

class Address(Base):
    __tablename__ = "address"
    fid = Column(Integer, primary_key=True)
    datum_unosa = Column(Date)
    kucni_broj_id = Column(Integer)
    kucni_broj = Column(String)
    kucni_broj_lat = Column(String)
    vrsta_stanja = Column(String)
    vrsta_stanja_lat = Column(String)
    created = Column(Date)
    retired = Column(Date)
    opstina_maticni_broj = Column(Integer)
    opstina_ime = Column(String)
    opstina_ime_lat = Column(String)
    ko_maticni_broj = Column(Integer)
    kat_opstina_ime = Column(String)
    kat_opstina_ime_lat = Column(String)
    naselje_maticni_broj = Column(Integer)
    naselje_ime = Column(String)
    naselje_ime_lat = Column(String)
    ulica_maticni_broj = Column(String)
    ulica_ime = Column(String)
    ulica_ime_lat = Column(String)
    wkb_geometry = Column(Geometry(geometry_type='POINT', srid=32634))

engine = create_engine("postgresql://postgres:postgres@db:5432/mydb")

Base.metadata.reflect(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

points = session.query(Address).filter(Address.fid == 1).limit(1)

for point in points:
    print(point.fid, point.wkb_geometry)

session.close()
