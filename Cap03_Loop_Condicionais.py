#!/usr/bin/env python
# coding: utf-8

# -- Cap03 -- Condicionais --

# In[5]:


if 5 > 2:
    print("Python fundamentos")


# In[6]:


if 5 < 2:
    print("Python fundamentos")
else:
    print("Algo está errado")


# In[7]:


6 > 3


# In[8]:


3 > 7


# In[9]:


4 < 8


# In[10]:


4 >= 4


# In[12]:


if 5 == 5:
    print("Testando python")


# In[14]:


if True:
    print("Python funciona")


# In[15]:


if False:
    print("not working")


# In[17]:


idade = 18
if idade > 17:
    print("Parece que funciona")


# In[18]:


Nome = "Bob"
if idade > 13:
    if Nome == "Bob":
        print("Ok, Bob, chega mais!")
    else:
        print("Nem vem Bob!")


# In[20]:


if idade >= 13 and Nome == "Bob":
    print("Chega mais")
else:
    print("Nem vem")


# In[21]:


if (idade >= 13) or (Nome == "Jó"):
    print("Chega não")


# In[22]:


dia = "Domingo"
if (dia == "Segunda"):
    print("Sol")
else:
    print("Chuva")


# In[23]:


if (dia == "Segunda"):
    print("Sol")
elif (dia == "Terça"):
    print("Nublado")
else:
    print("Chuva")


# In[24]:


idade = 18
nome = "Bob"
if idade > 17:
    print("Menor")


# In[25]:


if (idade <= 18) and (Nome == "Bob"):
    print("Venha")


# In[29]:


disciplina = input('Digite a disciplina: ')
nota_final = input('Digite a nota: ')
if (disciplina == "Geografia" and nota_final >= '70'):
    print("Passou")
else:
    print("Não passou")


# In[32]:


#Placeholder % e conversor de string para int
disciplina = input('Digite a disciplina: ')
nota_final = input('Digite a nota: ')
semestre = input('Semestre: ')
if (disciplina == 'Geografia' and nota_final >= '50' and int(semestre) != 1):
    print("Passou em %s com nota %r!" %(disciplina, nota_final))
else:
    print("Não passou")


#     -- Estruturas de repetição --

# In[35]:


numeros = [1, 5, 7, 9]
for numero in numeros:
    if (numero % 2):
        print(numero)
    else:
        print(numero - 1)


# In[37]:


tp = (2, 3, 4)
for i in tp:
    print(i)


# In[38]:


ListaDoMercado = ["Arroz", "Feijão", "Carne"]
for item in ListaDoMercado:
    print(item)


# In[39]:


for contador in range(0, 5):
    print(contador)


# In[40]:


#Verificando os numeros pares da lista, caso  o resto da divisão seja 0
lista = [0,1,2,3,4,5,6,7,8,9,10]
for i in lista:
    if (i % 2 == 0):
        print(i)


# In[42]:


for i in range(0, 101, 2):
    print(i)


# In[44]:


for caracter in "Pyhton é uma linguagem divertida -":
    print(caracter)


# In[45]:


#loop aninhado
for i in range(0,5):
    for a in range(0,5):
        print(a)


# In[46]:


listaB = [32,53,85,10,15,17,19]
soma = 0
for i in listaB:
    double_i = i * 2
    soma += double_i
    print(soma)


# In[47]:


listas = [[1,2,3], [10,11,12,13], [20,21,22,23]]
for item in listas:
    print(item)


# In[48]:


lista = [5,6,10,13,17]
count = 0
for item in lista:
    count += 1
    print(count)


# In[50]:


lst = [[1,2,3], [4,5,6], [7,8,9]]
primeira_linha = lst[1]
count = 0
for column in primeira_linha:
    count = count + 1
    print(count)


# In[51]:


listaC = [5,6,7,8,9]
for item in listaC:
    if (item == 5):
        print("Encontrado %s" %(item))


# In[52]:


#Padrão mostra a chave e não o valor
dict = {'k1':"chave1", 'k2':"chave2", 'k3':"Chave3"}
for item in dict:
    print(item)


# In[54]:


#metodo items do dicionario
for k,v in dict.items():
    print (k,v)


#     -- Loop While --

# In[1]:


counter = 0
while counter < 10:
    print(counter)
    counter = counter + 1


# In[2]:


x = 0
while x < 10:
    print("O valor de x é: ", x)
    print("x ainda é menor que 10, somando 1 a x")
    x += 1
else:
    print("Loop concluído")


# In[3]:


counter = 0
while counter < 100:
    if counter == 4:
        break
    else:
        pass
    print(counter)
    counter = counter + 1


# In[5]:


for verificador in "Python":
    if verificador == "h":
        continue
    print(verificador)


# In[8]:


for i in range(2,30):
    j = 2
    counter = 0
    while j < i:
        if i % j == 0:
            counter = 1
            j = j + 1
        else:
            j = j + 1
            
    if counter == 0:
        print(str(i) + "é um número primo")
        counter = 0
    else:
        counter = 0


#     -- RANGE --

# In[1]:


for i in range(50, 101, 2):
    print(i)


# In[2]:


for i in range(3, 6):
    print(i)


# In[3]:


for i in range(0, -20, -2):
    print(i)


# In[4]:


lista = ['morango', 'banana', 'abacaxi', 'uva']
lista_tamanho = len(lista)
for i in range(0, lista_tamanho):
    print(lista[i])


# In[5]:


type(range(0, 3))


# In[8]:


#Exercicio 6
contador = 0
while(contador < 100):
    if contador == 23:
        break
    else:
        print(contador)
        contador += 1


# In[10]:


#Exercicio 7
lista = []
var = 4
while(var <= 20):
    if var % 2 == 0:
        lista.append(var)
    var += 1
print(lista)

