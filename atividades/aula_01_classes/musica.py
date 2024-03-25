#criar uma classe que se chame musica
#deve ter 3 atributos: nome, artista e duração

class Musica:
    nome = ''
    artista = ''
    duracao = 00

lilian = Musica()
lilian.nome = 'Lilian'
lilian.artista = 'Insominium'
lilian.duracao = 4.30

print(vars(lilian))

the_temple_of_hate = Musica()
the_temple_of_hate.nome = 'The temple of hate'
the_temple_of_hate.artista = 'Angra'
the_temple_of_hate.duracao = 5.14

print(vars(the_temple_of_hate))

replica = Musica()
replica.nome = 'Replica'
replica.artista = 'Sonata Arctica'
replica.duracao = 4.55

print(vars(replica))