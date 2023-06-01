from acesso_cep import BuscaEndereco


cep = input(" Insira o seu cep: ")
objeto_cep = BuscaEndereco(cep)

bairro, logradouro, cidade, uf = objeto_cep.acessa_via_cep()
print(" Bairro: "+bairro+"\n Logradouro: "+logradouro+"\n Cidade: "+cidade+"\n Estado: "+uf+" ")