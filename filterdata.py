import pandas as pd

# Carica il file CSV
df = pd.read_csv('/Users/gianmarcoferrara/Desktop/us-counties-2020.csv')

# Converti la colonna 'data' in formato datetime
df['date'] = pd.to_datetime(df['date'])

# Scegli la data di riferimento
data_di_riferimento = '2023-03-19'  # Modifica questa data come necessario

# Filtra i dati per rimuovere record precedenti alla data di riferimento
df_filtrato = df[df['data'] >= data_di_riferimento]

# Salva il DataFrame filtrato in un nuovo file CSV (opzionale)
df_filtrato.to_csv('file_filtrato.csv', index=False)

print(df_filtrato)
