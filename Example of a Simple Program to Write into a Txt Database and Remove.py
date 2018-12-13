#AplicaÃ§ao com linha de comandos
#A: Adicionar Pessoa
#B: Ler Ficheiro
#C: Apagar Pessoa
#Q: Exit
 
#Apresentar lista de comandos para o utilizador
#Imprime Mensagem com o nome do comando
 
#O programa sÃ³ termina com o exit
 
 
 
class pessoa:
    def __init__ (self, nome, numero):
        self.nome = nome
        self.numero = numero
       
 
def update ():
    ficheiro = open("BaseDados3.txt", "r")
    ficheiro.seek(0)
    dados = []
    fim = ("Empty")
    while fim != (""):
        fim = ficheiro.readline()
        if fim != (""):
            dados = fim.split (" ")
            pessoa1 = pessoa (dados[0], dados[1])
            global lista_pessoas
            lista_pessoas.append(pessoa1)
    ficheiro.close()
   
lista_pessoas = []
 
mensagem = """
   Para Adicionar Pessoa Insere A
   Para Ler Ficheiro Insere B
   Para apagar pessoa Insere C
   Para sair do Programa insere Q
"""
print (mensagem)
 
 
run = True
while run == True:
   
    wewlad = input("Insere o Comando: ")
   
    if wewlad == ("A"):
        ficheiro = open("BaseDados3.txt", "a")
        print ("Insere a pessoa a adicionar")
        nome = input("Nome: ")
        numero = input("Numero: ")
        nome = nome + (" ") + numero + (" \n")
        ficheiro.write (nome)
        ficheiro.close ()
       
    elif wewlad == ("B"):
        ficheiro = open("BaseDados3.txt", "r+")
        fim = ficheiro.readline()
        while fim != (""):
            fim = fim.replace("\n", "")
            print (fim)
            fim = ficheiro.readline()
        ficheiro.close ()
   
    elif wewlad == ("C"):
        string = ""
        delete = input("Insere o nome a apagar e numero (case sensitive): ")
        delete2 = delete + (" \n")
        ficheiro = open("BaseDados3.txt", "r+")
        linha = ficheiro.readline()
        buffer_list = []
        while linha != (""):
            buffer_list.append(linha)
            linha = ficheiro.readline()
        for a in buffer_list:
            if delete in a or delete2 in a:
                buffer_list.pop(buffer_list.index(a))
        ficheiro.close ()
        ficheiro = open("BaseDados3.txt", "w")
        for a in buffer_list:
            b = buffer_list.index(a)
            string = string + buffer_list[b]
        ficheiro.write (string)
        ficheiro.close
       
 
 
    elif wewlad == ("Q"):
        ficheiro = open("BaseDados3.txt", "a")
        ficheiro.close()
        run = False
