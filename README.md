# Correlação
A funçãos deste código é medir a correlação da variação/desvaloriação de empresas das quais seus lucro é proveniente da venda de commodities, e a correlação em relação a empresa e suas respectivas commodities/indexador fazendo:

-Coleta dados históricos de preços de ativos financeiros e commodities usando a API yfinance, fazendo a escolha de dias e, em seguida, coleta, trata e salva os dados em um arquivo Excel.

-Coletando Dados via yfinance.download para obter os preços de fechamento dos ativos e commodities.

-Tratando valores nulos substituindo valores nulos e zeros com o valor mais próximo ou 0.

-Calculando a variação percentual entre o primeiro e o último preço dos ativos e commodities e suas correlações.

-Ultiza da biblioteca Tkinter como Interface Gráfica, uma interface simples para o usuário inserir o número de dias e obter os dados.

-O arquivo Excel gerado tem duas abas: uma com os dados de preços e outra com as variações calculadas.
