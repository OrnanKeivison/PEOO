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



