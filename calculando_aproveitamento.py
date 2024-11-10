import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados
df = pd.read_csv('brasileirao_serie_a.csv')  # Abrimos o arquivo
df = df.fillna(0)  # Substituímos valores nulos por 0

# Solicitar entrada do usuário
ano_escolhido = int(input('Escolha um ano para analisar: '))
time_escolhido = input('Escolha um time para comparar: ')

# Filtrar jogos do time escolhido como mandante e visitante no ano escolhido
jogos_mandante = df[(df['ano_campeonato'] == ano_escolhido) & (df['time_mandante'] == time_escolhido)]
jogos_visitante = df[(df['ano_campeonato'] == ano_escolhido) & (df['time_visitante'] == time_escolhido)]

# Calcular vitórias, empates e derrotas em casa
vitorias_casa = jogos_mandante[jogos_mandante['gols_mandante'] > jogos_mandante['gols_visitante']].shape[0]
empates_casa = jogos_mandante[jogos_mandante['gols_mandante'] == jogos_mandante['gols_visitante']].shape[0]
derrotas_casa = jogos_mandante[jogos_mandante['gols_mandante'] < jogos_mandante['gols_visitante']].shape[0]

# Calcular vitórias, empates e derrotas fora
vitorias_fora = jogos_visitante[jogos_visitante['gols_visitante'] > jogos_visitante['gols_mandante']].shape[0]
empates_fora = jogos_visitante[jogos_visitante['gols_visitante'] == jogos_visitante['gols_mandante']].shape[0]
derrotas_fora = jogos_visitante[jogos_visitante['gols_visitante'] < jogos_visitante['gols_mandante']].shape[0]

# Calcular pontos obtidos
pontos_casa = (vitorias_casa * 3) + (empates_casa * 1)
pontos_fora = (vitorias_fora * 3) + (empates_fora * 1)

# Calcular total de jogos
total_jogos_casa = jogos_mandante.shape[0]
total_jogos_fora = jogos_visitante.shape[0]

# Calcular pontos possíveis
pontos_possiveis_casa = total_jogos_casa * 3
pontos_possiveis_fora = total_jogos_fora * 3

# Calcular aproveitamento
aproveitamento_casa = (pontos_casa / pontos_possiveis_casa) * 100 if pontos_possiveis_casa > 0 else 0
aproveitamento_fora = (pontos_fora / pontos_possiveis_fora) * 100 if pontos_possiveis_fora > 0 else 0

# Criar o gráfico
labels = ['Casa', 'Fora']
aproveitamentos = [aproveitamento_casa, aproveitamento_fora]
plt.figure(figsize=(8, 5))
plt.bar(labels, aproveitamentos, color=['blue', 'orange'])
plt.title(f'Aproveitamento de {time_escolhido} em {ano_escolhido}')
plt.xlabel('Local do Jogo')
plt.ylabel('Aproveitamento (%)')
plt.show()