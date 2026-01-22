for c in range (10,0,-1):
 print (c)
print ("Feliz ano novo!")

print("_____________________________")

for n in range (2,50,2):
 print(n)
print("FIM!")

print("_____________________________")

num = int(input("Você quer saber a tabuada de qual número?"))

for t in range (1,11):
 print (num * t)
print ("Fim")

print("_____________________________")

s = 0    # Variável para somar os números pares
for q in range (1,7):  # Loop para ler 6 números
 n = int(input("Digite um valor:"))
 if n %2==0:   # Verifica se o número é par
  s+=n         # Acumula a soma dos números pares
print("O cálculo da soma dos números pares foi:", s)

print("_____________________________")

menor_idade = 0  # Contador de menores de idade
maior_idade = 0  # Contador de maiores de idade

for i in range (1,5): 
 ano = int(input("Digite seu ano de nascimento:"))
 calculoidade1 = 2025 - ano

 if calculoidade1 < 18:
  print("Você é menor de idade")
  menor_idade += 1  # Aumenta o contador de menores

 else:
  print("Você é maior de idade!")
  maior_idade += 1  # Aumenta o contador de maiores  

# Exibe o total de menores e maiores de idade  
print("Total de menores de idade: {}" .format(menor_idade))  
print("Total de maiores de idade: {}" .format(maior_idade)) 