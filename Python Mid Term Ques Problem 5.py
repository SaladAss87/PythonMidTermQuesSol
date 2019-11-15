monthlyPayment=eval(input ("Enter value for monthly payment such as 100.00: "))
interestRate=eval(input ("Enter annual interest rate: "))
savingsAmount=0
month=1
while month<=6:
    j=1+(interestRate/(100*12))
    monthlyPayment=monthlyPayment*j
    savingsAmount=savingsAmount+monthlyPayment
    print(round(savingsAmount,3),round(monthlyPayment,2))
    month=month+1
