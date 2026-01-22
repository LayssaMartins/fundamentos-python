
velocidade = int(input("Em que velocidade vc está andando?"))
print("Você está na velocidade {}" . format(velocidade))
multa = (velocidade - 80) * 7
if velocidade >80:
    print("Você foi multado, por excesso de velocidade!")
    print("E sua multa foi de:", multa)
else:
    print("continue a viagem e siga feliz!")

print("____________________________________________")

numero =  int(input ("Digite um número:"))
print ("O número digitado foi {}" .format(numero))

calculopar = numero % 2 == 0

if calculopar:
    print ("O número é PAR")
else:
    print("O número é IMPAR")

print("____________________________________________")



