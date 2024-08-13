def reverse_list():
    #recebe a entrada do usuario como " 1 2 3 4 5 6" em um unico input para adicionar tudo em uma lista
    lista = list(map(int,input("Informe a lista com espaços\nEx: 1 2 3 4 5").strip().split()))
    #se lista estiver contendo algum valor, ele retorna a lista de trás para frente
    if lista:
        print(lista[::-1])
        return True
    else:
        return False

def remove_duplicate():
    #recebe a entrada do usuario como " 1 2 3 4 5 6" em um unico input para adicionar tudo em uma lista
    lista = list(map(int,input("Informe a lista 1 com espaços\nEx: 1 2 3 4 5\nR-").strip().split()))

    #usamos uma variáel para localizar o indice
    index = 0

    #percorre a lista para verificar indice por indice da lista
    for i in lista:
        #se o indice atual da lista ( i ) for igual ao proximo indice da lista (index + 1)
        if i == lista[index + 1]:
            #ele deleta o indice atual da lista e passa para o proximo indice 
            del lista[index]
            index += 1
        else:
            index += 1
            

    print(lista)

def Mesclagem():

    #variavel de controle que podemos utilizar para percorrer as duas listas simultâneas
    #usamos esse tipo de declaração para ser mais eficiente, é como se fosse um i = 0 e j = 0
    i=j=0
    lista_conjunta = []
    lista_1 = list(map(int,input("Informe a lista 1 com espaços\nEx: 1 2 3 4 5\nR-").strip().split()))
    lista_2 = list(map(int,input("Informe a lista 2 com espaços\nEx: 1 2 3 4 5\nR-").strip().split()))

    #usamos a estrutura de repetição para verificar as duas listas ao mesmo tempo

    while i < len(lista_1) and j < len(lista_2):
        #se a lista 1 no indice i (no primeiro loop da lista está definido como 0),
        # for menor que o indice j da lista 2 (indice j definido como 0 no primeiro loop)
        # então ele adiciona o item lista_1[i] a lista conjunta
        if lista_1[i] < lista_2[j]:
            lista_conjunta.append(lista_1[i])
            # soma mais 1 a variavel i para ir para o proximo indice
            i += 1
        #se o inverso for verdadeiro, então ele adiciona o item lista_2[j] na lista conjunta
        else:
            lista_conjunta.append(lista_2[j])
            # soma mais 1 a variavel j para ir para o proximo indice 
            j += 1
    #faz a varredura na lista 1 para ver se sobrou mais itens e SE sobrou, ele adiciona a lista conjunta
    while i <len(lista_1):
        lista_conjunta.append(lista_1[i])
        i += 1
    #faz a varredura na lista 2 para ver se sobrou mais itens e SE sobrou, ele adiciona a lista conjunta
    while j <len(lista_2):
        lista_conjunta.append(lista_2[j])
        j += 1

    print(lista_conjunta)

def Palindromo():
    string = input()
    #Uma string pode ser manipulada de diversas maneira, uma delas é "identificando" ela como uma lista
    #digamos que em uma string "radar", nós queremos verificar uma letra.
    #podemos manipular ela como uma lista e pegar o indice de cada letra
    #por exemplo: "radar" r = [0], a = [1], d = [2] ...
    # Usamos esse quesito de manipulação para colocar a string de trás para frente, assim como se quisessemos inverter uma lista 
    palindromo = string[::-1]
    #Aqui apenas verificamos se a string invertida forma a mesma palavra
    if palindromo == string:
        print(True)
    else:
        print(False)
        
#Sequencia de fibonacci consiste em uma sequencia de numeros, onde os dois primeiros indices
#são 0 e 1, e os numeros seguintes são a soma dos dois numeros anteriores
#[0,1,1,2,3,5,8,13, ...]
def Fibonacci():

    #Aqui recebemos o valor que queremos fazer para criar a lista, ou seja, dado falor "n", montamos a lista
    # de [0, ..., n]
    nf = int(input("Por favor insira o valor que tu quer o numero de Fibonacci\nR-"))
    lista_fibonacci = []
    #as duas variaveis iniciais
    a,b = 0, 1
    #loop da lista de [0, ... , n]
    for i in range(nf):
        # Se a for menor que "n", então ele adiciona à lista
        if a < nf:
            lista_fibonacci.append(a)
        # Atualiza o valor das variáveis onde "a = b e b = a+b"
        a,b = b , a+b
    print(lista_fibonacci)



def Middleiten():
    #vai receber uma lista de n valores onde n % 2 != 0 
    lista = list(map(int,input("\nPor favor insira uma lista de tamanho ímpar\n").strip().split()))
    #Ordenamos a lista 
    lista.sort()
    #verifica se a lista é impar
    if len(lista)% 2 == 0:
        print("A lista precisa ser IMPAR\n")
    #usamos os operadores // para fazer uma divisão inteira 
    # Usamos o // e nao o round() pois porque o // arrendonda para o numero menor 
    # enquanto o round() arredonda para o numero par mais próximo
    mid_item = len(lista)//2
    print(lista[mid_item])

def Sublista():
    #Recebe os inputs como listas
    lista_1 = list(map(int,input("Informe a lista 1 com espaços\nEx: 1 2 3 4 5\nR-").strip().split()))
    lista_2 = list(map(int,input("Informe a lista 2 com espaços\nEx: 1 2 3 4 5\nR-").strip().split()))
    #usamos uma variavel de controle 
    count_hit = 0
    #Percorremos as duas listas e comparamos indice por indice das duas listas
    for i in lista_1:
        for j in lista_2:
            if i == j:
                #se os indices forem iguais, encrementamos na variavel de controle
                count_hit += 1
    #se a variavel de controle for igual a quantidade de itens da lista 2 (sublista), então
    #retorna True
    if count_hit == len(lista_2):
        print("True")
    else:
        print("False")
        
def SearchCount():
 




    
# Para iniciar, usamos a variavel global __name__, para iniciar o codigo na instancia de __main__
if __name__ == "__main__":
   while True:
        try:
            interacao = int(input("1 - reverse\n2 - Remover Duplicata\n3 - Mesclar lista\n4 - palindromo\n5 - fibonacci\n6 - Achar o item do meio\n7 - Sublista\nR - "))
            if interacao > 8 or interacao <1 :
                print()
                pass
            elif interacao == 1:
                reverse_list()
            elif interacao == 2:
                remove_duplicate()
            elif interacao == 3:
                Mesclagem()
            elif interacao == 4:
                Palindromo()
            elif interacao == 5:
                Fibonacci()
            elif interacao == 6:
                Middleiten()
            elif interacao == 7:
                Sublista()
            elif interacao == 8:
                SameNumber()
        except ValueError as e:
            print(e)


    