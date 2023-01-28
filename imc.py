print("\n==============================================")
print("=               Cálculo do IMC               =")
print("==============================================")
print('* Use "." ao invés de "," para casas decimais.') # Se for usar aspas duplas ou simples no texto exibido, não use o mesmo tipo no comando.

nome = str(input("\nQual seu nome? "))
altura = float(input("\nQual sua altura em metros(m)? "))
peso = float(input("\nQual seu peso atual em quilogramas(kg)? "))

imc = peso / (altura * altura)

# "{:.2f}" junto com o ".format()" formata para que apareça 2 casas decimais.
print("\n" + nome + ", seu IMC atual é: {:.2f}".format(imc) + "\n")

# Depois do primeiro "if' usa-se "elif" para economizar processamento, caso a primeira condição seja verdadeira, ele não processa nada mais abaixo.
if imc < 17:
    print("Você está muito abaixo do peso normal.\n") # Colocar cor vermelha.
elif imc >= 17 and imc <= 18.49:
    print("Você está abaixo do peso normal.\n") # Colocar cor amarela.
elif imc >= 18.50 and imc <= 24.99:
    print("Você está com o peso normal.\n") # Colocar cor verde.
elif imc >= 25 and imc <= 29.99:
    print("Você está acima do peso normal.\n") # Colocar cor amarela.
elif imc >= 30 and imc <= 34.99:
    print("Você está com obesidade I.\n") # Colocar cor vermelha.
elif imc >= 35 and imc <= 39.99:
    print("Você está com obesidade II, severa.\n") # Colocar cor vermelha.
elif imc > 40:
    print("Você está com obesidade III, mórbida.\n") # Colocar cor vermelha.
# "else" no final é opcional, ele não recebe parametro nenhum, fica "else:".

'''
Testes das condicionais:
1.75m, 50kg = if [ok] - vermelho []
1.75m, 55kg = 1º elif [ok] - amarelo []
1.75m, 70kg = 2º elif [ok] - verde []
1.75m, 80kg = 3º elif [ok] - amarelo []
1.75m, 95kg = 4º elif [ok] - vermelho []
1.75m, 110kg = 5º elif [ok] - vermelho []
1.75m, 130kg = 6º elif [ok] - vermelho []

Cores ANSI escape sequance
\033[0;33;44m
\033[(estilo);(cor do texto);(cor do fundo)m
"\033[" abre, "m" fecha.

Estilos:
0 - Nenhum
1 - Negrito
4 - Sublinhado
7 - Negativo, inverte texto e fundo.

Cor do Texto:
30 - Branco
31 - Vermelho
32 - Verde
33 - Amarelo
34 - Azul
35 - Roxo
36 - Ciano
37 - Cinza

Cor do Fundo:
40 - Branco
41 - Vermelho
42 - Verde
43 - Amarelo
44 - Azul
45 - Roxo
46 - Ciano
47 - Cinza
'''
