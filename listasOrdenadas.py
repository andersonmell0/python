from collections import deque
#Estruturas ordenadas

#PILHA
pilha = [0,1,2,3]
print(pilha)
pilha.append(4)
print(pilha)
pilha.append(5)
print(pilha)

pilha.pop() #sem parametro retira o ultimo elemento
print(pilha)
pilha.append(6)
print(pilha)

#FILAS
#fila = [0,1,2,3]
fila = deque([0,1,2,3])
print(fila)
fila.append(4)
fila.append(5)
print(fila)
fila.popleft()
print(fila)