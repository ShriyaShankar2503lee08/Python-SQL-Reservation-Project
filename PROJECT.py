import mysql.connector
from mysql.connector import Error

# Database connection
try:
    con = mysql.connector.connect(
        host="localhost",
        database="hotel",
        user="Shriya",
        password="lino"
    )
    mycursor = con.cursor()
except Error as e:
    print("Error connecting to database:", e)
    exit()

# Function to register a customer
def registercust():
    customer_data = []

    name = input('Enter name: ')
    address = input('Enter locality: ')
    city = input('Enter city: ')
    state = input('Enter state: ')
    pin = input('Enter PIN code: ')
    jr_date = input('Enter date of journey (YYYY-MM-DD): ')
    source = input('Enter source: ')
    destination = input('Enter destination: ')
    fulladd = address+', '+city+', '+state+', '+pin
    customer_data.extend([name, fulladd, jr_date, source, destination])

    # Insert into SQL
    sql = """INSERT INTO pdata
             (custname, addr, jrdate, source, destination)
             VALUES (%s,%s,%s,%s,%s)"""
    try:
        mycursor.execute(sql, customer_data)
        con.commit()
        print("Customer registered successfully.\n")
    except Error as e:
        print("Error inserting data:", e)

    # Write to bill file
    with open("Bill.txt", 'a') as f:
        f.write("----- Customer Details -----\n")
        f.write(f"Name: {name}\nState: {state}\nCity: {city}\nAddress: {address}\n")
        f.write(f"PIN code: {pin}\nJourney date: {jr_date}\nSource: {source}\nDestination: {destination}\n\n")
    
# Function to calculate ticket price
def ticketprice():
    print('We have the following rooms for you:')
    print("1. First class -> Rs 7000 PN")
    print("2. Business class -> Rs 5000 PN")
    print("3. Economy class -> Rs 3000 PN")

    choice = int(input('Enter your choice: '))
    passengers = int(input('Number of passengers: '))

    if choice == 1:
        price = 7000 * passengers
        class_name = "First class"
    elif choice == 2:
        price = 5000 * passengers
        class_name = "Business class"
    elif choice == 3:
        price = 3000 * passengers
        class_name = "Economy class"
    else:
        print('Invalid choice!')
        return 0

    print(f'You have opted {class_name}. Ticket fare = Rs {price}\n')
    with open("Bill.txt", 'a') as f:
        f.write(f"Ticket: {class_name}, Fare = {price}\n")
    return price

# Function to order food items
def orderitem():
    try:
        mycursor.execute("SELECT * FROM food")
        rows = mycursor.fetchall()
    except Error as e:
        print("Error fetching food items:", e)
        return 0

    print("\nAvailable food items:")
    for row in rows:
        print(f"{row[0]}. {row[1]} - Rs {row[2]}")

    choice = input("Enter your choice (number) or 0 to skip: ")
    if choice == '0':
        print("No food chosen.")
        with open("Bill.txt", 'a') as f:
            f.write("No food items chosen.\n")
        return 0

    quantity = int(input("Enter quantity: "))

    item = next((item for item in rows if str(item[0]) == choice), None)
    if item:
        total = item[2] * quantity
        print(f"Your amount for {item[1]} = Rs {total}")
        with open("Bill.txt", 'a') as f:
            f.write(f"{item[1]} x {quantity} = Rs {total}\n")
        return total
    else:
        print("Invalid food choice.")
        return 0

# Function to calculate luggage bill
def luggagebill():
    try:
        mycursor.execute("SELECT * FROM luggage")
        rows = mycursor.fetchall()
    except Error as e:
        print("Error fetching luggage info:", e)
        return 0

    print("\nAvailable luggage info (weight limits and charges):")
    for row in rows:
        print(f"{row[0]}. {row[1]} kg extra = Rs {row[2]} per kg")

    choice = input("Do you have extra luggage? (y/n): ").lower()
    if choice == 'y':
        weight = int(input("Enter weight of extra luggage (kg): "))
        bill = weight * 1000
        print(f"Luggage bill: Rs {bill}")
        with open("Bill.txt", 'a') as f:
            f.write(f"Luggage bill: Rs {bill}\n")
        return bill
    return 0

# Function to generate final bill
def generatebill():
    print("\n----- Generating Bill -----\n")
    try:
        with open("Bill.txt", 'r') as f:
            print(f.read())
    except FileNotFoundError:
        print("No bill found. Please register customer and choose services first.")

# FIXED Cancel Booking
def cancelbooking():
    name = input("Enter the customer name to cancel booking: ")

    # Check if customer exists
    sql_check = "SELECT * FROM pdata WHERE custname = %s"
    mycursor.execute(sql_check, (name,))
    record = mycursor.fetchone()

    # IMPORTANT FIX — clear unread rows
    mycursor.fetchall()

    if not record:
        print("No such booking found!")
        return

    # Delete customer booking
    sql_delete = "DELETE FROM pdata WHERE custname = %s"
    try:
        mycursor.execute(sql_delete, (name,))
        con.commit()
        print(f"Booking for {name} has been cancelled successfully.")

        with open("Bill.txt", "a") as f:
            f.write(f"Booking for {name} cancelled.\n")

    except Error as e:
        print("Error cancelling booking:", e)

# Main menu function
def Menuset():
    while True:
        print("\n===== Main Menu =====")
        print("1: Enter customer data")
        print("2: Services (Ticket, Food, Luggage)")
        print("3: Generate bill")
        print("4: Cancel Booking")
        print("5: Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Enter a valid number.")
            continue

        if choice == 1:
            registercust()
        elif choice == 2:
            ticket_total = ticketprice()
            food_total = orderitem()
            luggage_total = luggagebill()
            total_amount = ticket_total + food_total + luggage_total
            print(f"\nTotal Amount to be paid = Rs {total_amount}")
            with open("Bill.txt", 'a') as f:
                f.write(f"\nTotal Amount = Rs {total_amount}\n")
        elif choice == 3:
            generatebill()
        elif choice == 4:
            cancelbooking()
        elif choice == 5:
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

# Start program
if __name__ == "__main__":
    Menuset()



