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
          
