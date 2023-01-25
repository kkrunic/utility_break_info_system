# utility_break_info_system

## Project description

### Idea
The idea of this project is to serve informations about planned power shutdows and water pipe system malfunstions in Republic of Serbia. 

### Data
Data about power and water system breakdowns are public informations and for porpouse of this application relevant data is scrapped from competent state institution. 
Data is then matched with address registtry or geocoded using OSM geocoder Nominatim.
After matching, OGC services are created and server in a form of OGC WMS or WFS protocol. 

## How tu run 
All relevant libraries are mentioned in requirements.txt document are all you need to do is to create virtual enviroments using that file. 
Afret creating venv you should be able to run flask app. This part needs to be detaily explained once its configured.

## In the future
<!-- 
- Vodovod kvarovi

- Saobracaj GSP

- Radovi na putu -->