class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print("inicializando a classe...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __del__(self):
        print("Removendo a instância da classe")

    def falar(self):
        print("Au au au")

c1 = Cachorro("Totó", "Caramelo")
c1.falar()