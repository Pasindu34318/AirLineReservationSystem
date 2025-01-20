import sqlite3

def view_flights():
    conn = sqlite3.connect('airline.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM flights")
    flights = cursor.fetchall()
    print("\nAvailable Flights:")
    print("ID | Flight Number | Origin | Destination | Seats Available")
    for flight in flights:
        print(f"{flight[0]}  | {flight[1]}       | {flight[2]}  | {flight[3]}    | {flight[4]}")
    conn.close()

def add_passenger():
    name = input("Enter passenger's name: ")
    email = input("Enter passenger's email: ")
    conn = sqlite3.connect('airline.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO passengers (name, email) VALUES (?, ?)", (name, email))
    conn.commit()
    print("Passenger added successfully!")
    conn.close()

def book_ticket():
    view_flights()
    flight_id = int(input("\nEnter the Flight ID to book: "))
    name = input("Enter your name: ")
    email = input("Enter your email: ")

    conn = sqlite3.connect('airline.db')
    cursor = conn.cursor()

   
    cursor.execute("SELECT seats_available FROM flights WHERE id = ?", (flight_id,))
    flight = cursor.fetchone()
    if not flight or flight[0] <= 0:
        print("Sorry, no seats available for this flight.")
        conn.close()
        return

    
    cursor.execute("INSERT INTO passengers (name, email) VALUES (?, ?)", (name, email))
    passenger_id = cursor.lastrowid

   
    cursor.execute("INSERT INTO bookings (passenger_id, flight_id) VALUES (?, ?)", (passenger_id, flight_id))

    
    cursor.execute("UPDATE flights SET seats_available = seats_available - 1 WHERE id = ?", (flight_id,))

    conn.commit()
    print("Ticket booked successfully!")
    conn.close()

def main():
    while True:
        print("\nAirline Reservation System")
        print("1. View Flights")
        print("2. Add Passenger")
        print("3. Book Ticket")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            view_flights()
        elif choice == '2':
            add_passenger()
        elif choice == '3':
            book_ticket()
        elif choice == '4':
            print("Thank you for using the Airline Reservation System!")
            break
        else:
            print("Invalid choice. Please try again.")

if _name_ == "_main_":
    main()