# Correlação
O código coleta dados históricos de preços de ativos financeiros e commodities usando a API yfinance. Fazendo a escolha um número de dias e, em seguida, coleta, trata e salva os dados em um arquivo Excel.
Coletando Dados via yfinance.download para obter os preços de fechamento dos ativos e commodities.
Trata Valores Nulos substituindo valores nulos e zeros com o valor mais próximo ou 0.
Calcula a variação percentual entre o primeiro e o último preço dos ativos e commodities e suas correlações.
Interface Gráfica: Exibe uma interface simples com tkinter para o usuário inserir o número de dias e obter os dados.
O arquivo Excel gerado tem duas abas: uma com os dados de preços e outra com as variações calculadas.
