try:
    alder = int(input("Alder:"))
    fødselsår = 2023 - alder
    print(f'Fødselsår: {fødselsår}')
except:
    print("Feil: Alder må være et heltall")

print("Koden forsetter")

while True:
    try:
        alder = int(input("alder:"))
        break
    except:
        print("alder må være et heltall")

fødselsår = 2023 - alder
print(f'fødselsår: {fødselsår}')