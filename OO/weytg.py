class Produto:
    def __init__(self, nome, quantidade):
        self.nome = nome
        self.quantidade = quantidade

    def __str__(self):
        return f"{self.nome}: {self.quantidade} unidades"

class Inventário:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def remover_produto(self, nome):
        self.produtos = [p for p in self.produtos if p.nome != nome]

    def imprimir_produtos(self):
        for produto in self.produtos:
            print(produto)

    def ata(self):
        a = input("Qual nome do produto que deseja atualizar: ")
        for i in self.produtos:
            if i == a:
                


# Exemplo de uso
iventárino = Inventário()

# Adicionar produtos
inventário.adicionar_produto(Produto("Maçã", 10))
inventário.adicionar_produto(Produto("Banana", 20))
inventário.adicionar_produto(Produto("Laranja", 15))
inventário.adicionar_produto(Produto("Pêra", 8))
inventário.adicionar_produto(Produto("Uva", 12))

# Imprimir todos os produtos e suas quantidades
inventário.imprimir_produtos()



''''''''''''''''''''''''''''''''''''''''''

class Escola:
    def __init__(self) :
        self.turmas = [turma[nome[nota,nota]]]
    
    def AddTurma(self, turma):
        if turma not in self.turmas:
            self.turmas.append(turma)
            print(self.turmas)
        else:
            print("arthur gay")
    def ListarTurmas(self):
        for i in self.turmas:
            print(i.nometurma)


class Turma:
    def __init__(self, nometurma) :
        self.nometurma = nometurma
        

class CadAluno:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas