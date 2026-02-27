def rimuovilettereaccentate(stringa):
    sost=[('à', 'a'), ('è', 'e'), ('é', 'e'), ('ì', 'i'), ('ò', 'o'), ('ù', 'u'),
        ('À', 'A'), ('È', 'E'), ('É', 'E'), ('Ì', 'I'), ('Ò', 'O'), ('Ù', 'U')]
    for accentata,nonaccentata in sost:
        stringa=stringa.replace(accentata,nonaccentata)
    return stringa
def chiedicomune():
    comuni=["Lignano Sabbiadoro","Salerno","Palermo","Agropoli",
            "Lecce","Pontedera","Stezzano","Boltiere","Almenno San Bartolomeo",
            "Fara Olivana con Sola","San Giorgio a Cremano"]
    i = 1
    for comune in comuni:
        print( " - " + str(comune))
        i = i + 1
    try:
        scelta_comune = input("Quale comune vuoi scegliere? (nome comune): ").strip().capitalize()
        
        if scelta_comune not in comuni:
                raise SyntaxError
        else:
            return scelta_comune
    except: 
         print("<<!>> Errore: Il comune da te scelto non è disponibile!")
def rimuovi_spazi(stringa):
    try:
        if len(stringa)>=2:
            stringa= stringa.replace(" ","")
            return stringa
        else:
            raise SyntaxError
    except:
        print("<<!>> Errore: la stringa inserita è minore di 3 lettere!")
def chiediSesso():
    corretto=False
    while not corretto:
        sesso=input("inserisci il sesso m/f")
        
        if sesso.upper()=="M":
            return "M"
            
        elif sesso.upper()=="F":
            return"F"
        else:print("inserimento del sesso errato")
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
    


def chiediDataNascita():
 
    from datetime import datetime
    errore=True
    while errore:
            data = input("Inserisci la tua data di nascita (gg/mm/aaaa): ")
           
            try:
               
                data_nascita = datetime.strptime(data, "%d/%m/%Y")
                if data_nascita > datetime.now():
                    print("Data non valida, riprovare")
                else:
                    errore=False                
                    return data_nascita
           
            except:
                print("Data non valida, riprovare")
 
def calcolaCodiceComune(comune,lista_comuni):
    codice=lista_comuni[comune]
    return codice
 
def calcolaCodiceAnno(data):
    anno = data.year #estrae l'anno dall'oggetto in formato datetime
    codice= str(anno)[-2:]
    return codice
 
def calcolaCodiceCognome(cognome):
    consonanti = []
    for lettere in cognome:
        if lettere not in "aeiou" and len(consonanti) < 3:
            consonanti.append(lettere)
    if len(consonanti) < 3:
        for lettere in cognome:
            if lettere in "aeiou" and len(consonanti) < 3:
                consonanti.append(lettere)

    codice=consonanti[0] + consonanti[1] + consonanti[2]
    return codice
def CodiceMese(datetime):# in entrata la data di nascita
    meseint=datetime.month #restituisce un valore intero per il mese
    mesi={1: "A",2: "B", 3: "C", 4: "D", 5: "E", 6: "H", 7: "L", 8: "M", 9: "P", 10: "R",11: "S", 12: "T"}
    codice=mesi[meseint]
    return codice
def CodiceNome(stringa):
    cons = {'B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z'}
    vocali = {'A','E','I','O','U'}
    
    stringa = stringa.upper()
    
    consonanti_trovate = []
    for c in stringa:
        if c in cons:
            consonanti_trovate.append(c)
    
    vocali_trovate = []
    for c in stringa:
        if c in vocali:
            vocali_trovate.append(c)
    
    if len(stringa) < 3:
        codice = consonanti_trovate + vocali_trovate
        while len(codice) < 3:
            codice.append('X')
    else:
        if len(consonanti_trovate) >= 4:
            codice = [consonanti_trovate[0], consonanti_trovate[2], consonanti_trovate[3]]
        elif len(consonanti_trovate) == 3:
            codice = consonanti_trovate[:3]
        else:
            codice = consonanti_trovate[:]
            vocali_necessarie = vocali_trovate[:3 - len(codice)]
            codice = codice + vocali_necessarie
            while len(codice) < 3:
                codice.append('X')
    
    risultato = ''
    for c in codice[:3]:
        risultato += c
    
    return risultato
def chiediCognome():
 
    cognome = input("Inserisci il tuo cognome >> ")
    cognome=rimuovilettereaccentate(cognome)
    cognome=rimuovi_spazi(cognome)
    return cognome
            


sesso=chiediSesso()
date=chiediDataNascita
codice_g=calcolaCodiceGiorno(date,sesso)
print(codice_g)

#print("COMUNI")
#comune=chiedicomune()
#print(comune)
#nome=input("nome: ")
#stringa=rimuovi_spazi(nome)   #convalidate
#print(stringa)
#date=datetime(1910,4,12)
#codice=CodiceMese(date)
#print(codice)
#nome=input("Inserisci nome: ").upper().strip()
#codicen=CodiceNome(nome)
#print(codicen)