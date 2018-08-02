# Analise de sentimento dos presidenciáveis 2018

Projeto acadêmico da cadeira: Datawarehouse and Business Inteligence, UFRPE.

Esse projeto tem como objetivo principal, desenvolvimento intelectual dos alunos.
Funcionalidades do Sistema:
```
• Obter tweets sobre determinadas hashtags(sobre candidatos).
• Analizar o sentimento dos tweets.
• Usar um Datawarehouse para obter informações sobre os dados coletados.
```

## Requerimentos:
```
• Python 3 - Usado em todo o projeto
• Versão mais atual do perl
```
Perl - Usado no [Linguakit](https://github.com/citiususc/Linguakit) - Biblioteca de Analise de Sentimentos.


## Instalação
### Clone do repositório usando
```
git clone https://github.com/hugosteixeira/dwproject.git
```

### Instale os requerimentos usando
```
pip install -r requirements.txt
```

## Usando

### Minerando os Ids dos tweets
```
python main.py newHashtag <id do candidato no banco de dados> <hashtag>
python main.py mineHashtag <id do candidato no banco de dados> <hashtag> p
```

### Minerando e analisando os tweets
```
python main.py mineTweet
```

#### Limitação
Trabalhar com tweets tem os seus problemas, a maior parte das localizações fornecidas pelos usuários são invalidas ou dificeis de se trabalhar.
Estamos usando a api de geocoding do google para tratar esses lugares e transformar em localizaçoes válidas. Daí temos a maior limitação, o goole limita o uso de sua api de geocoding a 2500 usos diários em modo grátis.
