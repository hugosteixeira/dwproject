import requests
import json
from flask import request, jsonify
from flask.views import MethodView
from sqlalchemy import inspect
import googlemaps
from utils import printError,limparTexto
    

class FormatPlace :


    def __init__(self,location):
        self.gmaps = googlemaps.Client(key='AIzaSyD8b3UyPssRS9CwgWuW-788UFaZYS1oi9Q')
        self.address_components=location


    def localizationAddress(self):
        print ("Minha localizacao e ", self.address_components)
        geocode_result = self.gmaps.geocode(self.address_components,language='pt-br')
        print(geocode_result)
        result = {}
        result['city'] = 'Nao definido'
        result['state'] = 'Nao definido'
        result['country'] = 'Nao definido'
        if len(geocode_result) > 0:
            geocode_result = geocode_result[0]['address_components']
            for x in geocode_result:
                if x['types'][0] == 'administrative_area_level_2':
                    result['city'] = x['long_name']
                elif x['types'][0] == 'administrative_area_level_1':
                    result['state'] = x['long_name']
                elif x['types'][0] == 'country':
                    result['country'] = x['long_name']
        return result






texto = limparTexto('av gal/ newton /cavalcanti')
formatPlace = FormatPlace(texto)
print(formatPlace.localizationAddress())
 
