ficheiro = open("Base Dados2.txt", "r+")

ficheiro.write ("Hello World\n")

print (ficheiro.readline ())

ficheiro.write ("321")

print (ficheiro.readline ())

ficheiro.close ()

