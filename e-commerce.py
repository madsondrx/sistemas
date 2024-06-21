import mysql.connector #importando bibloteca mysql no python

class Cliente: #Criada a classe cliente
    def __init__(self,nome,cpf, email): #atributos
        self.nome = nome #atributos
        self.cpf= cpf #atributos
        self.email= email #atributos

class Produtos:
    def __init__ (self,nome,preço, categoria): #Definindo a inicialização da classe e definindo os parametros
        self.nome = nome #atributos
        self.preço = preço #atributos
        self.categoria= categoria #atributos

class SistemaDeProdutos:
    def __init__(self): #Definindo a inicialização da classe
        self.conexao = mysql.connector.connect(  #Estabelecendo a conexao do mysql e adicionado informaçoes do banco de dados logo a baixo
            host="localhost",
            user="root",
            password="he182555@",
            database="netshoes"
        )
        self.cursor = self.conexao.cursor() # adiconando o cursor permitindo com que eu possa manipular os dados sem precisar ir no workbench

    def adicionar_cliente(self,cliente): # defindo um metodo (adicionar_cliente)
    
       sql= "INSERT INTO clientes (nome, cpf, email) VALUES (%s,%s)" # funçao do mysql para inserir dados
       valores= (cliente.nome, cliente.cpf, cliente.email) # relacionando parametros e atributos
       self.cursor.execute(sql,valores) #executanto as variaveis
       self.conexao.commit() # utlizando o commit para a consulta do banco de dados

    def cadastrar_cliente(self): # Definindo metodo (cadastrar cliente)
        self.cursor.execute ("SELECT nome, cpf, email FROM clientes") # Selecionando os atributos e tabela
        clientes = self.cursor.fetchall() #utilizando fetchal para buscar dados nessa tabela
        for cliente in clientes: #para cliente em clientes
            print(f"Nome: {cliente[0]}, CPF: {cliente[1]}, EMAIL: {cliente[2]}") # Onde os dados vao ser guardados conforme o usuario for inserindo
                            
           
    def adicionar_produtos(self,produto):
    
        sql= "INSERT INTO produtos (nome, preço, categoria) VALUES (%s,%s)"  # funçao do mysql para inserir dados
        valores= (produto.nome, produto.preço, produto.categoria)  # relacionando parametros e atributos
        self.cursor.execute(sql,valores) #executanto as variaveis
        self.conexao.commit()# utlizando o commit para a consulta do banco de dado 
        

    def buscar_produtos(self):
        self.cursor.execute("SELECT nome, preço, categoria FROM produtos") # Selecionando os atributos e tabela
        produtos = self.cursor.fetchall()   #utilizando fetchal para buscar dados nessa tabela
        for produto in produtos: # para produto em produtos
            print(f"Nome: {produto[0]}, Preço: {produto[1]}, Categoria: {produto[2]}")  # Onde os dados vao ser guardados conforme o usuario for inserindo

    def fechar_conexao(self): # defindo metodo(fechar_conexao)
        self.cursor.close() #executar para fechar o cursor
        self.conexao.close() # executar para fechar o conexao

#usando a instacia para utlizar o metodos criada nela
sistema = SistemaDeProdutos()

# forma de se comunicar com o usuario e automaticamente salvar seus dados no banco de dados
nome_cliente=input("Digite o seu nome:")
cpf_cliente=input("Digite seu cpf:")
email_cliente=input("Digite seu email:")
cliente1= Cliente(nome_cliente, cpf_cliente,email_cliente) #amarzenando as informaçoes na instancia
sistema.adicionar_cliente(cliente1) #usando metodo para registrar o cliente
print("Cliente cadastrado.")

#Produtos criados e armazenados na instancia (Produtos)
produto1= Produtos('Camisa', "250", "Vestuario")
produto2= Produtos('Tenis', "150", "Calçados")
produto3= Produtos('Short',"100","Vestuario")
produto4= Produtos('Meia',"15", "Vestuario")

# usando metodo para adicionar os produtos
sistema.adicionar_produtos(produto1)
sistema.adicionar_produtos(produto2)
sistema.adicionar_produtos(produto3)
sistema.adicionar_produtos(produto4)

#Onde vai listar os clientes adicionados
print('Lista de clientes:')
sistema.cadastrar_cliente()

#Onde vai listar os produtos adicionados
print('Buscar produtos:')
sistema.buscar_produtos()

sistema.fechar_conexao()



    

    



    

    
