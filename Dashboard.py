import streamlit as st
import requests
import pandas as pd
import plotly.express as px

# Adicionando titulo ao aplicativo
st.title('DASHBOARD DE VENDAS :shopping_trolley:')

# Obtendo dados e tranformando para dataframe
url = 'https://labdados.com/produtos'
response = requests.get(url)
dados = pd.DataFrame.from_dict(response.json())

# Exibindo dataframe na aplicação
st.dataframe(dados)

