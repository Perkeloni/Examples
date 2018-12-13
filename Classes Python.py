class car:

    def __init__(self, marca, ano_do_carro) :
        self.marca = marca
        self.ano = ano_do_carro
        self.miles = 0
    def definir_milhas(self, milhas):
        print ("Agora tem: %d milhas" % self.miles)
        self.miles = milhas
        print ("Agora tem: %d milhas" % self.miles)
    def buzinar (self):
        print ("Honk do carro: %s" % self.marca)

novo_carro = car("BMW", 2018)
novo_carro.definir_milhas (2000)
novo_carro.buzinar()

novo_carro2 = car("MERCEDES", 1990)
novo_carro2.definir_milhas (100000)
novo_carro2.buzinar ()
