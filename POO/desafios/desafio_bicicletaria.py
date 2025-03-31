class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
# "self" é uma referencia explicita ao objeto

    def buzizar(self):
        print("Plim plim plim...")

    def parar(self):
        print("Parando Bicicleta...")
        print("Bicicleta parada!")

    def correr(self):
        print("Vrummmmmmmmmmm")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

b1 = Bicicleta("Vermelha", "Caloi", 2025, 1500.00)

b1.buzizar()
b1.correr()
b1.parar()

print(b1)

