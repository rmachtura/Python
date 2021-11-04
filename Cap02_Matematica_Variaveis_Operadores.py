#!/usr/bin/env python
# coding: utf-8

# Primeira aula de Python da DSA. Learn Life Mode. Matematica e funções

# In[1]:


4 + 4


# In[2]:


4 - 3


# In[3]:


3 * 3


# In[4]:


3 / 2


# In[8]:


#Potência
4 ** 2


# In[9]:


#Modulo
10 % 3


# In[12]:


#Função Type
type(5)
type(2.5)
a = 'Isso é uma string'
type(a)


# In[13]:


3.1 + 6.4


# In[14]:


4 + 4.0


# In[16]:


#Usando uma barra para divir inteiros, ele devolve float
4 / 2


# In[17]:


#Usando duas barras para dividir inteiros, ele devolve inteiro
4 // 2


# In[18]:


4 / 3.0


# In[19]:


4 // 3.0


# In[20]:


#conversao
float(5)


# In[21]:


int(5.0)


# In[22]:


#Ele não faz o arredondamento
int(6.5)


# In[23]:


int(6.8)


# In[24]:


hex(394)


# In[25]:


bin(390)


# In[26]:


#Retorna valor absoluto, retira o negativo
abs(-8)


# In[27]:


abs(8)


# In[28]:


#Retorna valor com arredondamento
round(3.1455)


# In[29]:


round(3.956)


# In[30]:


#Potência igual 4**2
pow(4,2)


# In[31]:


pow(5,3)


# Segunda aula do Cap2, variaveis e operadores. Life Learn Mode

# In[33]:


#atribuição de variavel
var_teste = 1
print(var_teste)


# In[34]:


#imprimindo valor da variavel
var_teste


# In[35]:


#variavel sem definição exibe erro: NameError: name 'my_var' is not defined
my_var


# In[36]:


var_teste = 5


# In[37]:


var_teste


# In[38]:


type(var_teste)


# In[39]:


var_teste = 'string na variavel'


# In[40]:


type(var_teste)


# In[41]:


var_teste = 2.4


# In[42]:


type(var_teste)


# In[43]:


pessoa1, pessoa2, pessoa3 = 'Maria', 'Rafael', 'José'


# In[44]:


type(pessoa1)


# In[45]:


pessoa1


# In[46]:


fruta1 = fruta2 = fruta3 = 'Laranja'


# In[47]:


fruta1


# In[48]:


fruta2


# In[49]:


type(fruta1)


# In[50]:


x1 = 50


# In[51]:


x1


# In[52]:


type(x1)


# In[53]:


x2 = 'Texto com numeros 50'


# In[54]:


type(x2)


# In[55]:


x2


# In[56]:


#palavras reservadas pela linguagem erro: SyntaxError: invalid syntax
break = 1


# In[57]:


largura = 2
altura = 4


# In[58]:


area = largura * altura


# In[59]:


area


# In[60]:


type(area)


# In[61]:


perimetro = 2 * largura + 2 * altura


# In[62]:


perimetro


# In[63]:


type(perimetro)


# In[64]:


#Ordem dos operadores deve ser lembrada
perimetro = 2 * (largura + 2) * altura


# In[65]:


perimetro


# In[66]:


idade1 = 25
idade2 = 20


# In[67]:


idade1 * idade2


# In[68]:


idade1 / idade2


# In[70]:


#resto da divisão
idade1 % idade2


# In[71]:


#concatenar
nome = "Steve"


# In[72]:


sobrenome = "Jobs"


# In[73]:


nome + sobrenome


# In[74]:


nome + " " + sobrenome


# Terceira aula do cap2 -- Strings

# In[76]:


#uma palavra
'Oi'


# In[77]:


#Uma frase
'Uma frase como string'


# In[78]:


"Podemos usar aspas duplas para string tbm"


# In[79]:


#Podemos usar aspas duplas e simples
"Texto com aspas duplas e 'simples'"


# In[80]:


print('Testando função de imprimir com aspas simples')


# In[81]:


print("Testando função de imprimir com aspas duplas")


# In[82]:


print("Testando string \n com contra barra \n N")


# In[83]:


#em branco, mas é um caracter
print('\n')


# In[84]:


#Atribuindo strin
s = 'Data science academy'


# In[85]:


print(s)


# In[86]:


s[0]


# In[87]:


s[5]


# In[93]:


s[2]


# In[95]:


#retornar todos os elementos a partir de um certo ponto
s[5:]


# In[97]:


#Retornar tudo até certa posição
s[:5]


# In[98]:


s[:]


# In[100]:


#retorna indexação de trás para frente
s[-5]


# In[101]:


#Retorna tudo menos as ultimas 5
s[:-5]


# In[102]:


#retornar todos os elementos a partir de um certo ponto de trás pra frente
s[-5:]


# In[103]:


#Ele traz os caracteres saltando uma posição, ou seja, um por vez. Normal, padrão
s[::1]


# In[104]:


#Ele traz os caracteres saltando duas posições, ou seja, ele pula um caracter
s[::2]


# In[105]:


#Ele traz pulando uma posição, porém de trás para frente
s[::-1]


# In[106]:


#Ele traz pulando duas posições, porém de trás para frente
s[::-2]


# In[107]:


s


# In[108]:


#Strings são imutáveis, erro: TypeError: 'str' object does not support item assignment
s[0] = 'x'


# In[110]:


#Posso concatenar, porém não altera a string original
s + ' Academia de dados'


# In[111]:


s


# In[114]:


#Para atribuir deve-se
s = s + ' Academia de dados'


# In[113]:


s


# In[115]:


#Podemos utilizar operações matematicos, exibe três vezes a variável
s * 3


# In[116]:


s


# In[117]:


letra = 'w'


# In[118]:


letra * 3


# In[119]:


s.upper()


# In[120]:


s = 'Data Science Academy'


# In[121]:


s


# In[122]:


s.upper()


# In[125]:


#usando tab após o ponto exibe a lista de atributos
s.lower()


# In[126]:


#Sem parametros, é o padrão, espaço em branco
s.split()


# In[127]:


s


# In[128]:


s.split('y')


# In[129]:


s.split('a')


# In[130]:


s = 'Seja bem vindo ao mundo de Python'


# In[131]:


#Primeira letra maiuscula
s.capitalize()


# In[133]:


#Contador de caracteres
s.count('a')


# In[134]:


s.find('y')


# In[135]:


s.islower()


# In[136]:


s.isupper()


# In[137]:


s


# In[138]:


s.endswith('J')


# In[140]:


s.endswith('n')


# In[141]:


s.isspace()


# In[142]:


print("Python" == "R")


# In[143]:


print(s == 'J')


# In[144]:


print("S" == "S")


# Estrutura de dados -- Listas

# In[145]:


#Criando uma lista de um elemento
lista_mercado = ["Ovos, tomate, farinha, açucar"]


# In[146]:


print(lista_mercado)


# In[149]:


#Criando uma lista de varios elementos
lista_mercado2 = ["Ovos", "Tomate", "Farinha", "Açucar"]


# In[148]:


print(lista_mercado2)


# In[156]:


lista_mercado.count


# In[157]:


lista_mercado2.count


# In[158]:


lista_mercado[0]


# In[159]:


lista_mercado2[0]


# In[160]:


lista3 = [1, 2, 'string', "string2"]


# In[161]:


print(lista3)


# In[162]:


item1 = lista3[0]
item2 = lista3[1]
item3 = lista3[2]
item4 = lista3[3]


# In[163]:


print(item1, item2, item3, item4)


# In[165]:


lista_mercado2


# In[167]:


lista_mercado2[2] = "chocolate"


# In[168]:


print(lista_mercado2)


# In[169]:


del lista_mercado2[3]


# In[171]:


print(lista_mercado2)


# In[172]:


#Lista aninhada. lista dentro de outra, uma matriz
listas = [[1,2,3], [50,60,70], ["string", "string2", "string3"]]


# In[173]:


print(listas)


# In[174]:


a = listas[0]


# In[175]:


print(a)


# In[176]:


b = a[0]


# In[177]:


print(b)


# In[178]:


list1 = listas[1]


# In[179]:


print(list1)


# In[180]:


valor_1_0 = list1[0]


# In[181]:


print(valor_1_0)


# In[182]:


print(listas)


# In[183]:


a = listas[0][0]


# In[184]:


print(a)


# In[185]:


b = listas[1][2]


# In[186]:


print(b)


# In[187]:


c = listas[1][1] + 40


# In[188]:


print(c)


# In[189]:


lista_s1 = [1, 2, 3]
lista_s2 = [4, 5, 6]


# In[190]:


lsita_total = lista_s1 + lista_s2


# In[191]:


lsita_total


# In[192]:


lista_teste_op = [100, 2, -5, 3.4]


# In[193]:


print(10 in lista_teste_op)


# In[194]:


print(100 in lista_teste_op)


# In[195]:


len(lista_teste_op)


# In[196]:


max(lista_teste_op)


# In[197]:


min(lista_teste_op)


# In[198]:


lista_mercado2.append('carne')


# In[199]:


print(lista_mercado2)


# In[201]:


lista_mercado2.count("carne")


# In[202]:


a = []


# In[203]:


print(a)


# In[204]:


a.append(10)


# In[205]:


print(a)


# In[206]:


old_list = [1,2,5,10]
new_list = []


# In[207]:


#Copiar itens de uma lista para outra
for item in old_list:
    new_list.append(item)


# In[208]:


print(new_list)


# In[209]:


print(old_list)


# In[210]:


cidades = ["Cedral", "Rio Preto", "Mauá"]
cidades.extend(["Itupeva", "Rio Claro"])


# In[211]:


print(cidades)


# In[212]:


cidades.index("Mauá")


# In[213]:


cidades.insert(2, "Fronteira")


# In[214]:


print(cidades)


# In[215]:


cidades.remove("Itupeva")


# In[216]:


cidades


# In[217]:


cidades.reverse()


# In[218]:


cidades


# In[219]:


x = [4, 3, 2, 1]


# In[220]:


x.sort()


# In[221]:


x


#     --- Aula de Dicionários ---

# In[1]:


#Lista
students_list = ["Mateus", 24, "Fernanda", 21, "Tamires", 30, "Cristiano", 25]


# In[2]:


students_list


# In[3]:


print(students_list)


# In[4]:


#Dicionario
students_dict = {"Mateus":24, "Fernanda":21, "Tamires":30, "Cristiano":25}


# In[5]:


print(students_dict)


# In[6]:


students_dict["Mateus"]


# In[7]:


#Adiciona item no dicionario
students_dict["Pedro"] = 23


# In[8]:


print(students_dict)


# In[9]:


students_dict["Pedro"]


# In[10]:


students_dict["Tamires"]


# In[11]:


students_dict["Rafael"] = 30


# In[12]:


students_dict


# In[13]:


print(students_dict)


# In[14]:


students_dict["Rafael"]


# In[15]:


students_dict


# In[16]:


print(students_dict)


# In[19]:


students_dict.items()


# In[20]:


students_dict.values()


# In[21]:


students_dict.clear()


# In[22]:


students_dict


# In[23]:


del students_dict


# In[24]:


students_dict


# In[25]:


estudantes = {"Mateus":24, "Fernanda":21, "Tamires":30, "Cristiano":25}


# In[26]:


estudantes


# In[27]:


len(estudantes)


# In[28]:


estudantes.items()


# In[29]:


estudantes.values()


# In[30]:


estudantes.keys()


# In[31]:


estudantes2 = {"Jorge": 32, "Gabriel":27, "Oswaldo":37, "João Martins":42}


# In[32]:


#Adicionar estudantes2 a estudantes
estudantes.update(estudantes2)


# In[33]:


estudantes


# In[34]:


dic1 = {}


# In[36]:


dic1["k1"] = 1


# In[37]:


dic1


# In[38]:


dic1[10] = 5


# In[39]:


dic1.values()


# In[41]:


#Tipos de dados diferentes
dic1


# In[42]:


dic1[8.2] = "Python"


# In[43]:


dic1


# In[44]:


dict1 = {}


# In[45]:


dict1["teste"] = 10
dict1[10] = "teste"


# In[46]:


dict1


# In[48]:


dict2 = {}


# In[49]:


dict2["key1"] = "Big Data"
dict2["key2"] = 10
dict2["key3"] = 9.2


# In[50]:


dict2


# In[51]:


#Dicionario de listas
dict3 = {"key1": 1230, "key2":[22,452,543,89], "key3":["Arroz", "Feijao", "Batata"]}


# In[52]:


dict3


# In[53]:


dict3["key2"]


# In[54]:


dict3["key3"][2].upper()


# In[55]:


#Colocar o valor na variavel
var1 = dict3['key2'][2] - 2


# In[56]:


var1


# In[57]:


#Atribuir valor
dict3['key2'][2] -= 2


# In[58]:


dict3["key2"]


# In[60]:


dict_aninhado = {"key1":{"key2_aninhada":{"key3_aninhada":"Dict aninhado em Python"}}}


# In[61]:


dict_aninhado


# In[63]:


dict_aninhado['key1']['key2_aninhada']['key3_aninhada']


# --Tuplas --

# In[64]:


#criando uma tupla - Tupla é IMUTÁVEL
tupla1 = ("Geografia", 23, "Matemática")


# In[65]:


tupla1


# In[66]:


tupla1.append("Elefantes")


# In[67]:


del tupla1("Geografia")


# In[68]:


tupla1 = ("chocolate")


# In[69]:


tupla1


# In[70]:


tupla1 = ("Geografia", 23, "Matemática")


# In[71]:


tupla1[0]


# In[72]:


len(tupla1)


# In[74]:


tupla1[1:]


# In[75]:


tupla1[:1]


# In[77]:


tupla1.index("Matemática")


# In[78]:


del tupla1


# In[79]:


t2 = ('A', "B", 'C')


# In[80]:


t2


# In[81]:


t2[0] = "Z"


# In[82]:


lista_t2 = list(t2)


# In[83]:


lista_t2


# In[84]:


lista_t2.append("Z")


# In[85]:


t2 = tuple(lista_t2)


# In[86]:


t2


#         --ITEM FINAL DO CAPITULO LABORATÓRIO 01   -- GAME --

# In[ ]:




