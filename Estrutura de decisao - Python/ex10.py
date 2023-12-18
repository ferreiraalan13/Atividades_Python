nome = input("Informe o nome do aluno: ")

n1 = float(input("Informe a PRIMEIRA nota: "))
n2 = float(input("Informe a SEGUNDA nota: "))
n3 = float(input("Informe a TERCEIRA nota: "))

media = (n1 + n2 + n3) / 3

if media >= 7:
    print(f"Nome do aluno: {nome}")
    print(f"Media: {media:.1f}")
    print(f"Menção: APROVADO")
else:
    if media <= 5:
        print(f"Nome do aluno: {nome}")
        print(f"Media: {media:.1f}")
        print(f"Menção: REPROVADO")
    else:
        if media >= 5.1 and media <= 6.9:
            print(f"Nome do aluno: {nome}")
            print(f"Media: {media:.1f}")
            print(f"Menção: RECUPERACAO")
