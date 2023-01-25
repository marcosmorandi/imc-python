print("\n==============================")
print("=       Cálculo do IMC       =")
print("==============================")

nome = str(input("\nQual seu nome? "))
altura = float(input("\nQual sua altura em metros(m) " + nome +"? "))
peso = float(input("\nQual seu peso atual em quilogramas(kg) " + nome +"? "))

imc  = peso / (altura * altura)

print("\n" + nome + ", seu IMC atual é: {:.2f}".format(imc) + "\n")