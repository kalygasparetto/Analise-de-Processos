import numpy as np
import matplotlib.pyplot as plt

# Sistema internacional de unidades
R = 8.314           # Constante dos gases
E = 49000          # Energia de ativação
A = 8e7        # Fator Pre-expoencial
Cain = 10         # Concentração de entrada de A
Cbin = 0           # Concentração de entrada de B
Car= 6.965        # Concentração de reciclo de A
Cbr= 3.035        # Concentração de reciclo de B
V= 60.82         # Volume do reator


# Declarando e limpando vetores
xp = []
yp = []
zp = []
xp3 = []
yp3 = []
zp3 = []
xp1 = []
yp1 = []
zp1 = []
Cp = []
Cp4 = []
Cpb = []
Ccc = []
CccV = []
cp3 = []
xp.clear()
yp.clear()
zp.clear()
xp1.clear()
yp1.clear()
zp1.clear()
Cp.clear()
Cpb.clear()
Ccc.clear()
CccV.clear()
xp3.clear()
yp3.clear()
zp3.clear()
cp3.clear()
Cp4.clear()

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
              CbCc[i][j][k] = (((Rcl[k]*Cbr)+(F0yy[i][j]*Cbin))+(V*(A*np.exp(-E/(R*Txx[i][j])))*(((Rcl[k]*Car)+(F0yy[i][j]*Cain))/(Rcl[k]+F0yy[i][j]+(V*(A*np.exp(-E/(R*Txx[i][j]))))))))/(Rcl[k]+F0yy[i][j])      #(V*(A*np.exp(-E/(R*Txx[i][j]))*Ca0))/(((Rcl[k]*Cr+F0yy[i][j]*Cain)/Ca0)+(V*(A*np.exp(-E/(R*Txx[i][j]))))) 
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
fig1 = plt.figure()
ax1 = plt.axes(projection='3d')
cmap = plt.get_cmap('jet') 
graf1 = ax1.scatter(Tx, F0y, Rclz, s = 5, alpha = 0.025, c = CbV.flat, cmap=cmap)
plt.colorbar(graf1, shrink=0.5)
ax1.set_xlabel('Temperatura')
ax1.set_ylabel('Vazao')
ax1.set_zlabel('Reciclo')
ax1.set_title('Colorbar: Cb')

# Plotando Função Custo no cenario V - F0 - Rcl
fig2 = plt.figure()
ax2 = plt.axes(projection='3d')
cmap = plt.get_cmap('jet') 
graf2 = ax2.scatter(Tx, F0y, Rclz, s = 5, alpha = 0.025, c = CcV.flat, cmap=cmap)
plt.colorbar(graf2, shrink=0.5)
ax2.set_xlabel('Temperatura')
ax2.set_ylabel('Vazao')
ax2.set_zlabel('Reciclo')
ax2.set_title('Colorbar: Custo')

# Plotando Concentração demandada no Cenário  Concentração - V - F0 - Rcl
ax2.scatter(xp1, yp1, zp1, s = 1, alpha = 1, color = 'blue')
ax2.set_xlabel('Temperatura')
ax2.set_ylabel('Vazao')
ax2.set_zlabel('Reciclo') 

# Plotando Concentração demandada no Cenário  Custo - V - F0 - Rcl
ax1.scatter(xp1, yp1, zp1, s = 1, alpha = 1, color = 'blue')
ax1.set_xlabel('Temperatura')
ax1.set_ylabel('Vazao')
ax1.set_zlabel('Reciclo')

# Plotando a Superficie de Concentração demandada com as cores do Custo
fig3 = plt.figure()
ax3 = plt.axes(projection='3d')
cmap = plt.get_cmap('jet') 
for i in range(0, len(xp1)): 
        Ccc=  ( 3*xp1[i] ) + np.exp(yp1[i]/2.75) + np.exp((zp1[i])/1.3  )                
        xp3.append(xp1[i])
        yp3.append(yp1[i])
        zp3.append(zp1[i])
        cp3.append(Ccc)
            
CccV = np.array(cp3)            
graf3 = ax3.scatter(xp3, yp3, zp3, s = 10, alpha = 1, c = CccV.flat, cmap=cmap)
ax3.set_xlabel('Temperatura')
ax3.set_ylabel('Vazao')
ax3.set_zlabel('Reciclo') 
ax3.set_title('Colorbar: Custo')  
plt.colorbar(graf3, shrink=0.5)      

# Limpando vetores para reutiliza-los
xp3.clear()
yp3.clear()
zp3.clear()

# Plotando a Superficie de Concentração demandada com as cores do Custo, com restrição de custo
fig4 = plt.figure()
ax4 = plt.axes(projection='3d')
cmap = plt.get_cmap('jet') 
for i in range(0, len(xp1)): 
        Ccc=  ( 3*xp1[i] ) + np.exp(yp1[i]/2.75) + np.exp((zp1[i])/1.3  ) 
        if Ccc <= 3600 :# and Ccc >= 1599:  
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