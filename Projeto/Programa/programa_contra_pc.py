#from playsound import playsound
from threading import Thread
from decidir   import Ia
from random    import randint, choice
from time      import sleep
from os        import system
import serial
global pygame
import pygame

global conexao
global entrada_agora
global vez
global reg

entrada_agora = False


def pmusic(file):
    #print('pmusic')
    print(file)
    pygame.init()
    pygame.mixer.init()
    clock = pygame.time.Clock()
    try:
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
    except:
        print("Erro aqui")
    #while pygame.mixer.music.get_busy():
    #    print("Playing...")
    #    clock.tick(1000)

def getmixerargs():
    #print('getmixerargs')
    pygame.mixer.init()
    freq, size, chan = pygame.mixer.get_init()
    return freq, size, chan

def initMixer():
    #print('initMixer')
    BUFFER = 3072  # audio buffer size, number of samples since pygame 1.8.
    FREQ, SIZE, CHAN = getmixerargs()
    pygame.mixer.init(FREQ, SIZE, CHAN, BUFFER)
initMixer()

def play(file = 'sons/futuristic_clicking_noise.wav'):
    #print('play')

    try:        
        pmusic(file)
    except Exception as erro:
        print("Erro ")

    #except KeyboardInterrupt:  # to stop playing, press "ctrl-c"
    #    pygame.mixer.music.stop()
 
# Tentar conectar através de diversas portas.
def tentar_conectar():
    #print('tentar_conectar')
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
    #print('atualizar_cor_botoes')
    global conexao

    # STRINGS E BYTES PARA CONTROLAR OS LEDS
    btdic = {"a":b"a",
             "b":b"b",
             "c":b"c",
             "d":b"d",
             "e":b"e",
             "f":b"f",
             "g":b"g",
             "h":b"h",
             "i":b"i",
             "j":b"j",
             "z":b"z",
             "l":b"l",
             "m":b"m",
             "n":b"n",
             "o":b"o",
             "p":b"p",
             "q":b"q",
             "r":b"r",
             "k":b"k"}

    # ENVIAR 3 VEZES O SINAL
    for num in range(0, 3):
        conexao.write(btdic[sinal])

# CONTROLE PARA LIGAR OS LEDS NAS POSIÇÕES ESPECIFICAS
def renderizar_botoes(reg):
    #print('renderizar_botoes')

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
    #print('reseta')
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
        renderizar_botoes(reg)   # RENDERIZAR BOTÕES
        sleep(0.2)

        for pos in posicao:
            reg[pos] = ' '
        renderizar_botoes(reg)   # RENDERIZAR BOTÕES
        sleep(0.2)

# ANIMAÇÃO QUANDO DER VELHA
def deu_velha_comemoracao():
    #print('deu_velha_comemoracao')
    atualizar_cor_botoes("z") # DESIGAR TUDO

    for num in range(0,8):
        reg = ['x','x','x','x','x','x','x','x','x']  # TABULEIRO DE X
        renderizar_botoes(reg)                       # RENDERIZAR BOTÕES
        sleep(0.2)                                   # ESPERA

        reg = ['o','o','o','o','o','o','o','o','o']  # TABULEIRO DE O
        renderizar_botoes(reg)                       # RENDERIZAR BOTÕES
        sleep(0.2)                                   # ESPERA

# ANIMAÇÃO QUANDO DER VELHA
def inicializacao_animacao():
    #print('inicializacao_animacao')
    atualizar_cor_botoes("z") # DESIGAR TUDO
    espera = 0.1
    sleep(espera)

    lista_vez = ['x','o']
    for elemento in lista_vez:
        reg = [' ',' ',' ',' ',' ',' ',' ',' ',' ']  # TABULEIRO DE X
        for x in range(len(reg)):
            reg[x] = elemento
            renderizar_botoes(reg)                    # RENDERIZAR   BOTÕES
            sleep(espera)                             # ESPERA
        for x in range(4):
            renderizar_botoes(reg)                    # RENDERIZAR   BOTÕES
            sleep(0.5)
            atualizar_cor_botoes("z")
            sleep(0.5)


    reg = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    renderizar_botoes(reg)                    # RENDERIZAR BOTÕES

# IMPEDIR QUE OS DADOS SE ACUMULEM NO ARDUINO.
def sem_pilha_por_favor():
    #print('sem_pilha_por_favor')
    while True:
        global entrada_agora
        entrada_agora = entrada()

def atualizar_interface(reg):
    #print('atualizar_interface')
    Ia.renderizar(reg)                # RENDERIZAR TERMINAL
    renderizar_botoes(reg)            # RENDERIZAR BOTÕES
            
# Tentar obter uma conexão
conexao = tentar_conectar() 

# Verificar se ela está conectada
conexao.isOpen()

# DEFINIR VALORES
vez, velha,reg = reseta()

Ia.renderizar(reg)     # RENDERIZAR TERMINAL
renderizar_botoes(reg) # RENDERIZAR BOTÕES

# THREAD PARA LER CONTINUAMENTE A SERIAL DO ARDUINO
t = Thread(target=sem_pilha_por_favor)
t.start()
sleep(1)

#inicializacao_animacao()

jogadas = 0
# LOOP DO GAME
while True:
    jogadas += 1
    print("Ja houve {} jogadas".format(jogadas))
    #print('loop1')
    # ================== JOGADOR ================== #
    # CAPTURAR O BOTÃO QUE O USUÁRIO DIGITAR
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
    play()

    '''
    #sleep(randint(1.0,4.0)) #remove
    reg = Ia.escolher_IA(reg,vez,velha) # remove
    play() # remove
    velha +=1  # remove
    print('loop2')
    '''
    
    Ia.renderizar(reg)       # TERMINAL
    renderizar_botoes(reg)   # RENDERIZAR BOTÕES

    # ALGUÉM GANHOU?
    status = Ia.ganhou(vez,reg,velha)
    if status[0] =='vitória':
        lista = ['sons/ganhou/tuudurt_piglevelwin2.mp3','sons/ganhou/foolboymedia_crowd-cheer.wav','sons/ganhou/kastenfrosch_ewonnen2.mp3']
        toque = choice(lista)
        play(toque)

        ganhei_comemoracao(status[1],reg) # ANIMAÇÃO VITÓRIA
        vez, velha,reg = reseta()         # RECOMEÇAR
        atualizar_interface(reg)
        print('loop3')
        continue



    elif status[0] == 'velha':
        lista = ['sons/velha/ninguem-acertou.mp3','sons/velha/76376__deleted-user-877451game-over.wav']
        toque = choice(lista)
        play(toque)

        deu_velha_comemoracao()           # ANIMAÇÃO DEU VELHA
        vez, velha,reg = reseta()         # RECOMEÇAR
        atualizar_interface(reg)
        print('loop4')
        continue
    # TROCAR A VEZ
    vez = Ia.troca_vez(vez)

    # ================ COMPUTADOR ================= #
    sleep(randint(1.0,2.0))

    reg = Ia.escolher_IA(reg,vez,velha)
    play()

    velha +=1
    '''
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
    '''

    Ia.renderizar(reg)       # TERMINAL
    renderizar_botoes(reg)   # RENDERIZAR BOTÕES
    status = Ia.ganhou(vez,reg,velha)
    if status[0] =='vitória':
        lista = ['sons/perdeu/errou.mp3','sons/perdeu/quartetofantastico__risadasaltas.wav','sons/perdeu/219876__polmdx__buu-loser-shout.mp3','sons/perdeu/321909__bboyjoe-15__fatality.mp3','sons/perdeu/219110__zyrytsounds__evil-laugh.wav']
        toque = choice(lista)
        play(toque)

        ganhei_comemoracao(status[1],reg) # ANIMAÇÃO VITÓRIA
        vez, velha,reg = reseta()         # RECOMEÇAR
        atualizar_interface(reg)
        continue

    elif status[0] == 'velha':
        lista = ['sons/velha/ninguem-acertou.mp3','sons/velha/76376__deleted-user-877451game-over.wav']
        toque = choice(lista)
        play(toque)

        play('sons/velha/76376__deleted-user-877451game-over.wav')
        deu_velha_comemoracao()           # ANIMAÇÃO DEU VELHA
        vez, velha,reg = reseta()         # RECOMEÇAR
        atualizar_interface(reg)
        continue
    # TROCAR A VEZ
    vez = Ia.troca_vez(vez)

