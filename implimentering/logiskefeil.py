assert 10 > 5 #Hvis ikke det stemmer gir den feilmelding, 10 er større en 5 derfor gjør denne ingenting

assert 10 > 20 #10 er ikke større en 20 derfor gir denne fielmdelding

print("Koden er ferdig")

def areal(høyde, bredde):
    return høyde * bredde

def omkrets(høyde, bredde):
    return høyde + høyde + bredde + bredde

assert areal(3,2) == 6
assert areal(3,3) == 9
assert areal(3,4) == 12
    