class Coleira:
    def __init__(self, marca, cor):
        self.cor = cor
        self.marca = marca

    def MostrarMarca(self):
        print(self.marca)


class Cachorro:
    #construtor
    def __init__(self, cor, raca, tamanho, sexo, coleira):#self usado para referencia do proprio objeto
        self.cor = cor
        self.raca = raca
        self.tamanho = tamanho
        self.sexo = sexo
        self.coleira = coleira


    def MostrarCachorro(self):
        print(f"{self.cor}, {self.raca}, {self.sexo}, {self.tamanho}")

    def MudarCor(self, CorNova):
        self.cor = CorNova

obj_coleira = Coleira("nikedog", "azulada")
obj_pinscher = Cachorro("preto" , "pinscher", 10, "macho", obj_coleira)
obj_pinscher.coleira.MostrarMarca()
obj_pinscher.MostrarCachorro()










# obj_piitbull = Cachorro()