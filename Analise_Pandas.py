#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd


# In[10]:


df = pd.read_csv(r'D:\Curso Python - Analise de Dados\cadastro_clientes.csv')


# In[ ]:


#exibir linhas
df.head(3)


# In[ ]:


#Dicionario {}
#Lista []
#Tuplas ()


# In[ ]:


# Operadores Relacionais (Comparação) 

"""
==   -> Igual a
!=   -> Diferente de
>    -> Maior que
<    -> Menor que
>=   -> Maior ou igual a
<=   -> Menor ou igual a


OPERADORES LÓGICOS

and  -> Retorna True se TODAS as condições forem verdadeiras
or   -> Retorna True se PELO MENOS UMA condição for verdadeira
not  -> Inverte o valor lógico da condição

OPERADORES DE ASSOCIAÇÃO

in      -> Verifica se o valor está presente
not in  -> Verifica se o valor NÃO está presente

OPERADORES DE IDENTIDADE

is      -> Mesmo objeto
is not  -> Objetos diferentes


- &     -> AND elemento a elemento
# - |   -> OR elemento a elemento
# - ~   -> NOT (negação)

"""


# In[17]:


# Filtrando apenas sexo 'Masculino' OBS : Isso não altera o valor original do Dataframe

df[df['Sexo'] == 'Masculino']


# In[ ]:


# Criar um novo df baseado no filtro sexo 'Masculino'

df_Masculino = df[df['Sexo'] == 'Masculino']


# In[ ]:


# Filtrando mais de um valor
# .isin função do python para filtrar valores

df[
    df['Estado'].isin(['RR','TO','PR'])   # Apenas filtra
]

df_Estado = df[
    df['Estado'].isin(['RR','TO','PR']) # Cria um dataframe df_estado
]


# In[ ]:


# Idade maior que 40

df[
    df['Idade'] > 40
]


# In[11]:


# Sexo Maculino e idade maior que 40 anos

df[
    (df['Sexo'] == 'Masculino') &
    (df['Idade'] > 40 )
]


# In[ ]:


# Parâmetro inplace=True aplica alterações diretamente no DataFrame original (sem precisar atribuir a outro objeto); inplace=False retorna uma cópia modificada.

df.rename(columns={'ID_Cliente':'ID'},inplace=False) # Apenas exibe a alteração sem modificar o df original
#df.rename(columns={'ID_Cliente':'ID'},inplace=True)  # Altera o df original


# In[ ]:


# Upper função para deixar em maiúsculo

df['Nome'] = df['Nome'].str.upper()

# Lower função para deixar em minúsculo

df['Nome'] = df['Nome'].str.lower()

# Capitalize função para deixar a primeira letra maiúscula
df['Nome'] = df['Nome'].str.capitalize()

# Title função para deixar a primeira letra de cada palavra maiúscula
df['Nome'] = df['Nome'].str.title()

# Strip função para remover espaços em branco no início e no final
df['Nome'] = df['Nome'].str.strip()

# Replacing função para substituir valores
df['Nome'] = df['Nome'].str.replace('a','@')  # Substitui todas as letras 'a' por '@'

