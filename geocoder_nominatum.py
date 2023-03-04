import requests
from shapely.geometry import shape
from shapely.geometry.polygon import Polygon


class Geocoder:
    def __init__(self):
        self.base_url = "https://nominatim.openstreetmap.org/search?"
        self.geocode_response = None
        self.json_response = None
        self.address = None
        self.geometry = None
        self.headers = {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET",
            "Access-Control-Allow-Headers": "Content-Type",
            "Access-Control-Max-Age": "3600",
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0",
        }

    def geocode(self, street, city, country, format, return_geometry):
        params = {
            "street": street,
            "city": city,
            "country": country,
            "format": format,
            "polygon_geojson": return_geometry,
        }

        response = requests.get(url=self.base_url, headers=self.headers, params=params)
        data = response.json()

        self.geocode_response = response
        self.json_response = data
        self._create_geometry()
        self.place_class = self.get_place_class()

    def get_geojson_geometry(self):
        if not self.geocode_response:
            print("Response object is NONE")
            return None

        elif isinstance(self.geocode_response, requests.Response):
            # print("Field is of type response")

            geometry = self.json_response[0]["geojson"]

            return geometry

    def _create_geometry(self):
        geojson_geometry = self.get_geojson_geometry()
        dict_geom = dict(geojson_geometry)
        self.geometry = shape(dict_geom)

    def get_shapely_geom(self):
        if self.geometry is None:
            return None
        else:
            return self.geometry

    def get_place_id(self):
        if not self.geocode_response:
            print("Response object is NONE")
            return None

        elif isinstance(self.geocode_response, requests.Response):
            # print("Field is of type response")

            place_id = self.json_response[0]["place_id"]
            return place_id

    def get_place_class(self):
        if not self.geocode_response:
            print("Response object is NONE")
            return None

        elif isinstance(self.geocode_response, requests.Response):
            # print("Field is of type response")

            class_type = self.json_response[0]["class"]

            return class_type
