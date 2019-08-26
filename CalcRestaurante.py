class Pessoa:
  def __init__(self,nome, valor):
    self.name = nome
    self.preco = valor
  
  def final(self):
    print(str(self.name)+ " deve pagar R$"+str(self.preco))

# Pega uma lista de objetos Pessoa e calcula o custo de cada uma e retorna o total
def CalcTotal(grupo):
  total = 0
  for i in range(0,len(grupo)):
    print(grupo[i].final())
    total += grupo[i].preco
  return total

##########################################################
# Começa o programa principal
##########################################################

# Define a quantidade de pessoas que vão dividir a conta  
while True:
  try:
    quantidadePessoas = int(input("Quantas pessoas estão na mesa?"))
    break
  except:
    print("Por favor, colocar um número")

galera = [] # Lista de objetos "Pessoa"

# Preenche a lista de Pessoas
for i in range(0,quantidadePessoas):
  print("Qual é o nome da pessoa nº",i+1,"?",end='')
  name = input()
  galera.append(Pessoa(name,0))
# Cálcula os gastos de cada um
while True:
  comida = input("Adicione o nome de um item ou 'fim' para terminar:")
  if comida == "fim":
    break
  else:
    while True: # Loop para o try de unidades e custo por unidade
      try:
        valor = float(input("Quantas unidades?"))
        valor =valor * float(input("Quanto custou por unidade?"))
        break
      except:
        print("Favor digitar somente números")    
    
    existe = True
    print(len(galera))
    while existe:
      existe = False
      print("Quem comeu este prato? Insira os números correspondentes aos nomes separados por uma vírgula") # Escolha de pessoas que comeram o prato
      for i in range(0,len(galera)):
        print(i,":",galera[i].name)

      div=[int(x) for x in input().split(',')] # Guarda quem dividiu o prato

      for i in range(0,len(div)):
        if div[i] >= len(galera):
          existe = True
          print("Uma das pessoa selecionadas não existe")

    valor = valor/len(div) # Divide o valor do prato entre as pessoas

    for i in range(0,len(div)): # Adiciona o valor do prato dividido entre as pessoas
      galera[div[i]].preco += valor

total = CalcTotal(galera)

print("Total sem serviço: R$",total)

while True:
  try:
    servico = int(input("Qual é a taxa de serviço (inserir somente o valor)?"))
    break
  except:
    print("Favor digitar somente números")

for i in range(0,len(galera)):
  galera[i].preco *= ((100+servico)/100)

total = CalcTotal(galera)

print("Total com serviço: R$",total)
input()