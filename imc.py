print("\n========================")
print("=    Cálculo do IMC    =")
print("========================")

nome = str(input("\nQual seu nome: "))
altura = float(input("\nQual a sua altura em cm: "))
peso = float(input("\nQual seu peso atual em kg: "))

imc = peso / (altura * altura)



# Apagar depois de pronto:
'''
Fórmula: quilos / (altura * altura)

    Resultado            |Situação
    Abaixo de 17         |Muito abaixo do peso
    Entre 17 e 18,49     |Abaixo do peso
    Entre 18,50 e 24,99  |Peso normal
    Entre 25 e 29,99     |Acima do peso
    Entre 30 e 34,99     |Obesidade I
    Entre 35 e 39,99     |Obesidade II (severa)
    Acima de 40          |Obesidade III (mórbida)
'''