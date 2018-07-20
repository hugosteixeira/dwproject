
import numpy
import re

def edit_distance(s1, s2):
    s1_len = len(s1)
    s2_len = len(s2)
    E = numpy.zeros(shape=(s1_len+1,s2_len+1))
    for i in range(s1_len):
        E[i, 0] = i
    for j in range(s2_len):
        E[0, j] = j
    for i in range(s1_len):
        i += 1
        for j in range(s2_len):
            j += 1
            diff_i_j = 0 if s1[i-1] == s2[j-1] else 1
            E[i, j] = numpy.min([1+E[i-1, j], 1+E[i, j-1], E[i-1, j-1] + diff_i_j])
    return E[s1_len, s2_len]



listSimple=['Acre', 'Alagoas', 'Amapá',
        'Amazonas', 'Bahia', 'Ceará',
        'Goiás', 'Maranhão', 'Pará',
        'Paraíba', 'Paraná', 'Pernambuco',
        'Piauí','Rondônia', 'Roraima',
        'Sergipe', 'Tocantins']

listaCompose=['Distrito Federal', 'Espírito Santo', 'Mato Grosso',
        'Mato Grosso Sul', 'Minas Gerais', 'Rio Janeiro',
        'Rio Grande Norte', 'Rio Grande Sul',
        'Santa Catarina', 'São Paulo']

listaComposeSpliit=['Distrito', 'Federal', 'Espírito', 'Santo', 'Mato', 'Grosso',
        'Mato', 'Grosso', 'Sul', 'Minas', 'Gerais', 'Rio', 'Janeiro',
        'Rio', 'Grande', 'Norte', 'Rio', 'Grande', 'Sul',
        'Santa', 'Catarina', 'São', 'Paulo']


dicSiglaEstado ={'RR': 'Roraima', 'PA': 'Pará', 'BA': 'Bahia', 'RO': 'Rondônia',
                 'RN': 'Rio Grande do Norte', 'SE': 'Sergipe', 'MT': 'Mato Grosso',
                 'AL': 'Alagoas', 'SP': 'São Paulo', 'PR': 'Paraná', 'RJ': 'Rio de Janeiro'
                 , 'AM': 'Amazonas', 'PE': 'Pernambuco', 'PI': 'Piauí', 'TO': 'Tocantins',
                 'RS': 'Rio Grande do Sul', 'DF': 'Distrito Federal', 'GO': 'Goiás', 'AC': 'Acre',
                 'MS': 'Mato Grosso do Sul', 'CE': 'Ceará','AP': 'Amapá', 'MA': 'Maranhão',
                 'PB': 'Paraíba', 'MG': 'Minas Gerais', 'ES': 'Espírito Santo', 'SC': 'Santa Catarina'}

listaSigla = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO',
              'MA', 'MT', 'do', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE',
              'PI', 'de', 'RJ','RN','RS', 'RO', 'RR',
              'SC', 'SP', 'SE', 'TO']

def getLocal(text):
    
    listText = re.findall(r"[\w']+", text)
    result = {'pais':None, 'estado':None, 'cidade':None}
    estate = False
    simpleState = False
    #simplePosible = []
    composePosible =[]
    
    for i in listText:

        if edit_distance('Brasil', i) < 3 :
            result['pais'] = 'Brasil'

        if len(i) == 2:   
            if i.upper() in listaSigla:
                result['estado'] = dicSiglaEstado[i.upper()]
            estate = True
            
        elif not(estate):
            for name in listSimple:
                if edit_distance(name, i) < 3:
                    result['estado'] = name
                    estate = True
                    
        if not(simpleState)
        
    return (result)


            
            
    
    


            


