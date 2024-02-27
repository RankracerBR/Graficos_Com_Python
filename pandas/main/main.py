import pandas as pd
import matplotlib.pyplot as plt

nome_do_arquivo = '../tabelas/frota_veiculos_Brasil.csv'
dados = pd.read_csv(nome_do_arquivo, delimiter=';')
print(dados)

automovel = dados[dados['Indicador'] == 'Veículo']

anos = automovel.columns[2:-1] # Pegando a coluna automóvel, e excluindo a coluna Unidade
valores = automovel.iloc[0, 2:-1].astype(int) # Tratando os valores como inteiros

plt.figure(figsize=(10,6))
plt.plot(anos, valores, marker='o', linestyle='-')
plt.title('Evolução do indicador "Automóvel" ao longo dos anos')
plt.xlabel('Ano')
plt.ylabel('Quantidade de veículos (milhões)')
plt.grid(True)
plt.show()
