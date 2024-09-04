menu={"Salad":70,
      "Coffee":40,
      "Pasta":50,
      "Pizza":90,
      "Paneer":120,
      "Roti":10}
print("Welcome to Raja Restaurant ")
print("The list of items avialable are:\n Salad 70\n Coffee 40\n Pasta 50\n Pizza 90\n Paneer 120\n Roti 10\n ")
total_amount=0
item_1=input("Enter the your order: ")
if item_1 in menu:
    total_amount+=menu[item_1]
    print(f"The total of {item_1} is {total_amount}")
else:
    print(f"the {item_1} is not available at our Restaurant\n Thank you!!")  
confirm=input("you want to order another item (YES/NO)").upper()  
if confirm=="YES":
    item_2=input("what  would you like to order")
    if item_2 in menu:
           total_amount+=menu[item_2]
           print(f"the total of  {item_1} and {item_2} is {total_amount}")
    else:
         print(f"the {item_2} is not available at our Restaurant")       
else:
     print(f"Thank you for your order.Your total bill is {total_amount}.")           
print("Thanking for you to visit my restaurant!!")
