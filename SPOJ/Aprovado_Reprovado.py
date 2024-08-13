def Exame(participantes):
    #ordena os alunos de acordo com o indice aluno[1] usnado o key=lambda aluno: aluno[1]
    participantes_ordem = sorted(participantes, key=lambda aluno: (aluno[1],aluno[0]))
    menor_nota = participantes_ordem[0][1]
    menores_notas = []
    instancia = 0
    #verifica se existe mais de um aluno com a menor nota
    for i in participantes_ordem:
        #se tiver ele ordena pelo nome 
        
        if i[1] == menor_nota:
            menores_notas.append(i[0])
            
        #se a nota for maior que a menor nota ele só passa para o proximo indice
        elif i[1] > menor_nota:
            pass
    #Faz ordena em decrescente para pegar o aluno com a menor nota e com a "menor" letra do alfabeto
    menores_notas.sort(reverse=True)    
    reprovado = str(menores_notas[0])
    print()
    print(f"Instancia {instancia}\n{reprovado}")
    print()
        



if __name__ == "__main__":
    participantes = []
    
    indice = 1
    #tenta receber o input de quantidade de participantes da atividade
    try:
        np = int(input())
        
        for i in range(np):
            
            #cria uma lista "aluno" para receber aluno[0] = nome, aluno[1] = nota
            aluno = list(map(str,input().strip().split()))
            
            
            #verifica se a lista aluno recebeu só dois indices ou se nao recebeu nenhum 
            if len(aluno)> 2 or not aluno or len(aluno) == 1:
                print("O aluno deverá ser preenchido apenas com ''nome'' + ''nota'' ")

            #pega o indice da lista que possui a nota e transforma em inteiro
            if indice < len(aluno):
                try:
                    aluno[indice] = int(aluno[indice])
                    participantes.append(aluno)
                    
                except ValueError as e:
                    print(e)


        Exame(participantes)
        exit()
            
    except Exception as e :
        print(e)