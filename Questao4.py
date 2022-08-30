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
