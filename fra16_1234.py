class Veicolo:
    def __init__(self, modello, velocita, km, capienza):
        self.modello = modello
        self.velocita = velocita
        self.km = km
        self.anno = 2022
        self.capienza = capienza

    def informazioni(self):
        print("Modello: {0}\nVelocità: {1}\nKm: {2}\nPosti: {3}".format(self.modello, self.velocita, self.km, self.capienza))

    def revisionata(self, anno_revisione):
        self.anno_revisione = anno_revisione
        if(self.anno_revisione<self.anno):
            print("Revisione: scaduta")
        elif(self.anno_revisione==self.anno):
            print("Revisione: valida.")
        else:
            print("Hai fatto la revisione in 'Back to the Future'!?")

    def costo(self):
        print("Costo corsa completa: {0}€".format(self.capienza*100))


class Autobus(Veicolo):
    def __init__(self, modello, velocita, km, capienza):
        super().__init__(modello, velocita, km, capienza)
              
    def informazioni(self):
        print("Modello: {0}\nVelocità: {1}\nKm: {2}\nPosti: {3}".format(self.modello, self.velocita, self.km, self.capienza))

    def rotta(self, rotte):
        self.rotte = list(rotte)
        self.n = int(len(rotte))
        
        print("")
        lista = ''
        for i in range(0,self.n):
            if(i==(self.n-1)):
                lista = lista + "{0}".format(self.rotte[i])
            else:
                lista = lista + "{0} >>> ".format(self.rotte[i])

        print(lista)

        print('')
    def costo(self):
        print("Costo corsa completa: {0}€".format(( (self.capienza*100) + (self.capienza*10)  )))


class Auto(Veicolo):
    def __init__(self, modello, velocita, km, capienza):
        super().__init__(modello, velocita, km, capienza)
        


print("\n==============1°=VEICOLO================")
#esercizio16.1
obj_veicolo1 = Veicolo("Lada", "180km/h", "300 000km", 5)
print("Informazioni auto {0}: \n".format(obj_veicolo1.modello))
obj_veicolo1.informazioni()

print("\n==============2°=VEICOLO================")

obj_autobus = Autobus("MAN", "200km/h", "250 000km", 130)
print("Informazioni autobus {0}: \n".format(obj_autobus.modello))

obj_autobus.informazioni()
obj_autobus.revisionata(2019)
obj_autobus.rotta(["Trieste", 'Gorizia', 'Udine', "Venezia"])
obj_autobus.costo()


print("\n==============3°=VEICOLO================")
#esercizio16.2
obj_veicolo2 = Auto('VolksWagen', '210km/h', '124 958km', 5)
print("Informazioni auto {0}: \n".format(obj_veicolo2.modello))
obj_veicolo2.informazioni()
obj_veicolo2.revisionata(2019)

#print("\n=========================================")