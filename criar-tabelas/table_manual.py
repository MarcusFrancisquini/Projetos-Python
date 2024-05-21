# pip install prettytable
from prettytable import PrettyTable

# colunas
myTable = PrettyTable(["Nome", "Idade", "Sexo"])

# linhas
myTable.add_row(["Marcus", "19", "Masculino"])
myTable.add_row(["Agatha", "18", "Feminino"])
myTable.add_row(["Alana", "15", "Feminino"])
myTable.add_row(["Carlos", "27", "Masculino"])

print(myTable)
