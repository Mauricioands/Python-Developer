# Utilizar 4 espaços em branco por nível de identação, ou seja, a cada novo bloco adicionamos 4 novos espaços em branco

def sacar(self, valor: float) -> None: # início do bloco do método
    if self.saldo >= valor: # inicio do bloco do if
        self.saldo -=valor
    # fim do bloco do if

# Fim do bloco do método


def sacar(valor):
    saldo = 500
    if saldo >= valor:
        print("Valor sacado!")


def depositar(valor):
    saldo = 500
    saldo += valor


sacar(100)
