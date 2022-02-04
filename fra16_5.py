class Potenza:
    def __init__(self, base, esponente):
        self.base = base
        self.esponente = esponente

    def potenza(self):
        return 'Risultato: ' + str(self.base**self.esponente)


potenza1 = Potenza(5, 2)
print(potenza1.potenza())