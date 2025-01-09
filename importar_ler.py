import pandas as pd

#Formatos permitidos no pandas (csv, excel, sql, json, parquet, …)

#read_* - Ler dados para o pandas
Clientes = pd.read_excel('Tabela.xlsx') #Ler dados de uma tabela (Formato excel)

#print(Clientes.head(10)), Exibi as primeiras 10 linhas da planilha
#print(Clientes.tail(10)), Exibi as ultimas 10 linhas da planilha

print(Clientes.dtypes) #Exibe o tipo dos dados que foram interpretados

#inteiros ( int64)
#flutuantes ( float64)
#strings ( object)

#to_* - Armazena os dados em formato de planilha
Clientes.to_excel('Tabela.xlsx', sheet_name='Clientes', index=False)
#Ler a planilha que foi criada e colocar os dados no DataFrame novamente
Clientes = pd.read_excel("Tabela.xlsx", sheet_name="Clientes")

#info() - Verificar informaçãos sobre o DataFrame
print(Clientes.info())
print(Clientes)
