import mysql.connector  #importando bibloteca mysql no python

class Cliente: #Criada a classe Cliente
    def __init__(self,nome,cpf,email): #defindo a inicializaçao da classe e parametros
        self.nome= nome #atributos
        self.cpf= cpf  #atributos
        self.email= email #atributos

class Registro: #Criada a classe Registro
    def __init__(self,data_registro): #defindo a inicializaçao da classe e parametros
        self.data= data_registro  #atributos

class SistemasDeRegistros: #Criada a classe SistemaDeRegistros 
    def __init__(self): #defindo a inicializaçao da classe
           self.conexao = mysql.connector.connect( #Estabelecendo a conexao com mysql com as informaçoes do banco de dados
            host="localhost",
            user="root",
            password="he182555@",
            database="dados_crm"

           )
           self.cursor = self.conexao.cursor() #Cursor é importante para que eu consiga manipular os dados do mysql sem precisar ir no workbench
         
    def registrar_cliente(self,cliente): #O metodo (registar_clientes)
       sql= "INSERT INTO clientes (nome, cpf, email) VALUES (%s,%s,%s)" #Usando funçoes do mysql para inserir dados
       valores= (cliente.nome, cliente.cpf, cliente.email) #adicionando os parametros com os atributos
       self.cursor.execute(sql,valores) #Executando as variaveis 
       self.conexao.commit()  #Utilizando o commit para a consulta de dados no mysql

    def dados_clientes(self): #Metodo(dados_clientes)
        self.cursor.execute("SELECT nome, cpf, email FROM clientes") #Executando a funçao select na tabela clientes do mysql
        clientes = self.cursor.fetchall() #Usando o fetchall para a busca de dados na tabela
        for cliente in clientes: #Para cliente em clientes
            print(f"Nome: {cliente[0]}, CPF: {cliente[1]}, EMAIL: {cliente[2]}") # Onde vao ser implementas as informaçoes dos atributos
           
    def fechar_conexao(self):
        self.cursor.close
        self.conexao.close
     
   
#Utlizando a instancia (SistemaDeRegistros)
sistema = SistemasDeRegistros()

#Forma de comunicaçao com o usuario e automaticas salvas no banco de dados com o metodo (registar_cliente)
nome_cliente= input("Digite seu nome:")
cpf_cliente= input("Digite seu cpf:")
email_cliente= input("Digite seu email: ")
cliente_registrado= Cliente(nome_cliente,cpf_cliente,email_cliente)
sistema.registrar_cliente(cliente_registrado) 



#Lista de clientes registrados
print("Clientes registrados:")
sistema.dados_clientes()

sistema.fechar_conexao()
