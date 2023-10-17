# • Defina uma classe com pelo menos 1 atributo e com os
# getters/setters no modo pythônico
# • Solicite ao usuário digitar os valores para criação de um objeto da
# classe criada
# • Crie um objeto da classe criada usando os valores digitados pelo
# usuário
# • Exiba na tela os valores atributos do objeto criado
# • Altere os atributos do objeto
# • Exiba os valores atributos do objeto criado mais uma vez

class Livro:
    def __init__(self, titulo, qtdPag):
        self.__titulo = titulo
        self.__qtdPag = qtdPag
    
    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo
    
    @property
    def qtdPag(self):
        return self.__qtdPag

    @qtdPag.setter
    def qtdPag(self, qtdPag):
        self.__qtdPag = qtdPag

l = Livro('narnia', 180)

print(l.titulo)
print(l.qtdPag)

l.qtdPag = '100'
l.titulo = 'o sobrinho do mago'

print(l.titulo)
print(l.qtdPag)