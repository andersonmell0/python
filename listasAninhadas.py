"""
lista = []
for i in range(11):
    lista.append(1*i)
print(lista)
"""
# Pode ser implementado também como
lista = [i*1 for i in range(11)]
print(lista)

matriz1 = [[1,2,3],
          [4,5,6],
          [7,8,9]]
transposta1 = []
for i in range(3):
    linhaTransposta = []
    for linha1 in matriz1:
        linhaTransposta.append(linha1[i])
    transposta1.append(linhaTransposta)
print(matriz1)
print(transposta1)

matriz2 = [[10,20,30],
          [40,50,60],
          [70,80,90]]
transposta2 = [[linha2[i] for linha2 in matriz2] for i in range(3)]
print(matriz2)
print(transposta2)