

def add_new ():
    var_2 = True
    notas = []
    nome = input("Nome")
    idade = int(input("Idade"))
    ano = int(input("Ano"))
    
    while var_2 == True:
        try:
            var_1 = int(input("Insere as notas do aluno, quando acabar inserir N"))
            notas.append (var_1)
        except ValueError:
            var_2 = False
        

        
    turma = input ("Insere turma")
    return [nome, idade, ano, notas, turma]


class aluno:
    def __init__ (self, dados):
        self.nome = dados[0]
        self.idade = dados[1]
        self.ano = dados[2]
        self.notas = dados[3]
        self.turma = dados[4]
        self.media = None



correr = True

while correr == True:
    escolha = input("Queres Inserir Novo Aluno? Y/N: ")
    if ("Y") in escolha:
        entry = add_new()
        entry = aluno
    escolha = input("Queres calcular a media dum aluno? Y/N: ")
        














'''
class aluno:
    def __init__ (self, nome, idade, ano) :
        self.nome = nome
        self.idade = None
        self.ano = None
        self.media = None

    def calcmedia (self, lista):
        self.lista = lista
        self.media = sum(lista)/len(lista)
        self.media = round(self.media)
        print ("O aluno %s teve a media %d" % (self.nome,  self.media))

class turma:
    def __init__ (self, lista):
        self.lista = lista
           
    def calcmedia (self):
        medias = []
        
        for a in (self.lista):      
            medias.append (a.media)
            self.media = sum(medias)/len(medias)
            self.media = round(self.media)
            
        print ("Media da turma é %d" % self.media)

    def nomes (self):
        
        nomes = []
        for a in (self.lista):
            nomes.append (a.nome)
        print (nomes)
            

colega1 = aluno ("Rui", 80, 4,)
colega1.calcmedia ([10, 15, 12, 10, 19, 5])


colega2 = aluno ("Jorge", 9999, 1934,)
colega2.calcmedia ([2, 12, 4, 3, 8, 5])


turma1 = turma (lista_alunos)
turma1.calcmedia ()
turma1.nomes ()
'''


'''
class aluno:
    def __init__ (self, nome, idade, ano) :
        self.nome = nome
        self.idade = None
        self.ano = None
        self.media = None

    def calcmedia (self, lista):
        number = 0
        for a in lista:
            number = a + number
        self.media = round(number/len(lista))
        print(self.media)
            

colega1 = aluno ("Rui", 80, 4,)
colega1.calcmedia ([10, 15, 12, 10, 19, 5])


colega2 = aluno ("Jorge", 9999, 1934,)
colega2.calcmedia ([18, 12, 16, 19, 8, 5])

print(colega1.media)
'''
