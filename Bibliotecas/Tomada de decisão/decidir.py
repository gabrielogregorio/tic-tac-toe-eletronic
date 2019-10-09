__author__       =  ' Gabriel Gregório da Silva '
__email__        =  ' gabriel.gregorio.1@outlook.com '
__description__  =  ' Projeto para a Fatec Aberta '
__status__       =  ' Desenvolvido '
__DATE__         =  ' 09/10/2019 '
__version__      =  ' 1.0 '

from random import choice
from os import system

def escolher_IA(reg):
    global vez

    #  =========================== SE TIVER CHANCE DE GANHAR ===========================  #
    maior = 0 
    
    # pegar as melhores possibilidades
    lista_melhor = []

    possibilidades = [[0,3,6],[1,4,7],[2,5,8],[0,1,2],[3,4,5],[6,7,8],[6,4,2],[0,4,8]]
    for pos in possibilidades:
        c = 0

        if ((reg[pos[0]] == ' ' or reg[pos[0]] == vez) and (reg[pos[1]] == ' ' or reg[pos[1]] == vez) and (reg[pos[2]] == ' ' or reg[pos[2]] == vez)):

            if (reg[pos[0]] == vez):
                c = c+1            
          
            if (reg[pos[1]] == vez):
                c = c+1            
               
            if (reg[pos[2]] == vez):
                c = c+1
               
        # SÓ FALTA UM PARA GANHAR!
        if (c == 2):
            reg[pos[0]] = vez
            reg[pos[1]] = vez
            reg[pos[2]] = vez

            print('Vou ganhar')
            return reg

    #  ===========================  IMPEDIR QUE ELE GANHE  ===========================  #
    # pegar as melhores possibilidades
    maior = 0 
    
    # pegar as melhores possibilidades
    lista_melhor = []

    # Qual ele é?
    if vez == "x":
        vez_dele = "o"
    else:
        vez_dele = "x"
    
    possibilidades = [[0,3,6],[1,4,7],[2,5,8],[0,1,2],[3,4,5],[6,7,8],[6,4,2],[0,4,8]]
    for pos in possibilidades:
        c = 0
        if ((reg[pos[0]] == ' ' or reg[pos[0]] == vez_dele) and (reg[pos[1]] == ' ' or reg[pos[1]] == vez_dele) and (reg[pos[2]] == ' ' or reg[pos[2]] == vez_dele)):


            if (reg[pos[0]] == vez_dele):
                c = c+1            
          
            if (reg[pos[1]] == vez_dele):
                c = c+1            
               
            if (reg[pos[2]] == vez_dele):
                c = c+1
               
        # SÓ FALTA UM PARA EELLEE GANHAR!
        if (c == 2):
            if reg[pos[0]] == ' ': 
                reg[pos[0]] = vez

            elif reg[pos[1]] == ' ': 
                reg[pos[1]] = vez

            elif reg[pos[2]] == ' ': 
                reg[pos[2]] = vez

            print('Impedir que ele ganhe')
            return reg

    # =========================== APENAS JOGAR =========================== #
    possibilidades = [0,1,2,3,4,5,6,7,8]

    # QUAIS POSIÇÕES ESTÃO DISPONÍVEIS?
    pos_disponiveis = []
    for pos in possibilidades:
        if reg[pos] == ' ':
            pos_disponiveis.append(pos)

    reg[choice(pos_disponiveis)] = vez
    print('jogada aleatória!')
    return reg

# Pontos de vitória
def marcar_vitoria(ganhador):
    print('Houve uma vitória em :{},{} e {}'.format(ganhador[0],ganhador[1],ganhador[2]))

# Alguem ganhou?
def ganhou(reg):
    global vez

    # Captura qual peça o computador é
    global qual_e_o_computador
    
    
    # Lista com três posições
    ganhador = []

    # Deu velha ?
    global velha

    # possibilidades de vitória nos quadrinhos...
    if reg[0]  == vez and reg[3] == vez and reg[6] == vez:
        ganhador = [0,3,6]
        marcar_vitoria(ganhador)
        
    if reg[1]  == vez and reg[4] == vez and reg[7] == vez:
        ganhador = [1,4,7]
        marcar_vitoria(ganhador)
        
    if reg[2]  == vez and reg[5] == vez and reg[8] == vez:
        ganhador = [2,5,8]
        marcar_vitoria(ganhador)
        
    if reg[0]  == vez and reg[1] == vez and reg[2] == vez:
        ganhador = [0,1,2]
        marcar_vitoria(ganhador)
        
    if reg[3]  == vez and reg[4] == vez and reg[5] == vez:
        ganhador = [3,4,5]
        marcar_vitoria(ganhador)
        
    if reg[6]  == vez and reg[7] == vez and reg[8] == vez:
        ganhador = [6,7,8]
        marcar_vitoria(ganhador)
        
    if reg[6]  == vez and reg[4] == vez and reg[2] == vez:
        ganhador = [6,4,2]
        marcar_vitoria(ganhador)
        
    if reg[0]  == vez and reg[4] == vez and reg[8] == vez:
        ganhador = [0,4,8]
        marcar_vitoria(ganhador)
        
    if velha == 9 and ganhador == []:
        msg = "Deu velha pessoal"
        vitoria(msg)

    # Alguem ganhou?
    if (ganhador != []):

        msg = "Jogador ",vez, " ganhou"

        # Tela de vitoria
        return vitoria(msg)

# Comemorar vitória ou velha
def vitoria(msg):
    global vez

    if (msg!="Deu velha pessoal"):
        print('Vitória! do ',vez)
    else:
        print('deu velha',vez)

def renderizar(reg):
    system('clear')
    print(reg[0:3])
    print(reg[3:6])
    print(reg[6:])

def troca_vez():
    global vez
    if vez == 'x':
        vez = 'o'
    else:
        vez = 'x'

global velha
global vez
vez = 'x'

velha = 0
reg = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

# loop do programa
while True:
    renderizar(reg)

    # JOGADOR
    escolha = int(input('Escolha uma opção: 0,1,2..,5,6,7,8'))
    reg[escolha] = vez
    ganhou(reg)
    troca_vez()
 
    reg = escolher_IA(reg)
    ganhou(reg)
    troca_vez()

    o = input()