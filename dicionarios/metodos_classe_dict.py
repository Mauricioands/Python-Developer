contatos = {
    "mauricio@hotmail.com": {"nome": "Maurício", "telefone": "3333-2222"},
    "marcos@hotmail.com": {"nome": "Marcos", "telefone": "3333-1111"},
    "marcelo@hotmail.com": {"nome": "Marcelo", "telefone": "3333-2200"},
}

contatos.clear()
print(contatos)



contatos = {
    "mauricio@hotmail.com": {"nome": "Maurício", "telefone": "3333-2222"},
    "marcos@hotmail.com": {"nome": "Marcos", "telefone": "3333-1111"},
    "marcelo@hotmail.com": {"nome": "Marcelo", "telefone": "3333-2200"},
}


copia = contatos.copy()
copia["mauricio@hotmail.com"] = {"nome": "Mau"}
print(contatos["mauricio@hotmail.com"])
print(copia["mauricio@hotmail.com"])

dict.fromkeys(["nome", "telefone"])


dict.fromkeys(["nome", "telefone"], "vazio")


contatos = {
    "mauricio@hotmail.com": {"nome": "Maurício", "telefone": "3333-2222"},
    "marcos@hotmail.com": {"nome": "Marcos", "telefone": "3333-1111"},
    "marcelo@hotmail.com": {"nome": "Marcelo", "telefone": "3333-2200"},
}

contatos.get("chave")
contatos.get("chave", {})
contatos.get("mauricio@hotmail.com")