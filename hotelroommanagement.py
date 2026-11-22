customers = []

#---------Hotel Rooms Data (Dictionary)----------
# Stores room number with its type, price per night, and status taaki pata chale ki kon book kar raha hai warna unlimited room book hote rahenge kuch track nahi ho payegi esleye ess dictionary ko define kara ki hamare paas 9 rooms hai 3 on the first floor ,3 on the second floor and 3 on the third floor 
rooms = {
    101: {"type": "Standard", "price": 1500, "status": "Available"},
    102: {"type": "Standard", "price": 1500, "status": "Available"},
    103: {"type": "Standard", "price": 1500, "status": "Available"},
    201: {"type": "Deluxe", "price": 2500, "status": "Available"},
    202: {"type": "Deluxe", "price": 2500, "status": "Available"},
    203: {"type": "Deluxe", "price": 2500, "status": "Available"},
    301: {"type": "Luxury", "price": 4000, "status": "Available"},
    302: {"type": "Luxury", "price": 4000, "status": "Available"},
    303: {"type": "Luxury", "price": 4000, "status": "Available"}
}

#abb hamko check karna hai konsa room occupied hai ya nahi hai toh hame esa data type chaiye jo duplicates entry allow na kare aur eske liye we are defining set esme daal denege jo bhi room check in ke waqt book hoga and while doing the checkout we will remove the room from there aur loop lagake dekhte rahenge kya yeh room availabe hai ya nahi 

occupied_room=set()

#abhi esme tuple define kar diya kyoki ham terminal se cheeze chalate hai toh galti se bhi koi ess rate card ko change na karde kyoki yeh cheeze toh generally fixed rheti hai toh enko tuple mein rakhna zayda fayde mand hai..
room_types = (
    ("Standard", 1500),
    ("Deluxe", 2500),
    ("Luxury", 4000)
)

#---------Room Booking Function Defined----------

def room_booking():
     while True:
          name= input("Enter customer name: ").strip().title()
          if name!= "":
               break 
          print("Name can't be empty try again!")
         
     while True:
          mobile_no=int(input("enter mobile number")).strip()
          if mobile_no.isdigit() and len(mobile_no)==10:
               break
          print("either no is not 10 digits or you're taking alphabets")
          
     while True:
          days=int(input("enter no of days: "))
          if days.isdigit() and days>0:
               break
          print("no of days should be integer")

     print("\n--------ROOM TYPE--------")

     num=1
     for items in room_types:
          print(num,".",items[0] ,"Room Price", items[1], "Per Night")
          num+=1

     while True:
          roomchoice=input("Enter Room Choice(1-3): ").strip()
          if roomchoice.isdigit() and 1<=int(roomchoice)<=len(room_types):
               break
          print("invalid choice choose from 1,2 or 3 Try again!")
     roomtype,roomprice= room_types[roomchoice-1]

     assigned_room=None
     for r in rooms:
          if rooms[r]["type"]==roomtype and r not in occupied_room:
               assigned_room=r
               break
     if assigned_room is None:
          print("\nSorry! No", roomtype, "room is available right now")
          return #taaki aage ki room booked wagera na chal jaye
     roomtype[assigned_room]["status"]=="Booked"
     occupied_room.add(assigned_room)

     room_bill= days*roomprice
     customer={
          "name": name,
          "Mobileno": mobile_no,
          "room_no": assigned_room,
          "room_type": roomtype,
          "days": days,
          "roombill": room_bill,
          "food_bill": 0
          
     }          

     customers.append(customer)
     print("\nRoom Booked Successfully:")
     print("assignend room:"+assigned_room)
     print("custormer name:", name)
     print("Room Type:", roomtype)
     print("Room Charges:", room_bill)

# ----add food order function --------
def food_order():
     if not customers:
        print("no customer record found..")
        return
     name=input("enter customer name: ")
     for customer in customers:
          if customer["name"]== name:
               print("\n--- Food Menu ---")
               print("1. Tea - 50rs")
               print("2. Coffee - 100rs")
               print("3. Lunch - 300rs")
               print("4. Snacks - 150rs")
               print("5. Dinner - 450rs")
               choice =int(input("enter food choices from above: "))
               qty = int(input("enter quantity: "))
               if choice==1:
                    customer["food_bill"]+= 50*qty
               elif choice==2:
                    customer["food_bill"]+=100*qty
               elif choice==3:
                    customer["food_bill"]+=300*qty
               elif choice==4:
                    customer["food_bill"]+=150*qty
               elif choice==5:
                    customer["food_bill"]+=450*qty
               else:
                    print("invalid food choice, try again!")
                    return
          else:
               print("customer not found!")

     
#----customer_details_funcitons-------
def view_customer_details():
     if not customers:
          print("No customer records available..")
          return  #agar abhi tak kisi customer ki entry he nahi hui hai customers mein toh yeh turant return karke rok dega aage ki program effieceny ko bada dega
     names=[]
     for customer in customers:
          names.append(customer["name"])
     names.sort()
     print("\n ALL CUSTOMERS NAME SORTED (A-Z):", ",".join(names))

     for customer in customers:
          print("\n---------------------")
          print("customer Name:", customer["name"])
          print("customer Mobileno:", customer["Mobileno"])
          print("Room Type:", customer["room_type"])
          print("Room Type:", customer["room_no"])
          print("Days Stayed:", customer["days"])
          print("Room Bill:", customer["room_bill"])
          print("food Bill:", customer["food_bill"])

     print("\nCustomer record of the last 3 entries")
     for recent in customers[-3:]:
        print(recent["name"], "- Room", recent["room_no"])     


def generate_bill():
     if not customers:
        print("No customer records available..")
        return #agar abhi tak ek bhi customer add nahi hua hai toh kya lega esleye yaha se he functions se bahar ho jayega
     name=input("enter customer name: ").strip().lower()
     for customer in customers:
          if customer["name"]==name:
               room_bills=customer["roombill"]
               food_bills=customer["food_bill"]
               days=customer["days"]
               if days>=4:
                    discount=room_bills*0.10
               elif days>=7:
                    discount=room_bills*0.15
               else:
                    discount=0
               sub_total=(room_bills-discount)+discount
               tax=sub_total*0.12
               final_bill=sub_total+tax

               total_bill=customer["room_bill"]+ customer["food_bill"]
               print("\n===== Final Bill ======")
               print("customer Name:", customer["name"])
               print("Mobileno:", customer["Mobileno"])
               print("Room Type:", customer["room_type"])
               print("Room Number:", customer["room_no"])
               print("Room Bill:", customer["room_bill"])
               print("food Bill:", customer["food_bill"])
               print("Days Stayed:", days)
               print(f"Room Bill:    Rs. {room_bills:.2f}")
               print(f"Discount:     Rs. {discount:.2f}")
               print(f"Food Bill:    Rs. {food_bills:.2f}")
               print(f"Tax (12%):    Rs. {tax:.2f}")
               print(f"Final Bill:   Rs. {final_bill:.2f}")
               print("=======================================")
               checkout=input("Do you want to checkout this guest? Yes/No").strip().lower()
               if checkout=="yes" or checkout=="y":
                    room_no=customer["room_no"]
                    rooms[room_no]["status"]="Available"
                    if room_no in occupied_room:
                         occupied_room.remove(room_no)
                         customers.remove(customer)
                         print("Check-out successful! Room", room_no, "is now Available.")

     print("customer not found!")

def show_room_grid("filter_type"=All):
     for floor in range(1,4):
          print("Floor", floor, ":", end=" ")
          for index in range(1,4):
               rmno=floor*100+index
               status=rooms[rmno]["status"]
               print(f"{rmno}:{status}", end=" ")
          print()

     # Show available rooms filtered by type
     print("\n--- Available Rooms (" + filter_type + ") ---")
     available_count = 0
     for r_no in rooms:
          if r_no not in occupied_room:
            if filter_type == "All" or rooms[rmno]["type"].lower() == filter_type.lower():
                print("Room", r_no, "-", rooms[rmno]["type"], "- Rs.", rooms[rmno]["price"])
                available_count += 1

     if available_count == 0:
        print("No available rooms found for:", filter_type)
        return available_count



#---------File Handling Function (Save & Load)----------
# Saves or loads customer booking records using hotel_bookings.txt
def manage_file(mode):
    if mode == "save":
        with open("hotel_bookings.txt", "w") as f:
            for c in customers:
                data = [
                    c["name"],
                    str(c["Mobileno"]),
                    str(c["room_no"]),
                    c["room_type"],
                    str(c["days"]),
                    str(c["room_bill"]),
                    str(c["food_bill"])
                ]
                f.write(",".join(data) + "\n")
        return len(customers)

    elif mode == "load":
        # Create empty file if it does not exist yet (prevents crash without try-except)
        with open("hotel_bookings.txt", "a") as f:
            pass

        with open("hotel_bookings.txt", "r") as f:
            for line in f:
                line = line.strip()
                if line == "":
                    continue
                parts = line.split(",")
                r_no = int(parts[2])
                customer = {
                    "name": parts[0],
                    "Mobileno": parts[1],
                    "room_no": r_no,
                    "room_type": parts[3],
                    "days": int(parts[4]),
                    "room_bill": int(parts[5]),
                    "food_bill": int(parts[6])
                }
                customers.append(customer)
                if r_no in rooms:
                    rooms[r_no]["status"] = "Booked"
                    occupied_room.add(r_no)
        return len(customers)


#--------------MAIN MENU------------------

# Load existing bookings from file when program starts
loaded = manage_file("load")
print("Loaded", loaded, "existing booking(s) from file.")

while True:
    print("\n========== HOTEL MANAGEMENT SYSTEM ==========")
    print("1. Room Booking")
    print("2. Food Order")
    print("3. View Customer Details")
    print("4. Generate Bill & Check-out")
    print("5. View Room Grid & Available Rooms")
    print("6. Save & Exit")

    choice = input("Enter your choice (1-6): ").strip()
    if not choice.isdigit():
        print("Invalid choice! Please enter a number from 1 to 6.")
        continue

    choice = int(choice)

    if choice == 1:
        room_booking()
        manage_file("save")
    elif choice == 2:
        food_order()
        manage_file("save")
    elif choice == 3:
        view_customer_details()
    elif choice == 4:
        generate_bill()
        manage_file("save")
    elif choice == 5:
        room_filter = input("Enter room type (Standard / Deluxe / Luxury / All): ").strip()
        if room_filter == "":
            room_filter = "All"
        count = show_rooms_status(room_filter)
        print("Total matching available rooms:", count)
    elif choice == 6:
        saved = manage_file("save")
        print("Saved", saved, "booking(s). Thank you for using our system!")
        break
    else:
        print("Invalid choice! Please select 1 to 6.")


          
