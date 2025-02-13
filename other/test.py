import pandas as pd

df = pd.read_csv('Categorias.csv',  sep=';', encoding='ISO-8859-1')
df.to_excel('Categorias_Ordenadas.xlsx')