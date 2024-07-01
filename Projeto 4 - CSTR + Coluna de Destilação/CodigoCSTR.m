clear
% Limpando vetores

 clear   tempoV;
 clear   CaV;
 clear    TV;
 clear    VV;
 clear    FV;
 clear    TjV;
 clear    FjV;
 clear    CbV;

%Condições iniciais de operação

% Alimentação (entrada)
Fr=5;
Car=10-3.035;
Cbr=3.035;

Fin=9.5;           % ft³/h
Cain=10;           % lb.mol/ft³
Cbin=0;            % lb.mol/ft³

T0=265;     % °R
Tj0=250;    % °R

F0=Fr+Fin;
Ca0=(((Fr*Car)+(Fin*Cain))/F0);
Cb0=(((Fr*Cbr)+(Fin*Cbin))/F0);

% Saida
F=14.5;                % ft³/h
T=301.50;                 % °R
Ca=4.2900;                % lb.mol/ft³
Cb=5.7100;               % lb.mol/ft³
Fj=3.8960;                % ft²/h
Tj=293.00;                % °R

% Dimensões
V=60.82;       % ft³
vj=4.28;      % ft³ A=250;
A=102.4;      % ft²

% Coeficiente global de troca térmica
U=805.5;      % BTU/(h.ft².°R)

% Propriedades do Fluido reativo
cp=3.135;    % BTU/(lb.°R)
ro=800;      % lb/ft³

% Propriedades do Fluido refrigerante (da jaqueta)
cpj=4186;      % BTU/(lb.°R)
roj=1;   % lb/ft³

% Condicoes de operação (set points)
Tset=301.5;         % lb.°R
Vset=60.82;        % ft³

% Vazões para quando o erro (variável no setpoint - variável) for zero
Fjerrozero = 2.812074;    % ft³/h
Ferrozero = 9.93;         % ft³/h

% Calor de reação
deltaH=-30000;          %BTU/lb mol de A

% Constantes de Arrhenius
Aa=8e7; % fator pre-exponencial  1/h
Ea=49000;   % energia de ativaï¿½ï¿½o    BTU/lb.mol
Ra=8.314;    % constante dos gases    BTU/(lb mol.°R)

% Constante do controlador do fluido refrigerante
Kj=-5;
Tdj=0.2;
Tij=0.5;

% Constantes do controlador da vazão de saida
Kf=-5;
Tdf=0.1;
Tif=0.1;

% Passo de tempo das equações diferenciais
dt=0.005;      % h

% Passo de impressão da tabela
pi=0.2;

% Tempo de simulação
tf=40;         % h

% Calculando os produtos V*Ca, V*Cb e V*T
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
   %F0=45;     % ft³/h

 % Inicio do loop
 i=1;
 tempo=0;
 while (tempo<=tf)

    % Imprimindo os resultados
    %if abs( eval(sym(tempo)/pi) - ceil(eval(sym(tempo)/pi)) ) <= 1e-3
    %   fprintf(' Tempo=%0.3f   Ca=%0.4f   Cb=%0.4f   Cc=%0.4f   Cd=%0.4f   T=%0.3f   V=%0.3f   F=%0.3f   Tj=%0.3f   Fj=%0.3f\n', tempo,Ca,Cb,Cc,Cd,T,V,F,Tj,Fj );
    %end

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
      subplot(3,3,4); plot(tempoV,FV,'.'); xlabel('tempo');ylabel('Vazï¿½o');             hold on;
      subplot(3,3,5); plot(tempoV,TjV,'.');xlabel('tempo');ylabel('Temp. Refigerante'); hold on;
      subplot(3,3,6); plot(tempoV,FjV,'.');xlabel('tempo');ylabel('Vazï¿½o Refrigerente');hold on;
      subplot(3,3,7); plot(tempoV,CbV,'.');xlabel('tempo');ylabel('Cb');                hold on;


