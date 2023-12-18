A = int(input("Informe o valor de A: "))
B = int(input("Informe o valor de B: "))

if A < B:
    print(f"A = {A} B = {B}")
else:
    auxiliar = B
    B = A
    A = auxiliar
    print(f"A = {A} B = {B}")