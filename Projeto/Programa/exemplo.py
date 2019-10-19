from playsound import playsound
from threading import Thread
from decidir   import Ia
from random    import randint
from time      import sleep
from os        import system
import serial

global conexao
global entrada_agora
global vez

entrada_agora = False

# Tentar conectar através de diversas portas.
def tentar_conectar():
    global conexao
    for num in range(0,10):
        porta = '/dev/ttyACM{}'.format(num)
        try:
            conexao = serial.Serial(porta, 9600)
        except:
            pass
        else:
            return conexao

# LER O ESTADO DOS BOTÕES
def leitura_de_botoes():
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
    return leitura_de_botoes()

# ZERANDO OS VALORES DO JOGO
def reseta():
    vez = 'x'                                    # VEZ
    velha = 0                                    # NUMERO DE JOGADAS
    reg = [' ',' ',' ',' ',' ',' ',' ',' ',' ']  # TABULEIRO
    return [vez, velha, reg]

# COMEMORAÇÃO DE VITÓRIA
def ganhei_comemoracao(posicao,reg):
    global vez
    sleep(0.1)
    for num in range(0,7):
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
    atualizar_cor_botoes("z") # DESIGAR TUDO

    for num in range(0,4):
        reg = ['x','x','x','x','x','x','x','x','x']  # TABULEIRO DE X
        renderizar_botoes(reg)                       # RENDERIZAR BOTÕES
        sleep(0.2)                                   # ESPERA

        reg = ['o','o','o','o','o','o','o','o','o']  # TABULEIRO DE O
        renderizar_botoes(reg)                       # RENDERIZAR BOTÕES
        sleep(0.2)                                   # ESPERA

# IMPEDIR QUE OS DADOS SE ACUMULEM NO ARDUINO.
def sem_pilha_por_favor():
    while True:
        global entrada_agora
        entrada_agora = entrada()

def atualizar_interface(reg):
    Ia.renderizar(reg)                # RENDERIZAR TERMINAL
    renderizar_botoes(reg)            # RENDERIZAR BOTÕES
            
def reproduzir_som_thread(link):
     playsound(link)

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

# LOOP DO GAME
while True:
    # ================== JOGADOR ================== #

    # CAPTURAR O BOTÃO QUE O USUÁRIO DIGITAR
    escolha = entrada_agora
    while escolha == False:
        escolha = entrada_agora

    reproduzir_som_thread('sons/futuristic_clicking_noise.wav')
    escolha = int(escolha)

    # JÁ ESTÁ SENDO USADO
    if reg[escolha-1] != ' ': 
        continue
    else:
        reg[escolha-1] = vez
        velha +=1

    Ia.renderizar(reg)       # TERMINAL
    renderizar_botoes(reg)   # RENDERIZAR BOTÕES

    # ALGUÉM GANHOU?
    status = Ia.ganhou(vez,reg,velha)
    if status[0] =='vitória':
        ganhei_comemoracao(status[1],reg) # ANIMAÇÃO VITÓRIA
        vez, velha,reg = reseta()         # RECOMEÇAR
        atualizar_interface(reg)
        continue

    elif status[0] == 'velha':
        deu_velha_comemoracao()           # ANIMAÇÃO DEU VELHA
        vez, velha,reg = reseta()         # RECOMEÇAR
        atualizar_interface(reg)
        continue

    # TROCAR A VEZ
    vez = Ia.troca_vez(vez)

    # ================ COMPUTADOR ================= #
    sleep(randint(1.0,4.0))

    reg = Ia.escolher_IA(reg,vez)
    reproduzir_som_thread('sons/futuristic_clicking_noise.wav')

    velha +=1

    Ia.renderizar(reg)       # TERMINAL
    renderizar_botoes(reg)   # RENDERIZAR BOTÕES

    status = Ia.ganhou(vez,reg,velha)
    if status[0] =='vitória':
        ganhei_comemoracao(status[1],reg) # ANIMAÇÃO VITÓRIA
        vez, velha,reg = reseta()         # RECOMEÇAR
        atualizar_interface(reg)
        continue

    elif status[0] == 'velha':
        deu_velha_comemoracao()           # ANIMAÇÃO DEU VELHA
        vez, velha,reg = reseta()         # RECOMEÇAR
        atualizar_interface(reg)
        continue

    # TROCAR A VEZ
    vez = Ia.troca_vez(vez)
