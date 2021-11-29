#!/usr/bin/env python
# coding: utf-8

# # <font color='blue'>Data Science Academy - Python Fundamentos - Capítulo 4</font>
# 
# ## Download: http://github.com/dsacademybr

# In[1]:


# Versão da Linguagem Python
from platform import python_version
print('Versão da Linguagem Python Usada Neste Jupyter Notebook:', python_version())


# ## Exercícios 

# In[2]:


# Exercício 1 - Crie uma lista de 3 elementos e calcule a terceira potência de cada elemento.


# In[5]:


lst = [2,4,6]
list(map(lambda x:x**3, lst))


# In[6]:


# Exercício 2 - Reescreva o código abaixo, usando a função map(). O resultado final deve ser o mesmo!
palavras = 'A Data Science Academy oferce os melhores cursos de análise de dados do Brasil'.split()
resultado = [[w.upper(), w.lower(), len(w)] for w in palavras]
for i in resultado:
    print (i)


# In[12]:


list(map(lambda x:(x.upper(), x.lower(), len(x)), palavras))


# In[88]:


# Exercício 3 - Calcule a matriz transposta da matriz abaixo.
# Caso não saiba o que é matriz transposta, visite este link: https://pt.wikipedia.org/wiki/Matriz_transposta
# Matriz transposta é um conceito fundamental na construção de redes neurais artificiais, base de sistemas de IA.
matrix = [[1, 2],[3,4],[5,6],[7,8]]


# In[93]:


transpose = [[row[1] for row in matrix] for i in range(2)]
print(transpose)


# In[3]:


# Exercício 4 - Crie duas funções, uma para elevar um número ao quadrado e outra para elevar ao cubo. 
# Aplique as duas funções aos elementos da lista abaixo. 
# Obs: as duas funções devem ser aplicadas simultaneamente.
lista = [0, 1, 2, 3, 4]


# In[1]:


def quadrado(num):
    return num ** 2


# In[2]:


def cubo(num):
    return num ** 3


# In[13]:


list(map(lambda x:(quadrado(x), (cubo(x))), lista))


# In[14]:


# Exercício 5 - Abaixo você encontra duas listas. Faça com que cada elemento da listaA seja elevado 
# ao elemento correspondente na listaB.
listaA = [2, 3, 4]
listaB = [10, 11, 12]


# In[24]:


lst = [x**y for x,y in zip(listaA,listaB)]


# In[25]:


print(lst)


# In[29]:


# Exercício 6 - Considerando o range de valores abaixo, use a função filter() para retornar apenas os valores negativos.
range(-5, 5)


# In[38]:


list(filter(lambda x: x < 0, range(-5,5)))


# In[42]:


# Exercício 7 - Usando a função filter(), encontre os valores que são comuns às duas listas abaixo.
a = [1,2,3,5,7,9]
b = [2,3,5,6,7,8]


# In[94]:


list(filter(lambda x: x in a, b))


# In[54]:


# Exercício 8 - Considere o código abaixo. Obtenha o mesmo resultado usando o pacote time. 
# Não conhece o pacote time? Pesquise!
import datetime
print (datetime.datetime.now().strftime("%d/%m/%Y %H:%M"))


# In[96]:


import time
print(time.strftime("%d/%m/%Y %H:%M"))


# In[97]:


# Exercício 9 - Considere os dois dicionários abaixo. 
# Crie um terceiro dicionário com as chaves do dicionário 1 e os valores do dicionário 2.
dict1 = {'a':1,'b':2}
dict2 = {'c':4,'d':5}


# In[119]:


dict3 = dict(zip(dict1,dict2.values()))


# In[120]:


type(dict3)


# In[121]:


print(dict3)


# In[122]:


# Exercício 10 - Considere a lista abaixo e retorne apenas os elementos cujo índice for maior que 5.
lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']


# In[125]:


for indice, valor in enumerate(lista):
    if indice <= 5:
        continue
    else:
        print(valor)        


# # Fim

# ### Obrigado
# 
# ### Visite o Blog da Data Science Academy - <a href="http://blog.dsacademy.com.br">Blog DSA</a>
