from datetime import date

class Viaggio:
    def __init__(self, nome_viaggio, giorno_p, mese_p, anno_p, giorno_r, mese_r, anno_r, localita, resort, prezzo, partecipanti, responsabile_viaggio):
        self.nome_viaggio = nome_viaggio
        self.giorno_p = giorno_p
        self.mese_p = mese_p
        self.anno_p = anno_p
        self.giorno_r = giorno_r
        self.mese_r = mese_r
        self.anno_r = anno_r 
        
        self.localita = localita
        self.resort = resort
        self.prezzo = prezzo
        self.partecipanti = partecipanti
        self.responsabile_viaggio = responsabile_viaggio

    def stampa(self):
        print("Informazioni viaggio:\n\nTitolo: {0}\nPartenza: {1}\nRitorno: {2}\nLocalità: {3}\nResort: {4}\nPrezzo: {5}\nPartecipanti: {6}\nResponsabile viaggio: {7}".format(self.nome_viaggio,self.giorno_p,self.giorno_r,self.localita,self.resort,self.prezzo,self.partecipanti,self.responsabile_viaggio))

    def periodo(self):
        self.data_partenza = date(self.giorno_p, self.mese_p, self.anno_p)
        self.data_ritorno = date(self.giorno_r, self.mese_r, self.anno_r)
        delta = self.data_ritorno - self.data_partenza
        print('Giorni di vacanza programmati: {0}'.format( (delta.days) ))


class Vacanza_invernale(Viaggio):
    def __init__(self, nome_viaggio, data_partenza, data_ritorno, localita, resort, prezzo, partecipanti, responsabile_viaggio, skipass, impianti_sciistici):
        super().__init__(nome_viaggio, data_partenza, data_ritorno, localita, resort, prezzo, partecipanti, responsabile_viaggio)
        self.skipass = skipass
        self.impianti_sciistici = impianti_sciistici

    def stampa(self):
        print("Informazioni viaggio:\n\nTitolo: {0}\nPartenza: {1}\nRitorno: {2}\nLocalità: {3}\nResort: {4}\nPrezzo: {5}\nPartecipanti: {6}\nResponsabile viaggio: {7}\n\nPrezzo skipass giornaliero: {8}€\nImpianto sciistico: {9}".format(self.nome_viaggio,self.data_partenza,self.data_ritorno,self.localita,self.resort,self.prezzo,self.partecipanti,self.responsabile_viaggio, self.skipass, self.impianti_sciistici))



class Vacanza_estiva(Viaggio):
    def __init__(self, nome_viaggio, data_partenza, data_ritorno, localita, resort, prezzo, partecipanti, responsabile_viaggio, distanza, escursioni_marine):
        super().__init__(nome_viaggio, data_partenza, data_ritorno, localita, resort, prezzo, partecipanti, responsabile_viaggio) 
        self.distanza = distanza
        self.escursioni_marine = escursioni_marine

print("\n===============1°=VIAGGIO=================")
viaggio1 = Viaggio('Avventura nella giungla', [23,6,2034], [12,7,2034], 'Burundi', 'Uga Buga', '245€', 'Pino, Ugo, Gianfranca', 'Giuliano Caravagno')
viaggio1.stampa()
viaggio1.periodo()

print("\n===============2°=VIAGGIO=================")
viaggio_invernale = Vacanza_invernale('Rotoliamo nella neve!', (15,11,2024), (14,12,2024), 'Triglav', 'Resort Triglav', '670€', 'Bruno, Jože, Svetina', 'Stefano Alberto Sloveno', 56, 'Triglavski smučarski park')
viaggio_invernale.stampa()
viaggio_invernale.periodo()