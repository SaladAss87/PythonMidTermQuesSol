#Corporate Tax Rate
#Category List
print("1: Publicly Traded Company")
print("2: Non-Publicly Traded Company")
print("3: Publicly Traded Cigarette Company")
print("4: Mobile Phone Operator Company")
print("5: Publicly Traded Mobile Phone Company")

#Inputs
taxpayerCategory = eval(input("Enter Your Category Number: "))

#Calculating Tax Amount#

# 1. Publicly Traded Company
if taxpayerCategory == 1:
    dividendRate = eval(input("Did The Publicly Traded Company Declare Dividend? If Yes Then Enter the Rate in %: "))
    profitAmount = eval(input("Enter The Profit Amount: "))
    if dividendRate == 0:
        if profitAmount>1000000:
            netTax = profitAmount*.275
        elif profitAmount < 1000000:
            netTax = profitAmount*.255
    elif dividendRate > 30:
        if profitAmount>1000000:
            netTax = profitAmount*.2475
        elif profitAmount < 1000000:
            netTax = profitAmount*.2075
    elif dividendRate < 10:
        if profitAmount>1000000:
            netTax = profitAmount*.35
        elif profitAmount < 1000000:
            netTax = profitAmount*.30

# 2. Non Publicly Traded Company
if taxpayerCategory == 2:
    paidupCapitalThroughIPO = eval(input("How Much Share of your Paid Up Capital was Transfered through IPO? Enter the rate in %: "))
    profitAmount = eval(input("Enter The Profit Amount: "))
    if paidupCapitalThroughIPO >= 20:
        if profitAmount>1000000:
            taxBeforeRebate = profitAmount*.35
            netTax = taxBeforeRebate  - taxBeforeRebate*.10
        elif profitAmount < 1000000:
            taxBeforeRebate = profitAmount*.32
            netTax = taxBeforeRebate  - taxBeforeRebate*.10
        else:
            if profitAmount>1000000:
                netTax = profitAmount*.35
            elif profitAmount < 1000000:
                netTax = profitAmount*.32

# 3. Publicly Traded Cigarette Company
if taxpayerCategory == 3:
    dividendRate = eval(input("Did The Publicly Traded Cigarette Company Declare Dividend? If Yes Then Enter the Rate in %: "))
    profitAmount = eval(input("Enter The Profit Amount: "))
    if dividendRate == 0:
        if profitAmount>1000000:
            netTax = profitAmount*.40
        elif profitAmount < 1000000:
            netTax = profitAmount*.35
    elif dividendRate > 30:
        if profitAmount>1000000:
            netTax = profitAmount*.2475
        elif profitAmount < 1000000:
            netTax = profitAmount*.2075
    elif dividendRate < 10:
        if profitAmount>1000000:
            netTax = profitAmount*.35
        elif profitAmount < 1000000:
            netTax = profitAmount*.30
            
# 4. Mobile Phone Operator Company
if taxpayerCategory == 4:
    profitAmount = eval(input("Enter The Profit Amount: "))
    if profitAmount>1000000:
        netTax = profitAmount*.45
    elif profitAmount < 1000000:
        netTax = profitAmount*.40

# 5. Publicly Traded Mobile Company
if taxpayerCategory == 5:
    dividendRate = eval(input("Did The Publicly Traded Mobile Company Declare Dividend? If Yes Then Enter the Rate in %: "))
    profitAmount = eval(input("Enter The Profit Amount: "))
    if dividendRate == 0:
        if profitAmount>1000000:
            netTax = profitAmount*.40
        elif profitAmount < 1000000:
            netTax = profitAmount*.35
    elif dividendRate > 30:
        if profitAmount>1000000:
            netTax = profitAmount*.2475
        elif profitAmount < 1000000:
            netTax = profitAmount*.2075
    elif dividendRate < 10:
        if profitAmount>1000000:
            netTax = profitAmount*.35
        elif profitAmount < 1000000:
            netTax = profitAmount*.30
            
#Print Tax Amount            
print("Net Tax For The Company is: ",round(netTax,2))
