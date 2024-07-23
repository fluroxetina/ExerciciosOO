class Produtos:
    def __init__(self, nome, qtd) :
        self.nome = nome
        self.qtd = qtd

class Estoque:
    def __init__(self):
       self.estoque = []

    def AddEstoque(self, ProdAdicinado):
        self.estoque.append(ProdAdicinado)

    def AtualizarEstoque(self, NomeProd):
        for i in self.estoque:
            if i.nome == NomeProd:
                NovaQtd = int(input("Digite nova quantidade "))
                i.qtd = NovaQtd
                print(f"Nova quatidade {i.qtd}")

    def CosultarEstoque(self, NomeProd):
        for i in self.estoque:
            if i.nome == NomeProd:
                print(i.qtd)

    def ListarProd(self):
       for i in self.estoque:
           print(f"Nome: {i.nome}, qtd: {i.qtd}")

prd = Estoque()
while True:
    acao = int(input("1 - Para adiconar\n2 - Para atualizar \n3 - Para consultar\n4 - Para listar\n0 - Para sair \n"))

   
    if acao == 1:
        
        nomePrd = input("Digite o nome do prd ")
        qtd = int(input("Digite a quantidade do prd "))
        prd.AddEstoque(Produtos(nomePrd, qtd))

    elif acao == 2:
        nomePrd = input("Digite o nome do prd ")        
        prd.AtualizarEstoque(nomePrd)

    elif acao == 3:
        nomePrd = input("Digite o nome do prd ")
        prd.CosultarEstoque(nomePrd)

    elif acao == 4:
        prd.ListarProd()

    else:
        break





[turma[nome[nota1,nota2]], turma2[nome[nota1,nota2]]]