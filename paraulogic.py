#demanem les lletres, ha de començar possant la del centre
lletres = input("Entra les lletres començant per la del centre: ")
lletres_escollides = list(lletres)

#carreguem l'arxiu de paraules
arxiu = open("./paraules.txt", "r", encoding="utf8")
paraula = arxiu.readline()
#eliminem caràcters especials
paraula = ''.join(char for char in paraula if char.isalnum())
#mentre que hi hagin paraules mirem si només té les lletres seleccionades
while paraula:
    #només paraules de 3 o més lletres
    if len(paraula)>2:
        lletres_paraula = list(paraula.lower())
        #eliminem el salt de línia
        lletres_paraula.pop()
        #primer mirem que hi hagi la lletra central
        if lletres_escollides[0] in lletres_paraula:
            #per cada paraula mirem si totes les lletres pertanyen a les entrades
            seleccionada = True
            for lletra in lletres_paraula:
             if not lletra in lletres_escollides: 
                    seleccionada = False
                    break
            if seleccionada:
                print(paraula)
    paraula = arxiu.readline()
    paraula = ''.join(char for char in paraula if char.isalnum())
arxiu.close() 