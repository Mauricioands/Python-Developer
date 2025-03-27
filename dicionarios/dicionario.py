pessoa = dict(nome="Maurício", idade=28)

pessoa["telefone"] = "3333-1234"

print(pessoa)

contatos = {
    "mauricio@hotmail.com": {"nome": "Maurício", "telefone": "3333-2222"},
    "marcos@hotmail.com": {"nome": "Marcos", "telefone": "3333-1111"},
    "marcelo@hotmail.com": {"nome": "Marcelo", "telefone": "3333-2200"},
}

print(contatos["marcos@hotmail.com"])


for chave in contatos:
    print(chave, contatos[chave])

for chave, valor in contatos.items():
    print(chave, valor)