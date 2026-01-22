from random import randint
computador = randint (0,10)
descubra = -1 #número pro loop rodar/ definindo a variavel
tentativa = 0 # Inicializa a contagem
print ("Vou pensar num numero de 0 a 10")
while descubra != computador:
    descubra = int (input("Tente descobrir qual numero foi..."))
    tentativa +=1 # Incrementando a contagem de tentativas
    print("Número de tentativas:", tentativa)
print ("Você descobriu! KKKKKKKKKKKKKK")
 
print("_____________________________________________________")
