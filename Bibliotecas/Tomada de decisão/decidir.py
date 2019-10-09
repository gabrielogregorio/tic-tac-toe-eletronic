__author__       =  ' Gabriel Gregório da Silva '
__email__        =  ' gabriel.gregorio.1@outlook.com '
__description__  =  ' Jogo da velha simples em Python 3 '
__status__       =  ' Desenvolvido '
__DATE__         =  ' 07/06/2019 '
__version__      =  ' 1.0 '

from tkinter import *

# Importacao da biblioteca de tempo
import time

# Aleatório para evitar "aprendizados" - implementação futura
from random import randint

# O Computador vai jogar
global computador
computador = "nao"

global qual_e_o_computador
qual_e_o_computador = ""

# Vitorias do jogador x , O
global venceu
venceu = [0,0]

# Jogador da vez
global vez
vez = "x"

# Se tiver 9, deu velha
global velha
velha = 0

# Registra todos os botões
global reg
reg = []

# Inteligencia do computador - o objetivo é ser razoável e não impossível!
def escolher_IA():
    print("\nDeixa eu pensar...")

    # Lista com todos os botoes
    global reg      
    
    # Indica qual jogador esta jogando agora
    global vez
    
    # Indica se o computador irá jogar contra a pessoa ou não
    global computador
    # Apenas para impedir que ele se chame
    computador = "arrumar"

    # **** SE TIVER CHANCE DE GANHAR... *** #
    # pegar as melhores possibilidades
    maior = 0 
    
    # pegar as melhores possibilidades
    lista_melhor = []

    possibilidades = [[0,3,6],[1,4,7],[2,5,8],[0,1,2],[3,4,5],[6,7,8],[6,4,2],[0,4,8]]
    for pos in possibilidades:
        teste = pos
        if (reg[ pos[0]] ["text"].lower()  == "z" or reg[pos[0]]["text"].lower()  == vez)  and (reg[teste[1]]["text"].lower() == "z"  or reg[teste[1]]["text"].lower()  == vez) and (reg[ teste[2]]  ["text"].lower() == "z"  or reg[teste[2]]["text"].lower()  == vez):
            
           c = 0
           
           if (reg[teste[0]] ["text"].lower() == vez ):
               c = c+1            
               
           if (reg[teste[1]]["text"].lower() == vez ):
               c = c+1            
               
           if (reg[teste[2]]["text"].lower() == vez):
               c = c+1

           print(pos,c)
               
           if (c>1):
               print("Eu posso ganhar!")
               lista_melhor.append(pos)

               if reg[ lista_melhor[0][0] ] ["text"] == "z":
                   clique( reg[lista_melhor[0][0]])
                   return 0
            
               elif reg[ lista_melhor[0][1] ] ["text"] == "z":
                   clique( reg[ lista_melhor[0] [1]])
                   return 0
            
               elif reg[ lista_melhor[0][2] ] ["text"] == "z":
                   clique( reg[ lista_melhor[0] [2]])
                   return 0

    # **** IMPEDIR QUE O JOGADOR MARQUE TRÊS CASAS *** #
    # pegar as melhores possibilidades
    maior = 0 
    
    # pegar as melhores possibilidades
    lista_melhor = []

    # Qual ele é?
    print("Minha vez é {}".format(vez))
    if vez.lower() == "x":
        vez_dele = "o"
    else:
        vez_dele = "x"
    
    possibilidades = [[0,3,6],[1,4,7],[2,5,8],[0,1,2],[3,4,5],[6,7,8],[6,4,2],[0,4,8]]
    for pos in possibilidades:
        teste = pos
        print(pos,)
        if (reg[ pos[0]] ["text"].lower()  == "z" or reg[pos[0]]["text"].lower()  == vez_dele)  and (reg[teste[1]]["text"].lower() == "z"  or reg[teste[1]]["text"].lower()  == vez_dele) and (reg[ teste[2]]  ["text"].lower() == "z"  or reg[teste[2]]["text"].lower()  == vez_dele):
            
           c = 0
           if (reg[teste[0]] ["text"].lower() == vez_dele ):
               c = c+1            
               
           if (reg[teste[1]]["text"].lower() == vez_dele ):
               c = c+1            
               
           if (reg[teste[2]]["text"].lower() == vez_dele):
               c = c+1
           print(pos,c)
               
                        
           if (c>1):
               lista_melhor.append(pos)
               print("Você acha que pode ganhar?")

               if reg[ lista_melhor[0][0] ] ["text"] == "z":
                   clique( reg[lista_melhor[0][0]])
                   return 0
            
               elif reg[ lista_melhor[0][1] ] ["text"] == "z":
                   clique( reg[ lista_melhor[0] [1]])
                   return 0
            
               elif reg[ lista_melhor[0][2] ] ["text"] == "z":
                   clique( reg[ lista_melhor[0] [2]])
                   return 0

    # **** JOGAR PARA GANHAR *** #
    # pegar as melhores possibilidades
    maior = 0 
    
    # pegar as melhores possibilidades
    lista_melhores = [] 
    
    possibilidades = [[0,3,6],[1,4,7],[2,5,8],[0,1,2],[3,4,5],[6,7,8],[6,4,2],[0,4,8]]
    for pos in possibilidades:
        teste = pos
        if (reg[ pos[0]] ["text"]  == "z" or reg[pos[0]]["text"]  == vez)  and (reg[teste[1]]    ["text"] == "z"  or reg[teste[1]]["text"]  == vez) and (reg[ teste[2]]  ["text"] == "z"  or reg[teste[2]]["text"]  == vez):
            
           c = 0
           
           if (reg[teste[0]] ["text"] == vez ):
               c = c+1            
               
           if (reg[teste[1]]["text"] == vez ):
               c = c+1            
               
           if (reg[teste[2]]["text"] == vez ):
               c = c+1   
                        
           if (c>=maior):
               lista_melhores.append(pos)
               
    if len(lista_melhores)>1:
        print("Jogar para ganhar!")
        # Presumo que uma dessas tres vai acontecer
        if reg[ lista_melhores[0][0] ] ["text"] == "z":
            clique( reg[ lista_melhores[0] [0]])
            return 0
            
        elif reg[ lista_melhores[0][1] ] ["text"] == "z":
            clique( reg[ lista_melhores[0] [1]])
            return 0
            
        elif reg[ lista_melhores[0][2] ] ["text"] == "z":
            clique( reg[ lista_melhores[0] [2]])
            return 0
        else:
            print("Tem um bug no código aqui <>")
            
    else:
        for t in reg:
            if t["text"] == "z":
                print("A lógica não funciona, qualquer coisa serve!")
                clique(t)
                return 0
            
# Marque os quadrinhos que deu vitória
def marcar_vitoria(ganhador):
    global reg
    
    # Atualização das cores
    reg[ganhador[0]].configure(bg = "white",fg = "black" , activebackground = "white",activeforeground="black")
    reg[ganhador[1]].configure(bg = "white",fg = "black" , activebackground = "white",activeforeground="black")
    reg[ganhador[2]].configure(bg = "white",fg = "black" , activebackground = "white",activeforeground="black")

# Alguem ganhou?
def ganhou(vez,bnt):
    print(vez)

    # Captura qual peça o computador é
    global qual_e_o_computador
    
    # Vitorias do jogador x , O
    global venceu
    
    # Lista com três posições
    ganhador = []

    # Registro com todos os botões
    global reg

    # Deu velha
    global velha

    # Computador está participando ou não?
    global computador

    # possibilidades de vitória nos quadrinhos...
    if reg[0]["text"]  == vez and reg[3]["text"] == vez and reg[6]["text"] == vez:
        ganhador = [0,3,6]
        marcar_vitoria(ganhador)
        
    if reg[1]["text"]  == vez and reg[4]["text"] == vez and reg[7]["text"] == vez:
        ganhador = [1,4,7]
        marcar_vitoria(ganhador)
        
    if reg[2]["text"]  == vez and reg[5]["text"] == vez and reg[8]["text"] == vez:
        ganhador = [2,5,8]
        marcar_vitoria(ganhador)
        
    if reg[0]["text"]  == vez and reg[1]["text"] == vez and reg[2]["text"] == vez:
        ganhador = [0,1,2]
        marcar_vitoria(ganhador)
        
    if reg[3]["text"]  == vez and reg[4]["text"] == vez and reg[5]["text"] == vez:
        ganhador = [3,4,5]
        marcar_vitoria(ganhador)
        
    if reg[6]["text"]  == vez and reg[7]["text"] == vez and reg[8]["text"] == vez:
        ganhador = [6,7,8]
        marcar_vitoria(ganhador)
        
    if reg[6]["text"]  == vez and reg[4]["text"] == vez and reg[2]["text"] == vez:
        ganhador = [6,4,2]
        marcar_vitoria(ganhador)
        
    if reg[0]["text"]  == vez and reg[4]["text"] == vez and reg[8]["text"] == vez:
        ganhador = [0,4,8]
        marcar_vitoria(ganhador)
        
    if velha == 9 and ganhador == []:
        msg = "Deu velha pessoal"
        vitoria(vez,msg)

    #Alguem ganhou? Atualize isso
    if (ganhador != []):
        # Somatória de pontos
        if (vez.lower() == 'x'):
            venceu[0] = venceu[0] +1
            n_vitorias = venceu[0]
        else:
            venceu[1] = venceu[1] +1
            n_vitorias = venceu[1]

        if computador == "sim" or computador == "arrumar":
            # Se o computador ganhar - Texto da mensagem de vitória
            if (vez == qual_e_o_computador):
                msg = "Você perdeu para o computador pela {}° vez".format(n_vitorias)
            else:
                msg = "Você ganhou pela {}° vez !".format(n_vitorias)
        else:
            msg = "Jogador {}, você ganhou pela {}° vez !".format(vez.upper(),n_vitorias)

        print(msg)
        
        # Tela de vitoria
        return vitoria(vez,msg)

# Comemorar vitória ou velha
def vitoria(vez,msg):
    # Atualiza tela
    jogo.update()

    if (msg!="Deu velha pessoal"):
        # Espera 2s, substituir pelo MESSAGE
        time.sleep(1)
    
    # Finalizar o frame jogo
    jogo.grid_forget()
    
    # Atualizar Mensagem ]
    lb["text"]  = msg

    # Avisar que o jogador ganhou
    mensagem.grid(row=1,column=1,sticky=NSEW)

    global computador
    if computador == "sim":
        computador = "arrumar"
    

# Limpar dados recomeçar
def resetar():
    global computador
    if computador == "arrumar": 
        computador = "sim"
        
    global vez
    vez = "x"
    
    global velha
    velha = 0
    
    global reg
    # limpar todas as marcações para o padrão
    for limpar in reg:

        limpar.configure(bg="black",fg="black",activeforeground="black",activebackground="black",text = "z")
        mensagem.grid_forget()
        
    # 'Reconstruir' a tela de jogo    
    jogo.grid(row=1,column=1,sticky=NSEW)

# Clique em algum 'quadro'
def clique(btn):
    btn["fg"] = "white"
    btn["activeforeground"] = "white"
    global vez      # Jogador da vez
    global reg      # Lista com todos os botões
    global velha  # Deu velha?

    # E um clique valido?    
    if btn["text"] == "z":
        # Marcar botao com a vez
        btn["text"] = vez
        
        # aumenta o valor da velha 
        velha = velha + 1

        # Verifica se ganhou
        ganhou(vez , btn)
        
        # Atualizar o jogador da vez
        if vez == "x":
            vez = "o"
        else:
            vez = "x"

        global computador
        if computador == "sim":
            escolher_IA()
        
        elif computador == "arrumar": # O Computador chamou esta definição
            computador = "sim"

# Carrega o game, contra uma pessoa ou contra o computador
def carregar_jogo(bt):
    if (bt["text"] == "Contra uma pessoa"):
        print("Boa sorte a vocês...")
        # Destroe o menu
        menu.grid_forget()

        # Exibe o frame do jogo
        jogo.grid(row=1,column=1,sticky=NSEW)
    else:
        print("Então vamos jogar!")
        # Destroe o menu
        menu.grid_forget()

        # Exibe o frame do jogo
        jogo.grid(row=1,column=1,sticky=NSEW)
        
        global computador
        computador = "sim"

        # É A PESSOA QUE COMEÇA
        # Mensagem personalizada se o computador ganhar
        global vez
        global qual_e_o_computador
        if (vez=="x"):
            qual_e_o_computador = "o"
        else:
            qual_e_o_computador = "x"

# INTERFACES
tela = Tk()
tela.geometry("500x600+100+100")
tela.title("Jogo da velha simples")

# Define o peso para ocupar os espaços livres
tela.rowconfigure(1,weight=1)
tela.grid_columnconfigure(1,weight=1)        

menu = Frame(tela)
menu.rowconfigure(1,weight=1)
menu.grid_columnconfigure(1,weight=1)        

bt = Button(menu,text="Contra uma pessoa",font=("",14), fg = "white",bg = "black",activebackground="white",activeforeground="black" ,relief=FLAT)
bt["command"] = lambda bt=bt: carregar_jogo(bt)
bt.grid(row=1,column=1,sticky=NSEW)

menu.rowconfigure(2,weight=1)
bt = Button(menu,text="Contra o computador",font=("",14), fg = "white",bg = "black",activebackground="white",activeforeground="black" ,relief=FLAT)
bt["command"] = lambda bt=bt: carregar_jogo(bt)
bt.grid(row=2,column=1,sticky=NSEW)

menu.grid(row = 1,column=1,sticky=NSEW)

# -----------------------------------------------------------------

# Frame da jogatina
jogo = Frame(tela)
for x in range(3):
    for y in range(3):
        
       # Define o peso para oculpar os espaços livres
        jogo.rowconfigure(x,weight=1)
        jogo.grid_columnconfigure(y,weight=1)        

        # Propiedades do botao
        btn = Button(jogo,text = "z",font=("",25),fg="black",bg="black",activebackground="black",activeforeground="black")
        btn["command"] = lambda btn=btn: clique(btn)
        btn.grid(row=x,column=y,sticky=NSEW)

        # Registrar todos os botoes de 0 a 8
        reg.append(btn)

# -----------------------------------------------------------------

# Cria o frame para exibir a mensagem de ganhador
mensagem = Frame(tela,bg="black")

# Define o peso para oculpar os espaços livres
mensagem.rowconfigure(1,weight=1)
mensagem.grid_columnconfigure(1,weight=1)        

# Propiedades da label 
lb = Label(mensagem,font=("",15),bg="black",fg="white")
lb.grid(row=1,column=1,sticky=NSEW)

# Propiedades do botao para resetar o jogo
bt = Button(mensagem,text="Recomeçar",font=("",15),bg="black",fg="white",activebackground="white",activeforeground="black",relief=FLAT)
bt["command"] = resetar
bt.grid(row=2,column=1,sticky=NSEW)

# Loop do programa
tela.mainloop()
