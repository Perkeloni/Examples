import time

tempo =int (input("Insere o tempo a contar"))


while tempo > 0:
    print ("Falta %d" % tempo)
    time.sleep (1)
    tempo = tempo - 1
print ("Acabou tempo")
