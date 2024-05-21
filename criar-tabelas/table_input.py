# pip install prettytable
from prettytable import PrettyTable

# especificando as colunas
myTable = PrettyTable(["Carro", "Cor", "Rebaixado"])

# quantidade de linhas
linhas = int(input("Quantas linhas terá a tabela: "))

# adicionando as linhas
for _ in range(linhas):
    carro = str(input('Carro: '))
    cor = str(input('Cor: '))
    rebaixado = str(input('Rebaixado: '))
    myTable.add_row([carro, cor, rebaixado])

# mostrando a tabela
print(myTable)
