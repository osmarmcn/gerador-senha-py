from tkinter import*
from tkinter import ttk


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

estilo = ttk.Style(janela)
estilo.theme_use('clam')



janela.mainloop()