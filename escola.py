import mysql.connector  #importando bibloteca mysql no python

class Alunos: #Criada a classe Alunos
    def __init__(self,nome,cpf):  #defindo a inicializaçao da classe e parametros
        self.nome = nome #atributos
        self.cpf = cpf #atributos

class Matriculas: #Criada a classe Matriculas
    def __init__(self,curso_nome):  #defindo a inicializaçao da classe e parametros
        self.curso_nome= curso_nome #atributos


class SistemaEscolar: #Criada a classe SistemaEscolar
    def __init__(self):
        self.conexao = mysql.connector.connect( #Estabelecendo a conexao do mysql e adicionado informaçoes do banco de dados logo a baixo
            host="localhost",
            user="root",
            password="he182555@",
            database="Escola"
        )
        self.cursor = self.conexao.cursor()  # adiconando o cursor permitindo com que eu possa manipular os dados sem precisar ir no workbench



    def matricular_alunos(self,aluno): # Criado metodo matricular_alunos
    
        sql="INSERT INTO alunos (nome,cpf) VALUES (%s,%s)"#Usando funçoes do mysql para inserir dados
        valores= (aluno.nome, aluno.cpf)  # relacionando parametros e atributos
        self.cursor.execute(sql,valores) #executanto as variaveis
        self.conexao.commit() #Utilizando o commit para a consulta de dados no mysql
        print("Aluno foi matriculado.")


    def listar_alunos(self): # Criado metodo listar_alunos
    
        self.cursor.execute("SELECT nome, cpf FROM alunos")  # Selecionando os atributos e tabela
        alunos = self.cursor.fetchall()   #utilizando fetchal para buscar dados nessa tabela
        for aluno in alunos: #para aluno em alunos
            print(f"Nome: {aluno[0]}, CPF: {aluno[1]}" )  # Onde os dados vao ser guardados conforme o usuario for inserindo


    def fechar_conexao(self): # defindo metodo(fechar_conexao)

        self.cursor.close() #executar para fechar o cursor
        self.conexao.close()  # executar para fechar o conexao
#Inserindo a instancia
sistema = SistemaEscolar()
#Comunicaçao do sistema com o usuario
nome_aluno= input("Nome do aluno:")
cpf_aluno=input("CPF do aluno:")
aluno1= Alunos(nome_aluno, cpf_aluno) 
sistema.matricular_alunos(aluno1)

#Para a lista de alunos
print("Lista de alunos:")
sistema.listar_alunos()


#Fecha conexao
sistema.fechar_conexao()       









    

