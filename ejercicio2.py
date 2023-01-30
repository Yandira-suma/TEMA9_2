from functools import reduce
lista = [10,11,12,13,14,15,16,17,18,19,20]
def impares(lista):
    return list(filter((lambda x: x % 2 != 0), lista))

def suma_impares(lista):
    return reduce((lambda x, y: x + y), impares(lista))


imp = impares(lista)
suma = suma_impares(imp)
print("lista numeros:", lista)
print("Lista de números impares:", imp)
print("Suma de números impares:", suma)
