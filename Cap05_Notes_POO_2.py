#!/usr/bin/env python
# coding: utf-8

# # Metodos

# In[12]:


class Circulo():
    
    pi = 3.4
    
    def __init__(self, raio = 5):
        self.raio = raio
        
    def area(self):
        return (self.raio * self.raio) * Circulo.pi
        
    def setRaio(self, novo_raio):
        self.raio = novo_raio
            
    def getRaio(self):
        return self.raio


# In[13]:


circ = Circulo()


# In[14]:


circ.getRaio()


# In[15]:


circ.setRaio(10)


# In[16]:


circ.getRaio()


# In[17]:


circ.area()


# ## Herança

# In[18]:


class Animal():
    def __init__(self):
        print("Animal criado")
        
    def Identif(self):
        print("Animal")
        
    def comer(self):
        print("Comendo")


# In[19]:


class Cachorro(Animal):
    
    def __init__(self):
        Animal.__init__(self)
        print("Objeto cachorro criado.")
        
    def Identif(self):
        print("Cachorro")
        
    def latir(self):
        print("Au au!")


# In[20]:


jhonny = Cachorro()


# In[21]:


jhonny.Identif()


# In[22]:


jhonny.comer()


# In[23]:


jhonny.latir()


# ## Metodos especiais 

# In[24]:


#Metodos especiais são identificados por __NOME__ igual ao __init__


# In[25]:


class Livro():
    def __init__(self, titulo, autor, paginas):
        print("Livro criado.")
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        
    def __str__(self):
        return "Título: %s, autor: %s, páginas: %s"     %(self.titulo, self.autor, self.paginas)
    
    def __len__(self):
        return self.paginas
    
    def len(self):
        return print("Paginas do livro com metodo comum: ", self.paginas)


# In[26]:


livro1 = Livro("Os Lusíadas", "Luis de Camões", 8816)


# In[28]:


print(livro1) #Metodo __str__ é chamado ao chamar o print


# In[29]:


str(livro1)


# In[30]:


len(livro1)


# In[31]:


livro1.len()


# In[32]:


del livro1.paginas


# In[34]:


hasattr(livro1, "paginas")


# In[ ]:





# In[ ]:




