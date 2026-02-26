import datetime
def chiediSesso():
    corretto=False
    while not corretto:
        sesso=input("inserisci il sesso m/f")
        
        if sesso.lower()=="m":
            return "m"
            
        elif sesso.lower()=="f":
            return"f"
        else:print("inserimento del sesso errato")
            

sesso=chiediSesso()
print(sesso)

date=datetime.datetime(1999,3,11) #!DA TOGLIERE
def calcolaCodiceGiorno(date,sesso):
    g=date.day
    if sesso=="m":
        if g<10:
           # print("ciao")
           g=str(g)
           giorno_codice="0"+g
           return giorno_codice
           #print(giorno_codice)
        else:
            g=str(g)
            #print(g)
           
    elif sesso=="f":
        g+=40
        g=str(g)
        #print(g)
        return g
        

codice_g=calcolaCodiceGiorno(date,sesso)
print(codice_g)