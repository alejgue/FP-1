n = 3
Paridad = "Par" if n % 2 == 0 else "impar"
print (Paridad)

nota = 6
if nota < 5:
    print("suspenso")
elif nota < 7:
    print("aprobado")
elif nota < 9:
    print("notable")
else:
    print("sobresaliente")

a, b = 4, 3
menor = a if a < b else b
print(menor)