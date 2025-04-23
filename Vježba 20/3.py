def je_prost(broj):
    if broj < 4:
        return(False)
    else:
        for i in range(3,broj):
            if broj % i == 0:
                 return(False)
                 break
    return(True)
 
print(je_prost(9))
    
