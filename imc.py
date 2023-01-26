print("\n==============================================")
print("=               Cálculo do IMC               =")
print("==============================================")
print("* Use '.' ao invés de ',' para casas decimais.")

nome = str(input("\nQual seu nome? "))
altura = float(input("\nQual sua altura em metros(m)? "))
peso = float(input("\nQual seu peso atual em quilogramas(kg)? "))

imc = peso / (altura * altura)

# "{:.2f}" junto com o ".format()" formata para que apareça 2 casas decimais.
print("\n" + nome + ", seu IMC atual é: {:.2f}".format(imc) + "\n")

# Depois do primeiro "if' usa-se "elif" para economizar processamento, caso a primeira condição seja verdadeira, ele não processa nada mais abaixo.
if imc < 17:
    print("Você está muito abaixo do peso normal.\n")
elif imc >= 17 and imc <= 18.49:
    print("Você está abaixo do peso normal.\n")
elif imc >= 18.50 and imc <= 24.99:
    print("Você está com o peso normal.\n")
elif imc >= 25 and imc <= 29.99:
    print("Você está acima do peso normal.\n")
elif imc >= 30 and imc <= 34.99:
    print("Você está com obesidade I.\n")
elif imc >= 35 and imc <= 39.99:
    print("Você está com obesidade II, severa.\n")
elif imc > 40:
    print("Você está com obesidade III, mórbida.\n")
# "else" no final é opcional, ele não recebe parametro nenhum, fica "else:".

'''
teste:
1.75m 50kg - if - ok
1.75m 55kg - 1º elif - ok
1.75m 70kg - 2º elif - ok
1.75m 80kg - 3º elif - ok
1.75m 95kg - 4º elif - ok
1.75m 110kg - 5º elif - ok
1.75m 130kg - 6º elif - ok
'''
