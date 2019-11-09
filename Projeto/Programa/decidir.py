__author__       =  ' Gabriel Gregório da Silva '
__email__        =  ' gabriel.gregorio.1@outlook.com '
__description__  =  ' Projeto para a Fatec Aberta '
__status__       =  ' Desenvolvido '
__DATE__         =  ' 09/10/2019 '
__version__      =  ' 1.2'

from random import choice
from os import system
class Ia():
    def escolher_IA(reg,vez,velha):

        # QUEM É O OPONENTE
        if vez == "x":
            vez_dele = "o"
        else:
            vez_dele = "x"

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

                print('Só falta um para ganhar')
                return reg

        #  ===========================  IMPEDIR QUE ELE GANHE  ===========================  #
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

                print('Você não irá ganhar de mim')
                return reg

        # =========================== QUEBRA DE JOGADAS =========================== #        
        # Jogou nos cantos
        if ((reg[0] == vez_dele) or (reg[2] == vez_dele) or (reg[6] == vez_dele) or (reg[8] == vez_dele)):

            # Os meios laterais estão vazios
            if ((reg[3] == ' ') or (reg[1] == ' ') or (reg[5] == ' ') or (reg[7] == ' ')):

                # Jogue no meio
                if (reg[4] == ' '):
                   reg[4] = vez

                   print('Quebra de jogadas, meios extremos vazios')
                   return reg

        # Ele marcou no meio, marque nas laterais
        if (reg[4] == vez_dele):
            for item in [0,2,6,8]:
                if (reg[item] == ' '):
                    reg[item] = vez
                    print('Quebra de jogadas, ele marcou no meio, vou nas laterais')
                    return reg
 
        # Ele marcou marcou os dois extremos, marque nos meios laterais.
        if ((reg[0] == vez_dele) and (reg[8] == vez_dele) or (reg[2] == vez_dele) and (reg[6] == vez_dele) ):
            for item in [1,3,5,7]:
                if (reg[item] == ' '):
                    reg[item] = vez
                    print('Quebra de jogada, extremos e meios')
                    return reg

        # No inicio, ele marcou em um dos meios laterais
        if (velha == 1):
            for num in [1,3,5,7]:
                if reg[num] == vez_dele:
                    if reg[4] == ' ':
                        reg[4] = vez
                        return reg
        # Ele marcou dois valores próximos, deixando apenas um extremo livre.
        dic = {tuple([5,7]) : 8,
               tuple([3,7]) : 6,
               tuple([1,3]) : 0,
               tuple([1,5]) : 2}

        for v1 , v2  in dic:
            if ((reg[v1] == vez_dele) and (reg[v2] == vez_dele)): 
                if (reg[ dic[(v1,v2)]] == ' '):
                    reg[ dic[(v1,v2)]] = vez
                    print('Quebra de L')
                    return reg

        # Ele fez um L.
        dic = {tuple([0,5]) : [1,2],
               tuple([1,8]) : [2,5], 
               tuple([2,7]) : [5,8],
               tuple([5,6]) : [7,8],
               tuple([8,3]) : [6,7],
               tuple([7,0]) : [3,6],
               tuple([6,1]) : [3,0],
               tuple([3,2]) : [0,1]}

        for v1 , v2  in dic:

            # Se a formação de L estiver sido feita.
            if (( reg[v1] == vez_dele) and ( reg[v2] == vez_dele )):

                # Se a jogada não tiver sido quebrada
                if ((reg[ dic[(v1,v2)][0]] != vez) and (reg[ dic[(v1,v2)][1]] != vez)):

                    # Tem possibilidade aqui?
                    if (reg[ dic[(v1,v2)][0]] == ' '):
                        reg[ dic[(v1,v2)][0]] = vez
                        return reg

                    # Tem possibilidade aqui?
                    elif ( reg[ dic[(v1,v2)][1]] == ' '):
                        reg[ dic[(v1,v2)][1]] = vez
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

