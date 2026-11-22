# ---------- Hotel Room Booking System (Group 15) ----------

# List of active customer records (each record is a dictionary)
customers = []

# Hotel rooms: room number -> type, price per night, status
# 9 rooms in total: 3 on each of the 3 floors
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

# Set of occupied rooms (a set does not allow duplicates, so a room cannot be booked twice)
# A room is added at booking time and removed at check-out
occupied_room = set()

# Fixed rate card stored as a tuple so it cannot be changed by mistake
room_types = (
    ("Standard", 1500),
    ("Deluxe", 2500),
    ("Luxury", 4000)
)


# ---------- Room Booking Function ----------
def room_booking():
     # Name: must not be empty, must not contain a comma, must not already be checked in
    while True:
        name = input("Enter customer name: ").strip().title()
        if name != "":
            break
        print("Name can't be empty try again!")
 # Mobile number: exactly 10 digits
    while True:
        mobile_no = input("Enter 10-digit mobile number: ").strip()
        if mobile_no.isdigit() and len(mobile_no) == 10:
            break
        print("Either number is not 10 digits or you're entering alphabets!")
     # Number of days: positive integer
    while True:
        days = input("Enter no of days: ").strip()
        if days.isdigit() and int(days) > 0:
            days = int(days)
            break
        print("No of days should be a positive integer!")
 # Show room types from the rate card
    print("\n--------ROOM TYPE--------")
    num = 1
    for items in room_types:
        print(num, ".", items[0], "Room - Rs.", items[1], "Per Night")
        num += 1
# Room choice: 1 to 3
    while True:
        roomchoice = input("Enter Room Choice (1-3): ").strip()
        if roomchoice.isdigit() and 1 <= int(roomchoice) <= len(room_types):
            roomchoice = int(roomchoice)
            break
        print("Invalid choice! Choose from 1, 2 or 3. Try again!")

    roomtype, roomprice = room_types[roomchoice - 1]

       # Find the first free room of the chosen type
    
    assigned_room = None
    for r in rooms:
        if rooms[r]["type"] == roomtype and r not in occupied_room:
            assigned_room = r
            break
    # No room free: stop here so booking is not completed
    if assigned_room is None:
        print("\nSorry! No", roomtype, "room is available right now.")
        return  

    rooms[assigned_room]["status"] = "Booked"
    occupied_room.add(assigned_room)

    room_bill = days * roomprice
    customer = {
        "name": name,
        "Mobileno": mobile_no,
        "room_no": assigned_room,
        "room_type": roomtype,
        "days": days,
        "room_bill": room_bill,
        "food_bill": 0
    }

    customers.append(customer)
    print("\nRoom Booked Successfully!")
    print("Assigned Room:", assigned_room)
    print("Customer Name:", name)
    print("Room Type:", roomtype)
    print("Room Charges: Rs.", room_bill)


# ---------- Food Order Function ----------
def food_order():
    if not customers:
        print("No customer record found..")
        return

    name = input("Enter customer name: ").strip().lower()
    found = False

    for customer in customers:
        if customer["name"].lower() == name:
            found = True
            print("\n--- Food Menu ---")
            print("1. Tea - 50rs")
            print("2. Coffee - 100rs")
            print("3. Lunch - 300rs")
            print("4. Snacks - 150rs")
            print("5. Dinner - 450rs")
          # Food choice: 1 to 5
            while True:
                choice = input("Enter food choice from above (1-5): ").strip()
                if choice.isdigit() and 1 <= int(choice) <= 5:
                    choice = int(choice)
                    break
                print("Don't enter alphabets; choose from 1 to 5!")
          # Quantity: positive integer
            while True:
                qty = input("Enter the quantity: ").strip()
                if qty.isdigit() and int(qty) > 0:
                    qty = int(qty)
                    break
                print("Invalid input, try again!")
            # Add the price of the chosen item to the food bill
            if choice == 1:
                customer["food_bill"] += 50 * qty
            elif choice == 2:
                customer["food_bill"] += 100 * qty
            elif choice == 3:
                customer["food_bill"] += 300 * qty
            elif choice == 4:
                customer["food_bill"] += 150 * qty
            elif choice == 5:
                customer["food_bill"] += 450 * qty

            print("Total Food Bill: Rs.", customer["food_bill"])
            break
 # Checked after the loop so it prints only once
    if not found:
        print("Customer not found!")


# ---------- View Customer Details Function ----------
def view_customer_details():
    if not customers:
        print("No customer records available..")
        return  
    # Collect names and sort them A-Z
    
    names = []
    for customer in customers:
        names.append(customer["name"])
    names.sort()
    print("\nALL CUSTOMERS NAME SORTED (A-Z):", ", ".join(names))

    for customer in customers:
        print("\n---------------------")
        print("Customer Name:", customer["name"])
        print("Customer Mobileno:", customer["Mobileno"])
        print("Room Type:", customer["room_type"])
        print("Room Number:", customer["room_no"])
        print("Days Stayed:", customer["days"])
        print("Room Bill: Rs.", customer["room_bill"])
        print("Food Bill: Rs.", customer["food_bill"])
  # Last 3 entries using slicing
    
    print("\nCustomer record of the last 3 entries:")
    for recent in customers[-3:]:
        print(recent["name"], "- Room", recent["room_no"])


# ---------- Generate Bill & Check-out Function ----------
def generate_bill():
    # Nothing to bill if there are no customers yet
    if not customers:
        print("No customer records available..")
        return  

    name = input("Enter customer name: ").strip().lower()
    found = False

    for customer in customers:
        if customer["name"].lower() == name:
            found = True
            room_bills = customer["room_bill"]
            food_bills = customer["food_bill"]
            days = customer["days"]

              # Long-stay discount: 15% for 7+ days, 10% for 4-6 days
            
            if days >= 7:
                discount = room_bills * 0.15
            elif days >= 4:
                discount = room_bills * 0.10
            else:
                discount = 0

             # Discount applies only to the room bill; then add food and 12% tax

            sub_total = (room_bills - discount) + food_bills
            tax = sub_total * 0.12
            final_bill = sub_total + tax

            print("\n===== Final Bill ======")
            print("Customer Name:", customer["name"])
            print("Mobileno:", customer["Mobileno"])
            print("Room Type:", customer["room_type"])
            print("Room Number:", customer["room_no"])
            print("Days Stayed:", days)
            print(f"Room Bill:    Rs. {room_bills:.2f}")
            print(f"Discount:    -Rs. {discount:.2f}")
            print(f"Food Bill:    Rs. {food_bills:.2f}")
            print(f"Tax (12%):    Rs. {tax:.2f}")
            print(f"Final Bill:   Rs. {final_bill:.2f}")
            print("=======================================")

            # Check-out: free the room and remove the guest record

            checkout = input("Do you want to checkout this guest? (yes/no): ").strip().lower()
            if checkout == "yes" or checkout == "y":
                room_no = customer["room_no"]
                rooms[room_no]["status"] = "Available"
                if room_no in occupied_room:
                    occupied_room.remove(room_no)
                customers.remove(customer)
                print("Check-out successful! Room", room_no, "is now Available.")
            break

    if not found:
        print("Customer not found!")


# ---------- Room Grid & Available Rooms Function ----------
def show_room_grid(filter_type="All"):
     # Nested loops: outer loop for floors, inner loop for rooms on each floor
    print("\n========== HOTEL ROOM GRID ==========")
    for floor in range(1, 4):
        print("Floor", floor, ":", end="  ")
        for index in range(1, 4):
            rmno = floor * 100 + index
            status = rooms[rmno]["status"]
            print(f"[{rmno}: {status}]", end="  ")
        print()

   # List available rooms, filtered by type
    print("\n--- Available Rooms (" + filter_type + ") ---")
    available_count = 0
    for r_no in rooms:
        if r_no not in occupied_room:
            if filter_type.lower() == "all" or rooms[r_no]["type"].lower() == filter_type.lower():
                print("Room", r_no, "-", rooms[r_no]["type"], "- Rs.", rooms[r_no]["price"])
                available_count += 1

    if available_count == 0:
        print("No available rooms found for:", filter_type)

    return available_count

# ---------- File Handling Function (Save & Load) ----------
# Saves or loads customer records using hotel_bookings.txt
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
        try:
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
        except FileNotFoundError:
             # First run: no saved file yet
            return 0
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
        count = show_room_grid(room_filter)
        print("Total matching available rooms:", count)
    elif choice == 6:
        saved = manage_file("save")
        print("Saved", saved, "booking(s). Thank you for using our system!")
        break
    else:
        print("Invalid choice! Please select 1 to 6.")
