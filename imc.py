print('\n==============================================')
print('=               Cálculo do IMC               =')
print('==============================================')
print('* Use "." ao invés de "," para casas decimais.') # O Python aceita aspas simples ou duplas no "print". Prefiro usas as simples no comando e as duplas caso precise no texto.

nome = str(input('\nQual seu nome? '))
altura = float(input('\nQual sua altura em metros(m)? '))
peso = float(input('\nQual seu peso atual em quilogramas(kg)? '))

imc = peso / (altura * altura)

print('\n' + nome + ', seu IMC atual é: {:.2f}'.format(imc) + '\n')

# Depois do primeiro "if' usa-se "elif" para economizar processamento, caso a primeira condição seja verdadeira, ele não processa nada mais abaixo.
if imc < 17:
    print('\033[1;41mVocê está muito abaixo do peso normal.\033[m\n') # Fundo vermelho, texto em negrito. Fechar o escape sequence para não colorir o que vem depois.
elif imc >= 17 and imc <= 18.49:
    print('\033[1;43mVocê está abaixo do peso normal.\033[m\n') # Fundo amarelo, texto em negrito.
elif imc >= 18.50 and imc <= 24.99:
    print('\033[1;42mVocê está com o peso normal.\033[m\n') # Fundo verde, texto em negrito.
elif imc >= 25 and imc <= 29.99:
    print('\033[1;43mVocê está acima do peso normal.\033[m\n') # Fundo amarelo, texto em negrito.
elif imc >= 30 and imc <= 34.99:
    print('\033[1;41mVocê está com obesidade I.\033[m\n') # Fundo vermelho, texto em negrito.
elif imc >= 35 and imc <= 39.99:
    print('\033[1;41mVocê está com obesidade II, severa.\033[m\n') # Fundo vermelho, texto em negrito.
elif imc > 40:
    print('\033[1;41mVocê está com obesidade III, mórbida.\033[m\n') # Fundo vermelho, texto em negrito.
# "else" no final é opcional, ele não recebe parametro nenhum, fica "else:".

'''
Cores ANSI escape sequence
\033[(estilo);(cor do texto);(cor do fundo)m
\033[0;33;44m
"\033[" abre, "m" fecha.
Não tem necessidade de definir os 3 parâmetros, se tiver mais de um separe com ";"
Não esqueça de fechar com "\033[m" para não colorir informações posteriores.

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
