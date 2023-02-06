from sqlalchemy import Column, Integer, Date, String, create_engine, Numeric
from sqlalchemy.ext.declarative import declarative_base
from geoalchemy2 import Geometry
from sqlalchemy.orm import sessionmaker
from scrapper import ShutdownScrapper


Base = declarative_base()

class Address(Base):
    __tablename__ = "address"
    ogc_fid = Column(Integer, primary_key=True)
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

    def __repr__(self) -> str:
        return f"Address(id={self.ogc_fid!r}, kucni_broj={self.kucni_broj!r}, ulica_ime={self.ulica_ime!r}, opstina={self.opstina_ime!r} )"

class PowerShutdownPoi(Base):
    __tablename__ = "power_shutdown_poi"
    id = Column(Integer, primary_key=True)
    scrapped_house_numb = Column(String)
    scrapped_street_name = Column(String)
    matched_kucni_broj = Column(String)
    matched_kucni_broj_lat = Column(String)
    matched_ulica_ime = Column(String)
    matched_ulica_ime_lat = Column(String)
    match_percentage = Column(Numeric)
    geom = Column(Geometry(geometry_type='POINT', srid=32634))

class AddressScrapped(Base):
    __tablename__ = "address_scrapped"
    id = Column(Integer, primary_key=True)
    scrapped_street_numb = Column(String)
    scrapped_street_name = Column(String)
    scrapped_municipality_name = Column(String)
    scrapped_date = Column(Date)