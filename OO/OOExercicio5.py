class Funcionario:
    def __init__(self, nome, sobrenome, hora_trabalhada, valor_hora) :

        self.nome = nome
        self.sobrenome = sobrenome
        self.hora_trabalhada = hora_trabalhada
        self.valor_hora = valor_hora
        
    def NomeCompleto(self):
        print(f"O nome do usuario é {self.nome} {self.sobrenome}")

    def CalcularSaldo(self):
        salario = self.hora_trabalhada * self.valor_hora
        print(f"Seu salario é igual a de {salario*30}")

    def IncrementarHora(self, valor):
        self.valor_hora = valor



hora_valor = float(input("Digite quanto você recebe por hora trabalhada "))

funcionario1 = Funcionario("Leonardo", "Silva", 8, hora_valor)

funcionario1.IncrementarHora(hora_valor)
funcionario1.NomeCompleto()
funcionario1.CalcularSaldo()