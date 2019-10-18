from tkinter import *
from threading import Thread
from time import sleep
from serial import Serial

conexao = Serial('/dev/ttyACM2', 9600)
conexao.isOpen()

global dic
dic = {'a':"LedVerde1  ligado",
       'b':"LedAzul1   ligado",
       'c':"LedVerde2  ligado",
       'd':"LedAzul2   ligado",
       'e':"LedVerde3  ligado",
       'f':"LedAzul3   ligado",
       'g':"LedVerde4  ligado",
       'h':"LedAzul4   ligado",
       'i':"LedVerde5  ligado",
       'j':"LedAzul5   ligado",
       'k':"LedVerde6  ligado",
       'l':"LedAzul6   ligado",
       'm':"LedVerde7  ligado",
       'n':"LedAzul7   ligado",
       'o':"LedVerde8  ligado",
       'p':"LedAzul8   ligado",
       'q':"LedVerde9  ligado",
       'r':"LedAzul9   ligado",
       'z':"*tudo      deslig"}

tela = Tk()
def clique():
    global dic
    global conexao

    sinal = tkvar.get()
    lbl['text'] = dic[sinal]

    opcoes2 = {'a':b'a',
               'b':b'b',
               'c':b'c',
               'd':b'd',
               'e':b'e',
               'f':b'f',
               'g':b'g',
               'h':b'h',
               'i':b'i',
               'j':b'j',
               'k':b'k',
               'l':b'l',
               'm':b'm',
               'n':b'n',
               'p':b'p',
               'q':b'q',
               'o':b'o',
               'r':b'r',
               'z':b'z'}

    conexao.write(opcoes2[sinal])

lbl = Label(tela, text = 'ENVIAR SINAL')
lbl.grid()

lbl = Label(tela, text = '')
lbl.grid()

tkvar = StringVar(tela)
tkvar.set('a')

opcoes = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','p','q','o','r','z']
poupMenu= OptionMenu(tela, tkvar, *opcoes)
poupMenu.grid()

btn = Button(tela,text='Enviar Sinal',command=clique)
btn.grid()

lbl = Label(tela, text = 'leitura de dados do arduino')
lbl.grid()

txt = Text(tela)
txt.grid()

def limpar_leitura_de_dados():
    txt.delete(0.0,'end')

bt = Button(tela, text='limpar',command=limpar_leitura_de_dados)
bt.grid()

def leitura_de_dados():
    global conexao
    while True:
        sleep(0.1)
        status = conexao.read()
        status = str(status) + '\n'
        txt.insert(END, status)


t = Thread(target=leitura_de_dados)
t.start()

tela.mainloop()
