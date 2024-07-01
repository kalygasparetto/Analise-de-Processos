
% Limpando vetores
 clear    tempoV;
 clear    VV;
 clear    FV;
 clear    F0V;
  
% Alimentacao (entrada)
F0=40;   
F0ant=F0;

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
tf=6;       

% Tempo de amostragem do controlador     <-----------  Novidade
tsample=1;

% Vazao para quando o erro (variavel no setpoint - variavel) for zero. V=cte
Ferrozero = F0;  

% Disturbio
% F0=45;    
 
 % Inicio do loop
 i=1;
 intPID=0;
 tempo=0;
 while (tempo<=tf)   
   
    % Função de F0 com o tempo
    if (tempo<4.8703)
      F0= 40 + sin(tempo*tempo - tempo);
    endif
  
    if (tempo>=4.8703)
      F0=40;
    endif         

    % Calculando as derivadas
    dVdt=F0-F;    

    % Calculando as variaveis
    V=V+dVdt*dt;              
    
    % Condição para diminuição do sample
    tsample=1;
    if (abs(F0-F0ant)/dt)>2  % Derivada da vazao de entrada no tempo
        tsample=0.2;
     endif          
    
     if (abs ( round(tempo/tsample)  -  (tempo/tsample) )  < 1e-4)   
        % disp(tempo)
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
      
      F0ant=F0;
      
    %Vetorizando   
    tempoV(i)=tempo;    
    VV(i)=V;  
    FV(i)=F;  
    F0V(i)=F0;
    i=i+1;
        
    tempo = tempo + dt;
 end
 
 % Plotando os gr�ficos
 subplot(3,1,1); plot(tempoV,VV,'.'); xlabel('tempo');ylabel('Volume'); hold on;    
 subplot(3,1,2); plot(tempoV,FV,'.'); xlabel('tempo');ylabel('Vazao saida'); hold on; 
 subplot(3,1,3); plot(tempoV,F0V,'.'); xlabel('tempo');ylabel('Vazao entrada'); hold on;   