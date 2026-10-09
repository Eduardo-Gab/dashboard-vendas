import pandas as pd
from sqlalchemy import create_engine

def carregar_dados():
    df = pd.read_csv('data/vendas.csv')
    df['data'] = pd.to_datetime(df['data'])
    
    engine = create_engine('sqlite:///database/vendas.db')
    df.to_sql('vendas', engine, if_exists='replace', index=False)
    print(f"{len(df)} registros carregados no banco!")

if __name__ == '__main__':
    carregar_dados()