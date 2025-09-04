# -*- coding: utf-8 -*-

import pandas as pd 

pd.read_csv("desafio_indicium_imdb - desafio_indicium_imdb.csv")

filmes = pd.read_csv("desafio_indicium_imdb - desafio_indicium_imdb.csv")

filmes['No_of_Votes'] = pd.to_numeric(filmes['No_of_Votes'])

colunas_numericas = ['IMDB_Rating', 'Meta_score', 'No_of_Votes', 'Gross', 'Runtime']

df_numerico = filmes[colunas_numericas]

filmes['Gross'] = pd.to_numeric(filmes['Gross'].astype(str).str.replace(',', '', regex=True), errors='coerce')

filmes['Runtime'] = pd.to_numeric(filmes['Runtime'].astype(str).str.replace(' min', '', regex=False), errors='coerce')

df_numerico['Gross'] = pd.to_numeric(df_numerico['Gross'].astype(str).str.replace(',', '', regex=True), errors='coerce')

df_numerico['Runtime'] = pd.to_numeric(df_numerico['Runtime'].astype(str).str.replace(' min', '', regex=False), errors='coerce')

matriz_correlacao = df_numerico.corr()

matriz_correlacao_spearman = df_numerico.corr(method='spearman')

import seaborn as sns
import matplotlib.pylot as plt
import numpy as np





