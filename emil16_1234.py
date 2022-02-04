class Veicolo:
    def __init__(self, modello, velocita,km, anno, revisionata):
        self.modello= modello
        self.velocita= velocita
        self.km= km
        self.anno= 2020
        self.revisionata=2019

        if self.anno < 2021:
            print("\nLa revisione è valida, non preoccuparti!")
        elif self.anno == 2021:
            print("\nLa revisione scadrà quest'anno, controlla quando l'hai fatta!")
        else:
            print("\nLa revisione è scaduta, devi rinovarla!")

    def CaratteristicheVeicolo(self):
        print("Caratteristiche Veicolo:\n\nModello: {0}\nVelocita massima: {1}\nKm: {2}\nAnno corrente: {3}".format(self.modello, self.velocita,self.km, self.anno))

class Autobus(Veicolo):
    def __init__(self, modello, velocita, km, capienza, rotta,revisionata, anno):
        super().__init__(modello,velocita,km,anno, revisionata)
        self.capienza= capienza
        self.rotta= rotta
    
    def CaratteristicheAutobus(self):
        print("\n\nCaratteristiche Autobus:\n\nModello: {0}\nVelocita massima: {1}\nKm: {2}\nCapienza: {3}\nRotta: {4}\nUltima Revisione: {5} \nAnno corrente: {6}".format(self.modello, self.velocita,self.km,self.capienza, self.rotta,self.revisionata, self.anno))
    
class Auto(Veicolo):
    def __init__(self, modello, velocita, km, capienza, revisionata, anno):
        super().__init__(modello,velocita,km,anno,revisionata)
        self.capienza= capienza
        

    def CaratteristicheAuto(self):
        print("\n\nCaratteristiche Auto:\n\nModello: {0}\nVelocita massima: {1}\nKm: {2}\nCapienza: {3}\nUltima Revisione: {4}\nAnno corrente: {5}".format(self.modello, self.velocita,self.km,self.capienza,self.revisionata,self.anno))




#esercizio 16.1
veicolo = Veicolo("Alfa Romeo","180 km\h", "250.000 km", "2022","2019")
veicolo.CaratteristicheVeicolo()
autobus = Autobus("Alfa Romeo 110A", "70km\h","300.000 km","75 persone", "Piazzale Gioberti,Via Giulia, Via Battisti,Piazza Goldoni,Largo Irneri", "2019", "duemila e qualcosa")
autobus.CaratteristicheAutobus()
#esercizio 16.2
auto= Auto("Giulia", "180 km\h", "300.000 km","4 persone","2022", "duemila e qualcosa")
auto.CaratteristicheAuto()