
a = int(input("Digite o valor do lado a: "))
b = int(input("Digite o valor do lado b: "))
c = int(input("Digite o valor do lado c: "))

if a + b > c and a + c > b and b + c > a:
    print("Pode ser um triangulo")

    if a == b == c:
        print("Equilátero")
    elif a == b or b == c or a == c:
        print("Isósceles")
    else:
        print("Escaleno")

else:
    print("Não é possível formar um triângulo")

