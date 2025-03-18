from random import randint
from time import sleep
computador = randint(0,5)
print("-=-"*20)
print("Vou pensar em um número de 0 a 5!")
print("-=-"*20)
numero = int(input("Digite sua tentativa! "))
print("Processando...")
sleep(3)
if numero == computador:
    print("Você acertou! Pensei no {}".format(computador))
else:
    print("Você errou... Pensei no {}".format(computador))

