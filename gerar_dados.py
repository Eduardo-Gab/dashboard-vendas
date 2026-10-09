import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

produtos = ['Notebook', 'Mouse', 'Teclado', 'Monitor', 'Headset', 'Webcam']
regioes = ['Sul', 'Sudeste', 'Nordeste', 'Norte', 'Centro-Oeste']

dados = []
data_inicial = datetime(2024, 1, 1)

for i in range(2000):
    data = data_inicial + timedelta(days=random.randint(0, 600))
    dados.append({
        'data': data.strftime('%Y-%m-%d'),
        'produto': random.choice(produtos),
        'regiao': random.choice(regioes),
        'quantidade': random.randint(1, 20),
        'preco_unitario': round(random.uniform(50, 3000), 2)
    })

df = pd.DataFrame(dados)
df['valor_total'] = df['quantidade'] * df['preco_unitario']
df.to_csv('data/vendas.csv', index=False)
print("Dados gerados!")