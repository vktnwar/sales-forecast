# SalesForecast-Optimizer

Um dashboard interativo para previsão de vendas e otimização de compras, desenvolvido em Python com Streamlit e modelos de séries temporais.

## ✨ Características

* 📊 Forecast de vendas por produto usando séries temporais (Prophet)
* ⚠️ Alertas automáticos para produtos em risco de encalhe
* 📈 Gráficos interativos consolidados e por produto
* 🧮 Indicadores resumidos: total previsto, média semanal, mínimo/máximo, alertas
* 💰 Otimização de compras baseada em orçamento
* ⬇️ Exportação de forecast detalhado em CSV

## 🚀 Instalação

### Opção 1: Clonar e rodar localmente

```bash
git clone https://github.com/seu-usuario/SalesForecast-Optimizer
cd SalesForecast-Optimizer
pip install -r requirements.txt
streamlit run app.py
```

### Opção 2: Executar diretamente no ambiente de desenvolvimento

```bash
streamlit run app.py
```

---

## 📖 Uso

1. Faça upload do CSV de vendas com as colunas: `data`, `produto`, `vendas`
2. Selecione os produtos que deseja analisar
3. Configure o número de semanas para previsão e o limite de alerta de encalhe
4. Navegue pelas abas:

   * **Dashboard**: gráficos consolidados
   * **Forecast**: previsão detalhada por produto
   * **Indicadores**: resumo estatístico
   * **Otimização de Compras**: sugestão de quantidade ideal com base no orçamento
5. Baixe os dados em CSV para análise externa

---

## ⚙️ Estrutura das abas

| Aba                   | Descrição                                                                 |
| --------------------- | ------------------------------------------------------------------------- |
| Dashboard             | Gráficos interativos consolidados de previsão por produto com alertas     |
| Forecast              | Forecast detalhado de cada produto com intervalo de confiança             |
| Indicadores           | Indicadores resumidos por produto (total, média, máximo, mínimo, alertas) |
| Otimização de Compras | Quantidade ideal de compra baseada em orçamento e preços unitários        |

---

## 💡 Exemplos

### Forecast de um produto

* Visualização de vendas previstas para as próximas semanas
* Alertas de encalhe destacados

### Otimização de Compras

* Entrada: orçamento disponível e preço unitário
* Saída: quantidade recomendada de cada produto para minimizar risco de encalhe e rupturas

---

## 📋 Requisitos

* Python 3.9 ou superior
* Bibliotecas: `pandas`, `plotly`, `streamlit`, `prophet`, `scipy`

## 🛠️ Desenvolvimento

```bash
# Clonar repositório
git clone https://github.com/seu-usuario/SalesForecast-Optimizer
cd SalesForecast-Optimizer

# Instalar dependências
pip install -r requirements.txt

# Rodar em modo desenvolvimento
streamlit run app.py
```

---

## 📄 Licença

MIT License - veja o arquivo [LICENSE](LICENSE) para detalhes.

---

## 🤝 Contribuição

Contribuições são bem-vindas! Por favor, abra uma issue ou envie um pull request.

---

## 🚧 Próximas Funcionalidades

* [ ] Previsão de ruptura de estoque (produtos que podem faltar)
* [ ] Dashboard com cores e painéis mais visuais
* [ ] Exportação de relatórios em PDF prontos para gestores
* [ ] Integração com base de dados real para atualização automática de vendas

Quer que eu faça essa versão visual mais “apresentável”?
