# ProvaSuzanoLetsCode
# Questão 1: 

Um parque de diversões tem 3 atrações principais: o carrossel, piscina de bolinhas e montanha-russa. Para poder participar de uma atração a pessoa deve cumprir as seguintes condições:

Carrossel: altura mínima de 1,00m e idade mínima de 3 anos.

Piscina de bolinhas: idade entre 4 e 9 anos e máximo de 1,30m de altura.

Montanha-russa: altura mínima de 1,10m.
O fiscal de cada atração verificará o ano de nascimento da pessoa e altura para liberar o acesso para uma pessoa.

Faça uma função em python que receba o ano de nascimento e altura da pessoa e informe quais as atrações que a pessoa pode participar.

# Programa 1:

def checkBrinquedos(anoDeNascimento, alturaP):
  CPM = ['Pode ir ao Carrossel', 'Pode ir à Piscina de Bolinhas', 'Pode ir à Montanha Russa'] # 0 = Carrossel, 1 = Piscina, 2 = Montanha
  if anoDeNascimento > 2019 and alturaP < 1:
    CPM[0] = 'Não pode ir ao carrossel'
  if anoDeNascimento < 2013 or anoDeNascimento > 2018 and alturaP > 1.30:
    CPM[1] = 'Não pode ir à Piscina de bolinhas'
  if alturaP < 1.10:
    CPM[2] = 'Não pode ir à Montanha Russa'
  else:
    pass
  for i in range(0, 3):
    print(CPM[i])

checkBrinquedos(2012, 1.20)


##############################################################################################################################################################################################################################################################################################################################################

# Questão 2:

Peça ao usuário para entrar com um número e faça uma função que retorne o fatorial dele como resposta. O fatorial de um número é o resultado da multiplicação de todos os números que o antecedem a partir de 1 até o número fornecido.
#Exemplo: fatorial de 4 = 1 * 2 * 3 * 4 = 24


# Programa 2:

def funcaoFatorial(numeroBase):
  contador = 1
  numerosAteFatorial = []
  for i in range(1, int(numeroBase)+ 1):
    contador *= i
  for i in range(1, int(numeroBase)+ 1):
    numerosAteFatorial.append(i)

  return print(f'Fatorial de {numeroBase} = {numerosAteFatorial} = {contador}')

funcaoFatorial(input('Digite um número base para  fatorial'))


##############################################################################################################################################################################################################################################################################################################################################



# Questão 3:

Dado um número fornecido pelo usuário, faça um programa que teste se é número primo e imprima na tela. Além disso, exiba uma lista de divisores do número testado. 
Um número primo é divisível somente por 1 e por ele mesmo. Seu programa deve ser funcional para qualquer número até o 100.

#13 é divisível somente por 1 e ele mesmo (13), então é primo.
#25 é divisível por 1, 5 e ele mesmo (25), então NÃO é primo.



# Programa 3:

def checkIfPrimo(numeroBase):
  checker = []
  if numeroBase == 1:
    return print('1 não é primo.')
  for i in range(1, numeroBase+1):
    if numeroBase % i == 0:
      checker.append(i)
    else:
      pass

  if len(checker) != 2:
    return print(f'{numeroBase} não é primo, é divisivel por {checker}')
  elif len(checker) == 2:
    return print(f'{numeroBase} é primo, é divisivel por 1 e por ele mesmo {numeroBase}.')


checkIfPrimo(int(input('Escreva um número para checar se é primo: ')))


##############################################################################################################################################################################################################################################################################################################################################

# Questão 4: 

#Faça um script que leia 10 números do usuário e informe se algum número foi inserido em sequência. 
#Se mais de um número for repetido, informe ao menos um (caso no Exemplo 3).

#Exemplo 1
#input 1: 3
##input 2: 5
#(etc...) 6.. 7.. 12.. 2... 43.. 5.. 
###input 9: 1
###input 10: 8
###output: Nenhum número foi repetido em sequência
##Exemplo 2
##input 1: 9
##input 2: 4
##(etc...) 9.. 5.. 9.. 6... 3.. 1.. 
###input 9: 6
##input 10: 6
output: O número 6 foi repetido em sequência


# Programa 4:

def checkRepetidos():
  numeros = []
  repetidos = []
  for i in range(0, 10):
    numeros.append(int(input(f'Digite o {i+1} número.')))
    if i != 0:
     if (numeros[i]) == (numeros[i-1]):
       repetidos.append(numeros[i])  
     else:
       pass
    
  return print(f'O(s) número(s) repetidos foram: {set(repetidos)}')

checkRepetidos()

