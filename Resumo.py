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

'''
Agora vamos falar sobre o conceito que representa a ideia de
generalização/especialização em POO que é a HERANÇA
'''
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

'''AGORA VAMOS FALAS SOBRE OS 4 PILARES DA POO'''




