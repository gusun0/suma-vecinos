def countArithmeticMeans(a):
    c = izq = der = 0
    for i in range(len(lista)):
        if(i==0):
            izq=0
            der=lista[i+1]
        elif(i==len(lista)-1):
            izq = lista[i-1]
            der=0
        else:
            izq = lista[i-1]
            der = lista[i+1]
        suma = izq+der
        valor = 2*lista[i]
        if(suma==valor):
            c+=1
    return c
        
lista = [2,4,6,6,3]
print(countArithmeticMeans(lista))
