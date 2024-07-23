
class Aluno:
    def __init__(self, nome, ra, listanota):
        self.nome = nome
        self.ra = ra
        self.listanota = listanota

    def Media(self):
        return sum(self.listanota)/len(self.listanota)
    
    def MostrarResultado(self):
        media = self.Media()
        print(media)

        if media >= 7:
            print("Aprovado")

        elif media < 5:
            print("Reprovado")

        else:
            print("Exame")

listanota = []     

for i in range(4):      
    
    notas = float(input("Digite as notas: ")) 
    listanota.append(notas)
   

p = Aluno("kin", "324567", listanota)
p.MostrarResultado()
