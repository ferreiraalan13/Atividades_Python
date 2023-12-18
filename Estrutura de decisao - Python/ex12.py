nome = input("Informe o nome do Atleta: ")
idade = int(input("Informe a idade do Atleta: "))

if idade >= 5 and idade <= 10:
    print(f"Nome do atleta: {nome}")
    print(f"Categoria: Infantil")
else:
    if idade >= 11 and idade <= 15:
        print(f"Nome do atleta: {nome}")
        print(f"Categoria: Juvenil")
    else:
        if idade >= 16 and idade <= 20:
            print(f"Nome do atleta: {nome}")
            print(f"Categoria: Junior")
        else:
            if idade >= 21 and idade <= 25:
                print(f"Nome do atleta: {nome}")
                print(f"Categoria: Profissional")