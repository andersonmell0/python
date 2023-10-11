# Estruturas de Repetição

# While

n = 0
while n < 5:
    n += 1
    print(n)
else:
    print('Sai do while')


# For
for letra in "texto":
    print(letra)

# Range de 0 a 10
for numero in range(11):
    print(numero)
    if numero == 8:
        print("achei 8")


# Range de 5 a 10
for numero in range(5,11):
    print(numero)
    if numero == 8:
        print("achei 8")

# Range com intervalos 0 - 20 de 2 em 2
for numero in range(0,20,2):
    print(numero)