def numeroPrimo(numero):
    primo=True
    if(type(numero)!=int):
        return None
    elif(numero<-1):
        return None
    elif(numero>1):
        for i in range(2,numero):
            if(numero%i==0):
                primo=False
        return primo

