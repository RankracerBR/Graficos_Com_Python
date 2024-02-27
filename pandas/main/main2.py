import pandas as pd
import matplotlib.pyplot as plt

nome_do_arquivo = '../tabelas/frota_veiculos_Brasil.csv'
dados = pd.read_csv(nome_do_arquivo, delimiter=';')

automovel = dados[dados['Indicador'] == 'Veículo']

anos = automovel.columns[2:-1] # Pegando a coluna automóvel e removendo a última coluna 'Unidades'
valores = automovel.iloc[0, 2:-1].astype(float) # Verificando se o tipo é float

plt.figure(figsize=(10, 6))
plt.plot(anos, valores, marker='o', linestyle='-')
plt.title('Evolução do número de "Automóveis" ao longo dos anos')
plt.xlabel('Ano')
plt.ylabel('Quantidade de Veículos')
plt.grid(True)
plt.show()