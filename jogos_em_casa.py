import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados
# Lê o arquivo CSV que contém os dados do Campeonato Brasileiro Série A e carrega em um DataFrame
df = pd.read_csv('brasileirao_serie_a.csv')

# Substituir valores nulos por 0
# Preenche valores ausentes (NaN) no DataFrame com 0, garantindo que não haja problemas durante as análises
df = df.fillna(0)

# Solicitar entrada do usuário
# Solicita ao usuário o ano a ser analisado
ano_escolhido = int(input('Escolha um ano para analisar: '))
# Solicita ao usuário o time para análise
time_escolhido = input('Escolha um time para comparar: ')

# Filtrar jogos do time escolhido no ano escolhido
# Seleciona apenas os jogos onde o time escolhido foi mandante e que ocorreram no ano escolhido
jogos_time = df[(df['ano_campeonato'] == ano_escolhido) & (df['time_mandante'] == time_escolhido)]

# Calcular vitórias, empates e derrotas
# Conta o número de vitórias: jogos em que o time mandante marcou mais gols que o visitante
vitorias = jogos_time[jogos_time['gols_mandante'] > jogos_time['gols_visitante']].shape[0]
# Conta o número de empates: jogos em que o time mandante e o visitante marcaram o mesmo número de gols
empates = jogos_time[jogos_time['gols_mandante'] == jogos_time['gols_visitante']].shape[0]
# Conta o número de derrotas: jogos em que o time mandante marcou menos gols que o visitante
derrotas = jogos_time[jogos_time['gols_mandante'] < jogos_time['gols_visitante']].shape[0]

# Preparar os dados para o gráfico
# Definição das categorias que serão mostradas no gráfico
labels = ['Vitórias', 'Empates', 'Derrotas']
# Quantidades correspondentes a cada categoria
sizes = [vitorias, empates, derrotas]
# Cores para cada categoria no gráfico
colors = ['blue', 'green', 'red']
# Destaca a fatia correspondente às vitórias no gráfico (explode desloca essa fatia)
explode = (0.1, 0, 0)

# Criar o gráfico de pizza
plt.figure(figsize=(8, 6))  # Define o tamanho do gráfico
# Gera o gráfico de pizza com os dados fornecidos
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%')
# Garante que o gráfico seja desenhado como um círculo perfeito
plt.axis('equal')
# Define o título do gráfico, indicando o time e o ano analisados
plt.title(f'Desempenho de {time_escolhido} em {ano_escolhido}')
# Exibe o gráfico
plt.show()
