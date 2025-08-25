import pandas as pd
from prophet import Prophet

def forecast_product(df, produto, periods=4, freq='W'):
    """
    Gera forecast para um único produto.
    
    df: DataFrame com colunas ['data','produto','vendas']
    produto: nome do produto
    periods: número de períodos futuros a prever
    freq: frequência ('D', 'W', 'M')
    
    Retorna DataFrame com colunas ['ds','yhat','yhat_lower','yhat_upper']
    """
    df_prod = df[df['produto'] == produto][['data','vendas']].rename(columns={'data':'ds','vendas':'y'})
    df_prod['ds'] = pd.to_datetime(df_prod['ds'], format="%d/%m/%Y")
    
    model = Prophet()
    model.fit(df_prod)
    
    future = model.make_future_dataframe(periods=periods, freq=freq)
    forecast = model.predict(future)
    
    return forecast[['ds','yhat','yhat_lower','yhat_upper']]

def forecast_all_products(df, periods=4, freq='W'):
    """
    Gera forecast para todos os produtos do DataFrame.
    
    Retorna um dict {produto: forecast_df}
    """
    produtos = df['produto'].unique()
    all_forecasts = {}
    
    for produto in produtos:
        all_forecasts[produto] = forecast_product(df, produto, periods, freq)
    
    return all_forecasts

def save_forecasts_to_csv(forecasts_dict, output_dir="forecasts"):
    """
    Salva cada forecast em CSV no diretório especificado.
    """
    import os
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for produto, forecast in forecasts_dict.items():
        filename = os.path.join(output_dir, f"forecast_{produto.replace(' ','_')}.csv")
        forecast.to_csv(filename, index=False, encoding="utf-8")
    print(f"Todos os forecasts salvos em {output_dir}/")
