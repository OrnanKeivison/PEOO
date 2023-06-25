class ControleRemoto:
    
    '''Construtor que inicializa os atributos'''
    def __init__(self, cor="preto", altura="5 cm", profundidade="2 cm", largura="2 cm", canal_atual = 'globo', ligada=False):
        self.cor=cor
        self.altura=altura
        self.profundidade=profundidade 
        self.largura=largura
        self.canal_atual=canal_atual
        self.ligada=ligada

   #Métodos do controle remoto
    def ligar (self):
        self.ligada = True

    def desligar(self):
        self.ligada = False    
    # - mudar canal
    # - mexer no volume
    # - abrir a netflix
    # - ligar a tv
    # - desligar a TV

#Criando novo objeto "controle_love" a partir da classe ControleRemoto
controle_love = ControleRemoto("red", "5 cm", "2 cm", "5 cm", "sbt", False)

#Criando novo objeto "controle_estrela" a partir da classe ControleRemoto
controle_estrela = ControleRemoto('yellow', '8 cm', '3 cm', '8 cm', 'globe', False)

#Criando novo objeto "controle_Ornan" a partir da classe ControleRemoto
controle_Ornan = ControleRemoto('Blue', '3 cm', '3 cm', '3 cm', 'globo', False)

controle_love.ligar()
controle_estrela.ligar()
controle_Ornan.ligar()

#Exibindo atributos do objeto "controle_love"
print ("Cor da TV: ",controle_love.cor)
print ("A TV tem altura de: ",controle_love.altura)
print ("A TV tem profundidade de: ",controle_love.profundidade)
print ("A TV tem largura de: ",controle_love.largura)
print ("A TV esta no canal: ",controle_love.canal_atual)
print ("A TV está ligada? ",controle_love.ligada)

#Exibindo atributos do objeto "controle_estrela"
print ("Cor da TV: ",controle_estrela.cor)
print ("A TV esta no canal: ",controle_estrela.canal_atual)
print ("A TV está ligada? ",controle_estrela.ligada)

#Exibindo atributos do objeto "controle_Ornan"
print ("Cor da TV: ",controle_Ornan.cor)
print ("A TV esta no canal: ",controle_Ornan.canal_atual)
print ("A TV está ligada? ",controle_Ornan.ligada)