print("Hello World!")

# metodos string 

nome = "gAbRiEl"

print(nome.upper()) # GABRIEL
print(nome.lower()) # gabriel
print(nome.title()) # Gabriel

texto = "    Olá Mundo!  "

print(texto.strip())    # "Olá Mundo!"
print(texto.lstrip())   # "Olá Mundo!  "
print(texto.rstrip())   # "    Olá Mundo!"

menu = "Python"

print("###" + menu + "###")
print(menu.center(10,"#"))  # ##Python##
print(".".join(menu))       # P.y.t.h.o.n