__author__       =  ' Gabriel Gregório da Silva '
__email__        =  ' gabriel.gregorio.1@outlook.com '
__description__  =  ' Projeto para a Fatec Aberta '
__status__       =  ' Desenvolvido '
__DATE__         =  ' 09/10/2019 '
__version__      =  ' 1.0 '

from random import choice
from os import system
class Ia():
    def escolher_IA(reg,vez):
        # Possibilidades de vitória
        possibilidades = [[0,3,6],[1,4,7],[2,5,8],[0,1,2],[3,4,5],[6,7,8],[6,4,2],[0,4,8]]

        #  =========================== SE TIVER CHANCE DE GANHAR ===========================  #    
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

                print('ACHO QUE GANHEI')
                return reg

        #  ===========================  IMPEDIR QUE ELE GANHE  ===========================  #
     
        # QUEM É O OPONENTE
        if vez == "x":
            vez_dele = "o"
        else:
            vez_dele = "x"
        
        for pos in possibilidades:
            c = 0
            if ((reg[pos[0]] == ' ' or reg[pos[0]] == vez_dele) and (reg[pos[1]] == ' ' or reg[pos[1]] == vez_dele) and (reg[pos[2]] == ' ' or reg[pos[2]] == vez_dele)):

                if (reg[pos[0]] == vez_dele):
                    c = c+1            
              
                if (reg[pos[1]] == vez_dele):
                    c = c+1            
                   
                if (reg[pos[2]] == vez_dele):
                    c = c+1
                   
            # SÓ FALTA UM PARA ELE GANHAR
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
    def ganhou(vez,reg,velha):
        # Lista com três posições
        ganhador = []


        # possibilidades de vitória nos quadrinhos...
        if reg[0]  == vez and reg[3] == vez and reg[6] == vez:
            ganhador += [0,3,6]
            Ia.marcar_vitoria(ganhador)
            
        if reg[1]  == vez and reg[4] == vez and reg[7] == vez:
            ganhador += [1,4,7]
            Ia.marcar_vitoria(ganhador)
            
        if reg[2]  == vez and reg[5] == vez and reg[8] == vez:
            ganhador += [2,5,8]
            Ia.marcar_vitoria(ganhador)
            
        if reg[0]  == vez and reg[1] == vez and reg[2] == vez:
            ganhador += [0,1,2]
            Ia.marcar_vitoria(ganhador)
            
        if reg[3]  == vez and reg[4] == vez and reg[5] == vez:
            ganhador += [3,4,5]
            Ia.marcar_vitoria(ganhador)
            
        if reg[6]  == vez and reg[7] == vez and reg[8] == vez:
            ganhador += [6,7,8]
            Ia.marcar_vitoria(ganhador)
            
        if reg[6]  == vez and reg[4] == vez and reg[2] == vez:
            ganhador += [6,4,2]
            Ia.marcar_vitoria(ganhador)
            
        if reg[0]  == vez and reg[4] == vez and reg[8] == vez:
            ganhador += [0,4,8]
            Ia.marcar_vitoria(ganhador)
            
        if velha == 9 and ganhador == []:
            msg = "Deu velha pessoal"
            return [Ia.vitoria(vez,msg),ganhador]

        # Alguem ganhou?
        if (ganhador != []):

            msg = "Jogador ",vez, " ganhou"

            # Tela de vitoria
            return [Ia.vitoria(vez,msg),ganhador]

        return [False,ganhador] # 10 não tem significado

    # Comemorar vitória ou velha
    def vitoria(vez,msg):
        if (msg!="Deu velha pessoal"):
            print('Vitória! do ',vez)
            return 'vitória'
        else:
            print('deu velha',vez)
            return 'velha'

    def renderizar(reg):
        print(reg[0:3])
        print(reg[3:6])
        print(reg[6:])

    def troca_vez(vez):
        if vez == 'x':
            return 'o'
        else:
            return 'x'

