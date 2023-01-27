# utility_break_info_system

## Project description

### Idea
The idea of this project is to serve informations about planned power shutdows and water pipe system malfunstions in Republic of Serbia. 

### Data
Data about power and water system breakdowns are public informations and for porpouse of this application relevant data is scrapped from competent state institution. 
Data is then matched with address registtry or geocoded using OSM geocoder Nominatim.
After matching, OGC services are created and server in a form of OGC WMS or WFS protocol. 

## How tu run 
Just run  `docker compose up ` and 3 containers will be created. One of flask app, one for a database and one for processign. You need to run data import using impoer.sh script and ther run inital scraping. 
Another mapserver for OGC service configuration. 

## In the future

1. Water system shutdowns

2. Public transport- bus line changes 

3. Road constuction