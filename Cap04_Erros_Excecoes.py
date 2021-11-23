#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Erro normalmente é de sintaxe
print('ola)


# In[4]:


def numDiv(num1, num2):
    print(num1 / num2)


# In[5]:


numDiv(4,2)


# In[7]:


#Exceção normalmente alguma regra ou condição não prevista
numDiv(4,0)


# # Try, Except e Finally

# In[8]:


8 + 's'


# In[9]:


try:
    8 + 's'
except TypeError:
    print("Operação não permitida")


# In[10]:


try:
    f = open('arquivos/testandoerros.txt', 'w')
    f.write("Gravando no arquivo")
except IOError:
    print("Arquivo não encontrado ou não pode ser salvo")
else:
    print("Arquivo salvo com sucesso")
    f.close()


# In[11]:


try:
    f = open('arquivos/testandoerros', 'r')
except IOError:
    print("Erro: arquivo não encontrado")
else:
    print("Conteúdo do arquivo:", f.read())
    f.close()


# In[12]:


try:
    f = open('arquivos/testandoerros.txt', 'w')
    f.write("Gravando mais dados")
except IOError:
    print("Erro. Arquivo não encontrado")
else:
    print("arquivo salvo com sucesso")
finally:
    print("SEMPRE HAVERÁ ESSA EXECUÇÃO")


# In[17]:


def askint():
    try:
        val = int((input("Digite um número: ")))
    except UnboundLocalError:
        print("Vc não digitou um número!")
    finally:
        print("Obrigado")
    print(val)


# In[18]:


askint()


# In[19]:


askint()


# In[20]:


def askint():
    try:
        val = int((input("Digite um número: ")))
    except:
        print("Vc não digitou um número!")
        val = int((input("Digite um número: ")))
    finally:
        print("Obrigado")
    print(val)


# In[21]:


askint()


# In[22]:


def askint():
    while True:
        try:
            val = int((input("Digite um numero: ")))
        except:
            print("Vc não digitou um numero!")
            continue
        else:
            print("Obrigado por digitar um numero")
            break
        finally:
            print("Fim da execução")
        print(val)


# In[23]:


askint()


# In[25]:


tuple = (1,2,3,4,5)
try:
    tuple.append(6)
    for each in tuple:
        print(each)
except AttributeError as e:
    print("Erro", e)
except IOError as e:
    print("Erro de I/O:", e)


# In[ ]:





# In[ ]:




