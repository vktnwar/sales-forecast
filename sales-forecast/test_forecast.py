import pandas as pd
from utils.forecast import forecast_all_products, save_forecasts_to_csv

# Ler CSV de vendas
df = pd.read_csv("data/exemplo_vendas.csv")

# Gerar previsões para todos os produtos
forecasts = forecast_all_products(df, periods=4, freq='W')

# Salvar previsões em CSV
save_forecasts_to_csv(forecasts)

# Teste: exibir forecast do Produto 1
print(forecasts['Produto 1'].tail())
