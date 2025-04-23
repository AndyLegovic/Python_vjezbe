def izracunaj_prosjek(lista):
    if len(lista) == 0:
        prosjek = 0
    else:
        prosjek = sum(lista) / len(lista)
    return(prosjek)

lista = []
print(izracunaj_prosjek(lista))

