# "Classe" define as caracteristicas e comportamentos de um objeto, porém não conseguimos utilizar diretamente.
# "Objetos" podem ser usados e possuem características e comportamentos definidos na classe


class Cachorro:
    def __init__(self, nome, cor, acordado =True):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def latir(self):
        print("Auauau")

    def dormir(self):
        self.acordado = False
        print("Zzzzzzzzz...")

cao_1 = Cachorro("Toto", "Caramelo", False)
cao_2 = Cachorro("Aquiles", "Preto")

cao_1.latir()
print(cao_2.acordado)
print(cao_2.acordado)