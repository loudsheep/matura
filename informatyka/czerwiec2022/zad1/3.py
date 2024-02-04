def SumaKwCyfr(n):
    suma = 0
    while n != 0:
        cyfra = n % 10
        suma += cyfra * cyfra

        n //= 10
    return suma

def in_array(x, arr):
    for i in arr:
        if i == x:
            return True
    return False


def CzyLiczbaNudna(n):
    sumy = []
    while True:
        suma = SumaKwCyfr(n)
        if suma == 1:
            return True
        
        if in_array(suma, sumy):
            return False

        n = suma

        sumy.append(suma)
