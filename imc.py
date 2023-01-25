print("\n==============================")
print("=       Cálculo do IMC       =")
print("==============================")

nome = str(input("\nQual seu nome? "))
altura = float(input("\nQual sua altura " + nome +"? "))
peso = float(input("\nQual seu peso atual " + nome +"? "))

imc  = peso / (altura * altura)

print("\n" + nome + ", seu IMC atual é:", + imc ,"\n")