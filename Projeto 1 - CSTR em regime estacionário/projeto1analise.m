% Limpando vetores

 clear   tempoV;
 clear   CaV;
 clear    TV;
 clear    VV;
 clear    FV;
 clear    TjV;
 clear    FjV;
 clear    CbV;
 clear    Xb;

%Condições iniciais de operaï¿½ï¿½o
%299.5, 9.5, 60.15

% Alimentação (entrada)
F0=9.93;            % ft³/h
T0=250;            % °R
Ca0=10;            % lb mol/ft³
Cb0=0;             % lb mol/ft³
Fj=2.812074;       % ft³/h
Tj0=250;           % °R

% Saída
F=9.5;                    % ft³/h
T=299.5;                   % °R
Ca=3.9172;                 % lb mol/ft³
Cb=6.0828;                 % lb mol/ft³
Tj=294.4871;               % °R

% Dimensões
V=60.15;       % ft³
vj=4.28;      % ft³
A=102.4;      % ft²

% Conversão, com Xb entre 0.59 e 0.61
Xa=Ca/(Ca+Cb)
Xb=Cb/(Ca+Cb)

% Coeficiente global de troca térmica
U=850.5;      % BTU/(h ft² °R)

% Propriedades do Fluido reativo
cp=3.135;    % BTU/(lb °R)
ro=800;      % lb/ft³

% Propriedades do Fluido refrigerante (da jaqueta)
cpj=4186;      % BTU/(lb.°R)
roj=1;   % lb/ft³

% Condições de operação (set points)
Tset=299.5;         % °R
Vset=60.15;         % ft³

% Vazões para quando o erro (variável no setpoint - variável) for zero
Fjerrozero = 2.812074;         % ft³/h
Ferrozero = 9.93;         % ft³/h

% Calor de reação
deltaH=-30000;          %BTU/lb.mol de A

% Constantes de Arrhenius
Aa=8e7;    % fator pre-exponencial  1/h
Ea=49000;      % energia de ativaï¿½ï¿½o    BTU/lb.mol
Ra=8.314;       % constante dos gases    BTU/(lb.mol °R)

% Constante do controlador do fluido refrigerante
Kj=-5;
Tdj=0.2;
Tij=0.5;

% Constantes do controlador da vazão de saída
Kf=-5;
Tdf=0.1;
Tif=0.1;

% Passo de tempo das equacões diferenciais
dt=0.005;   % h

% Passo de impressão da tabela
pi=0.2;

% Tempo de simulação
tf=10;       % h

% Calculado os produtos V*Ca, V*Cb e V*T
VCa=V*Ca;
VCb=V*Cb;
VT=V*T;

% Valores iniciais dos controladores
intPID=0;
erro1V=0;
erro2V=erro1V;

intPIDj=0;
erro1Vj=0;
erro2Vj=erro1Vj;

% Distúrbio
  %T0=545;     % ft³/h

 % Início do loop
 i=1;
 tempo=0;
 while (tempo<=tf)

   % Controlador PID na Vazão de Refrigerante
   %----------------------------------------------------------
   % A integral do PID no volume
      intPIDj= intPIDj + (Tset-T)*dt;
   % A derivada do PID no volume
      derPIDj = (erro2Vj-erro1Vj)/dt;
      erro1Vj = erro2Vj;
   % A parte proporcional do PID no volume
      proPIDj = (Tset-T);
   % A equação do PID no volume
      Fj = Fjerrozero + Kj*proPIDj + Kj*Tdj*derPIDj + (Kj/Tij)*intPIDj;
    %----------------------------------------------------------

    % Controlador PID no Volume
    %----------------------------------------------------------
    % A integral do PID no volume
      intPID = intPID + (Vset-V)*dt;
    % A derivada do PID no volume
      derPID = (erro2V-erro1V)/dt;
      erro1V = erro2V;
    % A parte proporcional do PID no volume
      proPID = (Vset-V);
    % A equação do PID no volume
      F = Ferrozero + Kf*proPID + Kf*Tdf*derPID + (Kf/Tif)*intPID;
    %----------------------------------------------------------

    % k da reação
    k=(Aa)*exp(-Ea/(Ra*T));

    % O calor trocado com a camisa
    Q=U*A*(T-Tj);

    % Calculando as derivadas

    dVdt=F0-F;
    dVCadt=F0*Ca0-F*Ca-V*k*Ca;
    dVCbdt=F0*Cb0-F*Cb+V*k*Ca;
    dVTdt= F0*T0-F*T-deltaH*V*k*Ca/(cp*ro)-Q/(cp*ro);
    dTjdt=Fj*(Tj0-Tj)/vj + Q/(cpj*roj*vj);

    % Calculando as variáveis
    V=V+dVdt*dt;
    VCa=VCa+dVCadt*dt;
    VCb=VCb+dVCbdt*dt;
    VT=VT+dVTdt*dt;
    Tj=Tj+dTjdt*dt;
    Ca=VCa/V;
    Cb=VCb/V;
    T=VT/V;

    erro2V = Vset-V;
    erro2Vj = Tset-T;

    tempoV(i)=tempo;
    CaV(i)=Ca;
    TV(i)=T;
    VV(i)=V;
    FV(i)=F;
    TjV(i)=Tj;
    FjV(i)=Fj;
    CbV(i)=Cb;
    i=i+1;

    tempo = tempo + dt;
 end

 % Plotando os gráficos
      subplot(3,3,1); plot(tempoV,CaV,'.');xlabel('tempo');ylabel('Ca');                hold on;
      subplot(3,3,2); plot(tempoV,TV,'.'); xlabel('tempo');ylabel('Temperatura');       hold on;
      subplot(3,3,3); plot(tempoV,VV,'.'); xlabel('tempo');ylabel('Volume');            hold on;
      subplot(3,3,4); plot(tempoV,FV,'.'); xlabel('tempo');ylabel('Vazão');             hold on;
      subplot(3,3,5); plot(tempoV,TjV,'.');xlabel('tempo');ylabel('Temp. Refigerante'); hold on;
      subplot(3,3,6); plot(tempoV,FjV,'.');xlabel('tempo');ylabel('Vazão Refrigerante');hold on;
      subplot(3,3,7); plot(tempoV,CbV,'.');xlabel('tempo');ylabel('Cb');                hold on;
