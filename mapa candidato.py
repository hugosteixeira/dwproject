from folium import plugins
from folium.plugins import HeatMap
import folium
from DAO import Dao
from DB_helper import DB_helper

dbHelper = DB_helper()
cursor = dbHelper.getCursor()
query = '''select c.nome,Sentimento_idSentimento,lat,lng from tweet t
inner join tweetcandidato tc on Tweet_idTweet= idTweet
inner join sentimento s on idSentimento=Sentimento_idSentimento
inner join lugar l on Lugar_idLugar=idLugar and lat<>0 and lng<>0
inner join candidato c on idCandidato=Candidato_idCandidato'''
cursor.execute(query)
result = cursor.fetchall()
#indexList = [1,2,3]
nomeCandidato = ['Bolsonaro', 'Lula', 'Ciro', 'Marina']

for nome in nomeCandidato :
    
    tList =[]
    positiveList =[]
    nullList = []
    negativeList =[]
    
    for i in result:
        if i['nome'] == nome:
            sent = int(i['Sentimento_idSentimento'])
            lat = float(i['lat'])
            lng = float(i['lng'])
            lista =[lat,lng]
            if sent == 1:
                negativeList.append(lista)
            elif sent == 2:
                nullList.append(lista)
            elif sent == 3:
                positiveList.append(lista)
            tList.append(lista)
    
    dicMap = {'mapaTotal': tList, 'mapaPositivo' : positiveList, 'mapaNeutro' : nullList, 'mapaNegativo': negativeList}

    config0 = location=[-16.1237611, -59.9219642]
    config1 = zoom_start=4

    for key in dicMap.keys():
        mapa = folium.Map(location=[-15.788497,-47.879873],tiles='Stamen Toner',zoom_start=4)
        mapa.add_child(plugins.HeatMap(dicMap[key]))
        mapa.save(nome+' '+key+'.html')
    


