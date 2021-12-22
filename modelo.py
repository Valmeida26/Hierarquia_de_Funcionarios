#Este programa printa o nome, quantas temporadas ou duração tem e o ano de lançamento do filme ou serie
#traz tambem uma lista com os filmes e serie e se a serie demolidor está entre elas.

#classe mãe
class Programas :
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0


    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome_novo(self, novo_nome):
        return self._nome == novo_nome.title()

    def __str__(self):
        return f"{self._nome} - {self.ano} - {self._likes}Likes"

    def __getitem__(self, item):
        return self._programa[item]

#classe filho filme
class Filme(Programas):
    def __init__(self, nome, ano, duracao):
            super().__init__(nome,ano)
            self.duracao = duracao

    def __str__(self):
        return f"{self._nome} - {self.ano} - {self.duracao} min - {self._likes} Likes"

#classe filho serie
class Serie(Programas):
    def __init__(self, nome, ano, temporadas):
            super().__init__(nome, ano)
            self.temporadas = temporadas

    def __str__(self):
        return f"{self._nome} - {self.ano} - {self.temporadas} temporadas - {self._likes} Likes"


'''class playlist(list):
    def __init__(self, nome, assistir):
        self.nome = nome
        super().__init__(assistir)'''
class playlist:
    def __init__(self, nome, programa):
        self.nome = nome
        self._programa = programa

    #Este @property permite acessar a lista em programa
    @property
    def listagem(self):
        return self._programa
    #Este @property permite acessar o tamanho

    def __len__(self):
        return len(self._programa)

#variavel responsável por guardar as informações nome, ano e duração do fime vingadores
vingadores = Filme('vingadores - end game', 2012, 160)

#variavel responsável por guardar as informações nome, ano e duração da serie dexter
dexter = Serie('dexter', 2009, 7)

#variavel responsável por guardar as informações nome, ano e duração do fime Armagedon
armagedon = Filme('armagedon', 2005, 140)

#variavel responsável por guardar as informações nome, ano e duração da serie demolidor
demolidor = Serie('demolidor', 2015, 5)


#LIKES
vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()
dexter.dar_likes()
dexter.dar_likes()
armagedon.dar_likes()
armagedon.dar_likes()
armagedon.dar_likes()
demolidor.dar_likes()
demolidor.dar_likes()



filmes_e_series = [vingadores, dexter, armagedon, demolidor]
playlist_fim_de_semana = playlist("Fim de Semana", filmes_e_series)
print("TELA DA LISTA DE FILMES_E_SERIES\n")
print(f"O tamanho da playlist é: {len (playlist_fim_de_semana.listagem)}")
for programa in playlist_fim_de_semana.listagem:
    print(programa)
print(f"O filme ou série Demolidor está na playlist? {demolidor in playlist_fim_de_semana.listagem} ")

print(len(playlist_fim_de_semana))

'''
#este comando abaixo faz o seguinte: cria a variavel detalhes onde "programa.duracao" é a duração do programa que só
#será executado caso o if seja verdadeiro "se programa conter duracao" ele printa na tela o tempo da duração, se não
#ele printa as temporadas referente a serie. (O HASATTR é um comando para fazer if em uma mesma linha)
filmes_e_series = [vingadores, dexter]
print("TELA DA LISTA DE FILMES_E_SERIES")
for programa in filmes_e_series:
    detalhes = programa.duracao if hasattr(programa, "duracao") else programa.temporadas
    print(f"{programa.nome} - {programa.likes}")
'''

