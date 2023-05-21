import pandas as pd
from flask_sqlalchemy import SQLAlchemy
from extractor import extrair_dados_vivareal
from data_processing import processar_dados

# Extrai os dados
url = "https://www.vivareal.com.br/aluguel/sp/sao-paulo/zona-sul/"
dados = extrair_dados_vivareal(url)

# Processa os dados
df = processar_dados(dados)

# Exporta os dados para um arquivo Excel
df.to_excel('dados_imoveis.xlsx', index=False)

# Salva os dados no banco de dados SQL
engine = create_engine('sqlite:///imoveis.db')
df.to_sql('imoveis', engine, if_exists='replace', index=False)
