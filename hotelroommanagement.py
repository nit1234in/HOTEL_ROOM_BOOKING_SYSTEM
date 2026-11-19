rdohrdghoih
dogh
dfogh








































































#----customer_details_funcitons-------
def view_customer_details():
     if not customers:
          print("No customer records available..")
          return
     for customer in customers:
          print("\n---------------------")
          print("customer Name:", customer["name"])
          print("customer Mobileno:", customer["Mobileno"])
          print("Room Type:", customer["room_type"])
          print("Days Stayed:", customer["days"])
          print("Room Bill:", customer["room_bill"])
          print("food Bill:", customer["food_bill"])

def generate_bill():
     if not customers:
        print("No customer records available..")
        return
     name=input("enter customer name: ")
     for customer in customers:
          if customer["name"]==name:
               total_bill=customer["room_bill"]+ customer["food_bill"]
               print("\n===== Final Bill ======")
               print("customer Name:", customer["name"])
               print("customer Mobileno:", customer["Mobileno"])
               print("Room Type:", customer["room_type"])
               print("Room Bill:", customer["room_bill"])
               print("food Bill:", customer["food_bill"])
               print("Total  Charges:", total_bill)
               print("=======================================")
               return
          print("customer not found!")
          
