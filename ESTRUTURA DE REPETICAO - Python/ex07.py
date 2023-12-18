#07) - Faça um algoritmo que receba o preço de custo e o preço de venda de 40 produtos.
# Mostre como resultado se houve lucro, prejuízo ou empate para cada produto.
# Informe média de preço de custo e do preço de venda.

contador = 1
total_vendas = 0
total_custo = 0
contador_vendas = 0
contador_custo = 0
media_vendas = 0
media_custo = 0


while contador <= 5:

    preco_custo = float(input(f"Digite o preço de custo do {contador}º produto: "))
    preco_venda = float(input(f"Digite o preço de venda do {contador}º produto: "))


    if preco_custo == preco_venda:
        print("O produto ficou em EMPATE de lucro e prejuizo ")
        print()
    else:
        if preco_custo > preco_venda:
            print(f"O produto ficou em PREJUIZO")
            print()
        else:
            if preco_custo < preco_venda:
                print(f"O produto ficou em LUCRO")
                print()

    total_vendas = total_vendas + preco_venda
    total_custo = total_custo + preco_custo

    contador_custo = contador_custo + 1
    contador_vendas = contador_vendas + 1

    contador = contador + 1

media_custo = total_custo / contador_custo
media_vendas = total_vendas / contador_vendas

print(f"A media de preço de custo foi R$ {media_custo}")
print(f"A media de preço de vendas foi R$ {media_vendas}")