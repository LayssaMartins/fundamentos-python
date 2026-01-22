numeros =[]
for c in range (0,5):
 n = int (input("Digite os números:"))
 numeros.append(n)
print("Os números digitados foram:", numeros)
print("Menor número:", min(numeros))
print("Maior número:", max(numeros))

print("Posições dos números digitados:")
for i, num in enumerate(numeros):  # Percorre a lista com índice e valor
    print(f"O número {num} está na posição {i}")

print("______________________________________")
opção = ()
num = []  
while True:
    n = int(input("Digite um número: "))  

    if n in num:
        print("Esse número já está na lista")
    else:
        num.append(n)
    
    opção = input("Deseja continuar? (S/N): ").strip().upper()  # Convertendo para maiúscula
    if opção == "N":  # Se o usuário digitar 'N', o loop para
        break

print(f"os valores digitados na lista foram: {num}")  

print("______________________________________")

numerosimpares=[]
numerospares =[]
numeros1 =[]
for o in range (0,10):
 n = int(input("Digite os números:"))
 numeros1.append(n)
print("Os números digitados foram:", numeros1)

for n in numeros1:
 if n % 2 == 0:
      numerospares.append(n)
 else:
      numerosimpares.append(n)
print("Números pares:")
print(numerospares)
print("Números impares:")
print(numerosimpares)
