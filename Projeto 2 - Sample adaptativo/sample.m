
% Limpando vetores
 clear    tempoV;
 clear    VV;
 clear    FV;
 
% Alimentacao (entrada)
F0=40;   

% Saida
F=40;                  

% Dimensao
V=48;    

% Condicoes de operacao (set points)
Vset=48;       

% Passo de tempo das equacoes diferenciais
dt=0.001;  

% Constantes do controlador PI (Proporcional Integral)
Kc=-1;   
Ti=1/500;  

% Tempo de simulacao
tf=5;       

% Tempo de amostragem do controlador     <-----------  Novidade
tsample=0.8;

% Vazao para quando o erro (variavel no setpoint - variavel) for zero. V=cte
Ferrozero = F0;  

% Disturbio
F0=45;    
 
 % Inicio do loop
 i=1;
 intPID=0;
 tempo=0;
 while (tempo<=tf)          

    % Calculando as derivadas
    dVdt=F0-F;    

    % Calculando as variavel
    V=V+dVdt*dt;              
    
     if (abs ( round(tempo/tsample)  -  (tempo/tsample) )  < 1e-4)   
         disp(tempo)
        % Controlador PI no Volume
        %----------------------------------------------------------
        % Definindo o erro
          Err=(Vset-V);         
          % A integral do PI no volume    
          intPID = intPID + (Err)*dt;   
          % A parte proporcional do PI no volume
          proPID = Err;              
          % A equacao do PI no volume
          F = Ferrozero + ( Kc*proPID + (Kc/Ti)*intPID );
          %----------------------------------------------------------    
      endif
      
    %Vetorizando   
    tempoV(i)=tempo;    
    VV(i)=V;  
    FV(i)=F;  
    i=i+1;
        
    tempo = tempo + dt;
 end
 
 % Plotando os gr?ficos
 subplot(2,1,1); plot(tempoV,VV,'.'); xlabel('tempo');ylabel('Volume'); hold on;    
 subplot(2,1,2); plot(tempoV,FV,'.'); xlabel('tempo');ylabel('Vazao saida'); hold on;    