vogais = ["a", "e", "i", "o", "u"]
program = 1

while (program == 1):
    user = 0
    user = input ("mete algo:")



    if len(user) < 2:
        if user in vogais:
            print ("É vogal")
        else:
            try:
                resultado = int(user)
                print ("É um numero")
            except ValueError:
                try:
                    resultado = float(user)
                    print ("É um float")
                except ValueError:
                    print("É consoante")
        program = 0
    else:
        print("Mete só um burro")
    
