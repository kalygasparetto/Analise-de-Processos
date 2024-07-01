%Limpando vetores
clear xAV; clear yAv; clear xretV; clear yretV;
clear xStripV; clear yStripV; clear xqLineV; clear yqLineV;
clear xLineEstV; clear yLineEstV;
clear all;
pctl=0;

%Dados de operação do sistema

%No caso do programa não convergir, ajustar os 3 parametros abaixo
passo=1e-3;     % passo de calculo da composição
err=1e-3;       % erro numerico aceitavel na composição
B=10;           % vazao no fundo saindo do sistema mol/h

%Setagem fisica do sistema
Nest=7;         % número fixo de estágios
alfa=2;         % volatilidade relativa
R=6;            % razao de refluxo = L/D
xF=0.5;         % composição da alimentação
F=20;           % vazao da alimentação mol/h
D=F-B;          % vazao no topo mol/h
xD=0.9999;      % composição máxima do destilado

Cont=1;

%Passo no alfa
passoalfa = 1;

%Passo no R
passoR = 1;

R=2;
while (R<=4)

   %Limpando vetores
   clear xAV; clear yAv; clear xretV; clear yretV;
   clear xStripV; clear yStripV; clear xqLineV; clear yqLineV;
   clear xLineEstV; clear yLineEstV;
   pctl=0;
   D=F-B;            % vazao no topo mol/h
   xD=0.9999;      % composição máxima do destilado

   alfa=2;
   while (alfa<=4)

      %Limpando vetores
      clear xAV; clear yAv; clear xretV; clear yretV;
      clear xStripV; clear yStripV; clear xqLineV; clear yqLineV;
      clear xLineEstV; clear yLineEstV;
      pctl=0;
      D=F-B;            % vazao no topo mol/h
      xD=0.9999;      % composição máxima do destilado

      %%plotando os graficos para aquele numero de estagios solicitado
      %if abs(Nest-Est)<err
      %    pctl=pctl+1;
      %endif

      %xD=xD-passo;

      %Condição de saida do programa
      %if abs(pctl-2)<err
      %  break
      %endif

      %Calculando a composição no fundo
      xB=(F*xF-D*xD)/B;

      %Impressao dos dados finais
      printf("Numero de estagios:");disp(Nest);
      printf("Composição no topo:");disp(xD);
      printf("Composição no fundo:");disp(xB);
      printf("Reciclo:");disp(R);
      printf("Volatilidade Relativa:");disp(alfa);

      x(Cont)=R;
      y(Cont)=alfa;
      z(Cont)=Nest;
      a(Cont)=xD;
      Cont = Cont + 1;

      %Nest = Nest + 1;

      alfa = alfa + passoalfa;

   endwhile
   R = R + passoR;

endwhile

scatter3 ( x, y, z, 50, a(:), "fill" );
xlim ([min(x)-1, max(x)+1]); ylim ([min(y)-1, max(y)+1]); zlim ([min(z)-1, max(z)+1]);
title('Operações possiveis de Projeto - Colobar: Fração mais volatil no topo');xlabel('Reciclo L/D');ylabel('Volatilidade relativa f(T)');zlabel('Numero de pratos');
colormap(jet);colorbar();

d = length(x);
VetorDados(1,1:d) = zeros(1,d);
VetorDados(2,1:d) = [x];
VetorDados(3,1:d) = [y];
VetorDados(4,1:d) = [z];
VetorDados(5,1:d) = [a];
csvwrite('DadosColunm.csv',VetorDados);

