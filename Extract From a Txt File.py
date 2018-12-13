file = open("Base Dados Alunos.txt", 'r')

class nomes:

    def __init__ (self, pessoa):
        self.nome = pessoa[0]
        self.idade = pessoa[1]



line = "empty"

esta_a_ler = True

lista_pessoas = []

while esta_a_ler == True:
    line = file.readline()
    if line != "":
        new_line = line.split(" ")
        if "\n" in new_line[-1]:
             new_line[-1] = new_line[-1].strip  ("\n")
        print(new_line)
        new_line = nomes (new_line)
        lista_pessoas.append (new_line)
    
    else:
        esta_a_ler = False

for a in (lista_pessoas):
    print (a.nome)
    


file.close()
