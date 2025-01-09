import pandas as pd

#.notna() - Se sua tabela tiver valores null é bom usar esse comando para puxar as linhas que tenham somente valores definidos
#isin() - Filtro para buscar somente valores conhecidos

# Ler a tabela de clientes
Clientes = pd.read_excel('Tabela.xlsx')

#Extrair somente a coluna de CPF e IDADE, tem que colocar mais colchetes quando for mais de uma coluna
print("Somente as colunas de CPF e IDADE: ")
Pessoa_Fisica = Clientes[['CPF', 'IDADE']]
print(Pessoa_Fisica)
print()

# Aqui ele exibe o ID do cliente e com uma coluna de True e False
Acima_de_25_True = Clientes['IDADE'] > 25 #Filtro de idade
print(Acima_de_25_True)
print()

# Extraindo somente pessoas com idades maiores que 25 anos
print("Pessoas com mais de 25 anos: ")
Acima_de_25 = Clientes[Clientes['IDADE'] > 25] #Filtro de idade
print(Acima_de_25)
print("Quantidade de linhas e colunas: ", Acima_de_25.shape)

#Codigo para filtrar somente as idades especificas
print()
print("Aprovados: ")
aprovados = Clientes[Clientes['IDADE'].isin([55,45,53,52])]
print(aprovados)

