import math
import numpy as np
import matplotlib.pyplot as plt

# Declarando Vetores
xVe = []
yVe = []
zVe = []
xV = []
yV = []
zV = []
cV = []

# Limpando vetores
xVe.clear()
yVe.clear()
zVe.clear()
xV.clear()
yV.clear()
zV.clear()
cV.clear()

# Sistema internacional de unidades
R = 8.314  # Constante dos gases
E = 49000  # Energia de ativação
A = 8e7  # Fator Pre-expoencial
Ca0 = 11000  # Concentração de entrada m3

# Vazão de entrada
F0 = 8
while F0 <= 10:
        # Temperatura
        T = 293
        while T <= 323:
                # Volume
                V = 59 #m3
                while V <= 62:

                        # equações do CSTR. Reação A -> B
                        Ca = F0 * Ca0 / (F0 + V * A * math.exp(-E / (R * T)))
                        Cb = V * A * Ca0 * math.exp(-E / (R * T)) / (F0 + V * A * math.exp(-E / (R * T)))
                        Xb = Cb / (Ca + Cb)

                        xV.append(T)
                        yV.append(F0)
                        zV.append(V)
                        cV.append(Xb)

                        # Intervalo da Composição escolhida
                        if 0.59 <= Xb <= 0.62:
                                xVe.append(T)
                                yVe.append(F0)
                                zVe.append(V)

                        V = V + 0.05
                T = T + 0.5
        F0 = F0 + 0.01

# Plotando
cVa = np.array(cV)
cmap = plt.get_cmap('jet')

fig1 = plt.figure(1)
ax1 = plt.axes(projection='3d')
graph1 = ax1.scatter(xV, yV, zV, alpha=0.02, s=10, c=cVa.flat, cmap=cmap)
graph2 = ax1.scatter(xVe, yVe, zVe, alpha=1, s=1, color='m')
plt.colorbar(graph1, orientation="horizontal", shrink=0.5)

ax1.set_title('Cor: Fração molar Produto')
ax1.set_xlabel('Temperatura')
ax1.set_ylabel('Vazao de entrada')
ax1.set_zlabel('Volume')
#plt.show()

# Plano da composição escolhida
from scipy.optimize import curve_fit
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

# Declarando os vetores
x_data = []
y_data = []
z_data = []
Pontos = []

# Limpando os vetores
x_data.clear()
y_data.clear()
z_data.clear()
Pontos.clear()


# Declarando o formato da superficie que ajustará os pontos
def funcdata(data, a, b, c, d, e, f, g, h, ab, bb, cb, db, eb, fb, gb, hb, ib, jb, kb, lb, mb, nb, pb, qb, rb):
        x = data[0]
        y = data[1]
        z = a + b * x + c * y + d * x * 2 + e * y * 2 + f * x * y + g * x * 3 + h * y * 3 + ab * x * 4 + bb * y * 4 + cb * x * 5 + db * y * 5 + eb * x * 6 + fb * y * 6  # + ib*(x*y)*jb + lb*ymb + nb*ypb + qb*xy + rb*y*x  # <--- Equação de ajuste
        return z


# Pontos para ajustar por uma superfície

for i in range(len(xVe)):
        Pontos.append([xVe[i], yVe[i], zVe[i]])

# Preenchendo os vetores de dados
for i in range(len(Pontos)):
        x_data.append(Pontos[i][0])
        y_data.append(Pontos[i][1])
        z_data.append(Pontos[i][2])

# Ajustando a curva
parameters, covariance = curve_fit(funcdata, [x_data, y_data], z_data)

# Calculando os pontos no chão - plano xy
model_x_data = np.linspace(min(x_data), max(x_data), 30)
model_y_data = np.linspace(min(y_data), max(y_data), 30)

# Criando a malha no chão
X, Y = np.meshgrid(model_x_data, model_y_data)

# Calculando a altura dos pontos para cada ponto da malha no chão criada acima
Z = funcdata(np.array([X, Y]), *parameters)

# Setando a figura
fig2 = plt.figure(2)
ax2 = plt.axes(projection='3d')
# Plotando a figura
ax2.plot_surface(X, Y, Z, alpha=0.5)
ax2.scatter(xVe, yVe, zVe, alpha=1, s=1, color='red')
# Nomeando os eixos
ax2.set_title('Curva dentro do Plano de Operação')
ax2.set_xlabel('Temperatura')
ax2.set_ylabel('Vazao de entrada')
ax2.set_zlabel('Volume')
#plt.show()

# Imprimindo os parametros de ajuste - Substituir na equação da superficie para obter a equação da superficie ajustada
print('\n Parametros da superficie \n')
print('a = ', parameters[0])
print('b = ', parameters[1])
print('c = ', parameters[2])
print('d = ', parameters[3])
print('e = ', parameters[4])
print('f = ', parameters[5])
print('g = ', parameters[6])
print('h = ', parameters[7])
print('ab = ', parameters[8])
print('bb = ', parameters[9])
print('cb = ', parameters[10])
print('db = ', parameters[11])
print('eb = ', parameters[12])
print('fb = ', parameters[13])
print('gb = ', parameters[14])
print('hb = ', parameters[15])
print('ib = ', parameters[16])
print('jb = ', parameters[17])
print('kb = ', parameters[18])
print('lb = ', parameters[19])
print('mb = ', parameters[20])
print('nb = ', parameters[21])
print('pb = ', parameters[22])
print('qb = ', parameters[23])
print('rb = ', parameters[24])

# Nomeando os parametros de ajuste
a = parameters[0]
b = parameters[1]
c = parameters[2]
d = parameters[3]
e = parameters[4]
f = parameters[5]
g = parameters[6]
h = parameters[7]
ab = parameters[8]
bb = parameters[9]
cb = parameters[10]
db = parameters[11]
eb = parameters[12]
fb = parameters[13]
gb = parameters[14]
hb = parameters[15]
ib = parameters[16]
jb = parameters[17]
kb = parameters[18]
lb = parameters[19]
mb = parameters[20]
nb = parameters[21]
pb = parameters[22]
qb = parameters[23]
rb = parameters[24]

# Caso a mudança seja em Temperatura e Vazão
# Ponto de partida
xe1 = 296
ye1 = 8
# Ponto de chegada
xe2 = 302
ye2 = 10

# Calculando o caminho (T,V,F0) dentro da composição escolhida
CmVx = []
CmVy = []
CmVz = []
CmVx.clear()
CmVy.clear()
CmVz.clear()
x = xe1
while x <= xe2:
        y = ye1 + ((ye2 - ye1) / (xe2 - xe1)) * (x - xe1)
        zxy = a + b * x + c * y + d * x * 2 + e * y * 2 + f * x * y + g * x * 3 + h * y * 3 + ab * x * 4 + bb * y * 4 + cb * x * 5 + db * y * 5 + eb * x * 6 + fb * y * 6  # + ib*(x*y)*jb + lb*ymb + nb*ypb + qb*xy + rb*y*x
        CmVx.append(x)
        CmVy.append(y)
        CmVz.append(zxy)
        x = x + 0.01

# Os Pontos do caminho
ax2.scatter(CmVx, CmVy, CmVz, alpha=1, s=1, color="m")
Caminho = []
Caminho.clear()
PontosOp = []
PontosOp.clear()
for i in range(len(CmVx)):
        Caminho.append([CmVx[i], CmVy[i], CmVz[i]])

for i in range(len(xVe)):
        PontosOp.append([round(xVe[i], 2), round(yVe[i], 2), round(zVe[i], 2)])

fig3 = plt.figure(3)
ax3 = plt.axes(projection='3d')
ax3.scatter(CmVx, CmVy, CmVz, alpha=1, s=1, color="m")
# Nomeando os eixos
ax3.set_title('Curva de Operação')
ax3.set_xlabel('Temperatura')
ax3.set_ylabel('Vazao de entrada')
ax3.set_zlabel('Volume')
plt.show()

# Para ver Pontos Operacionais (mesma conversão) conforme escolha de uma variavel (T,V ou F0)
F0Esc = 9.5 # Ver Pontos Operacionais para uma vazao de alimentacao F0 = 0.22
for i in range(len(PontosOp)):
        if (PontosOp[i][1] - F0Esc) ** 2 <= 1e-5:
                print(PontosOp[i])