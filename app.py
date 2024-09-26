#Laço de repetição
#Importa bibliotecas
import os
import time

n = int(input("Informe um número possitivo:  "))
while n >= 0:
    os.system("cls")
    print(n)
    time.sleep(2)
    n -= 1

os.system("cls")
print("BOOM!!!!!")