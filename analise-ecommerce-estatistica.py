import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Lendo o arquivo CSV
df = pd.read_csv('C:/Users/erika/Downloads/ecommerce_estatistica.csv')

print(df.columns)
df.head()

# Mudança e correção em Temporada
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

#  Histograma - Nota
plt.figure(figsize=(10,6))
sns.histplot(df['Preço'], kde=True, bins=20, color='orange')
plt.title('Distribuição dos Preços')
plt.xlabel('Preço (R$)')
plt.ylabel('Frequência')
plt.grid(True)
plt.show()


#  Gráfico de Dispersão - Avaliações x Preço
plt.figure(figsize=(10, 6))
plt.scatter(df['N_Avaliações'], df['Preço'])
plt.title("Dispersão entre Número de Avaliações e Preço")
plt.xlabel("Número de Avaliações")
plt.ylabel("Preço (R$)")
plt.tight_layout()
plt.show()

#  Mapa de Calor - Correlação
plt.figure(figsize=(12, 8))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Mapa de Calor das Correlações")
plt.tight_layout()
plt.show()

#  Gráfico de Barras - por Material
plt.figure(figsize=(12, 8))
df['Material'].value_counts().plot(kind='bar', color='#03a5fc')
plt.title("Quantidade de Produtos por Material")
plt.xlabel("Material")
plt.ylabel("Quantidade")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

#  Gráfico de Pizza - por Temporada (ajustando valores)
temporada = df['Temporada'].value_counts()
plt.figure(figsize=(8,8))
plt.pie(temporada, labels=temporada.index, autopct='%1.1f%%', startangle=140)
plt.title('Distribuição por Temporada')
plt.axis('equal')
plt.legend(title='Temporada')
plt.tight_layout()
plt.show()

#  Gráfico de Densidade - Preço
plt.figure(figsize=(10, 6))
sns.kdeplot(df['Preço'], fill=True, color="green")
plt.title("Densidade de Preço dos Produtos")
plt.xlabel("Preço (R$)")
plt.ylabel("Densidade")
plt.grid(True)
plt.show()

#  Gráfico de Regressão - Avaliações x Preço
plt.figure(figsize=(10, 6))
sns.regplot(x='N_Avaliações', y='Preço', data=df, line_kws={"color": "red"})
plt.title("Regressão: Número de Avaliações vs Preço")
plt.xlabel("Número de Avaliações")
plt.ylabel("Preço (R$)")
plt.tight_layout()
plt.show()

