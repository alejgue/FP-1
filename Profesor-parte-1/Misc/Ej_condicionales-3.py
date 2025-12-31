valores = [3, 5, 2, 8]
suma = 0
for x in valores:
    suma += x
suma

texto = "Programación en Python"
vocales = set("aeiouáéíóúAEIOUÁÉÍÓÚ")
conteo = 0
for ch in texto:
    if ch in vocales:
        conteo += 1
conteo

n = 7
for i in range(1, 11):
    print(f"{n} x {i} = {n*i}")