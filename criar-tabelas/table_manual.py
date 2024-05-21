# pip install prettytable
from prettytable import PrettyTable

# especificando as colunas
myTable = PrettyTable(["Nome", "Idade", "Sexo"])

# adicionando as linhas
myTable.add_row(["Marcus", "19", "Masculino"])
myTable.add_row(["Agatha", "18", "Feminino"])
myTable.add_row(["Alana", "15", "Feminino"])
myTable.add_row(["Carlos", "27", "Masculino"])

# mostrando a tabela
print(myTable)
