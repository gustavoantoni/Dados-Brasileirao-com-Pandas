# Análise de Desempenho no Campeonato Brasileiro Série A

Este projeto utiliza **Python**, **Pandas** e **Matplotlib** para realizar análises do Campeonato Brasileiro Série A. Ele permite explorar o desempenho dos times em diferentes contextos, analisar médias de público e visualizar resultados de forma intuitiva.

---

## Funcionalidades

### 1. **Desempenho de um time em um ano**
- Filtra dados de um time em um ano específico.
- Calcula:
  - Vitórias, empates e derrotas como mandante.
- Gera um gráfico de pizza mostrando a proporção dos resultados.

### 2. **Média de público por time e ano**
- Compara a média de público entre dois times no mesmo ano.
- Calcula a média de público considerando apenas os jogos como mandante.
- Exibe um gráfico de barras para comparação.

### 3. **Aproveitamento como mandante e visitante**
- Analisa o desempenho de um time em casa e fora.
- Calcula:
  - Vitórias, empates, derrotas e aproveitamento percentual.
- Gera um gráfico de barras para visualização.

---

## Estrutura do Projeto

### **Carregamento e Tratamento dos Dados**
- Dados extraídos de um arquivo `CSV` (`brasileirao_serie_a.csv`) contendo:
  - **Colunas**: `ano_campeonato`, `time_mandante`, `time_visitante`, `gols_mandante`, `gols_visitante`, `publico`.
- Tratamento de valores ausentes para garantir consistência.

### **Análises Realizadas**
- Filtragem por ano e time (mandante/visitante).
- Cálculo de estatísticas: vitórias, empates, derrotas, médias de público e aproveitamento percentual.

### **Visualização**
- **Gráficos de Pizza**: Proporção de vitórias, empates e derrotas.
- **Gráficos de Barras**: Comparação de médias de público e aproveitamento.

---

## Como Executar

1. **Pré-requisitos**:
   - Python 3.x instalado.
   - Instalar bibliotecas necessárias:
     ```bash
     pip install pandas matplotlib
     ```
2. **Executar scripts**:
   - Certifique-se de que o arquivo `brasileirao_serie_a.csv` está no mesmo diretório do script.
   - Execute o script desejado:
     - Desempenho de um time:
       ```bash
       python desempenho_time.py
       ```
     - Comparação de público:
       ```bash
       python media_publico.py
       ```
     - Aproveitamento:
       ```bash
       python aproveitamento.py
       ```
3. **Interação**:
   - Insira:
     - Ano do campeonato.
     - Nome do time (ou times) para análise.
   - Visualize os resultados e gráficos.

---

## Exemplos de Uso

### 1. **Desempenho de um time**
- Ano: 2023 | Time: Flamengo.
- Resultado: gráfico de pizza mostrando vitórias, empates e derrotas como mandante.

### 2. **Comparação de público**
- Ano: 2022 | Times: Flamengo e Palmeiras.
- Resultado: gráfico de barras comparando as médias de público.

### 3. **Aproveitamento em casa e fora**
- Ano: 2021 | Time: São Paulo.
- Resultado: gráfico de barras com o aproveitamento em casa e fora.

---

## Melhorias Futuras
- Suporte para análise de desempenho como visitante.
- Comparação direta entre dois times no mesmo ano.
- Adicionar análises mais detalhadas, como saldo de gols e eficiência defensiva.

---

## Contribuição

Contribuições são bem-vindas! Siga os passos:

1. Faça um fork do repositório.
2. Crie uma branch para sua alteração:
   ```bash
   git checkout -b minha-alteracao
   ```
3. Envie um pull request.

---

## Licença

Este projeto é de uso livre para fins educacionais. Caso utilize este código, dê os devidos créditos. 🚀 
