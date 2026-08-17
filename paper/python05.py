items = {
    "101": ["Rice", 250],
    "102": ["Sugar", 320],
    "103": ["Milk Powder", 1450],
    "104": ["Cooking Oil", 780],
    "105": ["Biscuit", 180]
}

customer_name = input("Enter customer name: ")
print("Items --> 101 --> Rice\n"
      "          102 --> Sugar\n"
      "          103 --> Milk Powder\n"
      "          104 --> Cooking Oil\n"
      "          105 --> Biscuit")
item_code = input("Enter item code (101-105): ")

if item_code not in items:
    print("Invalid item code")
else:
    quantity = float(input("Enter quantity purchased (kg, L, No. of packets): "))

    if quantity <= 0:
        print("Invalid quantity")
    else:
        item_name = items[item_code][0]
        unit_price = items[item_code][1]

        total_price = unit_price * quantity

        if total_price < 5000:
            discount_rate = 0

        elif total_price <= 9999:
            discount_rate = 5

        elif total_price <= 19999:
            discount_rate = 10

        else:
            discount_rate = 15

        discount = total_price * discount_rate / 100
        net_amount = total_price - discount

        Bulk_Purchase_Reward = "Yes" if quantity >= 10 else "No"
        Free_Shopping_Voucher = "Yes" if net_amount > 15000 else "No"
        Complimentary_Loyal_Point = "Yes" if item_code == "103" else "No"

        print("Enter customer name: " ,customer_name)
        print("Enter Item code : ",item_code)
        print("Enter Quantity : ",quantity)

        print("---------Supermarket Bill----------")
        print("Customer Name :", customer_name)
        print("Item Code :", item_code)
        print("Unit Price : Rs.", unit_price)
        print("Quantity :", quantity)
        print()
        print("Total Amount : Rs.", total_price)
        print("Discount : Rs.", discount)
        print("Net Amount Payable : Rs.", net_amount)
        print()
        print("Bulk Purchase Reward : ",Bulk_Purchase_Reward)
        print("Free Shopping Voucher : ",Free_Shopping_Voucher)
        print("Complimentary Loyal Point : ",Complimentary_Loyal_Point)



