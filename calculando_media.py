import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados
# Lê os dados do arquivo CSV que contém informações sobre os jogos do Brasileirão Série A
df = pd.read_csv('brasileirao_serie_a.csv')

# Substituir valores nulos por zero
# Preenche valores nulos (NaN) no DataFrame com 0 para evitar problemas em cálculos
df = df.fillna(0)

# Tratamento de dados para evitar conflitos de tipos
# Converte a coluna 'ano_campeonato' para tipo inteiro
df['ano_campeonato'] = df['ano_campeonato'].astype(int)
# Converte a coluna 'publico' para tipo numérico, substituindo valores inválidos por NaN e, em seguida, preenche esses NaN com 0
df['publico'] = pd.to_numeric(df['publico'], errors='coerce').fillna(0)

# Entrada do usuário
# Solicita ao usuário o ano desejado para análise
ano_escolhido = int(input('Escolha um ano para escolher: '))
# Solicita ao usuário o nome do primeiro time para comparação
time_escolhido = input('Escolha um time para comparar: ')
# Solicita ao usuário o nome do segundo time para comparação
time_escolhido2 = input('Escolha outro time para comparar: ')

# Calcular a média de público dos dois times escolhidos
# Filtra os jogos do primeiro time como mandante no ano escolhido e calcula a média de público
media_de_publico1 = df[(df['ano_campeonato'] == ano_escolhido) & (df['time_mandante'] == time_escolhido)]['publico'].mean()
# Filtra os jogos do segundo time como mandante no ano escolhido e calcula a média de público
media_de_publico2 = df[(df['ano_campeonato'] == ano_escolhido) & (df['time_mandante'] == time_escolhido2)]['publico'].mean()

# Exibir os resultados
# Exibe a média de público do primeiro time no ano escolhido com duas casas decimais
print(f'A média de público do {time_escolhido} em {ano_escolhido} foi de {media_de_publico1:.2f}')
# Exibe a média de público do segundo time no ano escolhido com duas casas decimais
print(f'A média de público do {time_escolhido2} em {ano_escolhido} foi de {media_de_publico2:.2f}')

# Plotar o gráfico de comparação das médias de público
# Lista com os nomes dos times
times = [time_escolhido, time_escolhido2]
# Lista com as médias de público calculadas
medias = [media_de_publico1, media_de_publico2]
# Define o tamanho da figura do gráfico
plt.figure(figsize=(8, 5))
# Cria um gráfico de barras com cores diferentes para cada time
plt.bar(times, medias, color=['black', 'green'])
# Adiciona um título ao gráfico
plt.title(f'Média de Público em {ano_escolhido}')
# Adiciona rótulo ao eixo X (nomes dos times)
plt.xlabel('Times')
# Adiciona rótulo ao eixo Y (valores das médias de público)
plt.ylabel('Média de Público')
# Define o limite superior do eixo Y como o valor máximo das médias + 10 para melhor visualização
plt.ylim(0, max(medias) + 10)
# Exibe o gráfico
plt.show()
