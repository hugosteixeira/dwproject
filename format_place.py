import requests
import json
from flask import request, jsonify
from flask.views import MethodView
from sqlalchemy import inspect
import googlemaps
from utils import limparTexto
    
class FormatPlace :


    def __init__(self,location=''):
        self.gmaps = googlemaps.Client(key='GOOGLE API KEY AQUI')
        if location == '':
            location = ' '
        self.address_components=location


    def localizationAddress(self):
        geocode_result = self.gmaps.geocode(self.address_components,language='pt-br')
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

    def localizationCoord(self,address):
        geocode_result = self.gmaps.geocode(address,language='pt-br')
        result = {}
        result ['lat'] = '0'
        result['lng'] = '0'
        if len(geocode_result) > 0:
            geocode_result = geocode_result[0]['geometry']['location']
            print(geocode_result)
            result ['lat'] = geocode_result['lat']
            result ['lng'] = geocode_result['lng']
        return result