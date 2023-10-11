#Tipos de listas

listaBoleana = [True,False]
listaNumerica = [1,2,3,4,5]
lista5 = listaNumerica[0:2]
listaCopiada = listaBoleana.copy()
lista = [1,2,3,4,500]

print(listaNumerica[0])
print(len(listaNumerica))
print(len(lista5))
print(listaCopiada)

print(lista.index(500)) # mostra o indice do primeiro elemento pesquisado

lista.append(600) # adiciona valor ao final da lista
lista.insert(6,700) # coloca na posição do primeiro numero o segundo valor
listaCopiada += [9,8,7] # concatena uma lista

print(lista[5])
print(lista[6])

print(listaCopiada)

listaCopiada.remove(1) #retira um elemento da lista pelo indice
print(listaCopiada)
listaCopiada.pop(0) #retira um elemento da lista pelo indice
print(listaCopiada)
del listaCopiada[0] #retira um elemento da lista pelo indice
print(listaCopiada)
listaCopiada.sort() #Ordena a lista
print(listaCopiada)
listaCopiada.reverse() #inverte a posição dos itens na lista
print(listaCopiada)