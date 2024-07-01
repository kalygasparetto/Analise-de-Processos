import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt

# Este modo de ler .csv pula a primeira linha. Preenche-la com zeros.
dadosDir ='C:/Users/kalya/OneDrive/Documentos/UTFPR/8º período - 2024.1/Análise de Processos'   #  <--- Colocar aqui o diretorio onde esta o arquivo .csv
nomeArquivo ='DadosColunm.csv'     # <----Colocar aqui o nome do arquivo csv
caminhoDados = os.path.join(dadosDir,nomeArquivo)
EsteAqui = pd.read_csv(caminhoDados)
dVet = np.array(EsteAqui)

cm = plt.cm.get_cmap('jet')
fig = plt.figure(figsize=(10, 10))
ax = plt.axes(projection='3d')
graph1 = ax.scatter3D(dVet[0,:], dVet[1,:], dVet[2,:], s=50, alpha=1, c=dVet[3,:].flat, cmap=cm)

fig.colorbar(graph1,location = 'left')  
ax.set_xlabel('Reciclo L/D')
ax.set_ylabel('Volatilidade relativa f(T)')
ax.set_zlabel('Numero de pratos')

t= np.arange(0, 1, 0.001)

# Ponto de partida
x1 = 4
y1 = 2
z1 = 7

# Ponto de chegada
x2 = 2
y2 = 4
z2 = 7

# Trajetória 1
n = 2
k = 0.8
r = 1
plt.plot((x2 - x1) * t**n + x1, (y2 - y1) * t**k + y1, (z2 - z1) * t**r + z1, 'b')

# Trajetória 2
n = 1
k = 2
r = 0.8
plt.plot((x2 - x1) * t**n + x1, (y2 - y1) * t**k + y1, (z2 - z1) * t**r + z1, 'b')


# Trajetória 3
n = 0.8
k = 1
r = 2
plt.plot((x2 - x1) * np.power(t, n) + x1, (y2 - y1) * np.power(t, k) + y1, (z2 - z1) * np.power(t, r) + z1, 'b*')

# Trajetória 4
n = 0.7
k = 0.6
r = 0.8
plt.plot((x2 - x1) * np.power(t, n) + x1, (y2 - y1) * np.power(t, k) + y1, (z2 - z1) * np.power(t, r) + z1, 'b*')

plt.show()
