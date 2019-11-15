#!/usr/bin/env python
# coding: utf-8

# In[4]:


#Store Sales In Asterisks

store1Sales = eval(input("Enter Store 1 Sales: "))
store2Sales = eval(input("Enter Store 2 Sales: "))
store3Sales = eval(input("Enter Store 3 Sales: "))

#Store1
print("Store 1 Sales: ",end = '')
for i in range(round(store1Sales/100)):
    print("*", end = '')
print()

#Store2
print("Store 2 Sales: ",end = '')
for i in range(round(store2Sales/100)):
    print("*", end = '')
print()

#Store3
print("Store 3 Sales: ",end = '')
for i in range(round(store3Sales/100)):
    print("*", end = '')
print()


# In[ ]:




