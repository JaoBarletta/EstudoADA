

# Quando criamos uma classe em python, o nosso construtor é sempre definido como __init__
class Pessoa :
    #No nosso construtor, já definimos os nossos atributos e setamos as variáveis que eles
    #irão receber. Para notação de nivel de acesso em python usamos o "_".
    #Sendo:
    # 
    # A variável "nome_da_variavel" para atributor public
    # 1 "_" (_nome_da_variavel) para o protected ; 
    # 2 "__" (__nome_da_variavel) para private ; 

    #Entretanto, o encapsulamento  em python não funciona de forma rigorosa que nem java ou C++
    #Apesar da sujestão dos "_", os atributos ainda podem ser acessados usando
    #__nomeDaClasse__atributo


    def __init__(self,nome,idade,genero):
        self.__nome = nome
        self.__idade = idade
        self.__genero = genero


    # Metodos GET and SET de cada atributo
    def getNome(self):
        return self.__nome
    
    def setNome(self,nome):
        self.__nome = nome

    def getIdade(self):
        return self.__idade
    
    def setIdade(self,idade):
        self.__idade = idade

    def getGenero(self):
        return self.__genero
    
    def setGenero(self,genero):
        self.__genero = genero
    
    def __str__(self):
        return f"Nome: {self.__nome}\nIdade: {self.__idade}\nGenero: {self.__genero}"


#Teste de estanciamento da classe e a criação de um array de objeto
if __name__ == "__main__":
    pessoas = []
    for i in range(3):
        nome = input("Nome: ")
        idade = int(input("idade: "))
        genero = input("genero: ")
        pessoa = Pessoa(nome,idade,genero)
        pessoas.append(pessoa)
    

