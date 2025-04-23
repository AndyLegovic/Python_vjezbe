def jedinstveni_elementi(lista):
    lista.sort()
    for clan in lista:
        if lista.count(clan) > 1:
            lista.remove(clan)
    return(lista)

lista = ["a","a","b","a","c","d","d","d","a"]
print(jedinstveni_elementi(lista))
            
