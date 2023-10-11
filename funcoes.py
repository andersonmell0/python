#Funções
# Função que recebe parametro
def minhaFuncao(nome):
    print('oi,',nome)
minhaFuncao('Anderson')

# Função com retorno
def adicionaDois(numero):
    numero +=2
    return numero
resultado = adicionaDois(5)
print(resultado)

def funcaoMultiplosAgumentos(*vars):
    total = 1
    for var in vars:
        total *= var
    return total

teste = funcaoMultiplosAgumentos(5,2)
print(teste)