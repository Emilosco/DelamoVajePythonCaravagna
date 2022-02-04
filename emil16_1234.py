class Veicolo:
    def __init__(self, modello, velocita,km):
        self.modello= modello
        self.velocita= velocita
        self.km= km

    def CaratteristicheVeicolo(self):
        print("Caratteristiche Veicolo:\n\nModello: {0}\nVelocita massima: {1}\nKm: {2}".format(self.modello, self.velocita,self.km))

veicolo = Veicolo("Rolls Royce","250 km\h", "250.000 km")
veicolo.CaratteristicheVeicolo()
