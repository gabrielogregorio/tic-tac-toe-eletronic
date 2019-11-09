global entrada_agora
global conexao
global pygame
global vez
global reg
global velha

from threading import Thread
from decidir   import Ia
from random    import randint, choice
from time      import sleep
from os        import system
import serial
import pygame

entrada_agora = False

def pmusic(file):
    print(file)
    pygame.init()
    pygame.mixer.init()
    clock = pygame.time.Clock()
    try:
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
    except:
        print("Erro aqui")

def getmixerargs():
    pygame.mixer.init()
    freq, size, chan = pygame.mixer.get_init()
    return freq, size, chan

def initMixer():
    BUFFER = 3072
    FREQ, SIZE, CHAN = getmixerargs()
    pygame.mixer.init(FREQ, SIZE, CHAN, BUFFER)
initMixer()

def play(file = 'sons/futuristic_clicking_noise.wav'):
    try:        
        pmusic(file)
    except Exception as erro:
        print("Erro ")
 
# Tentar conectar ao arduino através de diversas portas.
def tentar_conectar():
    global conexao
    lista = ['/dev/ttyACM','/com']
    for x in lista:
        for num in range(0,10):
            porta = '{}{}'.format(x,num)
            try:
                conexao = serial.Serial(porta, 9600)
            except:
                 pass
            else:
                return conexao

# LER O ESTADO DOS BOTÕES
def leitura_de_botoes():
    #print('leitura_de_botoes')
    global conexao

    # TECLAS VÁLIDAS POSSIVEIS
    teclas = [b'1',b'2',b'3',b'4',b'5',b'6',b'7',b'8',b'9']
    status = conexao.read()

    if status in teclas:
        return status
    else:
        return False

def atualizar_cor_botoes(sinal):
    global conexao

    # STRINGS E BYTES PARA CONTROLAR OS LEDS
    btdic = {"a":b"a","b":b"b","c":b"c",
             "d":b"d","e":b"e","f":b"f",
             "g":b"g","h":b"h","i":b"i",
             "j":b"j","z":b"z","l":b"l",
             "m":b"m","n":b"n","o":b"o",
             "p":b"p","q":b"q","r":b"r","k":b"k"}

    # ENVIAR 3 VEZES O SINAL
    for num in range(0, 3):
        conexao.write(btdic[sinal])

# CONTROLE PARA LIGAR OS LEDS NAS POSIÇÕES ESPECIFICAS
def renderizar_botoes():
    global reg

    # DESLIGAR TODOS OS LEDS
    atualizar_cor_botoes("z")

    liga_led_verde = ["a","c","e","g","i","k","m","o","q"] # LIGAR VERDE NA POSIÇÃO
    liga_led_azul  = ["b","d","f","h","j","l","n","p","r"] # LIGAR AZUL NA POSIÇÃO

    # ANDAR PELAS POSICOES DO GAME
    for item in range(0,len(reg)):
        if reg[item] == 'x':
            atualizar_cor_botoes(liga_led_verde[item])

        elif reg[item] == 'o':
            atualizar_cor_botoes(liga_led_azul[item])

# LER O ESTADO DOS BOTÕES
def entrada():
    #print('entrada')
    return leitura_de_botoes()

# ZERANDO OS VALORES DO JOGO
def reseta():
    global vez
    global velha
    global reg

    vez = 'x'                                    # VEZ
    velha = 0                                    # NUMERO DE JOGADAS
    reg = [' ',' ',' ',' ',' ',' ',' ',' ',' ']  # TABULEIRO
    return [vez, velha, reg]

# COMEMORAÇÃO DE VITÓRIA
def ganhei_comemoracao(posicao,reg):
    #print('ganhei_comemoracao')
    global vez
    sleep(0.1)
    for num in range(0,10):
        for pos in posicao:
            reg[pos] = vez
        renderizar_botoes()
        sleep(0.2)

        for pos in posicao:
            reg[pos] = ' '
        renderizar_botoes()
        sleep(0.2)

# ANIMAÇÃO QUANDO DER VELHA
def deu_velha_comemoracao():
    atualizar_cor_botoes("z") # DESIGAR TUDO

    for num in range(0,8):
        reg = ['x','x','x','x','x','x','x','x','x']  # TABULEIRO DE X
        renderizar_botoes()                       # RENDERIZAR BOTÕES
        sleep(0.2)                                   # ESPERA

        reg = ['o','o','o','o','o','o','o','o','o']  # TABULEIRO DE O
        renderizar_botoes()                       # RENDERIZAR BOTÕES
        sleep(0.2)                                   # ESPERA

# IMPEDIR QUE OS DADOS SE ACUMULEM NO ARDUINO.
def sem_pilha_por_favor():
    while True:
        global entrada_agora
        entrada_agora = entrada()

def atualizar_interface(reg):
    Ia.renderizar(reg)                # RENDERIZAR TERMINAL
    renderizar_botoes()            # RENDERIZAR BOTÕES

def som_comemoracao(tipo,status):
    if tipo == 'vitória':
        lista = ['sons/ganhou/tuudurt_piglevelwin2.mp3','sons/ganhou/foolboymedia_crowd-cheer.wav','sons/ganhou/kastenfrosch_ewonnen2.mp3']
        play(choice(lista))
        ganhei_comemoracao(status[1],reg)

    elif tipo == 'velha':
        lista = ['sons/velha/ninguem-acertou.mp3','sons/velha/76376__deleted-user-877451game-over.wav']
        play(choice(lista))
        deu_velha_comemoracao()
    elif tipo == 'perdeu':
        lista = ['sons/perdeu/errou.mp3','sons/perdeu/quartetofantastico__risadasaltas.wav','sons/perdeu/219876__polmdx__buu-loser-shout.mp3','sons/perdeu/321909__bboyjoe-15__fatality.mp3','sons/perdeu/219110__zyrytsounds__evil-laugh.wav']
        play(choice(lista))
        deu_velha_comemoracao()
    
    vez, velha,reg = reseta()
    atualizar_interface(reg)
            
# Tentar obter uma conexão
conexao = tentar_conectar() 

# Verificar se ela está conectada
conexao.isOpen()

# DEFINIR VALORES
vez, velha,reg = reseta()

Ia.renderizar(reg)     # RENDERIZAR TERMINAL
renderizar_botoes() # RENDERIZAR BOTÕES

# THREAD PARA LER CONTINUAMENTE A SERIAL DO ARDUINO
t = Thread(target=sem_pilha_por_favor)
t.start()
sleep(1)

# LOOP DO GAME
while True:
    # ================== JOGADOR 1 ================== #
    escolha = entrada_agora
    while escolha == False:
        escolha = entrada_agora
    escolha = int(escolha)

    # JÁ ESTÁ SENDO USADO
    if reg[escolha-1] != ' ': 
        continue
    else:
        reg[escolha-1] = vez
        velha +=1

    # toque 
    play()
    
    Ia.renderizar(reg)
    renderizar_botoes()

    # ALGUÉM GANHOU?
    status = Ia.ganhou(vez,reg,velha)
    if status[0] =='vitória':
        som_comemoracao('vitória',status)
        continue

    elif status[0] == 'velha':
        som_comemoracao('velha',status)
        continue

    # TROCAR A VEZ
    vez = Ia.troca_vez(vez)

    # ================ OUTRO JOGADOR ================= #
    escolha2 = entrada_agora
    while escolha2 == False:
        escolha2 = entrada_agora
    escolha2 = int(escolha2)

    # JÁ ESTÁ SENDO USADO
    if reg[escolha2-1] != ' ': 
        continue
    else:
        reg[escolha2-1] = vez
        velha +=1

    play()

    Ia.renderizar(reg)
    renderizar_botoes()

    status = Ia.ganhou(vez,reg,velha)

    # ALGUÉM GANHOU?
    status = Ia.ganhou(vez,reg,velha)
    if status[0] =='vitória':
        som_comemoracao('vitória',status)
        continue

    elif status[0] == 'velha':
        som_comemoracao('velha',status)
        continue

    # TROCAR A VEZ
    vez = Ia.troca_vez(vez)

