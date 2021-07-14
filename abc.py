rate=input("Enter  commission rate in percentage: ")
sales=input("Enter  sales amount: ")
temp=int(sales)*int(rate)/100
commission=int(sales)-int(temp)
print("Sales Commission=",commission)
