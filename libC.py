


























































































































































































































from datetime import datetime 
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