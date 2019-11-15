#Python Mid Term Ques Problem 3
#In Question there might be an error as the price of quantity 20 to 50 is not given
#I took quantity 10 to 50 shipping price as 10.5 and 50+ Can't be shipped

packageWeight = eval(input("Enter Your Package Weight: "))

if 0 < packageWeight <= 1:
    print("Shipping Cost Is: 3.5")
elif 1 < packageWeight <= 3:
    print("Shipping Cost Is: 5.5 ")
elif 3 < packageWeight <= 10:
    print("Shipping Cost Is: 8.5")
elif 10 < packageWeight <= 50:
    print("Shipping Cost Is: 10.5")
else:
    print("The Package Can't Be Shipped")
