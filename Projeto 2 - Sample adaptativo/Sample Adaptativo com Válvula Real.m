%Limpando vetores

tempoV = [];
TV = [];
TambV = [];
MrefV = [];
AMrefV = [];

% Condições iniciais de operação
% Fluido estocado: Propano
% Refrigerante: 134a

U = 250;  % W/m²C
A = 2; % m²
Cp = 2520;  % J/kgC
ma = 10;  % kg
Mref = 0;  % kg/s
Rmax = 0.1;  % razão de velocidade da válvula
dt = 0.001;  % s
hv = 247000;  % J/kg
hl = 50000;  % J/kg
M = 44;  % g/mol
T = 10.5;  % C
Tset = -15;  % temperatura do setpoint
kc = 0.04;  % constante do controlador
Mrefant = Mref;
Tant = T;

% Tempo de simulação
tf = 30;

% Tempo de amostragem do controlador
tsample = 4;
AMref = 0;
tempo = 0;

% Inicio do loop do tempo
while tempo <= tf
    
    % Temperatura ambiente
    Tamb = 22;

    % Condição para diminuição do sample
    tsample = 4;
    if abs(T - Tant) / dt > 2  % Derivada da temperatura de entrada no tempo
        tsample = 0.5;
         
        Tant = T;
         
        % if abs(Tant-T)<1e-4
        %    T = Tset
         
    end
    
    if abs(round(tempo / tsample) - (tempo / tsample)) < 1e-4
        % O controlador de vazao de refrigerante
        Mref = 0.10 - kc * (Tset - T);
    end

    % A Valvula real
    % --------------------------------------
    if Mref >= Mrefant
        if Mref - Mrefant > Rmax
            Mref = Mrefant + Rmax;
        end
    elseif Mref < Mrefant
        if Mrefant - Mref > Rmax
            Mref = Mrefant - Rmax;
        end
    end

    Mrefant = Mref;
    % -------------------------------------

    % Calculo da integral sobre Mref
    AMref = AMref + Mref * dt;

    % Calculando a derivada dT/dtempo
    dTdt = (U * A / (ma * Cp)) * (Tamb - T) - (Mref / (ma * Cp)) * (hv - hl);

    % Calculando a temperatura
    T = T + dTdt * dt;

    % Vetorizando para a plotagem
    tempoV(end+1) = tempo;
    TV(end+1) = T;
    TambV(end+1) = Tamb;
    MrefV(end+1) = Mref;
    AMrefV(end+1) = AMref;

    tempo = tempo + dt;
end

% Plotando os graficos
subplot(2,2,1); plot(tempoV,TV,'.');     xlabel('tempo');ylabel('Temperatura do Propano');      hold on;    
subplot(2,2,2); plot(tempoV,TambV,'.'); xlabel('tempo');ylabel('Temperatura Ambiente');         hold on;  
subplot(2,2,3); plot(tempoV,MrefV,'.'); xlabel('tempo');ylabel('Vazão de 134a');   hold on;    
subplot(2,2,4); plot(tempoV,AMrefV,'.'); xlabel('tempo');ylabel('Massa Total de 134a');   hold on;    