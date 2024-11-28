import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados
# Lê o arquivo CSV que contém informações do campeonato brasileiro série A e armazena em um DataFrame
df = pd.read_csv('brasileirao_serie_a.csv')  
# Substituímos valores nulos (NaN) por 0 para evitar erros em operações futuras
df = df.fillna(0)

# Solicitar entrada do usuário
# Solicita ao usuário que escolha um ano para análise
ano_escolhido = int(input('Escolha um ano para analisar: '))
# Solicita ao usuário que escolha um time para comparação
time_escolhido = input('Escolha um time para comparar: ')

# Filtrar jogos do time escolhido como mandante e visitante no ano escolhido
# Seleciona os jogos em que o time escolhido foi mandante no ano especificado
jogos_mandante = df[(df['ano_campeonato'] == ano_escolhido) & (df['time_mandante'] == time_escolhido)]
# Seleciona os jogos em que o time escolhido foi visitante no ano especificado
jogos_visitante = df[(df['ano_campeonato'] == ano_escolhido) & (df['time_visitante'] == time_escolhido)]

# Calcular vitórias, empates e derrotas em casa
# Conta o número de vitórias como mandante (gols do mandante > gols do visitante)
vitorias_casa = jogos_mandante[jogos_mandante['gols_mandante'] > jogos_mandante['gols_visitante']].shape[0]
# Conta o número de empates como mandante (gols do mandante == gols do visitante)
empates_casa = jogos_mandante[jogos_mandante['gols_mandante'] == jogos_mandante['gols_visitante']].shape[0]
# Conta o número de derrotas como mandante (gols do mandante < gols do visitante)
derrotas_casa = jogos_mandante[jogos_mandante['gols_mandante'] < jogos_mandante['gols_visitante']].shape[0]

# Calcular vitórias, empates e derrotas fora
# Conta o número de vitórias como visitante (gols do visitante > gols do mandante)
vitorias_fora = jogos_visitante[jogos_visitante['gols_visitante'] > jogos_visitante['gols_mandante']].shape[0]
# Conta o número de empates como visitante (gols do visitante == gols do mandante)
empates_fora = jogos_visitante[jogos_visitante['gols_visitante'] == jogos_visitante['gols_mandante']].shape[0]
# Conta o número de derrotas como visitante (gols do visitante < gols do mandante)
derrotas_fora = jogos_visitante[jogos_visitante['gols_visitante'] < jogos_visitante['gols_mandante']].shape[0]

# Calcular pontos obtidos
# Calcula os pontos obtidos em casa (3 pontos por vitória, 1 ponto por empate)
pontos_casa = (vitorias_casa * 3) + (empates_casa * 1)
# Calcula os pontos obtidos fora (3 pontos por vitória, 1 ponto por empate)
pontos_fora = (vitorias_fora * 3) + (empates_fora * 1)

# Calcular total de jogos
# Conta o total de jogos como mandante
total_jogos_casa = jogos_mandante.shape[0]
# Conta o total de jogos como visitante
total_jogos_fora = jogos_visitante.shape[0]

# Calcular pontos possíveis
# Calcula o total de pontos possíveis em casa (3 pontos por jogo)
pontos_possiveis_casa = total_jogos_casa * 3
# Calcula o total de pontos possíveis fora (3 pontos por jogo)
pontos_possiveis_fora = total_jogos_fora * 3

# Calcular aproveitamento
# Calcula o aproveitamento em casa (pontos obtidos / pontos possíveis * 100)
# Verifica se há pontos possíveis para evitar divisão por zero
aproveitamento_casa = (pontos_casa / pontos_possiveis_casa) * 100 if pontos_possiveis_casa > 0 else 0
# Calcula o aproveitamento fora (pontos obtidos / pontos possíveis * 100)
# Verifica se há pontos possíveis para evitar divisão por zero
aproveitamento_fora = (pontos_fora / pontos_possiveis_fora) * 100 if pontos_possiveis_fora > 0 else 0

# Criar o gráfico
# Define os rótulos para o gráfico de barras
labels = ['Casa', 'Fora']
# Lista com os valores de aproveitamento em casa e fora
aproveitamentos = [aproveitamento_casa, aproveitamento_fora]
# Define o tamanho da figura do gráfico
plt.figure(figsize=(8, 5))
# Cria um gráfico de barras com cores diferentes para cada local
plt.bar(labels, aproveitamentos, color=['blue', 'orange'])
# Adiciona título ao gráfico
plt.title(f'Aproveitamento de {time_escolhido} em {ano_escolhido}')
# Adiciona o rótulo do eixo X
plt.xlabel('Local do Jogo')
# Adiciona o rótulo do eixo Y
plt.ylabel('Aproveitamento (%)')
# Exibe o gráfico
plt.show()
