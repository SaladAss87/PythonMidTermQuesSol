#!/usr/bin/env python
# coding: utf-8

# In[11]:


#Deposit Amount
#Function of Calculating Present Deposit Amount

def presentValue(futureValue,annualInterestRate,numberOfYears):
    presentValue = futureValue / (pow((1+annualInterestRate),numberOfYears))
    return presentValue
def main():
    futureValue = eval(input("Future Value That You Want in The Account: "))
    annualInterestRate = eval(input("Enter Interest rate in Decimal Form,such as .042: "))
    numberOfYears = eval(input("Enter The Number of Years You Want Keep The Money In Account:"))
    depositAmount = presentValue(futureValue,annualInterestRate,numberOfYears)
    print("You need to deposit",round(depositAmount,2))
main()


# In[ ]:





# In[ ]:




