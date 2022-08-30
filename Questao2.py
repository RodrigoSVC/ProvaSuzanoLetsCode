def funcaoFatorial(numeroBase):
  contador = 1
  numerosAteFatorial = []
  for i in range(1, int(numeroBase)+ 1):
    contador *= i
  for i in range(1, int(numeroBase)+ 1):
    numerosAteFatorial.append(i)

  return print(f'Fatorial de {numeroBase} = {numerosAteFatorial} = {contador}')

funcaoFatorial(input('Digite um número base para  fatorial'))
