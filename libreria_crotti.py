
def chiediSesso():
    corretto=False
    while not corretto:
        sesso=input("inserisci il sesso m/f")
        
        if sesso.upper()=="M":
            return "M"
            
        elif sesso.upper()=="F":
            return"F"
        else:print("inserimento del sesso errato")
            

sesso=chiediSesso()
def calcolaCodiceGiorno(date,sesso):
    g=date.day
    if sesso=="M":
        if g<10:
           # print("ciao")
           g=str(g)
           giorno_codice="0"+g
           return giorno_codice
           #print(giorno_codice)
        else:
            g=str(g)
            #print(g)
            return g
           
    elif sesso=="F":
        g+=40
        g=str(g)
        #print(g)
        return g
        

codice_g=calcolaCodiceGiorno(date,sesso)
print(codice_g)

def chiedinome():
    corretto=False
    while not corretto:
        try:
            nome_ins=input("inserisci il nome (no numeri e min 2 lettere)")
            nome_ins=rimuovi_spazi(nome_ins)
            nome_ins=rimuovilettereaccentate(nome_ins)
            if nome_ins.isalpha()==True:
                corretto=True
        
                return nome_ins
            else:print("puoi inserire solo lettere")
        
                #print("ciao")
        except:print("ERRORE NEL FORMATO")

