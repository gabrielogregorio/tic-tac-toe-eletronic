#  Jogo da velha gamer
Um jogo da velha **"gamer"** para Fatec Aberta ( Gamer é por que tem LED’s, isso aumenta o FPS do computador em 256 %, hashuashuashuas… )

---------------------------------------------------------------------------------------------------------------

# Objetivo
Desenvolver um jogo da velha usando LED’s, que seja clicável, que tenha sons e que seja executado em um computador, usando a linguagem Python 3 (Porque já tínhamos uma biblioteca própria mais ou menos pronta), um Arduíno mega ( Porque temos um exemplar e temos uma noção de como ambos se encaixam ) e que tenha uma estrutura parecido com esse modelo 3D que fizemos:

![O que pensamos em fazer](https://github.com/gabrielogregorio/jogo_da_velha_gamer/blob/master/modelo%203D/Imagens/img2.png)

---------------------------------------------------------------------------------------------------------------

> Os passos descritos aqui não foram executados necessariamente nessa ordem que eles estão descritos.

---------------------------------------------------------------------------------------------------------------

# Planejando
Primeiramente criamos um quadro no [Trello](https://trello.com/), onde organizamos todas as etapas que iriamos precisar fazer para realizar o projeto.

Começamos por definir com exatidão o que cada parte do projeto faria:
- O Arduíno ligará e desligará os LED’s de acordo com letras que serão enviadas na sua serial. Ele também irá ler o estado dos botões e enviar números para a serial.
- O circuíto eletrônico só terá função de obedecer aos comandos do Arduíno e tratar de potenciais ruidos.
- O script em Python dará comandos para o Arduíno, sendo que ele irá ler números na serial e irá enviar letras por ela. Ele também irá controlar a reprodução do som.
- O sistema deve funcionar com perfeição no Windows 10.

Depois, começamos a definir quem faria o que:
- Quem vai fazer o script?
- Quem vai trabalhar no Arduíno?
- Quem vai fazer a placa?
- Quem vai trabalhar no design?
- Quem vai trabalhar nas melhorias?

Depois começamos a fazer testes, para ver como seria o modelo 3D, sem se preocupar com detalhes mais técnicos. Nesse passo, conseguimos descobrir diversas falhas que nosso projeto teria.

![](https://github.com/gabrielogregorio/jogo_da_velha_gamer/blob/master/modelo%203D/Imagens/img1.png)

Usando diversos softwares para celular e para computador, fizemos um circuito eletrônico que seria legal e acessível para o nosso projeto, depois geramos um modelo 3D. Percebemos alguns novos problemas que poderíamos ter, então já iniciamos um plano B, considerando que esses problemas poderiam aparecer. 

Na etapa de produção, acabamos contornando esses problemas, mas os modelos que fizemos, nos deram uma visão fantástica sobre como cada parte do circuito deveria funcionar, o que facilitou demais no desenvolvimento.
![](https://github.com/gabrielogregorio/jogo_da_velha_gamer/blob/master/modelo%203D/Imagens/3d.png)

---------------------------------------------------------------------------------------------------------------

# Criando os programas.
### Desenvolvendo um cérebro.
Começamos a desenvolver uma versão simples de como o script funcionaria, decidimos adotar o Python 3.6 com a biblioteca PySerial para que pudéssemos nos conectarmos com o Arduíno. Posteriormente, adicionamos a biblioteca PyGame para reproduzir o som.

A ideia é básica, eu reaproveitei pedaços de código de um jogo da velha que eu tinha feito anteriormente, em que ele recebe uma lista com 9 elementos, os elementos podem ser ' ', 'x' ou 'o'. Eles definem o estado de todas as posições no tabuleiro. A biblioteca analisa essa lista, com todos os dados sobre onde está cada jogador e então escolhe uma posição de acordo com uma série de regras pré definidas. A biblioteca retorna a própria lista com a posição que ela escolheu.

Então fizemos um outro script, que coordena a posição que o jogador escolheu, a posição que o “computador escolheu”, que envia e faz a leitura de dados da serial e que executa os sons de acordo com o que está acontecendo.

Inicialmente ele era independente, portanto, conseguimos testá-la sozinha no computador, deixando ela pronto para se conectar ao Arduíno, mesmo sem o Arduíno e sem a placa montada.

Isso só foi possível por que padronizamos como a comunicação entre o Arduíno e o computador seria feita, através de tabelas.

### Controlando o universo
Ao mesmo tempo, iniciamos o planejamento e a codificação do Arduíno.

Planejamos as respostas de duas perguntas principais:
- O que o Arduíno vai fazer ao receber um sinal dos botões?
- O que o Arduíno receberá para ligar ou desligar os LED’s?

Começando pela primeira:

**O que o Arduíno vai fazer ao receber um sinal dos botões?**

Ao receber um sinal dos botões, o Arduíno deve enviar para serial, reportando para o script qual botão que foi clicado, ou seja, se o botão 1 for pressionado **(button1)**, qual sinal que o Arduíno enviará para a serial?

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

Nesse caso, se o **button4** for pressionado, ele enviará um sinal HIGH para o pino 5, esse sinal será lido pelo Arduíno e ele enviará o sinal 4 para a serial. O papel do Arduíno é basicamente isso. O script irá ler a serial e ver o sinal 4, entendendo que o button4 foi pressionado.

Ou seja, seguimos basicamente essa estrutura:   
![](https://github.com/gabrielogregorio/jogo_da_velha_gamer/blob/master/imagens/botoes.png)

Resumindo:
- Um positivo alimenta todos os botões.
- Na saída, forçamos os botões a terem uma saída LOW, quando não estiverem sendo pressionados, através dos resistores de PULL DOWN.
- As saídas vão para os pinos do Arduíno, de 2 a 10.

Exemplificando novamente, se o pino 10 for acionado, significa que o button9 foi clicado, sendo assim, o Arduíno deverá enviar o sinal 9 para a serial e o script entenderá que o button9 foi clicado.

#### O que o Arduíno receberá para ligar ou desligar os LED’s?

Também criamos uma tabela padrão, que diz quais sinais devem estar na serial para que o Arduino ligue ou desligue os LED’s. 

|  sinal  |    led    | status | pinagem | 
|---------|-----------|--------|---------|
|   "a"   | LedVerde1 | ligado |  22     |
|   "b"   | LedAzul1  | ligado |  23     |
|   "c"   | LedVerde2 | ligado |  24     |
|   "d"   | LedAzul2  | ligado |  25     |
|   "e"   | LedVerde3 | ligado |  26     |
|   "f"   | LedAzul3  | ligado |  27     |
|   "g"   | LedVerde4 | ligado |  28     |
|   "h"   | LedAzul4  | ligado |  29     |
|   "i"   | LedVerde5 | ligado |  30     |
|   "j"   | LedAzul5  | ligado |  31     |
|   "k"   | LedVerde6 | ligado |  32     |
|   "l"   | LedAzul6  | ligado |  33     |
|   "m"   | LedVerde7 | ligado |  34     |
|   "n"   | LedAzul7  | ligado |  35     |
|   "o"   | LedVerde8 | ligado |  36     |
|   "p"   | LedAzul8  | ligado |  37     |
|   "q"   | LedVerde9 | ligado |  38     |
|   "r"   | LedAzul9  | ligado |  39     |
|   "z"   | *tudo     | deslig | SERIAL  |

Nessa tabela, vemos que, se o Arduíno receber o sinal "a", ele deverá ligar o conjunto de LED’s verde do primeiro quadrado, que está no pino 22. Se ele receber um sinal "z", ele deverá desligar todos os leds. 

Para otimizarmos fios, tempo e recurso financeiros, decidimos que os 4 negativos dos leds de um quadrado seriam ligados juntos, sendo assim, verificamos que seria viável usarmos um resistor de 220 OHM para cada 4 conjuntos de LED’s, custando menos tempo de manutenção, menos tempo montando, menos recursos financeiros.

> Os resistores servem para delimitar a corrente elétrica. Até onde sabemos, os LED’s que usamos possuem uma tensão nominal de 3.3 volts, sendo assim, ligar diretamente no 5 volts do Arduíno é uma péssima ideia, portanto, ao adicionarmos os resistores de 220 OHM na saída dos 4 leds, a tensão é reduzida a níveis seguros para o funcionamento dos leds.

Sendo assim, o esquema para cada botão fica assim:    
![](https://github.com/gabrielogregorio/jogo_da_velha_gamer/blob/master/imagens/leds.png)

Resumindo:
- Interligamos o positivo dos dois LED’s verdes de cada botão.
- Interligamos o positivo dos dois LED’s azuis de cada botão.
- O positivo do conjunto de LED’s verdes vão em um pino e o positivo do conjunto de LED’s azuis vão em outro pino, seguindo a tabela acima.
- Interligamos os quatro negativos a um resistor de 220 OHM conectando ao negativo.

---------------------------------------------------------------------------------------------------------------

# Testando coisas
Após definirmos como as coisas deveriam funcionar e quais padrões iriamos seguir, começamos a testar se a nossa lógica, tanto de programa quanto física estaria correta. Montamos uma versão simplificada e bem feia de como tudo deveria funcionar.

![Testando para ver se a lógica fazia sentido.](https://github.com/gabrielogregorio/jogo_da_velha_gamer/blob/master/imagens/etapa%20de%20testes.jpeg)

Nesse teste, descobrimos que nossa lógica estava correta, de forma bem robusta, nosso software e a parte física estavam respondendo conforme o planejado.

---------------------------------------------------------------------------------------------------------------

# Compras
Após definirmos padrões e validarmos nosso circuito, com testes e análises, iniciamos a etapa de comprar o que faltava. Compramos tudo seguindo a tabela abaixo. (Algumas coisas nós já tínhamos, faça a sua própria lista de compras).

###  Lista de materiais 
 
| Qt | Nome | Preço | Explicação |   
|-----|----------------------------|---------------|-------------------------------------|   
| 2 | Metros de fio de rede. | R$: 2,00 | Conexões entre os componentes |   
| 40 | Cabo Jumper Macho/?? | R$: 2,00 | Conexões entre o Arduíno e a placa | 
| 18 | LED’s verde de autobrilho. | R$: 0,5 cada | Xis | 
| 18 | LED’s azul de autobrilho. | R$: 0,5 cada | Bolinha | 
| 9 | Push Button. | R$: 0,2 cada | Leitura do clique | 
| 36 | Resistores 220 OHM. | R$: 0,15 cada | Controlar a tensão dos LEDS | 
| 27 | Resistores 2K2. | R$: 0,15 cada | Definir um GND | 
| 1 | Arduíno MEGA 2560 | R$: 80,00 | Controle | 
| 1 | Conector para Arduíno | R$: 15,00 | Enviar comandos e controle | 
| 1 | Placa De Circuitos 15x15 | R$:20.00 | Circuitos eletrônicos | 
| 3 | Metros de estanho. | R$: 2,00 | Conexões entre os sistemas | 
| 9 | Blocos brancos | R$: 0,00 | Design | 
| 1 | Notebook | R$: 450 | Celebro | 

###  Lista de ferramentas
 
| Qt  |            Nome            |     Preço     |              Explicação             | 
|-----|----------------------------|---------------|-------------------------------------| 
|  1  | Protoboard                 | R$: 20,00     | Circuitos de testes                 | 
|  1  | Ferro de solda             | R$: 15,00     | Solda de componentes                | 
|  1  | Alicate                    | R$: 00,00     | Corte de fios                       | 

---------------------------------------------------------------------------------------------------------------

# Montando tudo.
Quando tivemos a certeza que tudo deveria funcionar conforme o planejado e tínhamos comprado os itens básicos, iniciamos a etapa de montagem de tudo. Foi mais ou menos assim:

Com a placa em mãos, testamos o comportamento dos botões de plásticos que queriamos usar. Eles seriam a etapa final, mas nós precisávamos confirmar que eles ficariam bem com os botões.

Com tudo de acordo, posicionamos os botões, os leds, os resistores e fomos soldando eles na placa. Como regra, nós sempre fazíamos etapa por etapa, ou seja, a etapa de interligação dos resistores dos botões era apenas isso, iniciávamos e finalizávamos nisso, fazendo testes para verificar se a solda estáva boa, se algum fio se soltou, se tem alguma coisa se comportando mal, etc.

![](https://github.com/gabrielogregorio/jogo_da_velha_gamer/blob/master/imagens/etapa%20de%20produ%C3%A7%C3%A3o.jpg)

Fizemos isso até a última tarefa, sempre tentando fazer o melhor trabalho possível. Sem dúvidas, esse foi a tarefa mais demorada, e que exigiu mais testes.

Essa etapa também foi a que mais exigiu delicadeza, já que erros poderiam ocasionar na não conclusão do projeto.

Quando a parte eletrônica estava toda soldada, fizemos mais um teste geral, validando que tudo estava funcionando de acordo com o que foi previsto e que não haviam curtos na placa. Após isso que sentimos confiança para ligar o a placa no Arduíno, como já tínhamos feito um teste na protoboard e a placa estava respondendo de acordo, a integração foi literalmente só ligar os fios, o resto já havia sido testado e validado as etapas anteriores.

A parte superior ficou assim:
![](https://github.com/gabrielogregorio/jogo_da_velha_gamer/blob/master/imagens/parte%20superior.jpg)

A parte inferior ficou assim:
![](https://github.com/gabrielogregorio/jogo_da_velha_gamer/blob/master/imagens/parte%20inferior.jpg)

Colocando os botões obtivemos esse resultado:
![](https://github.com/gabrielogregorio/jogo_da_velha_gamer/blob/master/imagens/vers%C3%A3o%20final.jpg)

---------------------------------------------------------------------------------------------------------------

# Aperfeiçoando
Com tudo funcionando perfeitamente, adicionamos sons através do script em Python, adicionamos animações e fizemos diversas atualizações no código, deixando o jogo bem mais difícil contra o computador.

O resultado do nosso trabalho pode ser visto nesse repositório.

---------------------------------------------------------------------------------------------------------------

# Como executar o programa?

É necessário instalar o Python, de preferência na versão 3.6, adicionando o "Path" na variável de ambiente, caso você esteja usando o Windows.

Depois precisamos instalar a biblioteca PyGame, que nos permite reproduzir os sons.

```Bash
pip install pygame
```

E então precisamos instalar o PySerial, essa biblioteca nos permite ler e enviar dados para a serial do Arduíno, sendo a nossa ponte entre o script e o Arduino
```Bash
pip install pyserial
```
