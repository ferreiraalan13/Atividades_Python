compra = float(input("Digite o valor da compra: "))
print()
print("Forma de pagamento disponiveis: ")
print("1 - Venda a Vista - desconto de 10%")
print("2 - Venda a Prazo 30 dias - desconto de 5%")
print("3 - Venda a Prazo 60 dias - mesmo preço")
print("4 - Venda a Prazo 90 dias - acréscimo de 5%")
print("5 - Venda com cartão de débito - desconto de 8%")
print("6 - Venda com cartão de crédito - desconto de 7% ")
print()
forma_pagamento = int(input("Selecione a forma de pagamento: "))

if forma_pagamento == 1:
    desconto = compra * 0.10
    compra = compra - desconto
    print("Aplicado desconto de 10% ")
    print(f"Total atualizado da compra  R${compra:.2f}")
else:
    if forma_pagamento == 2:
        desconto = compra * 0.05
        compra = compra - desconto
        print("Aplicado desconto de 5% ")
        print(f"Total atualizado da compra  R${compra:.2f}")
    else:
        if forma_pagamento == 3:
            print("Não foi aplicado nenhum desconto ou acrescimo")
            print(f"Total da compra  R${compra:.2f}")
        else:
            if forma_pagamento == 4:
                acrescimo = compra * 0.05
                compra = compra + acrescimo
                print("Aplicado acrescimo de 5% ")
                print(f"Total atualizado da compra  R${compra:.2f}")
            else:
                if forma_pagamento == 5:
                    desconto = compra * 0.08
                    compra = compra - desconto
                    print("Aplicado desconto de 8% ")
                    print(f"Total atualizado da compra  R${compra:.2f}")
                else:
                    if forma_pagamento == 6:
                        desconto = compra * 0.07
                        compra = compra - desconto
                        print("Aplicado desconto de 7% ")
                        print(f"Total atualizado da compra  R${compra:.2f}")
