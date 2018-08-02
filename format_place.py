import requests
import json
from flask import request, jsonify
from flask.views import MethodView
from sqlalchemy import inspect
import googlemaps
from utils import limparTexto
    
#AIzaSyCotn92FQLnipKRx1Tr4PK34ws3XXo89ws
#AIzaSyC1r8ltFnKQYnSt5yRV-3PvdC73N3W3qRs
#AIzaSyDaL09Gi0yE7DU-aMpkwa0Dxoo_Mt9L7-s
#AIzaSyAFx1S50JHA8CEygyc2eqgRv2OQ596nc38
#AIzaSyD8b3UyPssRS9CwgWuW-788UFaZYS1oi9Q

class FormatPlace :


    def __init__(self,location=''):
        self.gmaps = googlemaps.Client(key='AIzaSyC1r8ltFnKQYnSt5yRV-3PvdC73N3W3qRs')
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