#Apenas uma função para definir mensagens padrão
def msg(msg):
    print("-"*10)
    print(f"Atenção: \n{msg}")
    print("-"*10)
#---------------------------------------------------------------------------------
#Criando a classe Vetor:
class Vetor:    
    #Construtor onde estamos definindo 
    def __init__(self,maximo, vetor=None):
        self.maximo = maximo

        if vetor is None:
            msg("O vetor iniciará vazio")
            self.vetor = []
#---------------------------------------------------------------------------------
#Função onde vamos verificar se ela as entradas que o usuário está fornecendo estão validas
    def range_vetor(self,indice):

        try:
            if indice > self.maximo:
                msg("Valor ultrapassa a fronteira do vetor")
                return False
            else:
                return True
        except ValueError :
            msg("Impossivel definir esse indice!")
#---------------------------------------------------------------------------------
#Verifica se o indice solicitado está vazio
    def verificar_indice(self,indice):
        if self.vetor[indice] is None:
            return True
        else:
            msg(f"O indice que deseja inserir está definido ja por {self.vetor[indice]}")
            return False
#---------------------------------------------------------------------------------
#Cria o vetor preenchendo todos os indices do vetor como None, para indicar que estão vazios
    def criar_vetor(self):
        self.vetor = [None] * self.maximo
#---------------------------------------------------------------------------------
#Solicita a entrada do usuário e adiciona o valor solicitado no indice solicitado
    def preencher(self,indice):
        if self.range_vetor(indice) is True  and self.verificar_indice(indice) is True:
            valor = input("Digite o que voce deseja colocar no vetor\n")
            self.vetor[indice] = valor
#---------------------------------------------------------------------------------
#Mostra o tamanho do vetor e quantos indices estão preenchidos e quantos estão vazios
    def lenght(self):
        preenchido = 0
        vazio = 0
        for indice in range(len(self.vetor)):
            if indice != None:
                preenchido += 1
            else:
                vazio += 1
        if vazio == 0:
            msg(f"A lista contem {self.maximo} espaços preenchidos ")
        elif preenchido == 0:
            msg("A lista está vazia")
        else:
            msg(f"A lista contem {vazio} espaços vazios e {preenchido} espaços preenchidos")
#---------------------------------------------------------------------------------
    #Retorna o indice fornecido para None
    def clear(self,indice):
        if not self.verificar_indice(indice):
            self.vetor[indice] = None
    
#---------------------------------------------------------------------------------
    #Reseta todos os indices do vetor
    def clear_all(self):
        self.vetor.clear()
        self.vetor = Vetor.criar_vetor()

        return True
#---------------------------------------------------------------------------------
# Exibe o vetor
    def display(self):
        print(self.vetor)
    

if __name__ == "__main__":
    maximo = int(input("Informe o tamanho da lista que você deseja\nR- "))
    vetor = Vetor(maximo)
    while True:
        try:
            maximo = int(input("Informe o tamanho da lista que você deseja\nR- "))
            print("*"*8)
            menu = int(input("Digite oq deseja\n1-Preencher a lista (OBRIGATÓRIO) \n2-Inserir na lista\n3-Remover da lista\n4-Limpar a lista\n5- Verificar lista\nR - "))
            print("*"*8)

            if menu == 1:
                vetor.criar_vetor()
                msg(f"Vetor criado com sucesso!{vetor.display()}")
            elif menu == 2:
                if vetor == 0 :
                    msg(f"O vetor ainda nao foi criado!\n{vetor.display()}\n Obs: O vetor criado possui os seus indices preenchidos com 'None' para informar um indice vazio\n")
                else:
                    
                    indice = int(input(f"Digite a localização que voce quer colocar [0 - {maximo}]\n"))
                    vetor.preencher(indice)
                    vetor.display()
                    msg("Valor alterado com sucesso!")
            
            elif menu == 3:
                if vetor == 0 :
                    msg(f"O vetor ainda nao foi criado!\n{vetor.display()}\n Obs: O vetor criado possui os seus indices preenchidos com 'None' para informar um indice vazio\n")
                else:
                    indice = int(input(f"Digite a localização que voce quer colocar [0 - {maximo}]\n"))
                    vetor.clear(indice)
                    msg("Localidade limpa com sucesso!")
                    vetor.display()
            elif menu == 4:
                msg("Vetor limpo com sucesso")
            
            elif menu == 5:
                if vetor == 0 :
                    msg(f"O vetor ainda nao foi criado!\n{vetor.display()}\n Obs: O vetor criado possui os seus indices preenchidos com 'None' para informar um indice vazio\n")
                else:
                    vetor.lenght()
                    vetor.display()
        except ValueError as e:
            msg(e)            

            
            
        