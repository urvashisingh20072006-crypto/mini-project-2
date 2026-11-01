# -----Smart Canteen-----

for i in range(1,6):
    if i==1:
        print("1. Veg Sandwich - Rs.60") 
    elif i==2:
        print("2. Masala Dosa - Rs.80")
    elif i==3:
        print("3. chole Rice - Rs.90")
    elif i==4:
        print("4. Paneer Roll - Rs.100")
    elif i==5:
        print("5. Tea - Rs.20")


Total_amount=0
item_count=0

order_name1=""
quantity1=0
cost1=0

order_name2=""
quantity2=0
cost2=0

order_name3=""
quantity3=0
cost3=0

order_name4=""
quantity4=0
cost4=0

order_name5=""
quantity5=0
cost5=0

while True:
    choice_item=int(input("choose item number(1-5):"))

    if choice_item < 1 or choice_item > 5:
        print("Invalid item number") 
        continue

    quantity=int(input("Enter quantity:"))
    if quantity<=0:
        print("Quantity must be greater than zero.")
        continue

    print("Your item number is :",choice_item)
    print("Your quantity is:",quantity)
    break


if choice_item==1:
    name="Veg Sandwich"
    price=60

elif choice_item==2:
    name="Masala Dosa"
    price=80

elif choice_item==3:
    name="Chole Rice"
    price=90

elif choice_item==4:
    name="Paneer Roll"
    price=100

else:
    name="Tea"
    price=20

print("Item Name:",name)
print("Item price:",price)


cost=price*quantity
Total_amount=Total_amount+cost
item_count=item_count+1

print("Item cost:",cost)
print("Total amount:",Total_amount)
