import numpy as np
import matplotlib.pyplot as plt

# Sistema internacional de unidades
R = 8.314          # Constante dos gases
E = 49000          # Energia de ativação
A = 8e7            # Fator Pre-expoencial
Cain = 10          # Concentração de entrada de A
Cbin = 0           # Concentração de entrada de B
Car= 6.965         # Concentração de reciclo de A
Cbr= 3.035         # Concentração de reciclo de B
V= 60.82           # Volume do reator

# Declarando e limpando vetores
aa = []
xp = []
yp = []
zp = []
xp3 = []
yp3 = []
zp3 = []
xp1 = []
yp1 = []
zp1 = []
xp4 = []
yp4 = []
zp4 = []
Cp = []
Cp4 = []
Cpb = []
Ccc = []
CccV = []
cp3 = []
Cpl4 = []

aa.clear()
xp.clear()
yp.clear()
zp.clear()
xp1.clear()
yp1.clear()
zp1.clear()
xp4.clear()
yp4.clear()
zp4.clear()
Cp.clear()
Cpb.clear()
Ccc.clear()
CccV.clear()
xp3.clear()
yp3.clear()
zp3.clear()
cp3.clear()
Cp4.clear()
Cpl4.clear()

# Numero de pontos nos intervalos
Nx = 50
Ny = 50
Nz = 50

# Intervalos para temperatura, Vazao de alimentação e Vazao de reciclo
T = np.linspace(301.5, 303, Nx)
Fin = np.linspace(8, 10, Ny)
Rcl =  np.linspace(5, 6, Nz)

# Formando as malhas
Txx, F0yy = np.meshgrid(T, Fin)
Tx, F0y, Rclz = np.meshgrid(T, Fin, Rcl)

# Preenchendo vetores
Cv = np.zeros((Nx, Ny, Nz) )  
CbCc = np.zeros((Nx, Ny, Nz) )       

for i in range(Nx):
    for j in range(Ny):
        for k in range(Nz): 
             # Declarar função Custo neste formato aqui
             Cv[i][j][k] =  ( 3*Txx[i][j] ) + np.exp(F0yy[i][j]/2.75) + np.exp((Rcl[k])/1.3  )                                  
#            if Cv[i][j][k] <= 1601 and Cv[i][j][k] >= 1599:
#               xp.append(Txx[i][j])
#               yp.append(F0yy[i][j])
#               zp.append(Rcl[k])
#               Cp.append(Cv[i][j][k])
 
for i in range(Nx):
    for j in range(Ny):
        for k in range(Nz): 
              # Declarar função para calculo da Concentração do produto aqui
              CbCc[i][j][k] = (((Rcl[k]*Cbr)+(F0yy[i][j]*Cbin))+(V*(A*np.exp(-E/(R*Txx[i][j])))*(((Rcl[k]*Car)+(F0yy[i][j]*Cain))/(Rcl[k]+F0yy[i][j]+(V*(A*np.exp(-E/(R*Txx[i][j]))))))))/(Rcl[k]+F0yy[i][j])
              # Intervalo da Concentração demandada
              if CbCc[i][j][k] <= 5.840 and CbCc[i][j][k] >= 5.82:
                xp1.append(Txx[i][j])
                yp1.append(F0yy[i][j])
                zp1.append(Rcl[k])
                Cpb.append(CbCc[i][j][k])

# Declarar função para calculo da Concentração do produto aqui, neste outro formato                
Cb = (((Rclz*Cbr)+(F0y*Cbin))+(V*(A*np.exp(-E/(R*Tx)))*(((Rclz*Car)+(F0y*Cain))/(Rclz+F0y+(V*(A*np.exp(-E/(R*Tx))))))))/(Rclz+F0y) 

# Declarar função Custo neste formato aqui, neste outro formato
Cc = 3*Tx + np.exp(F0y/2.75) + np.exp((Rclz)/1.3 )

# Vetorizando para servir de mapa de cores
CbV = np.array(Cb)
CcV = np.array(Cc)

# Plotando Concentração do produto no cenario V - F0 - Rcl
#fig1 = plt.figure()
#ax1 = plt.axes(projection='3d')
#cmap = plt.get_cmap('jet') 
#graf1 = ax1.scatter(Tx, F0y, Rclz, s = 5, alpha = 0.025, c = CbV.flat, cmap=cmap)
#plt.colorbar(graf1, shrink=0.5)
#ax1.set_xlabel('Temperatura')
#ax1.set_ylabel('Vazao')
#ax1.set_zlabel('Reciclo')
#ax1.set_title('Colorbar: Cb')

# Plotando Função Custo no cenario V - F0 - Rcl
#fig2 = plt.figure()
#ax2 = plt.axes(projection='3d')
#cmap = plt.get_cmap('jet') 
#graf2 = ax2.scatter(Tx, F0y, Rclz, s = 5, alpha = 0.025, c = CcV.flat, cmap=cmap)
#plt.colorbar(graf2, shrink=0.5)
#ax2.set_xlabel('Temperatura')
#ax2.set_ylabel('Vazao')
#ax2.set_zlabel('Reciclo')
#ax2.set_title('Colorbar: Custo')

## Plotando Concentração demandada no Cenário  Concentração - V - F0 - Rcl
#ax2.scatter(xp1, yp1, zp1, s = 1, alpha = 1, color = 'blue')
#ax2.set_xlabel('Temperatura')
#ax2.set_ylabel('Vazao')
#ax2.set_zlabel('Reciclo') 

# Plotando Concentração demandada no Cenário  Custo - V - F0 - Rcl
#ax1.scatter(xp1, yp1, zp1, s = 1, alpha = 1, color = 'blue')
#ax1.set_xlabel('Temperatura')
#ax1.set_ylabel('Vazao')
#ax1.set_zlabel('Reciclo')

# Plotando a Superficie de Concentração demandada com as cores do Custo
#fig3 = plt.figure()
#ax3 = plt.axes(projection='3d')
#cmap = plt.get_cmap('jet') 
#for i in range(0, len(xp1)): 
#        Ccc=  ( 5*xp1[i] ) + np.exp(10*yp1[i]) + 10*np.exp(1.5*(zp1[i])  )                
#        xp3.append(xp1[i])
#        yp3.append(yp1[i])
#        zp3.append(zp1[i])
#        cp3.append(Ccc)
#            
#CccV = np.array(cp3)            
#graf3 = ax3.scatter(xp3, yp3, zp3, s = 10, alpha = 1, c = CccV.flat, cmap=cmap)
#ax3.set_xlabel('Temperatura')
#ax3.set_ylabel('Vazao')
#ax3.set_zlabel('Reciclo') 
#ax3.set_title('Colorbar: Custo')  
#plt.colorbar(graf3, shrink=0.5)      
#
## Limpando vetores para reutiliza-los
#xp3.clear()
#yp3.clear()
#zp3.clear()

# Plotando a Superficie de Concentração demandada com as cores do Custo, com restrição de custo
fig4 = plt.figure()
ax4 = plt.axes(projection='3d')
cmap = plt.get_cmap('jet') 
for i in range(0, len(xp1)): 
        Ccc=  ( 3*xp1[i] ) + np.exp((yp1[i])/2.75) + np.exp((zp1[i])/1.3  ) 
        if Ccc <= 3600: #and Ccc >= 1599:  
            # Estados que obedecem a concentração demandada e a restrição de custo
            xp3.append(xp1[i])
            yp3.append(yp1[i])
            zp3.append(zp1[i])            
            Cp4.append(Ccc)
            
CccV = np.array(Cp4)            
graf4 = ax4.scatter(xp3, yp3, zp3, s = 10, alpha = 1, c = CccV.flat, cmap=cmap)
ax4.set_xlabel('Temperatura')
ax4.set_ylabel('Vazao')
ax4.set_zlabel('Reciclo') 
ax4.set_title('Colorbar: Custo')  
plt.colorbar(graf4, shrink=0.5)    

iva=100
ivb=2000

# Plotando Função Custo no cenario V - F0 - Rcl
ax4.scatter(xp3[iva], yp3[iva], zp3[iva], s = 100, alpha = 1, color = 'blue')
ax4.scatter(xp3[ivb], yp3[ivb], zp3[ivb], s = 100, alpha = 1, color = 'blue')


# ---------------------- Ajustando e plotando a superficie de ajuste
import numpy as np
from scipy.optimize import curve_fit
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
    #z = a + b*x + c*y + d*x**2 + e*y**2 + f*x*y + g*x**3 + h*y**3 + ab*x**4 + bb*y**4 + cb*x**5 + db*y**5 + eb*x**6 + fb*y**6  + ib*(x*y)**jb + lb*y**mb + nb*y**pb + qb*x**y + rb*y**x  # <--- Equação de ajuste
    z = a + b*x + c*y + d*x**2 + e*y**2 + f*x*y + g*x**3 + h*y**3 + ab*x**4 + bb*y**4 + cb*x**5 + db*y**5 + eb*x**6 + fb*y**6  # + ib*(x*y)**jb + lb*y**mb + nb*y**pb + qb*x**y + rb*y**x  # <--- Equação de ajuste
    return z 

# Pontos para ajustar por uma superfície
for i in range(len(xp3)):
    Pontos.append([xp3[i], yp3[i], zp3[i]])

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

# Plotando a figura
ax4.plot_surface(X, Y, Z, alpha=0.5)
plt.show()
    
# Imprimindo os parametros de ajuste - Substituir na equação da superficie para obter a equação da superficie ajustada
print('\n Parametros da superficie \n')
print ('a = ', parameters[0])
print ('b = ', parameters[1])
print ('c = ', parameters[2])
print ('d = ', parameters[3])
print ('e = ', parameters[4])
print ('f = ', parameters[5])
print ('g = ', parameters[6])
print ('h = ', parameters[7])
print ('ab = ', parameters[8])
print ('bb = ', parameters[9])
print ('cb = ', parameters[10])
print ('db = ', parameters[11])
print ('eb = ', parameters[12])
print ('fb = ', parameters[13])
print ('gb = ', parameters[14])
print ('hb = ', parameters[15])
print ('ib = ', parameters[16])
print ('jb = ', parameters[17])
print ('kb = ', parameters[18])
print ('lb = ', parameters[19])
print ('mb = ', parameters[20])
print ('nb = ', parameters[21])
print ('pb = ', parameters[22])
print ('qb = ', parameters[23])
print ('rb = ', parameters[24])

# Atribuindo os valores
a =  parameters[0]
b =  parameters[1]
c =  parameters[2]
d =  parameters[3]
e =  parameters[4]
f =  parameters[5]
g =  parameters[6]
h =  parameters[7]
ab =  parameters[8]
bb =  parameters[9]
cb =  parameters[10]
db =  parameters[11]
eb =  parameters[12]
fb =  parameters[13]
gb =  parameters[14]
hb =  parameters[15]
ib =  parameters[16]
jb =  parameters[17]
kb =  parameters[18]
lb =  parameters[19]
mb =  parameters[20]
nb =  parameters[21]
pb =  parameters[22]
qb =  parameters[23]
rb =  parameters[24]

x = xp3[iva]
while x <= xp3[ivb]:
    y = yp3[iva] + ((yp3[ivb]-yp3[iva])/(xp3[ivb]-xp3[iva])) * (x-xp3[iva])
    # Abaixo a mesma função que ajustou o plano
    z = a + b*x + c*y + d*x**2 + e*y**2 + f*x*y + g*x**3 + h*y**3 + ab*x**4 + bb*y**4 + cb*x**5 + db*y**5 + eb*x**6 + fb*y**6
    # Declarar Função Custo neste formato
    Ccc2 =  ( 3*x ) + np.exp(y/2.75) + np.exp((z)/1.3) 
    # Pontos da Curva de Operação
    xp4.append(x)
    yp4.append(y)
    zp4.append(z)
    Cpl4.append(Ccc2)
    x = x + 0.01

# Plotando a Curva de Operação junto com o ajuste da Superficie - para aferir o ajuste e a curva
ax4.scatter(xp4, yp4, zp4, s = 30, alpha = 1, color = 'm')
Cpl4V = np.array(Cpl4)

# Plotando a Curva de Operação entre os estados de mesma conversao e restrição de Custo
fig5 = plt.figure()
ax5 = plt.axes(projection='3d')
cmap = plt.get_cmap('jet') 
graf5 = ax5.scatter(xp4, yp4, zp4, s = 10, alpha = 1, c = Cpl4V.flat, cmap=cmap)
plt.colorbar(graf5, shrink=0.5)
ax5.set_xlabel('Temperatura')
ax5.set_ylabel('Vazao')
ax5.set_zlabel('Reciclo')
ax5.set_title('Colorbar: Custo')

# Pontos da Curva de Operação
for i in range(len(xp4)): 
    aa.append([ xp4[i], yp4[i], zp4[i] ])