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
          
