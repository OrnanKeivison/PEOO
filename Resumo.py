#PROGRAMAÇÃO ESTRUTURADA ORIENTADA AO OBJETO

#POO - Paradigma de Programação muito utilizado atualmente (Pyhton, Java, C++, C#, JavaScript, PHP);
#Facilidade de representação do mundo real no mundo computacional;
#Separar o programa em partes; e Reusabilidade de Código.
'''
• Programação Orientada a Objetos 
    • Paradigma de programação baseado em objetos 
    • Objetos executam ações (métodos) e possuem características (atributos)
    • Abstração e encapsulamento das informações
    • Programas mais modularizados 
    • Reutilização de código
'''
# Objetos são instancias de uma classe
# Classes criam categorias de objetos.
# Atributos são características de um objeto
# Métodos são ações que podem ser execultados pelos objetos

# EXEMPLO:
#iniciando a implementação da classe pessoa
class Pessoa: # inicia a classe pessoa
    # o __init__ é um método mágico que é chamado quando se cria um objeto por isso é conhecido como construtor
    # o self serve para referenciar um atributo da instancia
    def __init__(self, nome, idade): #iniciando o construtor
        # declarando os atributos abstraidos de uma pessoa 
        self.nome = nome 
        self.idade = idade
        print('vc acaba de criar uma instancia da classe Pessoa') 
    
    # criando o método comer
    def comer(self):
        print(f'o {self.nome} está comendo...')

    # criando o método crescer
    def crescer(self):
        self.idade = self.idade+1
        return self.idade

#iniciando a aplicação da classe pessoa
#criando um objetos
p1 = Pessoa('ornã', 16)
p2 = Pessoa('Bruna', 16)

p1.comer()
p2.comer()

print(p1.crescer())
print(p2.crescer())
print(p2.crescer())

'''MÉTODOS MÁGICOS'''
#Utilizados para que definir um comportamento específico para uma classe quando determinada operação acontecer
#Geralmente, não são executados pelos mesmos nomes que são utilizados para defini-los

#TOMANDO COMO EXEMPLO UMA MATRIZ 
#não podemos fazer soma ou multiplicação usando * ou +, mas se usarmos os métodos especiais...

class MatrizQuadrada:
    def __init__(self, a11, a12, a21, a22):
        self.a11 = a11
        self.a12 = a12
        self.a21 = a21
        self.a22 = a22

        self.Matriz = [[self.a11, self.a12], [self.a21, self.a22]]

    def __str__(self):
        return f'| {self.a11}  {self.a12} |\n| {self.a21}  {self.a22} |'

    def __add__(self, other):
        if isinstance(other, MatrizQuadrada):
            result = MatrizQuadrada(
                self.a11 + other.a11,
                self.a12 + other.a12,
                self.a21 + other.a21,
                self.a22 + other.a22
            )
            return result
        else:
            raise ValueError("Você só pode somar duas matrizes quadradas.")

    def __mul__(self, other):
        if isinstance(other, MatrizQuadrada):
            result = MatrizQuadrada(
                self.a11 * other.a11 + self.a12 * other.a21,
                self.a11 * other.a12 + self.a12 * other.a22,
                self.a21 * other.a11 + self.a22 * other.a21,
                self.a21 * other.a12 + self.a22 * other.a22
            )
            return result
        else:
            raise ValueError("Você só pode multiplicar duas matrizes quadradas.")

# Exemplo de uso
matriz1 = MatrizQuadrada(1, 2, 3, 4)
matriz2 = MatrizQuadrada(5, 6, 7, 8)

print("Matriz 1:")
print(matriz1)

print("Matriz 2:")
print(matriz2)

soma = matriz1 + matriz2
print("Soma das matrizes:")
print(soma)

produto = matriz1 * matriz2
print("Produto das matrizes:")
print(produto)

#outra coisa que podemos fazer é representar a classe como um dicionário, para isso usamos os seguintes comamdos:
print(vars(matriz1))
print(matriz1.__dict__)

'''AGORA VAMOS FALAS SOBRE OS 4 PILARES DA POO'''

'''Abstração'''
#Este conceito nos permite 'focar' apenas no que nos importa para o código
#por exemplo vamos criar uma classe pessoa, uma pessoa te infinitos atributos e métodos no mundo real mas para o mundo computacional escolhemos apenas o que é do nosso interesse
#uma pessoa pode ter cor, esporte, senha, tipo sanguineo, cpf
#mas para a classe pessoa usaremos apenas senha e cpf

'''Encapsulamento'''
#Encapsulamento é um princípio relacionado a POO que nos orienta a esconder as funcionalidades e funcionamento do nosso ocódigo dentro de pequenas unidades (normalmente métodos).
'''
• Python NÃO TEM modificadores de acesso
• Convenções:
• public: Pode ser usado em qualquer lugar (atributo sem underline)
• protected: Deve ser usado apenas na classe e subclasses _ (um underline)
• private: DEVE ser usado apenas na classe em que foi declarado
__ (dois underlines)'''
#Exemplo:
class Comodo:
    def __init__(self, metragem):
        self.__metragem = metragem # o '__' indica que o método é privado e só pode ser lido na classe com os metodos getters e setters como fizemos a baixo

    @property
    def metragem(self):
        return self.__metragem

    @metragem.setter
    def metragem (self, metragem):
        self.__metragem= metragem

quarto=Comodo("7m2")
print(quarto.metragem)
quarto.metragem="10m2"
print(quarto.metragem)

'''Herança'''
#com a herança podemos criar uma classe mais genérica e espessificar melhor em outras classes 
#chamamos a classe mais genérica de classe Mãe ou Superclasse
#já as classes especícas chamamos de filha ou subclasses e elas herdam atributos e métodos da classe Mãe

#EXEMPLO:
#IMPLEMENTANDO A SUPERCLASSE 
class Animal:
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor
        
    def comer(self):
        print(f'o {self.nome} está comendo...')
    
#IMPLEMENTANDO AS SUBCLASSES
class Gato(Animal):
    def __init__(self, nome, cor, vidas):
        super().__init__(nome, cor)
        self.vidas = vidas
    
    def PerdeuVida(self):
        self.vidas = self.vidas -1
        return 'agora o '+ self.nome +' tem ' + str(self.vidas) + ' vidas.'

class Coelho(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)
    
    def Pular(self):
        print(f'o {self.nome} está pulando')

#iniciando a aplicação das classes 
a = Animal('Gus', 'preto')
g = Gato('Mingau', 'Branco', 7)
c = Coelho('squik', 'marrom')

a.comer()
g.comer()
c.comer()

print(g.PerdeuVida())
c.Pular()

#em pytohon também temos um método que diz se um objeto é uma instancia da classe, por exemplo:
print(isinstance(a, Animal))
print(isinstance(g, Animal))
print(isinstance(c, Animal))
print(isinstance(g, Gato))
print(isinstance(g, Coelho))
print(isinstance(c, Gato))
print(isinstance(c, Coelho))

'''Polimorfismo'''
#Polimorfismo é a característica única de linguagens orientadas a objetos que permite que diferentes objetos respondam a mesma mensagem cada um a sua maneira.
#Exemplo:
class Vaca:
    def __init__(self, nome):
        self.nome = nome

    def emitirSom(self):
        print(f'o {self.nome} está mugindo')

class Cachorro:
    def __init__(self, nome):
        self.nome = nome

    def emitirSom(self):
        print(f'o {self.nome} está latindo')

v = Vaca('maribel')
c = Cachorro('luke')

v.emitirSom()
c.emitirSom()


'''
SOBRESCRITA
• Sobrescrita é a possibilita de rescrever métodos com o mesmo nome em classes filhas.
• Sobrescrita existe quando há relação de herança entre as classes.
• Sobrescrita permite especializar os métodos herdados das superclasses, alterando o seu comportamento nas subclasses por um comportamento mais específico.
'''
#EXEMPLO:

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





