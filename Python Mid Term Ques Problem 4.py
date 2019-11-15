#Determining The Economic Order Quantity

demandRate = eval(input("Enter The Demand Units: "))
setupCost = eval(input("Enter The Setup Cost: "))
holdingCost = eval(input("Enter The Holding Cost Per Item: "))

EOQ = ((2*demandRate*setupCost)/holdingCost)**.5

print("The Economic Order Quantity is ",round(EOQ), " Items")


#Determining The Economic Order Quantity Using SQRT
import math
demandRate = eval(input("Enter The Demand Units: "))
setupCost = eval(input("Enter The Setup Cost: "))
holdingCost = eval(input("Enter The Holding Cost Per Item: "))

EOQ = math.sqrt(((2*demandRate*setupCost)/holdingCost))

print("The Economic Order Quantity is ",round(EOQ), " Items")
