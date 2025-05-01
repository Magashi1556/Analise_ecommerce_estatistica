from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd

# 1. Carregar e preparar os dados (como no seu código original)
df = pd.read_csv('C:/Users/erika/Downloads/ecommerce_estatistica.csv')

# Limpeza da coluna Temporada (igual ao seu código)
df['Temporada'] = df['Temporada'].str.lower().str.strip()
df['Temporada'] = df['Temporada'].replace({
    'primavera/verão': 'Primavera-Verão',
    'primavera-verão': 'Primavera-Verão',
    'primavera/verão/outono/inverno': 'Todas Estações',
    'outono/inverno': 'Outono-Inverno',
    'primavera-verão - outono-inverno': 'Ano Todo',
    'primavera/verão - outono/inverno': 'Ano Todo',
    'primavera/verão/outono/inverno': 'Ano Todo',
    'não definido': 'Indefinido',
    '2021': 'Desatualizado'
})

# 2. Preparar opções para os filtros
lista_marcas = df['Marca'].unique()
options_marcas = [{'label': marca, 'value': marca} for marca in lista_marcas]

lista_temporadas = df['Temporada'].unique()
options_temporadas = [{'label': temp, 'value': temp} for temp in lista_temporadas]


# 3. Função para criar os gráficos (adaptada do seu código)
def cria_graficos(selecao_marca, selecao_temporada):
    # Aplicar filtros
    filtro_df = df.copy()
    if selecao_marca:
        filtro_df = filtro_df[filtro_df['Marca'].isin(selecao_marca)]
    if selecao_temporada:
        filtro_df = filtro_df[filtro_df['Temporada'].isin(selecao_temporada)]

    # Criar os gráficos (versão Plotly dos seus gráficos originais)
    fig1 = px.histogram(filtro_df, x='Preço', nbins=20, title='Distribuição dos Preços')
    fig2 = px.scatter(filtro_df, x='N_Avaliações', y='Preço', title='Dispersão: Avaliações × Preço')
    fig3 = px.bar(filtro_df['Material'].value_counts(), title='Produtos por Material')
    fig4 = px.pie(filtro_df, names='Temporada', title='Distribuição por Temporada')

    return fig1, fig2, fig3, fig4


# 4. Criar o aplicativo Dash no estilo que você já conhece
def cria_app():
    app = Dash(__name__)

    app.layout = html.Div([
        html.H1("Análise de E-commerce - Dashboard Interativo"),
        html.Div('Selecione os filtros para análise:'),

        html.Div([
            html.Label("Filtrar por Marca:"),
            dcc.Checklist(
                id='id_selecao_marca',
                options=options_marcas,
                value=[lista_marcas[0]],  # Valor padrão: primeira marca
                style={'margin-bottom': '20px'}
            ),

            html.Label("Filtrar por Temporada:"),
            dcc.Checklist(
                id='id_selecao_temporada',
                options=options_temporadas,
                value=[lista_temporadas[0]],  # Valor padrão: primeira temporada
                style={'margin-bottom': '20px'}
            )
        ], style={'padding': '20px', 'background-color': '#f5f5f5'}),

        dcc.Graph(id='id_histograma_precos'),
        dcc.Graph(id='id_dispersao_avaliacoes'),
        dcc.Graph(id='id_barras_materiais'),
        dcc.Graph(id='id_pizza_temporadas')
    ])

    return app


# 5. Executar o aplicativo com callbacks
if __name__ == '__main__':
    app = cria_app()


    @app.callback(
        [
            Output('id_histograma_precos', 'figure'),
            Output('id_dispersao_avaliacoes', 'figure'),
            Output('id_barras_materiais', 'figure'),
            Output('id_pizza_temporadas', 'figure')
        ],
        [
            Input('id_selecao_marca', 'value'),
            Input('id_selecao_temporada', 'value')
        ]
    )
    def atualizar_graficos(selecao_marca, selecao_temporada):
        fig1, fig2, fig3, fig4 = cria_graficos(selecao_marca, selecao_temporada)
        return fig1, fig2, fig3, fig4


    app.run(debug=True, port=8050)