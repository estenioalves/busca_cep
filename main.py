from acesso_cep import BuscaEndereco


cep = input("Insira o seu cep:")
objeto_cep = BuscaEndereco(cep)

bairro, cidade, uf = objeto_cep.acessa_via_cep()
print(bairro, cidade, uf)