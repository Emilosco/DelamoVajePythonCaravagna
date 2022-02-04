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
        print("Informazioni viaggio:\n\nTitolo: {0}\nPartenza: {1}/{2}/{3}\nRitorno: {4}/{5}/{6}\nLocalità: {7}\nResort: {8}\nPrezzo per persona: {9}€\nPartecipanti: {10}\nResponsabile viaggio: {11}".format(self.nome_viaggio,self.giorno_p,self.mese_p,self.anno_p,self.giorno_r,self.mese_r,self.anno_r,self.localita,self.resort,self.prezzo,self.partecipanti,self.responsabile_viaggio))

    def periodo(self):
        self.data_partenza = date(self.anno_p, self.mese_p, self.giorno_p)
        self.data_ritorno = date(self.anno_r, self.mese_r, self.giorno_r)
        differenza = self.data_ritorno - self.data_partenza
        print('Giorni di vacanza programmati: {0}'.format( (differenza.days) ))

    def guadagno(self):
        spese = (self.prezzo/100)*47
        guadagno = self.prezzo-spese
        print('\nGuadagno: {0}€'.format(guadagno))



class Vacanza_invernale(Viaggio):
    def __init__(self, nome_viaggio, giorno_p, mese_p, anno_p, giorno_r, mese_r, anno_r, localita, resort, prezzo, partecipanti, responsabile_viaggio, skipass, impianti_sciistici):
        super().__init__(nome_viaggio, giorno_p, mese_p, anno_p, giorno_r, mese_r, anno_r, localita, resort, prezzo, partecipanti, responsabile_viaggio)
        self.skipass = skipass
        self.impianti_sciistici = impianti_sciistici
        self.prezzo2 = self.prezzo + ( (self.prezzo/100)*15 )

    def stampa(self):
        print("Informazioni viaggio:\n\nTitolo: {0}\nPartenza: {1}/{2}/{3}\nRitorno: {4}/{5}/{6}\nLocalità: {7}\nResort: {8}\nPrezzo per persona: {9}€\nPartecipanti: {10}\nResponsabile viaggio: {11}\n\nPrezzo skipass giornaliero: {12}€\nImpianto sciistico: {13}\n\nPrezzo con skipass: {14}€".format(self.nome_viaggio,self.giorno_p,self.mese_p,self.anno_p,self.giorno_r,self.mese_r,self.anno_r,self.localita,self.resort,self.prezzo,self.partecipanti,self.responsabile_viaggio, self.skipass, self.impianti_sciistici, self.prezzo2))



class Vacanza_estiva(Viaggio):
    def __init__(self, nome_viaggio, giorno_p, mese_p, anno_p, giorno_r, mese_r, anno_r, localita, resort, prezzo, partecipanti, responsabile_viaggio, distanza, escursioni_marine):
        super().__init__(nome_viaggio, giorno_p, mese_p, anno_p, giorno_r, mese_r, anno_r, localita, resort, prezzo, partecipanti, responsabile_viaggio) 
        self.distanza = distanza
        self.escursioni_marine = escursioni_marine
        self.prezzo2 = self.prezzo + ( (self.prezzo/100)*10 )

    def stampa(self):
        print("Informazioni viaggio:\n\nTitolo: {0}\nPartenza: {1}/{2}/{3}\nRitorno: {4}/{5}/{6}\nLocalità: {7}\nResort: {8}\nPrezzo per persona: {9}€\nPartecipanti: {10}\nResponsabile viaggio: {11}\n\nDistanza resort-spiaggia: {12}m\nEscursioni marine: {13},{14},{15}\n\nPrezzo con escursioni_marine: {16}€".format(self.nome_viaggio,self.giorno_p,self.mese_p,self.anno_p,self.giorno_r,self.mese_r,self.anno_r,self.localita,self.resort,self.prezzo,self.partecipanti,self.responsabile_viaggio,self.distanza,self.escursioni_marine[0], self.escursioni_marine[1],self.escursioni_marine[2],self.prezzo2))





print("\n===============1°=VIAGGIO=================")
viaggio1 = Viaggio('Avventura nella giungla', 23,6,2034, 12,7,2034, 'Burundi', 'Uga Buga', 245, 'Pino, Ugo, Gianfranca', 'Giuliano Caravagno')
viaggio1.stampa()
viaggio1.periodo()
viaggio1.guadagno()

print("\n===============2°=VIAGGIO=================")
viaggio_invernale = Vacanza_invernale('Rotoliamo nella neve!', 15,11,2024, 14,12,2024, 'Triglav', 'Resort Triglav', 670, 'Bruno, Jože, Svetina', 'Stefano Alberto Sloveno', 56, 'Triglavski smučarski park')
viaggio_invernale.stampa()
viaggio_invernale.periodo()
viaggio_invernale.guadagno()

print("\n===============3°=VIAGGIO=================")
viaggio_estivo = Vacanza_estiva('Quanto si suda in Sudan', 23,7,2023, 19,8,2023, 'Sudan', 'Resort Aziz', 130, 'Paolo, Annamaria', 'Aziz Zizà', 400, ['snorkeling', 'surfing', 'danza tribù'])
viaggio_estivo.stampa()
viaggio_estivo.periodo()
viaggio_estivo.guadagno()



def funzione_di_input():

    titolo1 = 'Viaggio invernale', titolo2 = 'Viaggio estivo'
    giorno_p=0,mese_p=0,anno_p=0,giorno_r=0,mese_r=0,anno_r=0
    localita='',resort='',prezzo=0,partecipanti='',responsabile_viaggio=''
    prezzo_skipass=0,impianti_sciistici=''
    distanza=0,escursioni_marine=[]

    print("Scegliere il tipo di vacanza:\n[1] per vacanza invernale\n[2] per vacanza estiva")
    duo = input()

    if(duo==1):
        
        print('Inserire giorno(g), mese(m), anno(aaaa) di partenza:')
        giorno_p = input()
        mese_p = input()
        anno_p = input()
        print('Inserire giorno(g), mese(m), anno(aaaa) di ritorno:')
        giorno_r = input()
        mese_r = input()
        anno_r = input()


    elif(duo==2):
        
        print('Inserire giorno(g), mese(m), anno(aaaa) di partenza:')
        giorno_p = input()
        mese_p = input()
        anno_p = input()
        print('Inserire giorno(g), mese(m), anno(aaaa) di ritorno:')
        giorno_r = input()
        mese_r = input()
        anno_r = input()

    else:
        print("Inserire un numero valido!")
        funzione_di_input()

funzione_di_input()
