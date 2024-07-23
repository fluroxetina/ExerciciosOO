class Livro:
    def __init__(self, nome, autor, editora, pag):
        
        self.nome = nome
        self.autor = autor
        self.editora = editora
        self.pag = pag

    def AlterarEditora(self, novaeditora):
        self.editora = novaeditora
        print(f"Nome da editora atualizado para: {novaeditora}")
    def NumeroPag(self):
        print(f"O livro {self.nome}, possui {self.pag} paginas")


livro1 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", "Editora XYZ", 1000)

NomeNovaEditora = input("Digite o nome da nova editora: ")

livro1.AlterarEditora(NomeNovaEditora)
livro1.NumeroPag()

