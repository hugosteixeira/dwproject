import requests
import json
from flask import request, jsonify
from flask.views import MethodView
from sqlalchemy import inspect
import googlemaps
from utils import printError
    

class FormatPlace :


    def __init__(self,location):
        self.gmaps = googlemaps.Client(key='AIzaSyD8b3UyPssRS9CwgWuW-788UFaZYS1oi9Q')
        self.address_components=location


    def localizationAddress(self):
        try:
            print ("Minha localizacao e ", self.address_components)
            geocode_result = self.gmaps.geocode(self.address_components,language='pt-br',region='BR')
        
            address_components = {}

        
            if len(geocode_result[0]['address_components'])==3:
                address_components['city']= geocode_result[0]['address_components'][0]['long_name']
                address_components['state']=geocode_result[0]['address_components'][1]['long_name']
                address_components['country']=geocode_result[0]['address_components'][2]['long_name']
            if len(geocode_result[0]['address_components'])==2:
                address_components['city']= ''
                address_components['state']=geocode_result[0]['address_components'][0]['long_name']
                address_components['country']=geocode_result[0]['address_components'][1]['long_name']
            if len(geocode_result[0]['address_components'])==1:
                address_components['city']= ''
                address_components['state']=''
                address_components['country']=geocode_result[0]['address_components'][0]['long_name']
            else:
                address_components['city']= ''
                address_components['state']=''
                address_components['country']=''
            print('teste',address_components)
            return address_components

        except:
            address_components = {}
            address_components['city']= ''
            address_components['state']=''
            address_components['country']=''
            printError()
            return address_components





 
