# Dashboard de Vendas - Streamlit

Este é um aplicativo de dashboard de vendas desenvolvido com [Streamlit](https://streamlit.io/). O objetivo do aplicativo é fornecer uma visualização interativa das métricas de vendas, com opções para filtrar dados e gerar relatórios personalizados.

## Funcionalidades

O aplicativo possui duas páginas principais:

### 1. Dashboard de Vendas
Nesta página, você encontrará três abas principais com gráficos interativos:

- **Receita por Localização**: Gráficos de linhas e barras que mostram a receita geral, por localidade, por estado e por categorias.
- **Quantidade de Vendas**: Exibe gráficos sobre a quantidade de vendas por estado, vendas mensais, por categorias, entre outros.
- **Vendedores**: Gráficos com os principais vendedores por receita, quantidade de vendas e outros filtros.

Cada aba permite o uso de controladores e filtros para ajustar os dados exibidos e gerar gráficos dinâmicos.

### 2. Gerar Tabela e Download
Nesta página, você pode criar uma tabela filtrada dos dados de vendas e efetuar o download da tabela em diferentes formatos, incluindo CSV.

### 3. Tecnologias Utilizadas

- **Streamlit**: Para a criação de dashboards interativos.
- **Pandas**: Manipulação e análise de dados.
- **Plotly**: Criação de gráficos interativos.

### 4. Contribuição

- Faça um fork do repositório.
- Crie uma nova branch (git checkout -b feature-nova-funcionalidade).
- Faça as alterações necessárias e adicione os commits (git commit -m 'Adiciona nova funcionalidade').
- Envie para o repositório original (git push origin feature-nova-funcionalidade).
- Crie um Pull Request.

## Licença
  Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

## Contato
  Para mais informações, entre em contato através do e-mail: limarios18@outlook.com.

## Como Executar

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/Matlima/dashboard_streamlit.git
   cd dashboard_streamlit
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Execute o aplicativo:
````bash
streamlit run app.py
```

