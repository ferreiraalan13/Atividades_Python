n1 = int(input("Informe o primeiro numero: "))
n2 = int(input("Informe o segundo numero: "))
n3 = int(input("Informe o terceiro numero: "))

if n1 < n2:
    if n1 < n3:
        print(n2+n3)
    else:
        print(n1 + n2)
else:
    if n2 < n3:
        print(n1 + n3)
    else:
        if n3 < n1:
            print(n1 + n2)
        else:
            if n3 > n2:
                print(n1 + n3)
            else:
                print(n1 + n2)



