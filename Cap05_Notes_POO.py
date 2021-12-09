#!/usr/bin/env python
# coding: utf-8

# # Classes

# In[2]:


class Livro():
    
    def __init__(self):
        self.titulo = "O monge e o executivo"
        self.isbn = 899059
        print("Esse é o construtor. Utilizado para criar o objeto da classe")
        
    def imprime(self):
        print("Foi o criado o livro %s e o isbn %d" %(self.titulo, self.isbn))


# In[3]:


livro1 = Livro()


# In[5]:


type(livro1)


# In[7]:


type(Livro())


# In[8]:


print(livro1.titulo)


# In[9]:


print(livro1.isbn)


# In[11]:


#Pressione tab
livro1.imprime()


# In[13]:


class Livro():
    
    def __init__(self, titulo, isbn):
        self.titulo = titulo
        self.isbn = isbn
        print("Construtor criou com sucesso.")
        
    def imprime(self, titulo, isbn):
        print("Foi criado o livro %s com o isbn %d"%(titulo, isbn))


# In[14]:


livro2 = Livro("A menina que roubava livros", "983000")


# In[15]:


livro2.titulo


# In[16]:


livro2.isbn


# In[19]:


livro2.imprime("A menina que roubava livros", 983000)


# In[20]:


class cachorro():
    def __init__(self, raca):
        self.raca = raca
        print("Construtor utilizado para criar um objeto")


# In[21]:


rex = cachorro("Labrador")


# In[22]:


rex.raca


# In[23]:


jhonny = cachorro("vira-lata")


# In[24]:


jhonny.raca


# In[25]:


rex.raca


# In[2]:


#Criando um objeto sem especificação
class Carro():
    pass

palio = Carro()

print(type(palio))


# In[3]:


class Estudantes():
    def __init__(self, nome, idade, nota):
        self.nome = nome
        self.idade = idade
        self.nota = nota


# In[4]:


estudante1 = Estudantes("pelé", 28, 10.0)


# In[6]:


print(estudante1.nome)


# In[7]:


print(estudante1.idade)


# In[8]:


print(estudante1.nota)


# In[19]:


class Funcionarios():
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
        
    def lista_func(self, nome, salario):
        print("O nome do funcionário é " + nome + " e o salário é: " + str(salario))


# In[24]:


funcionario1 = Funcionarios("Lucas", 25.000)


# In[21]:


funcionario1.salario


# In[22]:


funcionario1.lista_func("Lucas", 25.000)


# In[26]:


#Usando atributos com attr
hasattr(funcionario1, "nome") #Tem o atributo nome? 


# In[27]:


hasattr(funcionario1, "salario") #Tem o atributo salario? 


# In[28]:


setattr(funcionario1, "salario", 23.000)


# In[29]:


hasattr(funcionario1, "salario") 


# In[30]:


getattr(funcionario1, "salario") #recebe o valor do atributo


# In[31]:


delattr(funcionario1, "salario") #deleta o valor do atributo


# In[32]:


hasattr(funcionario1, "salario")


# In[ ]:




