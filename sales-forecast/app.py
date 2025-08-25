import streamlit as st
import pandas as pd
import plotly.express as px
from utils.forecast import forecast_product
from scipy.optimize import linprog

st.set_page_config(page_title="📈 Dashboard Profissional de Vendas", layout="wide")
st.title("📈 Dashboard de Previsão e Otimização de Vendas/Estoque")

# Upload CSV
uploaded_file = st.file_uploader("📤 Faça upload do CSV de vendas", type="csv")
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    required_cols = ['data','produto','vendas']
    if not all(col in df.columns for col in required_cols):
        st.error(f"O CSV precisa ter as colunas: {required_cols}")
    else:
        produtos = df['produto'].unique()
        selected_products = st.multiselect("Selecione os produtos:", produtos, default=list(produtos))
        periods = st.number_input("Quantas semanas à frente prever?", min_value=1, max_value=12, value=4)
        alerta_limite = st.number_input("Alerta de encalhe: vendas previstas abaixo de", min_value=0, value=10)

        all_forecasts = []
        indicadores_resumidos = []

        for produto in selected_products:
            forecast = forecast_product(df, produto, periods=periods, freq='W')
            forecast['Produto'] = produto
            forecast['Alerta de Encalhe'] = forecast['yhat'] < alerta_limite
            all_forecasts.append(forecast)

            indicadores_resumidos.append({
                'Produto': produto,
                'Total Previsto': forecast['yhat'].sum(),
                'Média Semanal': forecast['yhat'].mean(),
                'Máximo Previsto': forecast['yhat'].max(),
                'Mínimo Previsto': forecast['yhat'].min(),
                'Semanas com alerta': forecast['Alerta de Encalhe'].sum()
            })

        df_forecast = pd.concat(all_forecasts, ignore_index=True)
        df_indicadores = pd.DataFrame(indicadores_resumidos)

        # Criar abas
        tab1, tab2, tab3, tab4 = st.tabs(["📊 Dashboard", "📈 Forecast", "🧮 Indicadores", "💰 Otimização de Compras"])

        # ------------------- Aba 1: Dashboard -------------------
        with tab1:
            st.subheader("📊 Gráfico consolidado de previsão")
            fig = px.line(
                df_forecast, x='ds', y='yhat', color='Produto',
                labels={'ds':'Data','yhat':'Vendas Previstas'},
                title="Forecast consolidado"
            )
            alert_points = df_forecast[df_forecast['Alerta de Encalhe']]
            fig.add_scatter(
                x=alert_points['ds'], y=alert_points['yhat'], 
                mode='markers', marker=dict(color='orange', size=8, symbol='triangle-down'),
                name='Alerta de Encalhe'
            )
            st.plotly_chart(fig, use_container_width=True)

        # ------------------- Aba 2: Forecast detalhado -------------------
        with tab2:
            st.subheader("📄 Forecast detalhado por produto")
            forecast_display = df_forecast.rename(columns={
                'ds': 'Data',
                'yhat': 'Vendas Previstas',
                'yhat_lower': 'Vendas Mínimas (Confiança)',
                'yhat_upper': 'Vendas Máximas (Confiança)',
                'Produto': 'Produto',
                'Alerta de Encalhe': 'Alerta de Encalhe'
            })
            st.dataframe(forecast_display)
            csv = forecast_display.to_csv(index=False, encoding="utf-8")
            st.download_button("⬇️ Baixar forecast detalhado", data=csv, file_name="forecast_detalhado.csv", mime="text/csv")

        # ------------------- Aba 3: Indicadores resumidos -------------------
        with tab3:
            st.subheader("📊 Indicadores resumidos")
            st.dataframe(df_indicadores)

        # ------------------- Aba 4: Otimização de Compras -------------------
        with tab4:
            st.subheader("💰 Otimização de Compras")
            st.write("Defina o orçamento disponível e preço unitário de cada produto para receber a recomendação de quantidade ideal a comprar.")
            budget = st.number_input("Orçamento disponível", min_value=0, value=10000)
            df_prices = pd.DataFrame({
                'Produto': selected_products,
                'Preço Unitário': [st.number_input(f"Preço unitário {p}", min_value=0.0, value=10.0, step=0.1) for p in selected_products],
                'Total Previsto': df_indicadores['Total Previsto'].values
            })

            # Função de otimização linear
            c = -df_prices['Total Previsto'].values  # Maximizar vendas previstas
            A = df_prices['Preço Unitário'].values.reshape(1, -1)
            b = [budget]
            bounds = [(0, None) for _ in selected_products]

            result = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')
            if result.success:
                df_prices['Quantidade Recomendada'] = result.x
                st.dataframe(df_prices[['Produto','Preço Unitário','Quantidade Recomendada','Total Previsto']])
            else:
                st.error("Não foi possível otimizar a compra com o orçamento fornecido.")
