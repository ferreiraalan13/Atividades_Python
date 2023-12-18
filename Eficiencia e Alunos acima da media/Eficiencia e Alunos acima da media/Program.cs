bool continuar = false;

while (continuar == false)
{
    int totalAlunos;

    Console.WriteLine("Quantas amostras deseja calcular? ");

    totalAlunos = int.Parse(Console.ReadLine());

    int[] notas = new int[totalAlunos];


    for (int i = 0; i < totalAlunos; i++)
    {
        Console.WriteLine("DIGITE A " + (i+1) + "º AMOSTRA");
        notas[i] = int.Parse(Console.ReadLine());
    }

    int somaDasNotas = 0;
    for (int i = 0; i < totalAlunos; i++)
    {
        somaDasNotas += notas[i];
    }

    double media = (double)somaDasNotas / totalAlunos;

    int alunosAcimaDaMedia = 0;
    for (int i = 0; i < totalAlunos; i++)
    {
        if (notas[i] > media)
        {
            alunosAcimaDaMedia++;
        }
    }

    double porcentagemAcimaDaMedia = (double)alunosAcimaDaMedia / totalAlunos * 100;

    Console.WriteLine($"Média das amostras: {media}");
    Console.WriteLine($"Porcentagem de alunos acima da média: {porcentagemAcimaDaMedia.ToString("0.000")}%");

    Console.WriteLine("DESEJA CONTINUAR? (S / N) ");
    string resposta = Console.ReadLine();
    if (resposta == "s" || resposta == "S")
    {
        continuar = false;
        Console.Clear();
    }
    else
    {
        continuar = true;
        Console.WriteLine("PROGRAMA FINALIZADO, OBRIGADO POR UTILIZAR");
    }
}