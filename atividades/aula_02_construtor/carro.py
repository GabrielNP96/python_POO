class Carro:
    carros = []
    def __init__(self, fabricante, modelo, ano:int, cor):
        self.fabricante = fabricante
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.carros.append(self)
    def mostrar_carros():
        for carro in Carro.carros:
            print(f'Fabricante: {carro.fabricante}\nModelo: {carro.modelo}\nAno: {carro.ano}\nCor: {carro.cor}')
            print(15 * '-')

uno = Carro('Fiat', 'Uno', 1998, 'Preto')
celta = Carro('Chevrolet', 'Celta', 2000, 'Preto')
marea = Carro('Fiat', 'Marea', 1996, 'Preto')

Carro.mostrar_carros()
