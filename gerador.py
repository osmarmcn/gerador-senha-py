from tkinter import*
from tkinter import ttk
from PIL import ImageTk, Image

import string
import random


# -------------- cores ---------------
cor_preta = '#444466'
cor_branca = '#feffff'
cor_vermelha = '#f05a43'
cor_cinza = 'darkgray'

# -------------- janela ---------------


janela = Tk()
janela.title('Gerador de senha')
janela.geometry('300x390')
janela.config(bg=cor_branca)

estilo = ttk.Style(janela)
estilo.theme_use('clam')


frame_nav =Frame(janela, width=300, height=60, bg=cor_branca, padx=0, pady=0, relief='flat')
frame_nav.grid(row=0, column=0, sticky=NSEW)

frame_main =Frame(janela, width=300, height=320, bg=cor_preta, padx=0, pady=0, relief='flat')
frame_main.grid(row=1, column=0, columnspan=10, sticky=NSEW)

# -------------- nav ----------------

img = Image.open('password.png')
imagem = img.resize((30, 30), Image.LANCZOS)
imagem = ImageTk.PhotoImage(imagem)


logo = Label(frame_nav, height=60, image=imagem, compound=LEFT, padx=10, relief='flat', anchor='nw', bg=cor_branca)
logo.place(x=3, y=0)

nome = Label(frame_nav, text='Gerador de senhas', width=200, height=40, padx=0, relief='flat', anchor='nw', font=('Ivy 16 bold'), bg=cor_branca, fg=cor_preta)
nome.place(x=56, y=1)

nome = Label(frame_nav, text='', width=300, height=1, padx=0, relief='flat', anchor='nw', font=('Ivy 1'), bg=cor_vermelha, fg=cor_preta)
nome.place(x=0, y=38)

# -------------- function ----------------


def criar_senha():
    alfabeto_maiuscula = string.ascii_uppercase
    alfabeto_minuscula = string.ascii_lowercase
    numeros = '123456789'
    simbolos = '[]{}()*;:/,_-'

    global combinar

    if estado_1.get() == alfabeto_maiuscula:
        combinar = alfabeto_maiuscula

    else:
        pass

    if estado_2.get() == alfabeto_minuscula:
        combinar = combinar + alfabeto_minuscula

    else:
        pass

    if estado_3.get() == numeros:
        combinar = combinar + numeros

    else:
        pass

    if estado_4.get() == simbolos:
        combinar = combinar + simbolos

    else:
        pass

    
    comprimento = int(spin.get())

    

    # combinar = alfabeto_maiuscula + alfabeto_minuscula + numeros + simbolos
    password = "".join(random.sample(combinar, comprimento))
    print(password)





# -------------- main ----------------

senha = Label(frame_main, text='- - - -', width=20, height=3, padx=0, relief='solid', anchor='center', font=('Ivy 12 bold'), bg=cor_branca, fg=cor_preta)
senha.grid(row=0, column=0, columnspan=1, sticky=NSEW, padx=3 , pady=10)


info = Label(frame_main, text='Número total de caracteres ', height=1, padx=0, relief='flat', anchor='nw', font=('Ivy 10 bold'), bg=cor_branca, fg=cor_preta)
info.grid(row=1, column=0, columnspan=2, sticky=NSEW, padx=5 , pady=1)


var = IntVar()
var.set(0)
spin = Spinbox(frame_main, from_=0, to=50, width=5, textvariable=var)
spin.grid(row=2 , column=0, columnspan=2, sticky='nw', padx=5, pady=8)

alfabeto_maiuscula = string.ascii_uppercase
alfabeto_minuscula = string.ascii_lowercase
numeros = '123456789'
simbolos = '[]{}()*;:/,_-'

frame_caract =Frame(frame_main, width=295, height=210, bg=cor_branca, padx=0, pady=0, relief='flat')
frame_caract.grid(row=3, column=0, sticky=NSEW, columnspan=10)

# -------------- main: check ----------------
estado_1 = StringVar()
estado_1.set(False)

valor_1 = Checkbutton(frame_caract, width=1, var=estado_1, onvalue=alfabeto_maiuscula, offvalue='off', relief='flat',bg=cor_branca)
valor_1.grid(row=0 , column=0, sticky='nw', padx=2, pady=5)

info = Label(frame_caract, text='Letras Maiusculas ', height=1, padx=0, relief='flat', anchor='nw', font=('Ivy 10 bold'), bg=cor_branca, fg=cor_preta)
info.grid(row=0, column=1, sticky=NW, padx=2 , pady=5)

estado_2 = StringVar()
estado_2.set(False)

valor_2 = Checkbutton(frame_caract, width=1, var=estado_2, onvalue=alfabeto_maiuscula, offvalue='off', relief='flat',bg=cor_branca)
valor_2.grid(row=1 , column=0, sticky='nw', padx=2, pady=5)

info = Label(frame_caract, text='Letras Minusculas ', height=1, padx=0, relief='flat', anchor='nw', font=('Ivy 10 bold'), bg=cor_branca, fg=cor_preta)
info.grid(row=1, column=1, sticky=NW, padx=2 , pady=5)

estado_3 = StringVar()
estado_3.set(False)

valor_3 = Checkbutton(frame_caract, width=1, var=estado_3, onvalue=alfabeto_maiuscula, offvalue='off', relief='flat',bg=cor_branca)
valor_3.grid(row=2 , column=0, sticky='nw', padx=2, pady=5)

info = Label(frame_caract, text='Símbolos ', height=1, padx=0, relief='flat', anchor='nw', font=('Ivy 10 bold'), bg=cor_branca, fg=cor_preta)
info.grid(row=2, column=1, sticky=NW, padx=2 , pady=5)

estado_4 = StringVar()
estado_4.set(False)

valor_4 = Checkbutton(frame_caract, width=1, var=estado_4, onvalue=alfabeto_maiuscula, offvalue='off', relief='flat',bg=cor_branca)
valor_4.grid(row=3 , column=0, sticky='nw', padx=2, pady=5)

info = Label(frame_caract, text='Caractere ', height=1, padx=0, relief='flat', anchor='nw', font=('Ivy 10 bold'), bg=cor_branca, fg=cor_preta)
info.grid(row=3, column=1, sticky=NW, padx=2 , pady=5)

# -------------- main: botão ----------------

botao = Button(frame_caract, command=criar_senha, text='Criar senha',width=40, height=2, relief='flat',  anchor='center', font=('Ivy 10 bold'), bg=cor_cinza, fg=cor_branca)
botao.grid(row=5, column=0, sticky=NSEW, padx=0 , pady=20, columnspan=5)

copiar = Button(frame_main, text='Copiar',width=7, height=2, relief='raised',  anchor='center', font=('Ivy 10 bold'), bg=cor_branca, fg=cor_preta)
copiar.grid(row=0, column=1, sticky=NSEW, padx=5 , pady=10, columnspan=1)


janela.mainloop()