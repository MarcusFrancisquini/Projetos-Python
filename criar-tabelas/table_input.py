# pip install prettytable
from prettytable import PrettyTable

# colunas
myTable = PrettyTable(["Carro", "Cor", "Rebaixado"])

# linhas
linhas = int(input("Quantas linhas terá a tabela: "))

for _ in range(linhas):
    carro = str(input('Carro: '))
    cor = str(input('Cor: '))
    rebaixado = str(input('Rebaixado: '))
    myTable.add_row([carro, cor, rebaixado])

print(myTable)
