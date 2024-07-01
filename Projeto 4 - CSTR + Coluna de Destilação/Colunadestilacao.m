
%Limpando vetores
clear xAV;clear yAv;clear xretV;clear yretV;
clear xStripV;clear yStripV;clear xqLineV;clear yqLineV;
clear xLineEstV;clear yLineEstV;
clear all;
pctl=0;

%Dados de operação do sistema

%No caso do programa não convergir, ajustar os 3 parametros abaixo
passo=1e-3;     % passo de calculo da composição
err=1e-2;       % erro numerico aceitavel na composição
B=5;             % vazao no fundo saindo do sistema

Nest=10;            % numero de estagios
alfa=2;             % volatilidade relativa
R=3;                % razao de refluxo = L/D
xF=0.571;         % composição da alimentação
F=14.5;             % vazao da alimentação
D=F-B;              % vazao no topo
q=1;                % tipo de alimentação (liquido saturado)

%Construindo a curva de equilibrio
i=1;
xA=0;
while (xA<=1)
    yA=alfa*xA/(1+(alfa-1)*xA);
    xAV(i)=xA;
    yAV(i)=yA;
    i=i+1;
    xA=xA+passo;
endwhile
plot(xAV,xAV,'.'); xlabel('x - Composição do mais volatil no liquido');ylabel('y - Composição do mais volatil no vapor'); hold on;
plot(xAV,yAV,'.'); hold on;

%Calculando as composições para o numero de estagios solicitados
xD=0.9999;
while (xD>xF)
    xB=(F*xF-D*xD)/B;

    %Limpando vetores
    clear xAV;clear yAv;
    clear xretV;clear yretV;
    clear xStripV;clear yStripV;
    clear xqLineV;clear yqLineV;
    clear xLineEstV;clear yLineEstV;

    %Construindo a linha de retificação - acima da alimentacao
    i=1;
    xret=xD;
    while (xret>=xF)
        yret=xD+(R/(R+1))*(xret-xD);
        xretV(i)=xret;
        yretV(i)=yret;
        i=i+1;
        xret=xret-passo;
    endwhile
    if abs(pctl-1)<err
        plot(xretV,yretV,'.'); hold on;
    endif

    %Construindo a q-line
    i=1;
    xqLine=xF;
    yqLine=xqLine;
    yAtop=alfa*xqLine/(1+(alfa-1)*xqLine);
    while (yqLine<=yAtop)
        xqLineV(i)=xF;
        yqLineV(i)=yqLine;
        i=i+1;
        yqLine=yqLine+passo;
    endwhile
    if abs(pctl-1)<err
      plot(xqLineV,yqLineV,'.'); hold on;
    endif

    %Construindo a linha de stripping - abaixo da alimentação
    x1Strip=xB;y1Strip=xB;
    x2Strip=xF;y2Strip=xD+(R/(R+1))*(xF-xD);
    i=1;
    xStrip=xB;
    while (xStrip<=xF)
        yStrip= y1Strip + ( (y2Strip-y1Strip)/(x2Strip-x1Strip) )*(xStrip - x1Strip);
        xStripV(i)=xStrip;
        yStripV(i)=yStrip;
        i=i+1;
        xStrip=xStrip+passo;
    endwhile
    if abs(pctl-1)<err
        plot(xStripV,yStripV,'.'); hold on;
    endif

    %Construindo as linhas dos estagios
    Est=0;
    xLineEst=xD;
    yLineEst=xD;
    while (xLineEst>xB)

        %Linhas horizontais
        i=1;
        while (xLineEst>=0)
            xLineEstV(i)=xLineEst;
            yLineEstV(i)=yLineEst;
            dist=sqrt(  ( (alfa*xLineEst/(1+(alfa-1)*xLineEst))- yLineEst) * ( (alfa*xLineEst/(1+(alfa-1)*xLineEst))- yLineEst) );
            i=i+1;
            xLineEst=xLineEst-passo;
            if dist <= err
              break
            endif
        endwhile
        if abs(pctl-1)<err
            plot(xLineEstV,yLineEstV,'.'); hold on;
        endif

        %Linhas verticais
            if (xLineEst>=xB)
            i=1;
            while (yLineEst>=xB)
                xLineEstV(i)=xLineEst;
                yLineEstV(i)=yLineEst;
                dist=sqrt(   (( xD+(R/(R+1))*(xLineEst-xD) )- yLineEst) *   (( xD+(R/(R+1))*(xLineEst-xD) )- yLineEst) );
                if xLineEst<=xF
                   dist=sqrt(  ( (y1Strip + ( (y2Strip-y1Strip)/(x2Strip-x1Strip) )*(xLineEst - x1Strip)) - yLineEst ) * ( (y1Strip + ( (y2Strip-y1Strip)/(x2Strip-x1Strip) )*(xLineEst - x1Strip)) - yLineEst ) );
                endif
                i=i+1;
                yLineEst=yLineEst-passo;
                if dist <= err
                      Est=Est+1;
                      break;
                endif
            endwhile
            endif

            if abs(pctl-1)<err
                plot(xLineEstV,yLineEstV,'.'); hold on;
            endif
    endwhile

    %Plotando os graficos para aquele numero de estagios solicitado
    if abs(Nest-Est)<err
        pctl=pctl+1;
    endif

    xD=xD-passo;

    %Condição de saida do programa
    if abs(pctl-2)<err
      break
    endif

endwhile

%Impressao dos dados finais
printf("Numero de estagios:");disp(Est);
printf("Composição no topo:");disp(xD);
printf("Composição no fundo:");disp(xB);
