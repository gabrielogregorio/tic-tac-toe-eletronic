#  jogo_da_velha_gamer
Um jogo da velha "gamer" para Fatec Aberta

 -------------------------------------------------- --------------------------------------------------

#  Nossas expectativas
##  Placa de Circuitos  


 -------------------------------------------------- --------------------------------------------------

##  Modelos visuais
 
![](https://github.com/gabrielogregorio/jogo_da_velha_gamer/blob/master/modelo%203D/Imagens/img4.png)

 -------------------------------------------------- --------------------------------------------------

# Colocando em prática   

### Planejando
Criamos um quadro no ![Trello](https://trello.com/), onde organizamos todas as etapas que preciariamos fazer para realizar o projeto.

Começamos por definir com exatidão o que cada parte iria fazer:
- O arduino irá ligar e desligar os leds e também irá ler o estado do botões. Nada mais!
- O circuto eletrônico só terá função de obedecer aos comandos do Arduino, filtrando sinais indesejados para ele.
- O script em Python irá dar comandos para o arduino, sendo ele quem lê as entradas, comanda as saidas e inicia a reprodução do som.
- O sistema deve funcionar com perfeição no Windows.

Depois, começamos a definir quem iria fazer o que:
- Quem vai fazer o script?
- Quem vai fazer a placa?
- Quem vai trabalhar no design?

Depois começamos a fazer testes, para ver come seria o modelo 3D, sem se preocupar com detalhes mais técnicos. Nesse passo, conseguimos descobrir diversas falhas que nosso projeto teria.
![](https://github.com/gabrielogregorio/jogo_da_velha_gamer/blob/master/modelo%203D/Imagens/img1.png)

Usando diversos softwares, para celular e para computador, definimos um modelo que seria legal para os nossos circuitos eletrônicos, depois geramos um modelo 3D, percebemos alguns novos problemas que poderiamos ter, então já iniciamos um plano B, considerando que esses problemas poderiam aparecer. Na etapa de produção, acabamos contornando esses problemas, mas os modelos que fizemos, nos deram uma visão fantastica sobre como cada parte do circuito, o que facilitou demais no desenvolvimento.
![](https://github.com/gabrielogregorio/jogo_da_velha_gamer/blob/master/modelo%203D/Imagens/3d.png)

# Criando os programas.  
### Desenvolvendo um celebro
Começamos a desenvolver uma versão simples de como o script iria funcionar, decimos adotar o Python com a biblioteca pyserial para que pudessemos escreve-la e nos conectarmos com o arduino. Posteriormete, adicionamos a biblioteca pygame para reproduzir o som.

A ideia é básica, eu reaproveitei pedaços de código de um jogo da velha que eu tinha feito anteriormente, em que ele recebe uma lista com 9 elementos, os elementos podem ser ' ', 'x' ou 'o'. Eles definem o estado daquela posição no tabuleiro. A biblioteca analisa essa lista, com todos os dados sobre onde está cada jogador e então escolhe uma posição de acordo com uma série de regras. A biblioteca retorna a própria lista com a posição que ela escolheu.

Então fizemos um outro script, que coordena a posição que o jogador escolheu, executa a biblioteca espera a posição que o "computador escolheu", que envia e faz a leitura de dados da serial e que executa os sons de acordo com o que está acontecendo.

Inicialmente ele era independente, portanto, conseguimos testa-la sozinha no computador, deixando ela pronto para se conectar ao arduino, mesmo sem o arduino e sem a placa montada.

Isso só foi possivel por que padronizamos como a comunicação entre o Arduino e o computador seria feita, através de tabelas.

### Controlando o universo
Ao mesmo tempo, iniciamos o planejamento e codificação de como o arduino iria controlar os leds e ler os botões.

Planejamos as respostas de duas perguntas principais:
- O que o arduino vai fazer ao receber um sinal dos botões?
- O que o arduino irá receber para ligar ou desligar os leds?

Começando pela primeira:

**O que o arduino vai fazer ao receber um sinal dos botões?**

Qual sinal que o arduino deve enviar para serial *( que é onde o nosso script vai entender o que está acontecendo)*, quando cada botão for pressionado, ou seja, se o botão 1 for pressionado **(button1)**, qual sinal que o Arduino irá enviar para a serial?

Definimos uma tabela padrão, que segue o modelo abaixo. 

> A tabela foi atualizada com a pinagem que usamos. 

| sinal   |    botão  | pinagem |
|---------|-----------|---------| 
|    1    |  button1  |     2   |
|    2    |  button2  |     3   |
|    3    |  button3  |     4   |
|    4    |  button4  |     5   |
|    5    |  button5  |     6   |
|    6    |  button6  |     7   |
|    7    |  button7  |     8   |
|    8    |  button8  |     9   |
|    9    |  button9  |     10  |

Nesse caso, se o **button4** for pressionado, ele enviará um sinal HIGH para o pino 5, esse sinal será lido pelo Arduino e ele irá enviar o sinal 4 para a serial. O papel do Arduino é basicamente isso. O script irá ler a serial e ver o sinal 4, entendendo que o button4 foi pressionado.

Ou seja, seguimos basicamente essa estrutura:   
![](https://github.com/gabrielogregorio/jogo_da_velha_gamer/blob/master/imagens/botoes.png)

Resumindo:
- Um positivo alimenta todos os botões.
- Na saída, forçamos os botões a terem uma saida LOW, quando não estiverem sendo pressionados, atravéz dos resistores de PULL DOWN.
- As saidas vão para os pinos do Arduino, de 2 a 10.
- Exemplificando, se o pino 10 for acionado, significa que o button 9 foi clicado, sendo assim, o Arduino deverá enviar o sinal 9 para a serial.

#### O que o arduino irá receber para ligar ou desligar os leds?

Também criamos uma tabela padrão, que diz quais sinais devem estar na serial para que o arduino ligue ou desligue os Leds. 

|  sinal  |    led    | status |
|---------|-----------|--------|
|   "a"   | LedVerde1 | ligado |
|   "b"   | LedAzul1  | ligado |
|   "c"   | LedVerde2 | ligado |
|   "d"   | LedAzul2  | ligado |
|   "e"   | LedVerde3 | ligado |
|   "f"   | LedAzul3  | ligado |
|   "g"   | LedVerde4 | ligado |
|   "h"   | LedAzul4  | ligado |
|   "i"   | LedVerde5 | ligado |
|   "j"   | LedAzul5  | ligado |
|   "k"   | LedVerde6 | ligado |
|   "l"   | LedAzul6  | ligado |
|   "m"   | LedVerde7 | ligado |
|   "n"   | LedAzul7  | ligado |
|   "o"   | LedVerde8 | ligado |
|   "p"   | LedAzul8  | ligado |
|   "q"   | LedVerde9 | ligado |
|   "r"   | LedAzul9  | ligado |
|   "z"   | *tudo     | deslig |

Nessa tabela, se o Arduino receber o sinal "a", ele deverá ligar o conjunto de leds verde do primeiro quadrado. Se ele receber um sinal "z", ele deverá desligar todos os leds. Para otimizarmos fios, tempo e recurso financeiros, decidimos que os 4 leds de um quadrado seriam ligados juntos, sendo assim, verificamos que seria viável usarmos um led de 220 OHM para cada 4 conjunto de leds, sendo assim, cumprindo o papel de funcionar durante o evento (Fatec Aberta) e custando menos tempo de manutenção, menos tempo montando, menos recursos financeiros e menos linhas de código.

> Os resistores servem para delimitar a corrente elétrica. Até onde sabemos, os leds que usamos possuem uma tensão nominal de 3.3 volts, sendo assim, ligar diretamente no 5 volts do Arduino é uma péssima ideia, portanto, ao adicionarmos os resistores de 220 OHM na saida dos 4 leds, a tensão é reduzida a níveis mais seguros para o funcionamento dos leds.

Sendo assim, o esquema para cada botão fica assim:    
![](https://github.com/gabrielogregorio/jogo_da_velha_gamer/blob/master/imagens/leds.png)

# Testando coisas
# Compras
Após definirmos e testarmos a parte eletronica todas as 

#  Lista de materiais 
 
| Qt | Nome | Preço | Explicação |   
|-----|----------------------------|---------------|-------------------------------------|   
| 2 | Metros de fio de rede. | R$: 2,00 | Conexões entre os componentes |   
| 40 | Cabo Jumper Macho/?? | R$: 2,00 | Conexões entre o aruino e a placa | 
| 18 | Leds verde de auto brilho. | R$: 0,5 cada | Xis | 
| 18 | leds azul de auto brilho. | R$: 0,5 cada | Bolinha | 
| 9 | Push Button. | R$: 0,2 cada | Leitura do clique | 
| 36 | Resistores 220 OHM. | R$: 0,15 cada | Controlar a tensão dos LEDS | 
| 27 | Resistores 2K2. | R$: 0,15 cada | Definir um GND | 
| 1 | Arduino MEGA 2560 | R$: 80,00 | Controle | 
| 1 | Conector para Arduino | R$: 15,00 | Enviar comandos e controle | 
| 1 | Placa De Circuitos 15x15 | R$:20.00 | Circuitos eletrônicos | 
| 3 | Metros de estanho. | R$: 2,00 | Conexões entre os sistemas | 
| 9 | Blocos brancos | R$: 0,00 | Design | 
| 1 | Notebook | R$: 450 | Célebro | 

#  Lista de ferramentas
 
| Qt  |            Nome            |     Preço     |              Explicação             | 
|-----|----------------------------|---------------|-------------------------------------| 
|  1  | Protoboard                 | R$: 20,00     | Circuitos de testes                 | 
|  1  | Ferro de solda             | R$: 15,00     | Solda de componentes                | 
|  1  | Alicate                    | R$: 00,00     | Corte de fios                       | 
