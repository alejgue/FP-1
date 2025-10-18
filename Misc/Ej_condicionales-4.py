# FizzBuzz
for n in range(1, 51):
    if n % 15 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)

# Primos < 50
primos = []
for n in range(2, 50):
    es_primo = True
    for d in range(2, int(n**0.5) + 1):
        if n % d == 0:
            es_primo = False
            break
    if es_primo:
        primos.append(n)
print(primos)

# Fibonacci <= 500
seq = [0, 1]
while seq[-1] + seq[-2] <= 500:
    seq.append(seq[-1] + seq[-2])
print(seq)