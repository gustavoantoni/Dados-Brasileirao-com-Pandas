import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados
df = pd.read_csv('brasileirao_serie_a.csv')  # Abrimos o arquivo
df = df.fillna(0)  # Substituímos valores nulos por 0

# Solicitar entrada do usuário
ano_escolhido = int(input('Escolha um ano para analisar: '))
time_escolhido = input('Escolha um time para comparar: ')

# Filtrar jogos do time escolhido no ano escolhido
jogos_time = df[(df['ano_campeonato'] == ano_escolhido) & (df['time_mandante'] == time_escolhido)]

# Calcular vitórias, empates e derrotas
vitorias = jogos_time[jogos_time['gols_mandante'] > jogos_time['gols_visitante']].shape[0]
empates = jogos_time[jogos_time['gols_mandante'] == jogos_time['gols_visitante']].shape[0]
derrotas = jogos_time[jogos_time['gols_mandante'] < jogos_time['gols_visitante']].shape[0]

# Preparar os dados para o gráfico
labels = ['Vitórias', 'Empates', 'Derrotas'] 
sizes = [vitorias, empates, derrotas]
colors = ['blue', 'green', 'red']
explode = (0.1, 0, 0)  # Destaca a fatia de vitórias

# Criar o gráfico de pizza
plt.figure(figsize=(8, 6))
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%')
plt.axis('equal') 
plt.title(f'Desempenho de {time_escolhido} em {ano_escolhido}')
plt.show()