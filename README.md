# Análise de Desempenho no Campeonato Brasileiro Série A
Este projeto tem como objetivo realizar análises sobre o desempenho de times no Campeonato Brasileiro Série A, utilizando Python, Pandas e Matplotlib para manipulação de dados e criação de visualizações. O código permite extrair informações como desempenho em vitórias, empates e derrotas, média de público nos estádios e comparações entre diferentes times e anos.

Funcionalidades
1. Desempenho de um time em um ano específico
Filtra os dados de um time escolhido no ano selecionado pelo usuário.
Calcula:
Número de vitórias, empates e derrotas como mandante.
Cria um gráfico de pizza que visualiza a proporção de vitórias, empates e derrotas do time no ano analisado.
2. Média de público por time e ano
Permite comparar a média de público entre dois times no mesmo ano.
Calcula a média considerando apenas os jogos onde cada time foi mandante.
Exibe um gráfico de barras para comparar visualmente as médias de público entre os dois times escolhidos.
3. Aproveitamento como mandante e visitante
Analisa o desempenho de um time como mandante e visitante em um ano específico.
Calcula:
Número de vitórias, empates e derrotas em casa e fora.
Aproveitamento percentual em pontos (em casa e fora).
Exibe um gráfico de barras para visualizar o aproveitamento em diferentes contextos.
Estrutura do Código
Carregamento dos Dados

Os dados são carregados de um arquivo CSV (brasileirao_serie_a.csv) que contém informações como:
Ano do campeonato (ano_campeonato),
Times mandante e visitante,
Número de gols,
Público presente.
Os valores ausentes (nulos) são tratados, garantindo consistência para cálculos e análises.
Tratamento e Filtragem

Filtragem dos jogos baseada no ano escolhido pelo usuário.
Foco nos jogos de um time específico, seja como mandante ou visitante.
Cálculos Estatísticos

Cálculo de vitórias, empates, derrotas e médias de público.
Determinação de aproveitamento percentual em pontos possíveis.
Visualização dos Resultados

Gráficos intuitivos são criados usando Matplotlib:
Gráfico de Pizza: Visualiza proporções de resultados (vitórias, empates, derrotas).
Gráfico de Barras: Compara médias de público ou aproveitamentos.
Pré-requisitos
Antes de executar o projeto, certifique-se de que seu ambiente possui:

Python 3.x instalado.
As bibliotecas necessárias:
pandas
matplotlib
Você pode instalá-las com o seguinte comando:

bash
Copy code
pip install pandas matplotlib
Como Executar
Certifique-se de que o arquivo CSV (brasileirao_serie_a.csv) está no mesmo diretório do script.

Execute qualquer um dos scripts dependendo da análise desejada:

Desempenho de um time:
bash
Copy code
python desempenho_time.py
Comparação de média de público:
bash
Copy code
python media_publico.py
Aproveitamento mandante e visitante:
bash
Copy code
python aproveitamento.py
Siga as instruções interativas para inserir:

Ano do campeonato.
Nome do time (ou times) para análise.
Visualize os resultados no console e nos gráficos gerados.

Estrutura do Arquivo CSV
O arquivo brasileirao_serie_a.csv deve conter as seguintes colunas:

ano_campeonato: Ano em que a partida ocorreu.
time_mandante: Nome do time mandante.
time_visitante: Nome do time visitante.
gols_mandante: Gols marcados pelo time mandante.
gols_visitante: Gols marcados pelo time visitante.
publico: Número de espectadores presentes na partida.
Exemplos de Uso
Exemplo 1: Desempenho de um time
Usuário escolhe o ano 2023 e o time Flamengo.
O script calcula vitórias, empates e derrotas do Flamengo como mandante em 2023.
Um gráfico de pizza é exibido mostrando o desempenho do time.
Exemplo 2: Comparação de média de público
Usuário escolhe o ano 2022, Flamengo e Palmeiras.
O script calcula as médias de público de ambos os times como mandantes.
Um gráfico de barras é exibido comparando essas médias.
Exemplo 3: Aproveitamento em casa e fora
Usuário escolhe o ano 2021 e o time São Paulo.
O script calcula o aproveitamento do time em pontos como mandante e visitante.
Um gráfico de barras é exibido para visualizar o desempenho.
Possíveis Melhorias
Adicionar suporte para análise de desempenho como visitante.
Permitir comparações diretas entre dois times no mesmo ano, incluindo desempenho e resultados.
Implementar análises mais avançadas, como saldo de gols ou eficiência do ataque/defesa.
Contribuição
Sinta-se à vontade para contribuir com melhorias no código, seja adicionando novas funcionalidades ou corrigindo bugs. Para isso:

Faça um fork do repositório.
Crie uma branch para sua alteração:
bash
Copy code
git checkout -b minha-alteracao
Envie um pull request com suas alterações.
Licença
Este projeto é de livre uso para fins educacionais. Se utilizar este código como base, por favor, dê os créditos adequados.