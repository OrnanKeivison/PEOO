class Livro:
    def __init__(self, titulo , pag , pag_lidas):
        self.titulo = titulo
        self.pag = pag
        self.pag_lidas = pag_lidas
    
    def getTitulo(self):
        return self.titulo
    
    def setTitulo(self, new_titulo):
        self.titulo = new_titulo
    
    def getQtdPaginas(self):
        return self.pag

    def setQtdPaginas(self, new_pag):
        self.pag = new_pag

    def getPaginasLidas(self):
        return self.pag_lidas
    
    def setPaginasLidas(self, new_pag_lidas):
        self.pag_lidas = new_pag_lidas

    def verificarProgresso(self):
        prog = ((100*self.pag_lidas)//self.pag)
        return prog

    
    


narnia = Livro('Nárnia', 110, 10)

narnia.setQtdPaginas(100)

print(narnia.getQtdPaginas())

print(f'vc já leu aproximadamente {narnia.verificarProgresso()}% do livro')
