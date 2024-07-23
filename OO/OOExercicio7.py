'''• Cadastrar Turmas:
• O sistema deve permitir que novas turmas sejam adicionadas.
• Cada turma deve ter um nome exclusivo.

• Cadastrar Alunos:
• O sistema deve permitir que alunos sejam adicionados a uma turma específica.
• Ao cadastrar um aluno, devem ser informados seu nome e suas notas.
• As notas devem ser inseridas como uma lista de valores numéricos.

• Atualizar Informações de Alunos:
• O sistema deve permitir a atualização das informações de um aluno existente.
• Deve ser possível alterar o nome do aluno e/ou suas notas.

• Remover Alunos:
• O sistema deve permitir que um aluno seja removido de uma turma específica.

• Visualizar Informações:
• O sistema deve permitir a visualização de todas as turmas cadastradas.
• Para cada turma, deve ser possível visualizar a lista de alunos e suas respectivas
notas.

Estrutura de Dados:
• Cada turma deve conter as seguintes informações:
• Nome da Turma: Identificador exclusivo da turma.
• Lista de Alunos: Cada aluno deve ter um nome e uma lista de notas
associadas.

Implementação:
O sistema será implementado utilizando dicionários em Python e incluirá um menu
interativo para que o usuário (professor) possa escolher a operação desejada. Além disso,
para o usuário acessar o sistema, ele deve possuir um cadastro de login. Esse cadastro é feito
pelo adm e deve ter tratamento para erros na hora de efetuar o login, somente user e senhas
cadastrados devem possuir a permissão, caso contrário, uma mensagem de erro deve ser
apresentada.'''


class Escola:
    def __init__(self) :
        self.turmas = []
    
    def AddTurma(self, turma):
        if turma not in self.turmas:
            self.turmas.append(turma)
            
        else:
            print("Nome de turma já existente")
    def ListarTurmas(self):
        for i in self.turmas:
            for j in i.alunos:
                print(i.nometurma,j.nome,j.notas)


class Turma:
    def __init__(self, nometurma) :
        self.nometurma = nometurma
        self.alunos = []

    def AddAluno(self, aluno):
        self.alunos.append(aluno)

    def AtualizarAluno(self, n):
        
        for i in self.alunos:
            if i.nome == n:
                acao = int(input("1 - Para mudar o nome\n2 - Para mudar as notas\n3 - Para mudar os two \n"))

                if acao == 1:
                    novonome = input("Digite o novo nome ")
                    i.nome = novonome
                
                elif acao == 2:
                    novanota = 0
                    notas = []
                    novanota = input("Digite as novas notas ")

                    while novanota > 0:
                        notas.append(novanota)
                        print("Para sair digite um valor negativo")
                        novanota = input("Digite as novas notas ")
                    
                    i.notas = novanota

                elif acao == 3:
                    novonome = input("Digite o novo nome ")
                    i.nome = novonome
                    
                    novanota = 0
                    notas = []
                    novanota = input("Digite as novas notas ")

                    while novanota > 0:
                        notas.append(novanota)
                        print("Para sair digite um valor negativo")
                        novanota = input("Digite as novas notas ")
                    
                    i.notas = novanota

    def RemoverAluno(self, nomedocabaçopraremover):
        for i in self.alunos:
            if i == nomedocabaçopraremover:
                self.alunos.remove(i)




class Aluno:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas

escola1 = Escola()


while True:

    escolha = input("1 - Para adicionar turma\n2 - Para adicionar aluno\n3 - Para atualizar info de alunos \n4 - Para remover aluno\n5 - Vizualizar turmas\n0 - Para sair ")

    if escolha == "1":
        nameclas = input("Digite o nome da turma ")
        escola1.AddTurma(Turma(nameclas)) 
    
    elif escolha == "2":
        notas = []
        turmadoaluno = input("Digite em qual turma deseja adicionar o aluno: ")
        for i in escola1.turmas:
            if i.nometurmas == turmadoaluno:
                nomealuno = input("Digite o nome do aluno ")
                notaaluno = float(input("Para sair digte uma nota negativa\nDigite as notas do aluno: "))
                notas.append(notaaluno)
                i.AddAluno(Aluno(nomealuno,notas))

    elif escolha == "3":
        nomealuno = input("Digite o nome do aluno para atualizar as informações ")
        for i in escola1.turmas:
            i.AtualizarAluno(nomealuno)

    elif escolha == "4"












turmadoaluno = input("Digite em qual turma deseja adicionar o aluno: ")
for i in escola1.turmas:
    if i.nometurma == turmadoaluno:
        i.AddAluno(Aluno("Rafael",[10,10,10]))
        for j in i.alunos:
            print(j.nome, j.notas)