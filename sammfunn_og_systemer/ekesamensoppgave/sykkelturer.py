fil = open("sykkelturer.csv") #åpner fila
data = fil.read() #leser innholder i fila som en string
linjer = data.split("\n") #splitter innholdet i fila til en liste

holdeplasser = {} # en tom ordbok som sakl fylles med innhold

for linje in linjer[:-1]:
    spilttert_linje = linje.split(",") #splitter hver linje ved komma
    start = spilttert_linje[4]
    if start not in holdeplasser:
        holdeplasser[start]= 1
    else:
        holdeplasser[start]+= 1



sortert = sorted(holdeplasser, key = holdeplasser.get, reverse=True)
print(sortert[0:3])