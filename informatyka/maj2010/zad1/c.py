import math

def encode(d, tekst):
    n = math.ceil(math.sqrt(d))

    # zamień puste znaki na _ i dopisz do końca tekstu _ aż długość to d
    while len(tekst) < d:
        tekst += "_"
    tekst = tekst.replace(" ", "_")

    # nie wiem jak to wytłumaczyć, ale to działa
    x = 0
    y = 0
    result = ""
    while True:
        result += tekst[y * n + x]

        y += 1
        if y == n:
            y = 0
            x += 1
        if x == n:
            break
    
    return result

print(encode(64, "BTLLTU_ĘL_EOYPM_ĄPJZLCYNDREOKYLI_ZMFO_ĄGJY_Ó_N_DEWFWGISYSII_ŁEI_"))
