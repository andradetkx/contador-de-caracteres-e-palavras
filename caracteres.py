pal = str(input("digite uma frase: "))
contadordepal = 0
contadordecar = 0
for i in range(len(pal.split())):
    contadordepal += 1
for i in range(len(pal.replace(" ", ""))):
    contadordecar +=1
print(f"sao {contadordepal} palavras")
print(f"sao {contadordecar} caracteres")
