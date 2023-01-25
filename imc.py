print("\n==============================")
print("=       Cálculo do IMC       =")
print("==============================")

nome = str(input("\nQual seu nome? "))
altura = float(input("\nQual sua altura em metros(m)? "))
peso = float(input("\nQual seu peso atual em quilogramas(kg)? "))

imc  = peso / (altura * altura)

print("\n" + nome + ", seu IMC atual é: {:.2f}".format(imc) + "\n") # "{:.2f}" junto com o ".format()" formata para que apareça 2 casas decimais.

if imc < 17: # Depois do primeiro "if' usa-se "elif" para economizar processamento, caso a primeira condição seja verdadeira, ele não processa nada mais abaixo.
    print("Você está muito abaixo do peso normal.")
elif imc == 17 and imc <= 18.49:
    print("Você está abaixo do peso normal.")
elif imc == 18.50 and imc <= 24.99:
    print("Você está com o peso normal.")
elif imc == 25 and imc <= 29.99:
    print("Você está acima do peso normal.")
elif imc == 30 and imc <= 34.99:
    print("Você está com obesidade I.")
elif imc == 35 and imc <= 39.99:
    print("Você está com obesidade II, severa.")
elif imc > 40:
    print("Você está com obesidade III, mórbida.")
# "else" no final é opcional, ele não recebe parametro nenhum, fica "else:".
