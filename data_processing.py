import pandas as pd

def processar_dados(data):
    df = pd.DataFrame(data)
    df['aluguel'] = df['aluguel'].apply(lambda x: float(x.replace('R$ ', '').replace('.', '').replace('/mês', '').replace(',', '.')))
    df['area'] = df['area'].apply(lambda x: float(x.replace(' m²', '')))
    return df
