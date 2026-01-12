#Diseña un programa que permita contar vocales en una frase.
frase="Esto es una frase"
vocal=["a","e","i","o","u"]
contador=0
for letra in frase.lower():
    if letra in vocal:
        contador+=1
print(contador)