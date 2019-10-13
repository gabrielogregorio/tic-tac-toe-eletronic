from decidir import Ia
import serial

global conexao

conexao = serial.Serial('/dev/ttyACM0', 9600)
conexao.isOpen()

# LER O ESTADO DOS BOTÕES
def leitura_de_botoes():
    global conexao

    # TECLAS POSSIVEIS
    teclas = [b'0',b'1',b'2',b'3','4',b'5',b'6',b'7',b'8']
    status = conexao.read()

    if status in teclas:
        return status
    else:
        return False

def atualizar_cor_botoes(sinal):
    global conexao                          # CONEXÃO 
    for num in range(0, 10):                 # LOOP DE 10
        conexao.write(b'{}'.format(sinal))  # ENVIAR SINAL

def renderizar_botoes(reg):
    atualizar_cor_botoes("z") # DESIGAR TUDO

    liga_led_verde = ["a","c","e","g","i","k","m","o","q"] # LIGAR VERDE NA POSIÇÃO
    liga_led_azul  = ["b","d","f","l","h","j","n","p","r"] # LIGAR AZUL NA POSIÇÃO

    for item in range(0,len(reg)): # DE 0 A 8
        if reg[item] == 'x':
            atualizar_cor_botoes(liga_led_verde[item])

        elif reg[item] == 'o':
            atualizar_cor_botoes(liga_led_azul[item])

# RECOMEÇAR JOGO
def reseta():
    vez = 'x'                                    # VEZ
    velha = 0                                    # NUMERO DE JOGADAS
    reg = [' ',' ',' ',' ',' ',' ',' ',' ',' ']  # TABULEIRO
    return vez, velha, reg

def entrada():
    return leitura_de_botoes()

# SETANDO OS VALORES
vez, velha,reg = reseta()

Ia.renderizar(reg)       # TERMINAL
renderizar_botoes(reg)   # COR DAS PEÇAS

# LOOP DO GAME
while True:    
    # ================== JOGADOR ================== #
    escolha = entrada()
    while escolha == False:
        escolha = entrada()
    escolha = int(escolha)

    # JÁ ESTÁ SENDO USADO
    if reg[escolha] != ' ': 
        continue
    else:
        reg[escolha] = vez
        velha +=1

    Ia.renderizar(reg)       # TERMINAL
    renderizar_botoes(reg)   # COR DAS PEÇAS

    # ALGUÉM GANHOU?
    status = Ia.ganhou(vez,reg,velha)

    if status =='vitória':
        i = input('Parabéns jogador {}'.format(vez))
        vez, velha,reg = reseta()
        continue

    elif status == 'velha':
        i = input('Deu velha pessoal')
        vez, velha,reg = reseta()
        continue

    # TROCAR A VEZ
    vez = Ia.troca_vez(vez)

    # ================ COMPUTADOR ================= #
    reg = Ia.escolher_IA(reg,vez)
    velha +=1

    Ia.renderizar(reg)       # TERMINAL
    renderizar_botoes(reg)   # COR DAS PEÇAS

    status = Ia.ganhou(vez,reg,velha)
    if status =='vitória':
        i = input('Parabéns jogador {}'.format(vez))
        vez, velha,reg = reseta()
        continue

    elif status == 'velha':
        i = input('Deu velha pessoal')
        vez, velha,reg = reseta()
        continue

    # TROCAR A VEZ
    vez = Ia.troca_vez(vez)
