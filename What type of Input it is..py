A = input("Insere o que quiseres")
try:
    resultado = int(A)
    print ("É um numero")
except ValueError:
    try:
        resultado = float(A)
        print ("É um float")
    except:
        print ("É um string")
