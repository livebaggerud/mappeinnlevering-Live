# Vern mot kjøretidsfeil og logiske feil i programmer

## Kjøretidsfeil

Håndtering av kjøreitdsfeil i python gjøres med nøkkel orden try og except i python.
Python forsøkker å skrive kodeblokken som ligger under `try:`hvis python får en feil melding, vil den kjøre kodeblokken som ligger under `except:`. 

```python
try:
    alder = int(input("Alder:"))
    fødselsår = 2023 - alder
    print(f'Fødselsår: {fødselsår}')
except:
    print("Feil: Alder må være et heltall")

print("Koden forsetter")

```

### Ekseprttips: While-løkke med try-except

```python
while True:
    try:
        alder = int(input("alder:"))
        assert alder >= 0
        break
    except:
        print("alder må være et heltall")

fødselsår = 2023 - alder
print(f'fødselsår: {fødselsår}')
```

## LOGISKE FEIL I PROGRAMMER

For å oppdage logiske feil i python-prgrammer kan vi bruke nøkkelordet `assert` for å forsikre oss om at kode gir korrekt svar.

```python
assert 10 > 5 #Hvis ikke det stemmer gir den feilmelding, 10 er større en 5 derfor gjør denne ingenting
assert 10 > 20 #10 er ikke større en 20 derfor gir denne fielmdelding
```

Eksempler: Test av 

```python
def areal(høyde, bredde):
    return høyde * bredde

def omkrets(høyde, bredde):
    return høyde + høyde + bredde + bredde

assert areal(3,2) == 6
assert areal(3,3) == 9
assert areal(3,4) == 12
```

### Eksperttips: Håndtering av kjøretidsfeil og logisk feil
```python
while True:
    try:
        alder = int(input("alder:"))
        break
    except:
        print("alder må være et heltall")

fødselsår = 2023 - alder
print(f'fødselsår: {fødselsår}')
```