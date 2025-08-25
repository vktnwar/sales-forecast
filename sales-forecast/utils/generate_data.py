import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Configurações
num_produtos = 30
num_semanas = 24
start_date = datetime(2025, 1, 1)

# Gerar lista de produtos
produtos = [f"Produto {i+1}" for i in range(num_produtos)]

# Gerar datas semanais
datas = [start_date + timedelta(weeks=i) for i in range(num_semanas)]

# Criar lista de registros
registros = []
for data in datas:
    for produto in produtos:
        vendas = np.random.randint(5, 100)  # vendas aleatórias entre 5 e 100
        registros.append([data.strftime("%d/%m/%Y"), produto, vendas])

# Criar DataFrame
df = pd.DataFrame(registros, columns=["data", "produto", "vendas"])

# Salvar CSV
df.to_csv("data/exemplo_vendas.csv", index=False, encoding="utf-8")

print("CSV de exemplo gerado em data/exemplo_vendas.csv")
