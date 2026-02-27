def rimuovilettereaccentate(stringa):
    sost=[('à', 'a'), ('è', 'e'), ('é', 'e'), ('ì', 'i'), ('ò', 'o'), ('ù', 'u'),
        ('À', 'A'), ('È', 'E'), ('É', 'E'), ('Ì', 'I'), ('Ò', 'O'), ('Ù', 'U')]
    for accentata,nonaccentata in sost:
        stringa=stringa.replace(accentata,nonaccentata)
    return stringa
def chiedicomune():
    comuni=["Lignano Sabbiadoro","Salerno","Palermo","Agropoli",
            "Lecce","Pontedera","Bergamo","Boltiere","Almenno San Bartolomeo",
            "Milano","San Giorgio a Cremano"]
    
    
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
        sesso=input("inserisci il sesso m/f ")
        
        if sesso.upper()=="M" or sesso.upper()=="F":
            corretto=True
            return sesso.upper()
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
    import datetime
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
    try:
        codice=lista_comuni[comune]
        return codice
    except:print("QUESTO COMUNE NON è PRESENTE")
 
def calcolaCodiceAnno(data):
    anno = data.year #estrae l'anno dall'oggetto in formato datetime
    codice= str(anno)[-2:]
    return codice
 
def calcolaCodiceCognome(cognome):
    cognome=cognome.upper()
    consonanti = []
    for lettere in cognome:
        if lettere not in "AEIOU" and len(consonanti) < 3:
            consonanti.append(lettere)
    if len(consonanti) < 3:
        for lettere in cognome:
            if lettere in "AEIOU" and len(consonanti) < 3:
                consonanti.append(lettere)

    codice=consonanti[0] + consonanti[1] + consonanti[2]
    return codice
def CodiceMese(datetime):# in entrata la data di nascita
    meseint=datetime.month #restituisce un valore intero per il mese
    mesi={1: "A",2: "B", 3: "C", 4: "D", 5: "E", 6: "H", 7: "L", 8: "M", 9: "P", 10: "R",11: "S", 12: "T"}
    codice=mesi[meseint]
    return codice
def CodiceNome(stringa):
    cons = ['B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z']
    vocali = ['A','E','I','O','U']
    
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
    corretto=False
    while not corretto:
        try:
            cognome = input("Inserisci il tuo cognome (almeno 3 lettere) >> ")
            if len(cognome)<3 or cognome.isalpha()==False:
                raise ValueError
                
            else:
                cognome=rimuovilettereaccentate(cognome)
                cognome=rimuovi_spazi(cognome)
                return cognome
        except:print("ERRORE FORMATO")
            
            


def calcolaprecontrollocod(cognome, nome, data, sesso, comune,lista_comuni):
    try:
        cod_cognome=calcolaCodiceCognome(cognome.upper())
        cod_nome=CodiceNome(nome)
        cod_anno=calcolaCodiceAnno(data)
        cod_mese=CodiceMese(data)
        cod_giorno=calcolaCodiceGiorno(data, sesso)
        cod_comune=calcolaCodiceComune(comune,lista_comuni)
        return (cod_cognome+cod_nome+cod_anno+cod_mese+cod_giorno+cod_comune).upper()
    except:print("ERRORE NEL CALCOLO DEL CODICE FISCALE")


def calcolaCodiceControllo(codice_quasi):
    try:
        codice_quasi=calcolaprecontrollocod(cognome,nome,data,sesso,comune,lista_comuni)
        diz_dispari={"0": 1, "1": 0, "2": 5, "3": 7, "4": 9, "5": 13, "6": 15, "7": 17, "8": 19, "9": 21, "a": 1, "b": 0, "c": 5, "d": 7, "e": 9, "f": 13, "g": 15, "h": 17, "i": 19, "j": 21, "k": 2, "l": 4, "m": 18, "n": 20, "o": 11, "p": 3, "q": 6, "r": 8, "s": 12, "t": 14, "u": 16, "v": 10, "w": 22, "x": 25, "y": 24, "z": 23}
        diz_pari={"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7, "i": 8, "j": 9, "k": 10, "l": 11, "m": 12, "n": 13, "o": 14, "p": 15, "q": 16, "r": 17, "s": 18, "t": 19, "u": 20, "v": 21, "w": 22, "x": 23, "y": 24, "z": 25}
        resto_sin={0:"A", 1: "B", 2: "C", 3: "D",4: "E", 5: "F", 6: "G", 7: "H", 8: "I", 9: "J", 10: "K", 11: "L", 12:"M", 13: "N", 14: "O", 15: "P", 16:"Q",17: "R", 18: "S", 19:"T", 20:"U", 21: "V", 22: "W", 23: "X", 24: "Y",25:"Z"}
        somma=0
        for i in range(len(codice_quasi)):
            if (i+1) %2!=0:
                somma+=diz_dispari[codice_quasi[i].lower()]
            else:
                somma+=diz_pari[codice_quasi[i].lower()]
        resto=somma%26
        return resto_sin[resto]
    except:print("ERRORE NEL CALCOLO DEL CODICE FISCALE TOTALE")


    #PROGRAMMA PRINCIPALE----------------------------------------
corretto=False
while not corretto:
    try:

        cognome =chiediCognome()
        nome=chiedinome()
        data=chiediDataNascita()
        sesso=chiediSesso()
        comune=chiedicomune()
        lista_comuni={"Lignano Sabbiadoro": "G941","Salerno": "H703","Palermo":"G273","Agropoli":"A091","Lecce": "E506","Pontedera": "G843","Bergamo": "A794","Boltiere": "A950","Almenno San Bartolomeo" :"A216","Milano"  : "F205","San Giorgio a Cremano"  : "H894"}
        codice_quasi=calcolaprecontrollocod(cognome, nome, data, sesso, comune,lista_comuni)
        carat_controllo=calcolaCodiceControllo(codice_quasi)   
        codice_finale=codice_quasi+carat_controllo
        print(f" ecco il codice fiscale: {codice_finale}")
        if len(codice_finale)==16:
            corretto=True
    except:print("ERRORE CODICE FISCALE")