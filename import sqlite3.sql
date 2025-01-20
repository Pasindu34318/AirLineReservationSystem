import sqlite3

def setup_database():
    conn = sqlite3.connect('airline.db')
    cursor = conn.cursor()

    # Create Flights Table
    cursor.execute('''CREATE TABLE IF NOT EXISTS flights (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        flight_number TEXT NOT NULL,
        origin TEXT NOT NULL,
        destination TEXT NOT NULL,
        seats_available INTEGER NOT NULL
    )''')

    # Create Passengers Table
    cursor.execute('''CREATE TABLE IF NOT EXISTS passengers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL
    )''')

    # Create Bookings Table
    cursor.execute('''CREATE TABLE IF NOT EXISTS bookings (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        passenger_id INTEGER NOT NULL,
        flight_id INTEGER NOT NULL,
        FOREIGN KEY (passenger_id) REFERENCES passengers(id),
        FOREIGN KEY (flight_id) REFERENCES flights(id)
    )''')

    # Insert sample flights
    cursor.execute("INSERT INTO flights (flight_number, origin, destination, seats_available) VALUES ('AI101', 'New York', 'London', 50)")
    cursor.execute("INSERT INTO flights (flight_number, origin, destination, seats_available) VALUES ('AI202', 'Paris', 'Dubai', 30)")
    cursor.execute("INSERT INTO flights (flight_number, origin, destination, seats_available) VALUES ('AI303', 'Tokyo', 'Sydney', 20)")

    conn.commit()
    conn.close()

setup_database()