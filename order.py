totale = lambda prezzo,quantita : prezzo*quantita

def totale_semplice (prezzo, quantita):
    return prezzo*quantita

prezzo = 12
quantita = 3

ris = totale(prezzo, quantita)
ris_semplice = totale_semplice(prezzo, quantita)
print(ris)
print(ris_semplice)

