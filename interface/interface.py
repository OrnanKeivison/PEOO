#Conseitos GUI
'''
• Container: É uma analogia a um container físico e tem como objetivo
organizar e guardar objetos. Nesse caso, os objetos que estamos
armazenando são os widgets;
• Widget: É um componente qualquer na tela, que pode ser um botão, um
ícone, uma caixa de texto, etc.;
• Event Handler: São tratadores de eventos. Por exemplo, ao clicarmos em
um botão para executar uma ação, uma rotina é executada. Essa rotina é
chamada de event handler;
• Event Loop: O event loop verifica constantemente se outro evento foi
acionado. Caso a hipótese seja verdadeira, ele irá executar a rotina
correspondente.
'''

#introdução ao TKinter
'''
• Tkinter é a ferramenta padrão para construção de interfaces gráficas
em python.
• Disponível para: Windows, Linux e Mac.
• Nativo da linguagem Python.
• Documentação: https://tkdocs.com/shipman/
• Referência para comandos:
• https://www.tcl.tk/man/tcl8.6/TkCmd/contents.html
'''
from tkinter import *
from tkinter import ttk

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()