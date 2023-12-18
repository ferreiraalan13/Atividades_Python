n1 = int(input("Digite o primeiro numero inteiro: "))
n2 = int(input("Digite o segundo numero inteiro: "))
n3 = int(input("Digite o terceiro numero inteiro: "))

if n1 > n2 and n1 > n3:
    print(n1)
else:
    if n2 > n1 and n2 > n3:
        print(n2)
    else:
        print(n3)