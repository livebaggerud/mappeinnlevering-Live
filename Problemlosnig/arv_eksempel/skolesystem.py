class Bruker:
    '''Superklasse for brukere i skolesystemet. Skal ikke brukes direkte. 
    
    Attribute:
        epost: En string med brukers epost
        fornavn: En string med brukes fornavn
        etternavn: En string med brukes etternavn
    '''
    def __init__(self, epost, fornavn, etternavn):
        self._epost = epost
        self._fornavn = fornavn
        self._etternavn = etternavn

    def logg_inn(self):
        print(f'{self._epost} logget inn')

    def logg_ut(self):
        print(f'{self._epost} logget ut')

class Laerer(Bruker):
    '''Superklasse for faglærere og kontaktlærere i skolesystemet og subklasse av Bruker. Skal ikke brukes direkte. 
    
    Attribute:
        epost: En string med brukers epost
        fornavn: En string med brukes fornavn
        etternavn: En string med brukes etternavn
        lønnskonto: En int med brukerens lønnskonto
    '''
    def __init__(self, epost, fornavn, etternavn, lønnskonto):
        super().__init__(epost, fornavn, etternavn)
        self._lønnskonto = lønnskonto



class Faglaerer(Laerer):
    '''Subklasse av Laerer. Brukes direkte

    Innholder liste med lærerens klasser og kompetasne
    
    Attribute:
        epost: En string med brukers epost
        fornavn: En string med brukes fornavn
        etternavn: En string med brukes etternavn
        lønnskonto: En int med burkerens kontonummer
    '''
    def __init__(self,epost, fornavn, etternavn, lønnskonto):
        super().__init__(epost, fornavn, etternavn, lønnskonto)
        self._kompetanse = []
        self._klasser = []

class Kontaktlaerer(Laerer):
    '''Subklasse av Laerer. Brukes direkte
    
    Attribute:
        epost: En string med brukers epost
        fornavn: En string med brukes fornavn
        etternavn: En string med brukes etternavn
        lønnskonto: En int med burkerens kontonummer
        klasse: En str med brukerns kontaktklasse
        trinn: en int med hvilket trinn brukerens kontaktkalsse er
    '''
    def __init__(self, epost, fornavn, etternavn, lønnskonto, klasse, trinn):
        super().__init__(epost, fornavn, etternavn, lønnskonto)
        self._klasse = klasse
        self._trinn = trinn


class Elev(Bruker):
    '''Subklasse av Bruker. Brukes direkte

    Klassen innholder en liste med hvilke fag eleven har 

    Attribute:
        epost: En string med brukers epost
        fornavn: En string med brukes fornavn
        etternavn: En string med brukes etternavn
        trinn: En int med brukerens klassetrinn
        klasse: En string med brukerens klasse
    '''
    def __init__(self, epost, fornavn, etternavn, trinn, klasse):
        super().__init__(epost, fornavn, etternavn)
        self._trinn = trinn
        self._klasse = klasse
        self._fag = []


#Denne burkes for testning, betyr at koden inn i if-setnignen kumn kjøres hvis vi trykker play på denne fila eller kjører den i terminalen
if __name__ == "__main__":
    ravi = Laerer("ravim@viken.no", "David Ravi", "Manikarnika", 970034056654)
    ravi.logg_inn()
    ravi.logg_ut()

    live = Elev("liveba@viken.no","Live", "Baggerud", "vg3", "3STC")
    live.logg_inn()
    live.logg_ut()

