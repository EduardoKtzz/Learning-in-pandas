import pandas as pd
import matplotlib.pyplot as plt

Clientes = pd.read_excel('Tabela.xlsx', index_col=0, parse_dates=True)
print(Clientes)
Clientes['IDADE'].plot()
plt.show()