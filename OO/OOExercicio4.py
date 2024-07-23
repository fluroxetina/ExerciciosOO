class Conta:
    def __init__(self, nome, cpf, numero, saldo) :
        self.nome = nome
        self.cpf = cpf
        self.numero = numero
        self.saldo = saldo

    def Depositar(self, valordeposito):

        self.saldo += valordeposito
        self.ImprimirSaldo()

    def Sacar(self):
        if self.saldo > 0:
            valor_saque = float(input("Digite o valor que deseja sacar: "))
            if valor_saque > self.saldo:
                print("Saldo insuficiente")
            else:
                self.saldo -= valor_saque
                self.ImprimirSaldo()
        else:
            print("Sem saldo")

    def ImprimirSaldo(self):
        print(f"Seu saldo atual é ingual a {self.saldo}")



conta1 = Conta("Calebe", "23456789098", "345678", 1000)

deposito = float(input("Digite o valor do deposito: "))
conta1.Depositar(deposito)
conta1.Sacar()