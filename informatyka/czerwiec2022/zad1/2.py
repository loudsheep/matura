def SumaKwCyfr(n):
    suma = 0
    while n != 0:
        cyfra = n % 10
        suma += cyfra * cyfra

        n //= 10
    return suma
