class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    @property
    def nome(self):
        return self._nome

    def dar_like(self):
        self._likes += 1

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def __str__(self):
        return f'{self.nome} - {self.ano} - {self.likes} likes'


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'{self.nome} - {self.ano} - {self.duracao} minutos - {self.likes} likes'


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'{self.nome} - {self.ano} - {self.temporadas} temporadas - {self.likes} likes'


vingadores = Filme('vingadores - guerra Infinita', 2018, 160)
vingadores.dar_like()

atlanta = Serie('atlanta', 2018, 2)
atlanta.dar_like()
atlanta.dar_like()

filmes_e_series = [vingadores, atlanta]

for programas in filmes_e_series:
    print(programas)
