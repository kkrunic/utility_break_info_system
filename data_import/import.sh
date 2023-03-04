for f in /data_import/*.gpkg;
do
 echo "Processing $f file..."
 ogr2ogr -f 'PostgreSQL' PG:'dbname=mydb host=db user=postgres password=postgres' -nln address -progress -append $f
 ogrinfo $f
done
