import pandas as pd

file_path = 'C:/ExamenBDA/archive/US_Accidents_March23.csv'
df = pd.read_csv(file_path)
print(df.columns)
# Resto de tu código...
df.sample(5)