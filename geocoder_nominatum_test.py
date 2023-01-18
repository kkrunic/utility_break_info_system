from geocoder_nominatum import Geocoder
import matplotlib.pyplot as plt
import geopandas as gpd


g = Geocoder()
g.geocode("6 Vukasina Mandrape", "Belgrade", "Serbia", "json",1)
print(type(g))
clas_type = g.get_place_class()
print("aaaa")

p = gpd.GeoSeries(geo)
p.plot()
plt.show()

print("AAA")