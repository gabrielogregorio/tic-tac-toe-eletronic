from decidir import Ia

def reseta():
    vez = 'x'
    velha = 0
    reg = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    return vez, velha, reg

def entrada():
    escolha = int(input('Escolha uma opção: 0,1,2..,5,6,7,8: '))
    return escolha

vez, velha,reg = reseta()

while True:
    Ia.renderizar(reg)
    
    # ============== JOGADOR ============== #
    escolha = entrada()
    if reg[escolha] != ' ':
        continue
    else:
        reg[escolha] = vez
        velha +=1

    status = Ia.ganhou(vez,reg,velha)
    if status =='vitória' or status == 'velha':
        vez, velha,reg = reseta()
        i = input('você ganhou ou deu velha')
        continue

    # ============== JOGADOR ============== #

    vez = Ia.troca_vez(vez)

    # ============ COMPUTADOR ============= # 
    reg = Ia.escolher_IA(reg,vez)
    velha +=1
    status = Ia.ganhou(vez,reg,velha)

    if status =='vitória' or status == 'velha':
        vez, velha,reg = reseta()
        i = input('computador ganhou ou deu velha')
        continue

    vez = Ia.troca_vez(vez)
    # ============ COMPUTADOR ============= # 

    o = input()