n1 = int(input("Informe o primeiro numero: "))
n2 = int(input("Informe o segundo numero: "))
n3 = int(input("Informe o terceiro numero: "))

if n1 > n2 and n1 > n3:
    maior1 = n1
    if n2 > n3:
        maior2 = n2
        print(maior1 + maior2)
    else:
        maior2 = n3
        print(maior1 + maior2)

else:
    if n2 > n1 and n2 > n3:
        maior1 = n2
        if n1 > n3:
            maior2 = n1
            print(maior1 + maior2)
        else:
            maior2 = n3
            print(maior1 + maior2)

    else:
        if n3 > n1 and n3 + n2:
            maior1 = n3
            if n2 > n1:
                maior2 = n2
                print(maior1 + maior2)
            else:
                maior2 = n1
                print(maior1 + maior2)





