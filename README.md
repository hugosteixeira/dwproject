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
• Google Chrome
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

### Criação do banco de dados
Rode os seguintes scrips SQL para criação da estratura dos bancos
```
• databaseStructure.sql
• dwStructure.sql
```

### Alterar os placeholders nos arquivos
```
format_place.py
tweet_from_id.py
```

### Minerando os Ids dos tweets
```
python main.py newHashtag <id do candidato no banco de dados> <hashtag>
python main.py mineHashtag <id do candidato no banco de dados> <hashtag> p
```

### Minerando e analisando os tweets
Minerará 2000 tweets se baseando pela tabela manager, onde o id inicial é o conteudo do arquivo Last_id.txt
```
python main.py mineTweet
```

#### Limitação
Trabalhar com tweets tem os seus problemas, a maior parte das localizações fornecidas pelos usuários são invalidas ou dificeis de se trabalhar.

Estamos usando a api de geocoding do google para tratar esses lugares e transformar em localizaçoes válidas. Daí temos a maior limitação, o goole limita o uso de sua api de geocoding a 2500 usos diários em modo grátis.

### Antes de usar as tranformações
Antes de usar as tranformações devemos povoar o banco com as datas, e alterar as conexões no pentaho para se adequar ao seu ambiente.
O arquivo para inserção das datas é
```
dimdata_carga.sql
```
### Usando as tranformações
Depois de que todos os seus dados forem minerados, você deve usar as tranformações para alimentar o seu DW.
Usando o pentaho use os seguintes arquivos da pasta transformações.
```
• transformacaoHashtag.ktr
• transformacaoCandidato.ktr
• transformacaoLugar.ktr
• transformacaoFato.ktr
```

### Depois das transformações
Depois das transformações prontas utilize o pentaho server juntamente com o [Saiku](https://www.dropbox.com/s/1j0symkdtpwb0g6/saiku-plugin-p7-3.15.zip?dl=1)(Colocar nesta pasta) para fazer as seleções do seu desejo.
```
pentaho-server/pentaho-solutions/system/
```
