# Programa que diz a faixa etária

idade = int(input("Insere a tua idade"))

if idade < 18:
    print("Menor")
elif idade >= 18 and idade <65:
    print("Adulto")
elif idade >= 65:
    print("Idoso")
