import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados
df = pd.read_csv('brasileirao_serie_a.csv')

# Substituir valores nulos por zero
df = df.fillna(0)


df['ano_campeonato'] = df['ano_campeonato'].astype(int) #Nesse caso tivemos que realizar um tratamento de erro para evitar conflitos de tipos no csv
df['publico'] = pd.to_numeric(df['publico'], errors='coerce').fillna(0)


ano_escolhido = int(input('Escolha um ano para escolher: ')) #Solicitamos a entrada do usuario
time_escolhido = input('Escolha um time para comparar: ')
time_escolhido2 = input('Escolha outro time para comparar: ')


media_de_publico1 = df[(df['ano_campeonato'] == ano_escolhido) & (df['time_mandante'] == time_escolhido)]['publico'].mean() #Calculamos a media de público
media_de_publico2 = df[(df['ano_campeonato'] == ano_escolhido) & (df['time_mandante'] == time_escolhido2)]['publico'].mean() 



print(f'A média de público do {time_escolhido} em {ano_escolhido} foi de {media_de_publico1:.2f}') #Exibimos as medias
print(f'A média de público do {time_escolhido2} em {ano_escolhido} foi de {media_de_publico2:.2f}')


times = [time_escolhido, time_escolhido2] #plotamos o gráfico
medias = [media_de_publico1, media_de_publico2]
plt.figure(figsize=(8, 5))
plt.bar(times, medias, color=['black', 'green'])
plt.title(f'Média de Público em {ano_escolhido}')
plt.xlabel('Times')
plt.ylabel('Média de Público')
plt.ylim(0, max(medias) + 10)
plt.show()