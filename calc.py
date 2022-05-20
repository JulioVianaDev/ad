# + / * -
num1 = int(input("Digite um numero: "))
num2= int(input("Digite outro numero"))

print("Escolha \n 1 para somar\n 2 para multiplcar\n 3 para dividir\n 4 para subtrair")
escolha = int(input())
if escolha == 1:
    print(num1+num2)
elif escolha == 2:
    print(num1 * num2)
elif escolha == 3:
    print(num1 / num2)
else:
    print(num1 - num2)
    