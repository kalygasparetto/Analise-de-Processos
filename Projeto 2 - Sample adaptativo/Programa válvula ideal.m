%Limpando vetores

clear tempoV;
clear TV;
clear TambV;
clear MrefV;
 
%Condicoes iniciais de operacao

%Fluido estocado: Propano
%Refrigerante:    134a

U    = 250;                       % W/m2C
A    = 2;                         % m2
Cp   = 2520;                      % J/kgC
ma   = 10;                        % kg
Mref = 0;                         % kg/s
Rmax = 0.1;                       %razao de velocidade da valvula
dt=0.001;                         % s
hv   = 247000;                    % J/kg
hl   = 50000;                     % J/kg
M    = 44;                        % g/mol
T    = 10.5;                      % C  
Tset = -10;                       %temperatura do setpoint
kc = 1;                           %constante do controlador
Mrefant = Mref;

% Tempo de simulacao
tf=1;

i=1;
tempo = 0;   
%Inicio do loop do tempo
 while (tempo<=tf)
     
    %Temperatura ambiente
    Tamb = 20;       
    
    %O controlador de vazao de refrigerante
    Mref = 0.10 - kc*(Tset - T);
            
    % Calculando a derivada dT/dtempo
    dTdt=(U*A/(ma*Cp))*(Tamb - T) - (Mref/(ma*Cp))*(hv-hl);

    % Calculando a temperatura
    T=T+dTdt*dt;    
    
    %Vetorizando para a plotagem
    tempoV(i)=tempo;
    TV(i)=T;
    TambV(i)=Tamb;
    MrefV(i)=Mref;
    i=i+1;
           
    tempo = tempo + dt;
 end
 
  % Plotando os graficos
    subplot(2,2,1); plot(tempoV,TV,'.');     xlabel('tempo');ylabel('T');                           hold on;    
    subplot(2,2,2); plot(tempoV,TambV,'.'); xlabel('tempo');ylabel('Temperatura amb.');         hold on;  
    subplot(2,2,3); plot(tempoV,MrefV,'.'); xlabel('tempo');ylabel('Massa de Refrigerante');   hold on;    
    
