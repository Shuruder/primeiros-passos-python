nome = "Gabriel"
idade = 28
profissao = "Programador"
linguagem = "Python"

dados = {
    "nome": "Gabriel",
    "idade": 28,
    "profissao": "Programador",
    "linguagem": "Python"
}

# old style em desuso

print("Meu nome é %s e tenho %d anos" % (nome, idade))

# format

print("Meu nome é {} e tenho {} anos".format(nome,idade))
print("Meu nome é {0} e tenho {1} anos".format(nome,idade))

print("Meu nome é {} e tenho {} anos, sou {} e utilizo {}".format(nome,idade,profissao,linguagem))
print("Meu nome é {0} e tenho {1} anos, sou {2} e utilizo {3}".format(nome,idade,profissao,linguagem))
print("Meu nome é {1} e tenho {3} anos, sou {2} e utilizo {0}".format(linguagem,nome,profissao,idade))

print("Meu nome é {nome} e tenho {idade} anos, sou {profissao} e utilizo {linguagem}".format(**dados))

#acionar direto das variaveis
print(f"Meu nome é {nome} e tenho {idade} anos")