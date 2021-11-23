#!/usr/bin/env python
# coding: utf-8

# ## Map

# #Map vai aplicar uma função a cada elemento de uma lista e devolve uma lista. map(funcao, lista)

# In[1]:


def quadrado(numero):
    return (numero ** 2)


# In[3]:


quadrado(8)


# In[4]:


lista = [2,4,6,8,10]


# In[5]:


#Não sei pq não funcionou. R. pq a função retorna um iterator e não uma lista
map(quadrado, lista)


# In[11]:


#Convertendo em lista, o resultado é o correto
list(map(quadrado, lista))


# In[6]:


def fahrenheit(t):
    return((float(9)/5)*t + 32)


# In[7]:


def celsius(t):
    return(float(5)/9)*(t-32)


# In[8]:


temperaturas = [0,2.75,22,45,100]


# In[12]:


list(map(fahrenheit, temperaturas))


# In[13]:


list(map(celsius, temperaturas))


# In[14]:


for temp in map(celsius, temperaturas):
    print(temp)


# In[15]:


for temp in map(fahrenheit, temperaturas):
    print(temp)


# In[16]:


map(lambda x: (5.0/9)*(x-32), temperaturas)


# In[17]:


list(map(lambda x: (5.0/9)*(x-32), temperaturas))


# In[20]:


a = [1,2,3,4,5]
b = [6,7,8,9,10]
c = [11,12,13,14,15]


# In[19]:


list(map(lambda x,y:x+y, a, b))


# In[21]:


list(map(lambda x,y,z:x+y+z, a, b, c))


# ## Reduce 

# #Devolve apenas um valor. Ele aplica a função a todos os elementos da lista. reduce(funcao, lista)

# In[4]:


#Tem que importar de functools, mas é considerada built-in
from functools import reduce


# In[23]:


lista = [12,23,45,89]


# In[24]:


def soma(v1,v2):
    return v1+v2


# In[26]:


#O que ela faz? R. Nesse caso a soma de todos os valores da lista: 12+23=35+45=80+89=169
reduce(soma, lista)


# In[28]:


#Interessante mas não foi explicado nessa aula. Pelo jeito importou a função Image de IPython para exibição de imagens
from IPython.display import Image
Image('arquivos/reduce.png')


# In[6]:


lst = [20,30]
reduce(lambda x,y:x+y, lst)


# In[7]:


max_find2 = lambda a,b: a if (a > b) else b


# In[8]:


type(max_find2)


# In[9]:


reduce(max_find2, lst)


# #Função Filter vai retornar o valor quando for true. filter(funcao, lista)

# In[39]:


def verificaPar(num):
    if num % 2 == 0:
        return True
    else:
        return False


# In[40]:


verificaPar(25)


# In[41]:


verificaPar(26)


# In[42]:


lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]


# In[43]:


print(lista)


# In[44]:


filter(verificaPar, lista)


# In[45]:


list(filter(verificaPar, lista))


# In[46]:


list(filter(lambda x: x%2==0, lista))


# In[47]:


list(filter(lambda x: x>8, lista))


# # List Comprehension

# #Grande parte dos cientistas de dados nao usam essa forma, apesar de ser mais rapida do que map ou reduce.
# Basicamente ela é um loop for dentro de []

# In[48]:


lst = [x for x in 'Python']


# In[49]:


lst


# In[50]:


type(lst)


# In[51]:


lst = [x**2 for x in range(0,100)]


# In[53]:


print(lst)


# In[54]:


lst = [x for x in range(11) if x % 2 == 0]


# In[55]:


lst


# In[58]:


celsius = [10, 25.5, 32.0]
fahrenheit = [((float(9)/5)*temp + 32) for temp in celsius]


# In[59]:


fahrenheit


# In[60]:


lst = [x**2 for x in [x**2 for x in range(11)]]


# In[61]:


lst


# #Zip - Ele "junta" as duas listas, traz o item 1 da lista 1 junto com o item 1 da lista 2

# In[1]:


x = [1,2,3]
y = [4,5,6]


# In[2]:


zip(x,y)


# In[3]:


list(zip(x,y))


# In[1]:


type(list)


# In[2]:


list(zip("ABCD", '123'))


# In[3]:


d1 = {'a':1,'b':2}
d2 = {'c':4, 'd':5}


# In[4]:


list(zip(d1,d2))


# In[10]:


list(zip(d1,d2.values()))


# In[7]:


list(zip(d1.values(),d2.values()))


# In[15]:


def trocaValores(d1,d2):
    dicTemp = {}
    
    for d1key, d2val in zip(d1,d2.values()):
        dicTemp[d1key] = d2val
        
    return dicTemp


# In[16]:


trocaValores(d1,d2)


# #Enumerate - Retorna o indice e o elemento da lista

# In[17]:


seq = ['a', 'b', 'c']


# In[18]:


enumerate(seq)


# In[19]:


list(enumerate(seq))


# In[20]:


for indice, valor in enumerate(seq):
    print(indice, valor)


# In[21]:


for indice, valor in enumerate(seq):
    if indice >=2:
        break
    else:
        print(valor)


# In[22]:


lista = ['marketing', 'tecnologia', 'business']


# In[23]:


for i, item in enumerate(lista):
    print(i,item)


# In[24]:


for i, item in enumerate('Python é maravilhoso'):
    print(i, item)


# In[25]:


for i, item in enumerate(range(0,11)):
    print(i,item)


# In[ ]:




