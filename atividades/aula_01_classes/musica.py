#criar uma classe que se chame musica
#deve ter 3 atributos: nome, artista e duração

class Musica:
    musicas = []
    def __init__(self, nome, artista, duracao: int):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao
        self.musicas.append(self)

    def mostrar_musicas():
        for musica in Musica.musicas:
            print(f'Nome: {musica.nome}\nArtista: {musica.artista}\nDuração: {musica.duracao}')
            print(25 * '-')

lilian = Musica('Lilian', 'Insomninun', 4.29)
first_in_line = Musica('First in line', 'Sonata Artica', 5.22)
caverman = Musica('Caverman', 'Angra', 5.53)

Musica.mostrar_musicas()