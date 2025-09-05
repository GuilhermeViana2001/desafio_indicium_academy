# Projeto cinematográfico da Indicium Academy

Projeto envolvendo o uso de Python para aplicação ao programa Lighthouse na modalidade de ciência de dados.

1. Análise Exploratória dos Dados (EDA)
O primeiro passo foi entender a estrutura e a qualidade do conjunto de dados. O arquivo desafio_indicium_imdb.csv foi carregado em um DataFrame do pandas. Algumas colunas, como 'Gross' (faturamento) e 'Runtime' (duração), estavam em formato de texto e continham caracteres como vírgulas e a unidade de medida (" min"), que precisaram ser limpos e convertidos para o formato numérico.

Com os dados limpos, a análise exploratória revelou insights cruciais:

Correlação: A matriz de correlação de Pearson mostrou uma relação forte e positiva entre o número de votos (No_of_Votes) e o faturamento (Gross). Isso sugere que filmes com maior popularidade, seja pelo diretor ou pelo gênero, tendem a gerar mais receita. A análise com o método de Spearman, cujos resultados foram muito próximos aos de Pearson, confirmou a ausência de outliers significativos que pudessem distorcer a análise.

2. Identificação dos Fatores de Sucesso
Para aprofundar as conclusões da EDA, a análise se concentrou em como os fatores categóricos se relacionam com o faturamento. O código agrupou os dados pelos 5 principais diretores e 5 principais gêneros com base na receita total. Os gráficos gerados a partir desses dados demonstraram visualmente que:

Os diretores com maior faturamento são também os que possuem o maior número de votos.

O mesmo se aplica aos gêneros: aqueles com a maior receita (Ação, Aventura, Sci-Fi) também são os mais populares.

Esses achados reforçam a conclusão de que o No_of_Votes é a variável-chave que liga a popularidade de um diretor ou de um gênero ao sucesso financeiro de um filme.

3. Considerações e Limitações do Projeto
Este projeto demonstra uma abordagem inicial para a análise de dados cinematográficos. No entanto, algumas limitações precisam ser observadas:

Análise de Texto (Overview): A análise da sinopse (Overview) não foi incluída, pois a extração de insights de texto corrido requer técnicas avançadas de Processamento de Linguagem Natural (PLN), um mecanismo que está além do meu escopo de conhecimento.

Modelo de Machine Learning: A construção de um modelo de machine learning para prever a nota do IMDB, bem como as suas etapas de preparação dos dados, foram tentadas. Contudo, esta etapa esbarrou no mesmo problema da análise de Overviews, ou seja, está além de meu escopo.

Em meu MBA, ainda não tive a oportunidade de construir um modelo de machine learning e este foi o meu primeiro projeto, onde depositei o conhecimento em Python que venho desenvolvendo nos últimos meses. É só o começo.