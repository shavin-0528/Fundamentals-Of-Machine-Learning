#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
a=np.array([1,2,3,4,5])
print(a)


# In[6]:


import numpy as np
a=[1,2,3,4]
print(a)


# In[18]:


import sys
s=range(10)
print("The size of elements list in bytes",sys.getsizeof(s))
print("The size of whole elements list in bytes",sys.getsizeof(s)*len(s))


# In[11]:


import numpy as np
a=np.array(2)
print(a)


# In[20]:


import numpy as np
a=np.array([[1,2,3],[4,5,6]])
print(a)


# In[15]:


import numpy as np
a=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[0,9,8]]])
print(a)


# In[17]:


import numpy as np
a=np.zeros(5)
print(a)


# 

# In[19]:


import numpy as np
a=np.zeros([5,2])
print(a)


# In[21]:


import numpy as np
a=np.empty(6)
print(a)


# In[27]:


import numpy as np
a=np.eye(3)
print(a)


# In[30]:


import numpy as np
arr1 = np.array([1, 2, 3], dtype=np.float64) 
arr2 = np.array([1, 2, 3], dtype=np.int32) 
print(arr1.dtype) 
print(arr2.dtype)


# In[31]:


import numpy as np
arr = np.array([1, 2, 3]) 
print("Before", arr, arr.dtype) 
new_arr = arr.astype('f') 
print("After", new_arr, new_arr.dtype) 


# In[36]:


import numpy as np
arr1 = np.arange(10) 
arr2 = np.random. randn (10) 
print("arr1", arr1, arr1.dtype) 
print("arr2", arr2, arr2.dtype) 
new_arr = arr1.astype (arr2.dtype) 
print("New Array", new_arr, new_arr.dtype) 


# In[37]:


import numpy as np
str_arr = np.array(['hello', 'world', 'numpy)']) 
print(str_arr)


# In[38]:


a = np.array([1., 2., 3., 4.]) 
b = np.array([5., 6., 7., 8.]) 
print(a + b) 
print(a - b) 
print(a + b)  
print(a/b)  
print(a ** b)  


# In[39]:


import numpy as np 
arr = np.arange(12) 
newarr = arr.reshape(4, 3) 
print(newarr) 
newarr = arr.reshape((4, 3), order='F')
print("\n", newarr) 


# In[41]:


import numpy as np 
arr = np.array([[1, 2, 3, 4,9,10], [5, 6, 7, 8,11,12]]) 
print(arr) 
newarr = arr. reshape (3, 2, 2) 
print("\n", newarr) 


# In[45]:


original_array = np.array([[10, 20], [30, 40]])
print("O array:\n", original_array) 
flattened_array = original_array.flatten()
flattened_array[0] = 999 
print("f array:", flattened_array) 
print("O array:", original_array) 
raveled_array = original_array.ravel() 
raveled_array [1] = 888 
print("R array:", raveled_array) 
print("o array:", original_array) 


# In[49]:


import numpy as np
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[2, 1], [3, 5]]) 
less_than = arr1 < arr2 
greater_than=arr1>arr2
equal_to = arr1 == arr2 
print("Greater than:", greater_than)
print("\nLess than:", less_than) 
print("\nEqual to: ", equal_to) 
arr3 = np.array([1, 2, 3]) 
arr4 = np.array([1, 2, 3]) 
arr5 = np.array([1, 2, 4]) 
result1= np.array_equal(arr3, arr4)
result2 = np.array_equal(arr3, arr5) 
print("\nArray 1:", result1) 
print("Array 2:", result2) 


# In[51]:


import numpy as np
x = np.arange(10) 
print("x= ",x)
print("\n x= ",x[:5]) 
print("\n x= ",x[5:]) 
print("\n x= ",x[4:7]) 


# In[52]:


import numpy as np
x = np.arange(10) 
print(x) 
x[5] = 2 
print("\n  x1",x) 
x[::2] = 100 
print("\n x2",x) 


# In[53]:


x2 = np.array([[12, 5, 2, 4], [ 7, 6, 8, 8]])
print(x2[0])


# In[54]:


x2 = np.array([[12, 5, 2, 4], [7, 6, 8, 8], [1, 6, 7, 7]]) 
print("x2= ",x2)  
print("\n x2[:2, :3] = \n",x2[:2, :3])
print("\n x2[:3, ::2]=\n",x2[:3, ::2])
print("\n x2[::-1,::-1]= \n",x2[::-1, ::-1])


# In[55]:


import numpy as np 
a = np.arange(12). reshape (3,4) 
print("a= \n",a) 
b = a > 4 
print("b= \n", b) 
print("a[b]= \n",a[b]) # 1d array 
a [b] = 1 
print("a= \n",a) 


# In[58]:


import numpy as np 
arr = np.arange(12).reshape((3, 4)) 
print(arr) 
print("Transpose using .T") 
print(arr.T) 
print("Transpose using the transpose() function")


# In[ ]:




