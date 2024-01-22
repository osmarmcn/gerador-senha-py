from tkinter import*
from tkinter import ttk
from PIL import ImageTk, Image


# -------------- cores ---------------
cor_preta = '#444466'
cor_branca = '#feffff'
cor_vermelha = '#f05a43'
cor_cinza = 'darkgray'

# -------------- janela ---------------

janela = Tk()
janela.title('Gerador de senha')
janela.geometry('380x360')
janela.config(bg=cor_branca)

frame_nav =Frame(janela, width=380, height=60, bg=cor_cinza, padx=0, pady=0, relief='flat')
frame_nav.grid(row=0, column=0, sticky=NSEW)

frame_main =Frame(janela, width=280, height=320, bg=cor_preta, padx=0, pady=0, relief='flat')
frame_main.grid(row=1, column=0, columnspan=6, sticky=NSEW)

# -------------- nav ----------------

img = Image.open('password.png')
imagem = img.resize((30, 30), Image.LANCZOS)
imagem = ImageTk.PhotoImage(imagem)


logo = Label(frame_nav, height=60, image=imagem, compound=LEFT, padx=10, relief='flat', anchor='nw', bg=cor_branca)
logo.place(x=2, y=0)

nome = Label(frame_nav, text='Gerador de senhas', width=200, height=40, padx=0, relief='flat', anchor='nw', font=('Ivy 16 bold'), bg=cor_branca, fg=cor_preta)
nome.place(x=36, y=1)

nome = Label(frame_nav, text='', width=380, height=1, padx=0, relief='flat', anchor='nw', font=('Ivy 1'), bg=cor_vermelha, fg=cor_preta)
nome.place(x=0, y=38)

# -------------- main ----------------



estilo = ttk.Style(janela)
estilo.theme_use('clam')



janela.mainloop()