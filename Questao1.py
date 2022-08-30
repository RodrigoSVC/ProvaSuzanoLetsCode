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
