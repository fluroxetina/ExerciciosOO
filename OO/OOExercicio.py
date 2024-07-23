class Pessoa:
    def __init__(self, nome, idade, endereco) :
        self.nome = nome
        self.idade = idade
        self.endereco = endereco

    def MostrarNome(self):
        print(f"O nome é {self.nome}")

    def AlterarIdade(self): 
        NovaIdade = input("Digite a nova idade ")
        self.idade = NovaIdade
    
    def MostrarEndereco(self):
        print(f"O endereço é {self.endereco}")

    def MostrarInfo(self):
        print(f"O seu nome é {self.nome}, sua idade é {self.idade}, e seu endereço é {self.endereco}")

    
pessoa1 = Pessoa("Arthur", 18, "Tijuca")
pessoa1.MostrarNome()
pessoa1.AlterarIdade()
pessoa1.MostrarEndereco()
pessoa1.MostrarInfo()