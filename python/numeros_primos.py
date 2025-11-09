def numeros_primos(numero_max: int) -> None:
    '''
        Algoritimo simples para encontrar numeros primos
        Busca numeros primos em um intervalo de 0 a numero_max
    '''
    if numero_max < 2:
        print( f"Não tem numeros primos no intervalo.")
        return

    for i in range(2, numero_max+1):
        divisor = 0

        for j in range(1,i+1):
            if i % j == 0:
                divisor += 1

        if divisor == 2:
            print(f"Numero primo encontrado: |   {i}   |")



def numeros_primos_raiz(numero_max: int) -> None:
    '''
    Algoritmo que encontra números primos até numero_max
    usando divisores até a raiz quadrada de numero_max.
    '''
    if numero_max < 2:
        print("Não tem números primos no intervalo.")
        return

    for numero in range(2, numero_max + 1):
        primo = True

        for i in range(2, int(numero ** 0.5) + 1):
            if numero % i == 0:
                primo = False
                break

        if primo:
            print(f"Número primo encontrado: {numero}")



def e_primo(numero: int)-> bool:
    if numero < 2:
        return False

    for i in range(2, int(numero**0.5)+1):
        if numero % i == 0:
            return False
        return True


def crivo_eratostenes(numero_max: int):
    '''
    https://pt.wikipedia.org/wiki/Crivo_de_Erat%C3%B3stenes
    '''
    if numero_max < 2:
        print("Não existem numeros primos no intervalo.")
    
    primos = [True] * (numero_max+1)
    primos[0] = primos[1] = False

    i = 2
    while i * i < numero_max:
        if primos[i]:
            for j in range(i*i, numero_max+1, i):
                primos[j] = False
        i+=1

    return [x for x in range(2, numero_max+1) if primos[x]]



print("\nUsando o algoritimo simples (metodo dos divisores):")
numeros_primos(10)

print("\nUsando metodo da raiz.")
numeros_primos_raiz(10)

print(f"\nUnsando o metodo das raizes para encontrar um numero apenas. {10}")
print(e_primo(10))

print(f"\nUnsando o metodo das raizes para encontrar um numero apenas. {7}")
print(e_primo(7))



print("\nUsando o metodo do crivo de eratostenes.")
for i in crivo_eratostenes(100):
    print(i)
