# Correlação
A funçãos deste código é medir a correlação da variação/desvaloriação das empresas que negociam commodities em relação a sua respectiva commodities. 

O código coleta dados históricos de preços de ativos financeiros e commodities usando a API yfinance, fazendo a escolha de dias e, em seguida, coleta, trata e salva os dados em um arquivo Excel.

Coletando Dados via yfinance.download para obter os preços de fechamento dos ativos e commodities.

Tratando Valores Nulos substituindo valores nulos e zeros com o valor mais próximo ou 0.

Calculando a variação percentual entre o primeiro e o último preço dos ativos e commodities e suas correlações.

Ultiiza da biblioteca Tkinter como Interface Gráfica, uma interface simples para o usuário inserir o número de dias e obter os dados.

O arquivo Excel gerado tem duas abas: uma com os dados de preços e outra com as variações calculadas.
