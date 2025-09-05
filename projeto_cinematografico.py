# -*- coding: utf-8 -*-

import pandas as pd 

# Carregamento do arquivo
pd.read_csv("desafio_indicium_imdb - desafio_indicium_imdb.csv")

# Criação do primeiro DataFrame 
filmes = pd.read_csv("desafio_indicium_imdb - desafio_indicium_imdb.csv")

# Conversão da coluna 'No_of_Votes'
filmes['No_of_Votes'] = pd.to_numeric(filmes['No_of_Votes'])

# Criação de lista com as variáveis numéricas do DataFrame
colunas_numericas = ['IMDB_Rating', 'Meta_score', 'No_of_Votes', 'Gross', 'Runtime']

# A partir da extração da lista, criação de um DataFrame só com essas variáveis
df_numerico = filmes[colunas_numericas]

# Conversão da coluna 'Gross' no DataFrame 'filmes'
filmes['Gross'] = pd.to_numeric(filmes['Gross'].astype(str).str.replace(',', '', regex=True), errors='coerce')

# Conversão da coluna 'Runtime' no DataFrame 'filmes'
filmes['Runtime'] = pd.to_numeric(filmes['Runtime'].astype(str).str.replace(' min', '', regex=False), errors='coerce')

# Conversão da coluna 'Gross' no DataFrame 'df_numerico'
df_numerico['Gross'] = pd.to_numeric(df_numerico['Gross'].astype(str).str.replace(',', '', regex=True), errors='coerce')

# Conversão da coluna 'Runtime' no DataFrame 'df_numerico'
df_numerico['Runtime'] = pd.to_numeric(df_numerico['Runtime'].astype(str).str.replace(' min', '', regex=False), errors='coerce')

# Cálculo a partir de uma matriz de correlação
matriz_correlacao = df_numerico.corr()

# Cálculo a partir de uma matriz de correlação com o método Spearman
matriz_correlacao_spearman = df_numerico.corr(method='spearman')

# A primeira matriz utiliza o método padrão Pearson, que é mais sensível a outliers.
# A segunda matriz utiliza o método Spearman apenas com o intuito de validação
# do baixo indíce de dispersão dos dados, visto que são valores próximos à primeira.

# As conexões mais fortes são vistas entre as variáveis IMDB_Rating e
# No_of_Votes e também entre No_of_Votes e Gross.

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Novo carregamento do arquivo
filmes = pd.read_csv("desafio_indicium_imdb - desafio_indicium_imdb.csv")

# Limpeza e conversão das colunas
filmes['Gross'] = pd.to_numeric(filmes['Gross'].astype(str).str.replace(',', '', regex=True), errors='coerce')
filmes['Runtime'] = pd.to_numeric(filmes['Runtime'].astype(str).str.replace(' min', '', regex=False), errors='coerce')
filmes['No_of_Votes'] = pd.to_numeric(filmes['No_of_Votes'].astype(str).str.replace(',', '', regex=True), errors='coerce')

# Remover linhas com valores nulos
filmes.dropna(subset=['Gross', 'Director', 'Genre'], inplace=True)

# Agrupar por diretor e encontrar o top 5
agrupamento_diretores = filmes.groupby('Director').agg({'Gross': 'sum'})
top_5_diretores = agrupamento_diretores.nlargest(5, 'Gross')

# Agrupar por gênero e encontrar o top 5
# A coluna de gênero precisa de tratamento especial, pois um filme pode ter múltiplos gêneros
df_generos = filmes.copy()

df_generos['Genre'] = df_generos['Genre'].str.split(', ')

df_generos = df_generos.explode('Genre')

agrupamento_generos = df_generos.groupby('Genre').agg({'Gross': 'sum'})

top_5_generos = agrupamento_generos.nlargest(5, 'Gross')

print(top_5_diretores)

print(top_5_generos)

# Novo carregamento para criação dos gráficos
df = pd.read_csv('desafio_indicium_imdb - desafio_indicium_imdb.csv')

# 'Gross' é lido como `object` e precisa ser limpo e convertido para numérico
df['Gross'] = pd.to_numeric(df['Gross'].astype(str).str.replace(',', '', regex=True), errors='coerce')

# 'Runtime' é lido como `object` e precisa ser limpo e convertido para numérico
df['Runtime'] = pd.to_numeric(df['Runtime'].astype(str).str.replace(' min', '', regex=False), errors='coerce')

# Remover linhas com valores nulos nas colunas de interesse para os gráficos
df.dropna(subset=['Gross', 'IMDB_Rating', 'Director', 'No_of_Votes'], inplace=True)

# Agrupar por diretor e somar o faturamento e o número de votos
diretores_agrupados = df.groupby('Director').agg({'Gross': 'sum', 'No_of_Votes': 'sum'})
top_5_diretores = diretores_agrupados.nlargest(5, 'Gross')

# Criação do gráfico de diretores
top_5_diretores[['Gross', 'No_of_Votes']].plot(kind='barh', figsize=(12, 8))
plt.title('Relação entre Faturamento e Votos para Top 5 Diretores')
plt.xlabel('Valor Total')
plt.ylabel('Diretor')
plt.legend(['Faturamento', 'Número de Votos'])
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig('top_5_diretores_grafico.png')

# Tratamento dos dados para o gráfico de gêneros
df_genres = df.copy()
df_genres['Genre'] = df_genres['Genre'].str.split(', ')
df_genres = df_genres.explode('Genre')

# Agrupar por gênero e somar o faturamento e o número de votos
generos_agrupados = df_genres.groupby('Genre').agg({'Gross': 'sum', 'No_of_Votes': 'sum'})
top_5_generos = generos_agrupados.nlargest(5, 'Gross')

# O gráfico demonstra visualmente que os diretores com maior faturamento total
# também são aqueles cujos filmes têm o maior número de votos.

#Criação do gráfico de gêneros
top_5_generos[['Gross', 'No_of_Votes']].plot(kind='barh', figsize=(12, 8), color=['coral', 'lightblue'])
plt.title('Relação entre Faturamento e Votos para Top 5 Gêneros')
plt.xlabel('Valor Total')
plt.ylabel('Gênero')
plt.legend(['Faturamento', 'Número de Votos'])
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig('top_5_generos_grafico.png')

# De maneira semelhante, este gráfico mostra que os gêneros de maior faturamento
# também são os que recebem o maior número de votos.

# Para encontrar o filme com a maior nota no IMDB e o maior número de votos
top_rated_movie = df.sort_values(by=['IMDB_Rating', 'No_of_Votes'], ascending=[False, False]).iloc[0]

print("\n### Recomendação de Filme para uma pessoa desconhecida ###")
print(f"Filme: {top_rated_movie['Series_Title']}")
print(f"Ano: {top_rated_movie['Released_Year']}")
print(f"Gênero: {top_rated_movie['Genre']}")
print(f"IMDB_Rating: {top_rated_movie['IMDB_Rating']}")
print(f"Votos: {top_rated_movie['No_of_Votes']}")
print(f"Diretor: {top_rated_movie['Director']}")
print(f"Sinopse: {top_rated_movie['Overview']}")

# O filme a ser recomendado, com base nestes critérios, seria 'The Godfather'.

# Retomar a seleção das colunas numéricas para nova análise de correlação
colunas_numericas = ['IMDB_Rating', 'Meta_score', 'No_of_Votes', 'Gross', 'Runtime']
df_numerico = df[colunas_numericas].dropna()

# Matriz de Correlação para mostrar a relação entre as variáveis
matriz_correlacao = df_numerico.corr()
print("\n### Matriz de Correlação das Variáveis Numéricas ###")
print(matriz_correlacao)

# Análise de top diretores e gêneros
top_diretores = df.groupby('Director')['Gross'].sum().nlargest(5)
top_generos = df_genres.groupby('Genre')['Gross'].sum().nlargest(5)

print("\n### Top 5 Diretores por Faturamento ###")
print(top_diretores)
print("\n### Top 5 Gêneros por Faturamento ###")
print(top_generos)

# Como vimos na primeira análise de correlação, o fator mais correlacionado ao
# faturamento (Gross) é a popularidade do diretor e/ou gênero (No_of_Votes).
