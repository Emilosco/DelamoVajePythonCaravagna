class Veicolo:
    def __init__(self, modello, velocita,km):
        self.modello= modello
        self.velocita= velocita
        self.km= km
        

    def CaratteristicheVeicolo(self):
        print("Caratteristiche Veicolo:\n\nModello: {0}\nVelocita massima: {1}\nKm: {2}".format(self.modello, self.velocita,self.km))

class Autobus(Veicolo):
    def __init__(self, modello, velocita, km, capienza, rotta):
        super().__init__(modello,velocita,km)
        self.capienza= capienza
        self.rotta= rotta
    
    def CaratteristicheAutobus(self):
        print("\n\nCaratteristiche Veicolo:\n\nModello: {0}\nVelocita massima: {1}\nKm: {2}\nCapienza: {3}\nRotta: {4}".format(self.modello, self.velocita,self.km,self.capienza, self.rotta))

#esercizio 16.1
veicolo = Veicolo("Alfa Romeo","180 km\h", "250.000 km")
veicolo.CaratteristicheVeicolo()
autobus = Autobus("Alfa Romeo", "70 km\h", "300.000 km", "75 persone", "Piazzale Gioberti>> Via Giulia>> Via Battisti>> Piazza Goldoni>> Largo Irneri")
autobus.CaratteristicheAutobus()
#esercizio 16.2
auto= Auto("Giulia", "180 km\h", "300.000 km", 
