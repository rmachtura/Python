#!/usr/bin/env python
# coding: utf-8

# # Métodos

# In[1]:


lista = [10, -2, 30, 45, 200]


# In[2]:


lista.append(20)


# In[3]:


print(lista)


# In[5]:


lista.count(10)


# In[6]:


help(lista.count)


# In[8]:


#Metodos e atributos
dir(lista)


# In[9]:


a = 'string isso é'


# In[10]:


print(a.split())


# In[11]:


help(a.split)


# #     -- FUNÇÕES --

# In[14]:


def primeiraFunc():
    print("Hello world!!")


# In[15]:


primeiraFunc()


# In[16]:


def primeiraFunc(nome):
    print("Hello %s" %(nome))


# In[18]:


primeiraFunc("Rafael")


# In[21]:


def funcLeitura():
    for i in range(0, 5):
        print("Numero " + str(i))


# In[22]:


funcLeitura()


# In[23]:


def addNum(firstNum, secondNum):
    print('O primeiro numero é %s' %(firstNum))
    print('O segundo numero é %r' %(secondNum))
    print("A soma é:", firstNum + secondNum)


# In[24]:


addNum(2,2)


# In[25]:


var_global = 10
def multiply(num1, num2):
    var_global = num1 * num2
    print(var_global)


# In[26]:


multiply(5,25)


# In[27]:


print(var_global)


# In[31]:


#Funções built-in
abs(-56)


# In[29]:


abs(23)


# In[30]:


bool(1)


# In[32]:


idade = input("Digite sua idade: ")
if idade > 13:
    print("Voce pode usar!")


# In[34]:


idade = int(input("Digite sua idade:"))
if idade > 13:
    print("Você pode usar!")


# In[3]:


valor = float(input("Digite o valor desejado: "))
if valor > 15.0:
    print("Valor acessível! ")


# In[4]:


float("123.455")


# In[5]:


str(14)


# In[6]:


len([14,15,16])


# In[7]:


array = ['a', 'b', 'c']


# In[8]:


max(array)


# In[9]:


min(array)


# In[11]:


array.append(['d', 'e', 'f', 'g'])


# In[17]:


array = ['a', 'b', 'c', 'd', 'A', 'B', 'C', 'D']


# In[18]:


max(array)


# In[19]:


min(array)


# In[20]:


list1 = [23, 32, 34, 45]


# In[21]:


sum(list1)


# In[22]:


import math
def numPrimo(num):
    '''
    verificando se num é primo
    '''
    if (num % 2) == 0 and num > 2:
        return "Este número não é primo"
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if(num % i) == 0:
            return "Esse numero não é primo"
    return "Este numero é primo"


# In[25]:


numPrimo(541)


# In[26]:


numPrimo(542)


# In[27]:


def split_string(text):
    return text.split(" ")


# In[28]:


texto = "Função útil para separar grandes volumes de dados."


# In[29]:


split_string(texto)


# In[30]:


token = split_string(texto)


# In[31]:


token


# In[32]:


caixa_baixa = "ESSE TEXTO DEVERIA ESTAR EM LowerCase"


# In[34]:


def lower_case(texto):
    return texto.lower()


# In[35]:


lower_case(caixa_baixa)


# In[37]:


lowercased_string = lower_case(caixa_baixa)


# In[38]:


lowercased_string


# In[39]:


#Quando eu não sei o numero de parâmetros que serão recebidos
def printVarInfo(arg1, *vartuple):
    print("O parâmetro passado foi: ", arg1)
    
    for item in vartuple:
        print("Os parâmetros passados foram: ", item)
    return;


# In[40]:


printVarInfo("texto")


# In[41]:


printVarInfo(1, 2, 3, 4, 5)


#     -- Expressões Lambda --

# In[42]:


lambda x: x**2


# In[43]:


def potencia(num):
    result = num ** 2
    return result


# In[44]:


potencia(5)


# In[45]:


def potencia(num):
    return num ** 2


# In[46]:


potencia(5)


# In[47]:


def potencia(num): return num**2


# In[48]:


potencia(5)


# In[49]:


potencia = lambda num: num ** 2


# In[50]:


potencia(5)


# In[51]:


Par = lambda x: x%2==0


# In[52]:


Par(2)


# In[53]:


Par(3)


# In[54]:


first = lambda s: s[0]


# In[56]:


first("Python")


# In[58]:


reverso = lambda r: r[::-1]


# In[60]:


reverso("Python")


# In[61]:


addNum = lambda x,y:x+y


# In[62]:


addNum(2,3)


# In[ ]:




