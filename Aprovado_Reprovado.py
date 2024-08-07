
def Exame(participantes):
    #ordena os alunos de acordo com o indice aluno[1] usnado o key=lambda aluno: aluno[1]
    participantes_ordem = sorted(participantes, key=lambda aluno: (aluno[1],aluno[0]))

    print(participantes_ordem)
    return participantes
        



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
            
    except Exception as e :
        print(e)