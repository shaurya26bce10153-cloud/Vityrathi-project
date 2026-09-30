# Hotel system: customer side + management side (with login)

# Room Data
rooms = {
    "101": {
        "room_number": "101", "type": "Single Room", "bed": "Single",
        "capacity": 1, "area_m2": 12, "wifi": True, "available": True,
        "price_per_night": 35.00, "view": "City view",
        "amenities": ["Air conditioning", "TV", "Private bathroom"],
        "pets_allowed": False, "smoking": False,
    },
    "102": {
        "room_number": "102", "type": "Single Room", "bed": "Single",
        "capacity": 1, "area_m2": 14, "wifi": True, "available": True,
        "price_per_night": 40.00, "view": "Courtyard view",
        "amenities": ["Air conditioning", "TV", "Desk", "Private bathroom"],
        "pets_allowed": False, "smoking": False,
    },
    "103": {
        "room_number": "103", "type": "Double Room", "bed": "Double",
        "capacity": 2, "area_m2": 25, "wifi": True, "available": True,
        "price_per_night": 86.00, "view": "Garden view",
        "amenities": ["Air conditioning", "TV", "Minibar", "Balcony", "Room safe"],
        "pets_allowed": False, "smoking": False,
    },
    "104": {
        "room_number": "104", "type": "Economy Double", "bed": "Double",
        "capacity": 2, "area_m2": 20, "wifi": False, "available": False,
        "price_per_night": 60.00, "view": "Street view",
        "amenities": ["Fan", "TV", "Shared bathroom"],
        "pets_allowed": False, "smoking": True,
    },
    "105": {
        "room_number": "105", "type": "Twin Room", "bed": "2 Single",
        "capacity": 2, "area_m2": 24, "wifi": True, "available": True,
        "price_per_night": 80.00, "view": "City view",
        "amenities": ["Air conditioning", "TV", "Kettle", "Private bathroom"],
        "pets_allowed": False, "smoking": False,
    },
    "201": {
        "room_number": "201", "type": "Deluxe Double", "bed": "King",
        "capacity": 2, "area_m2": 32, "wifi": True, "available": True,
        "price_per_night": 120.00, "view": "Sea view",
        "amenities": ["Air conditioning", "TV", "Minibar", "Balcony", "Bathrobes"],
        "pets_allowed": False, "smoking": False,
    },
    "202": {
        "room_number": "202", "type": "Deluxe Twin", "bed": "2 Single",
        "capacity": 2, "area_m2": 30, "wifi": True, "available": False,
        "price_per_night": 110.00, "view": "Sea view",
        "amenities": ["Air conditioning", "TV", "Minibar", "Balcony"],
        "pets_allowed": False, "smoking": False,
    },
    "203": {
        "room_number": "203", "type": "Family Room", "bed": "King + 2 Single",
        "capacity": 4, "area_m2": 45, "wifi": True, "available": True,
        "price_per_night": 150.00, "view": "Garden view",
        "amenities": ["Air conditioning", "TV", "Kettle", "Baby cot", "Balcony"],
        "pets_allowed": True, "smoking": False,
    },
    "301": {
        "room_number": "301", "type": "Family Suite", "bed": "Queen + Sofa bed",
        "capacity": 5, "area_m2": 55, "wifi": True, "available": True,
        "price_per_night": 190.00, "view": "Sea view",
        "amenities": ["Air conditioning", "TV", "Minibar", "Kitchenette", "Balcony"],
        "pets_allowed": True, "smoking": False,
    },
    "302": {
        "room_number": "302", "type": "Penthouse Suite", "bed": "King",
        "capacity": 3, "area_m2": 60, "wifi": True, "available": True,
        "price_per_night": 250.00, "view": "Panoramic view",
        "amenities": ["Air conditioning", "TV", "Minibar", "Jacuzzi", "Terrace", "Room safe"],
        "pets_allowed": False, "smoking": False,
    },
}
bookings=[] 
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "1234"


# functions 
def yes_no(value):
    if value:
        return "Yes"
    return "No"


def ask_text(prompt):
    while True:
        text = input(prompt).strip()
        if text != "":
            return text
        print("This cannot be empty.")


def ask_whole_number(prompt):
    while True:
        text = input(prompt).strip()
        if text.isdigit() and int(text) > 0:
            return int(text)
        print("Please enter a whole number greater than 0.")


def ask_price(prompt):
    while True:
        text = input(prompt).strip()
        if text.replace(".", "", 1).isdigit() and float(text) > 0:
            return float(text)
        print("Please enter a valid price greater than 0 (e.g. 85.50).")


def ask_yes_no(prompt):
    while True:
        answer = input(prompt + " (yes/no): ").strip().lower()
        if answer == "yes":
            return True
        if answer == "no":
            return False
        print("Please type yes or no.")


def ask_amenities():
    while True:
        text = input("Amenities (separated by commas): ")
        amenities = []
        for item in text.split(","):
            item = item.strip()
            if item != "":
                amenities.append(item)
        if len(amenities) > 0:
            return amenities
        print("Please enter at least one amenity.")


def show_rooms(rooms_to_show):
    print("\nRooms:")
    for number, room in rooms_to_show.items():
        print(f"\nRoom {room['room_number']} - {room['type']}")
        print(f"  Bed: {room['bed']}  |  Capacity: {room['capacity']}  |  Area: {room['area_m2']} m2")
        print(f"  Wi-Fi: {yes_no(room['wifi'])}  |  View: {room['view']}")
        print(f"  Price per night: {room['price_per_night']:.2f}")
        print(f"  Amenities: {', '.join(room['amenities'])}")
        print(f"  Pets allowed: {yes_no(room['pets_allowed'])}  |  Smoking: {yes_no(room['smoking'])}")
        if room["available"]:
            print("  Status: Available")
        else:
            print("  Status: Booked")


# ---------- Customer side code ----------
def view_rooms_by_capacity():
    guests = input("Room for how many people? ")
    if not guests.isdigit():
        print("Please enter a number.")
        return

    guests = int(guests)
    matching_rooms = {}
    for number, room in rooms.items():
        if room["capacity"] == guests:
            matching_rooms[number] = room

    if len(matching_rooms) == 0:
        print(f"No rooms found for {guests} person(s).")
    else:
        show_rooms(matching_rooms)


def book_room():
    customer_name = input("Your name: ")
    number = input("Room number to book: ")

    if number not in rooms:
        print("Sorry, that room does not exist.")
        return

    room = rooms[number]
    if not room["available"]:
        print("Sorry, that room is already booked.")
        return

    print(f"Room {number} costs {room['price_per_night']:.2f} per night.")
    nights = input("Number of nights: ")
    if not nights.isdigit() or int(nights) == 0:
        print("Please enter a number of nights (1 or more).")
        return

    nights = int(nights)
    total = room["price_per_night"] * nights

    print("\n--- BOOKING SUMMARY ---")
    print(f"Name:   {customer_name}")
    print(f"Room:   {number} ({room['type']})")
    print(f"Nights: {nights}")
    print(f"Price:  {room['price_per_night']:.2f} x {nights} = {total:.2f}")

    confirm = input("Confirm booking? (yes/no): ").lower()
    if confirm == "yes":
        room["available"] = False
        bookings.append({"customer": customer_name, "room": number,
                         "nights": nights, "total": total, "checked_out": False})
        print(f"Booking confirmed! Room {number} is yours. Total to pay: {total:.2f}")
    else:
        print("Booking cancelled.")


def check_out():
    customer_name = input("Your name: ").strip()
    number = input("Room number: ").strip()

    for booking in bookings:
        if (booking["customer"].lower() == customer_name.lower()
                and booking["room"] == number
                and not booking["checked_out"]):
            booking["checked_out"] = True
            if number in rooms:
                rooms[number]["available"] = True
            print(f"Checked out. Thank you for staying with us, {booking['customer']}!")
            print(f"Room {number} is now available again.")
            return

    print("No active booking found for that name and room.")


def customer_menu():
    while True:
        print("\n--- CUSTOMER MENU ---")
        print("1. View rooms")
        print("2. Book a room")
        print("3. Check out")
        print("4. Back")
        choice = input("Choose: ")

        if choice == "1":
            view_rooms_by_capacity()
        elif choice == "2":
            book_room()
        elif choice == "3":
            check_out()
        elif choice == "4":
            break
        else:
            print("Invalid choice.")


# ---------- Management side code ----------
def login():
    for attempt in range(3):
        username = input("Username: ")
        password = input("Password: ")
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            return True
        print(f"Wrong username or password. {2 - attempt} tries left.")
    return False


def add_room():
    number = ask_text("New room number: ")
    if number in rooms:
        print("That room number already exists.")
        return

    rooms[number] = {
        "room_number": number,
        "type": ask_text("Room type (e.g. Double Room): "),
        "bed": ask_text("Bed type: "),
        "capacity": ask_whole_number("Capacity (people): "),
        "area_m2": ask_whole_number("Area (m2): "),
        "wifi": ask_yes_no("Wi-Fi?"),
        "available": True,
        "price_per_night": ask_price("Price per night: "),
        "view": ask_text("View (e.g. Sea view): "),
        "amenities": ask_amenities(),
        "pets_allowed": ask_yes_no("Pets allowed?"),
        "smoking": ask_yes_no("Smoking allowed?"),
    }
    print("Room added.")


def remove_room():
    number = input("Room number to remove: ")
    if number in rooms:
        del rooms[number]
        print("Room removed.")
    else:
        print("Room not found.")


def view_bookings():
    if len(bookings) == 0:
        print("No bookings yet.")
        return
    total_income = 0
    for booking in bookings:
        if booking["checked_out"]:
            status = "checked out"
        else:
            status = "staying"
        print(f"  {booking['customer']}: room {booking['room']}, "
              f"{booking['nights']} night(s) = {booking['total']:.2f} ({status})")
        total_income += booking["total"]
    print(f"Total income: {total_income:.2f}")


def management_menu():
    while True:
        print("\n--- MANAGEMENT MENU ---")
        print("1. View rooms")
        print("2. Add room")
        print("3. Remove room")
        print("4. View bookings")
        print("5. Log out")
        choice = input("Choose: ")

        if choice == "1":
            show_rooms(rooms)
        elif choice == "2":
            add_room()
        elif choice == "3":
            remove_room()
        elif choice == "4":
            view_bookings()
        elif choice == "5":
            break
        else:
            print("Invalid choice.")


# ---------- Main program ----------
def main():
    while True:
        print("\n=== WELCOME ===")
        print("1. Customer")
        print("2. Management")
        print("3. Exit")
        choice = input("Choose: ")

        if choice == "1":
            customer_menu()
        elif choice == "2":
            if login():
                management_menu()
            else:
                print("Too many failed attempts.")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


main()