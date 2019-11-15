#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Calculating Monthly Payment

loanAmount = eval(input("Enter The Loan Amount: "))
annualInterestRate = eval(input("Enter The Annual Interest Rate in %: "))
numberOfPayments = eval(input("Enter Number of Payments: "))

monthlyInterestRate = annualInterestRate/1200
monthlyPayment = ((monthlyInterestRate*((1+monthlyInterestRate)**numberOfPayments))/(((1+monthlyInterestRate)**numberOfPayments)-1))*loanAmount
amountPaidBack = monthlyPayment*numberOfPayments
interestPaid = amountPaidBack - loanAmount

print("Monthly Payment: ",round(monthlyPayment,2))
print("Amount Paid Back: ",round(amountPaidBack,2))
print("Interest Paid",round(interestPaid,2))


# In[ ]:




