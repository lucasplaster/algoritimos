import re


def _gerador_digito_verificador(cpf: int) -> str:
    soma1 = sum(int(cpf[i]) * (10-i) for i in range(9))
    digito1 = soma1 % 11

    if digito1 == 0 or digito1 == 1:
        digito1 = 0
    else:
        digito1 = 11 - digito1

    soma2 = sum(int(cpf[i]) * (11-i) for i in range(9)) + digito1 * 2

    digito2 = soma2 % 11

    if digito2 == 0 or digito2 == 1:
        digito2 = 0
    else:
        digito2 = 11 - digito2

    print(f"O CPF completo é: {cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{digito1}{digito2}")
    return str(f"{digito1}{digito2}")


def _verificador_cpf(cpf):

    digito_verificador1, digito_verificador2 = int(cpf[9]), int(cpf[10])
    cpf = cpf[:9]
    
    soma1 = sum(int(cpf[i]) * (10-i) for i in range(9))
    digito1 = soma1 % 11

    if digito1 == 0 or digito1 == 1:
        digito1 = 0
    else:
        digito1 = 11 - digito1

    soma2 = sum(int(cpf[i]) * (11-i) for i in range(9)) + digito1 * 2

    digito2 = soma2 % 11

    if digito2 == 0 or digito2 == 1:
        digito2 = 0
    else:
        digito2 = 11 - digito2

    if digito1 == digito_verificador1 and digito2 == digito_verificador2:
        print(f"O CPF: {cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{digito1}{digito2} é válido")
        return "Válido"
    else:
        print(f"O CPF: {cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{digito1}{digito2} não é válido")
        return "Inválido"




def validador_cpf(cpf: str) -> str:

    cpf = re.sub(r'\D', '', cpf)

    
    numero_digitos = len(cpf)

    if numero_digitos < 9 or numero_digitos > 11:
        return 'Inválido'

    if numero_digitos == 9:
       return _gerador_digito_verificador(cpf)

    if numero_digitos == 11:
        return _verificador_cpf(cpf)
    


if __name__ == '__main__':
    entrada_usuario = input("Entre com o numero do CPF para validar: ")
    resultado = validador_cpf(entrada_usuario)
    print(resultado)