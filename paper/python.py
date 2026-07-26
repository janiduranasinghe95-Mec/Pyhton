Cus_name = input("Enter your name : ")
Cus_age = int(input("Enter your age : "))

if Cus_age < 0 or Cus_age > 120:
    category = "Invalid age"
    price = 0
    dis = 0
    dis_price = price-dis
else:
    if Cus_age <= 12:
        category = "child"
        price = 400
        dis = 0
        dis_price = price-dis
    else:
        if Cus_age >= 60:
            price = 800
            dis = price*10 / 100
            dis_price = price-dis
            category = "Adult"
        else:
            category = "Adult"
            price = 800
            dis = 0
            dis_price = price-dis

print("Enter customer Name : ",Cus_name)
print("Enter age : ",Cus_age)
print("----------Ticket Details----------")
print("Customer Name : ",Cus_name)
print("Category : ",category)
print("Ticket Price : Rs",price)
print("Discount : Rs", dis)
print("Amount Payble : Rs.",dis_price)


