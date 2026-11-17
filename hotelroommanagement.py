# ==============================================================================
# GROUP 15 - HOTEL ROOM BOOKING SYSTEM (Upgraded from Nitin's Base Code)
# Members: 1. Nitin Bhargav  2. Kalpana Kumari  3. Amit Tiwari  4. Beeraka Sharath
# Run doctests: python -m doctest -v hotelroom.py
# ==============================================================================

import doctest
import random

# 1. COMPULSORY TUPLE: Fixed room categories
ROOM_TYPES = ("Standard", "Deluxe", "Suite")

# 2. COMPULSORY DICTIONARY (Main Data Store) + TUPLE (type, price)
rooms = {
    101: {"info": ("Standard", 1500.0), "status": "Available"},
    102: {"info": ("Standard", 1500.0), "status": "Available"},
    103: {"info": ("Deluxe",   2500.0), "status": "Available"},
    201: {"info": ("Deluxe",   2500.0), "status": "Available"},
    202: {"info": ("Suite",    4000.0), "status": "Available"},
    203: {"info": ("Suite",    4000.0), "status": "Available"}
}

# 3. COMPULSORY SET: Stores currently occupied room numbers
occupied_rooms = set()

# 4. COMPULSORY LIST: Stores customer booking records (from your base code!)
customers = []

DATA_FILE = "hotel_data.txt"
