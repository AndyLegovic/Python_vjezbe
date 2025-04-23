def broj_rjeci(recenica):
    rjeci = 1
    for slovo in recenica:
        if slovo == " ":
            rjeci += 1
        else:
            pass
    return(rjeci)

recenicaa = input("Unesite recenicu")

print(broj_rjeci(recenicaa))
            
