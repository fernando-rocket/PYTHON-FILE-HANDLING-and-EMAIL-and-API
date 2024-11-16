print("\n")
import re

data_file = open("A1 - Extraindo dados csv/A1_Dados_csv - Folha1.csv")
data = data_file.readlines()
x = lambda tupla: tupla.split(",")
data = list(map(x, data))
print(data)
for item in data:
    last = item[-1]
    last = last.replace("\n", "")
    item.pop()
    item.append(last)

print(data)
data_file.close()

# Ou também podemos:

print("\n")
import csv

file_data = open("A1 - Extraindo dados csv/A1_Dados_csv - Folha1.csv")
file = csv.reader(file_data)
print(file)
for row in file:
    print(row)

file_data.close()

# Também podemos:


print("\n")
import pandas as pd

arquivo = pd.read_csv("A1 - Extraindo dados csv/A1_Dados_csv - Folha1.csv")
print(arquivo)

