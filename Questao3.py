
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
