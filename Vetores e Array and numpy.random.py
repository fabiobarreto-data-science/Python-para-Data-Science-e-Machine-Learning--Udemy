#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np


# In[4]:


minha_lista = [1,2,3]


# In[6]:


minha_lista


# In[8]:


np.array(minha_lista) #Vai converter minha lista em um Array de Python


# In[41]:


minha_matriz = [[1,2,3], [4,5,6],[7,8,9]]


# In[42]:


minha_matriz


# In[43]:


np.array(minha_matriz)


# In[16]:


np.arange(0, 10, 2) #Cria uma sequência de números pulando de acordo com a constante dada


# In[17]:


np.zeros(5)


# In[19]:


arr = np.zeros((5,5))


# In[21]:


arr


# In[22]:


np.ones(10)


# In[24]:


arr2 = np.ones((10,10))


# In[26]:


arr2


# In[28]:


np.eye(5) # Cria uma matrix identidade


# In[30]:


np.linspace(0,10,5) # Números igualmente espaçados


# In[32]:


np.random.rand(5) # Números entre 0 e 1


# In[34]:


np.random.rand(5)*100


# In[40]:


np.random.rand(5,5) # 5 Linhas e 5 colunas


# In[46]:


np.random.rand(5,5,5) # Matriz de 3 dimensões


# In[48]:


np.random.randn(4) # Distribuição Gauciana (ver em estatística)


# In[50]:


np.random.randint(0,100,10) # Tirei 10 números dentro intervalo de 100 números.


# In[52]:


arr3 = np.random.rand(25)


# In[54]:


arr3


# In[69]:


arr3.reshape((5,5))


# In[70]:


arr3.shape


# In[72]:


arr.shape


# In[74]:


arr3.max()


# In[76]:


arr3.min()


# In[78]:


arr3.argmax() # Vai retornar o índice na qual o maior elemento se encontra.


# In[80]:


arr3.argmin() # Vai retornar o índice na qual o menor elemento se encontra.

