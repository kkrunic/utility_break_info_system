#!/bin/bash

# Put any commands you want to execute here
ogr2ogr -f 'PostgreSQL' 'PG:dbname=mydb host=localhost user=postgres password=postgres' -nln 'test_zvezdara' -progress zvezdara.gpkg