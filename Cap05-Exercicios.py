#!/usr/bin/env python
# coding: utf-8

# # <font color='blue'>Data Science Academy - Python Fundamentos - Capítulo 5</font>
# 
# ## Download: http://github.com/dsacademybr

# In[1]:


# Versão da Linguagem Python
from platform import python_version
print('Versão da Linguagem Python Usada Neste Jupyter Notebook:', python_version())


# ## Exercícios

# In[2]:


# Exercício 1 - Crie um objeto a partir da classe abaixo, chamado roc1, passando 2 parâmetros e depois faça uma chamada
# aos atributos e métodos
from math import sqrt

class Rocket():
     
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def move_rocket(self, x_increment=0, y_increment=1):
        self.x += x_increment
        self.y += y_increment
        
    def print_rocket(self):
        print(self.x, self.y)
        


# In[3]:


roc1 = Rocket(2, 4)


# In[4]:


roc1.move_rocket()


# In[5]:


roc1.print_rocket()


# In[6]:


roc1.x


# In[7]:


roc1.y


# In[9]:


roc1.print_rocket()


# In[3]:


# Exercício 2 - Crie uma classe chamada Pessoa() com os atributos: nome, cidade, telefone e e-mail. Use pelo menos 2
# métodos especiais na sua classe. Crie um objeto da sua classe e faça uma chamada a pelo menos um dos seus métodos
# especiais.


# In[14]:


class Pessoa():
    def __init__(self, nome, cidade, telefone, email):
        self.nome = nome
        self.cidade = cidade
        self.telefone = telefone
        self.email = email
        
    def __str__(self):
        return("A pessoa cadastrada possui o nome: %s, mora na cidade: %s, tem o telefone: %s e o email: %s")         %(self.nome, self.cidade, self.telefone, self.email)


# In[15]:


Pessoa1 = Pessoa("Rafael", "Cedral", 17997736374, "rmachtura@gmail.com")


# In[16]:


print(Pessoa1)


# In[17]:


str(Pessoa1)


# In[4]:


# Exercício 3 - Crie a classe Smartphone com 2 atributos, tamanho e interface e crie a classe MP3Player com os 
# atributos capacidade. A classe MP3player deve herdar os atributos da classe Smartphone.


# In[32]:


class Smartphone(object):
    def __init__(self, tamanho, interface):
        self.tamanho = tamanho
        self.interface = interface


# In[34]:


class MP3Player(Smartphone):
    def __init__(self, capacidade, tamanho = "pequeno", interface = "Led"):
        self.capacidade = capacidade
        Smartphone.__init__(self, tamanho, interface)
        
    def printMp3(self):
        print("Valores para o objeto criado: %s %s %s"  %(self.tamanho, self.interface, self.capacidade))


# In[35]:


Smart = Smartphone(3, "Android")


# In[36]:


mp3 = MP3Player(5.0)


# In[37]:


mp3.printMp3()


# ### FIM

# ### Obrigado
# 
# ### Visite o Blog da Data Science Academy - <a href="http://blog.dsacademy.com.br">Blog DSA</a>
