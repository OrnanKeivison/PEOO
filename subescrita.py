# • Crie um programa em python contendo 3 classes: Integrante_IFRN,
# Professor, Aluno.
# • Integrante_IFRN será a superclasse e Professor e Aluno serão
# sublasses de Integrante_IFRN.
# • As três classes deverão conter o método exibirMensagem. Cada um
# dos métodos deverá exibir uma mensagem conforme a seguir:
# • Integrante_IFRN: “Seja bem vindo(a) ao IFRN!!!”
# • Professor: “Meus alunos são os melhores!!!”
# • Aluno: “Vou estudar pra tirar 100 em POO!!!”

class Integrante_IFRN:
    def __init__(self, matricula, senha):
        self.__matricula = matricula
        self.__senha = senha

    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula
    
    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, senha):
        self.__senha = senha

    def exibirMensagem(self):
        print('Seja bem vindo(a) ao IFRN!!!')

class Professor(Integrante_IFRN):
    def __init__(self, matricula, senha, materia):
        super().__init__(matricula, senha)
        self.__materia = materia

    @property
    def materia(self):
        return self.__materia

    @materia.setter
    def materia(self, materia):
        self.__materia = materia
    
    def exibirMensagem(self):
        print('Meus alunos são os melhores!!!')

class Aluno(Integrante_IFRN):
    def __init__(self, matricula, senha, boletin):
        super().__init__(matricula, senha)
        self.__boletin = boletin

    @property
    def boletin(self):
        return self.__boletin

    @boletin.setter
    def boletin(self, boletin):
        self.__boletin = boletin

    def exibirMensagem(self):
        print('Vou estudar pra tirar 100 em POO!!!')

a = Integrante_IFRN('20221174010009', 'borboletinha')
b = Professor('20221174010010', 'glimpse', 'biologia')
c = Aluno('20221174010012', 'paoComMortadela', 'boletin.csv')

print(a.matricula)
print(a.senha)
a.exibirMensagem()

print(b.matricula)
print(b.senha)
print(b.materia)
b.exibirMensagem()

print(c.matricula)
print(c.senha)
print(c.boletin)
c.exibirMensagem()