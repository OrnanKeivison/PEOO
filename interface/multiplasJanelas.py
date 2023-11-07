from tkinter import *

def abrir_janela():
    janela2 = Toplevel()
    janela2.title('hello new window')
    txt = Label(janela2, text = 'congratulations')
    txt.pack()
    sair = Button(janela2, text = 'sair', command = janela2.destroy)
    sair.pack()

janela = Tk()

buton = Button(janela, text= 'new window', command = abrir_janela)
buton.pack()
janela.mainloop()