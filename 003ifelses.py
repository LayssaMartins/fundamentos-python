numero1 = int(input ("Escreva um numero;"))
numero2 = int(input("escreva outro número:"))

if numero1 > numero2:
    print ("O primeiro número é maior")

elif numero2 > numero1:
    print("O segundo número é maior")

else:
     print("Eles são iguais")

print("_____________________________________________________")

anodn = int(input("Digite o ano do seu nascimento:"))

idade = 2025 - anodn
print ("Sua idade é {}" .format(idade))

calculotempo1 = 18 -idade
calculotempo2 = idade - 18

if idade < 18:
    print("ainda vai se alistar e falta {}" .format(calculotempo1), "anos")
elif idade == 18:
    print ("está na hora de se alistar!!!")
else:
    print ("Já passou do tempo de alistar-se, o prazo era há {}" .format(calculotempo2), "anos atrás")


print("_____________________________________________________")

n1 = int (input ("Digite sua primeira nota:"))
n2 = int (input ("Digite sua segunda nota:"))

média = (n1 + n2)/2
print("Sua média foi:", média)

if média < 7:
    print ("Vc está reprovado")
elif média == 7:
    print("Vc está na média!")
else:
    print ("você está acima da média e foi aprovado, parabéns!!")



