import random
import json
import os
import uuid  
from src.database import connect
from src.logger import log_info, log_error
from src.data import rows, cols, screen_price

# Ensure folder exists
DATA_PATH = "data_storage"
os.makedirs(DATA_PATH, exist_ok=True)

# Limits
MAX_USER_TICKETS = 6
ADMIN_PASSWORD = "admin123"


# BOOKING ID
def generate_booking_id():
    return "MB-" + str(uuid.uuid4())[:8]


# ----------------------------
# SEAT SYSTEM
# ----------------------------
def get_all_seats():
    return [r + c for r in rows for c in cols]


def get_booked_seats(movie, time):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT seats FROM bookings WHERE movie=? AND time=?", (movie, time))
    data = cursor.fetchall()
    conn.close()

    booked = []
    for row in data:
        if row[0]:
            booked.extend(row[0].split(","))

    return booked


def display_seats(booked, selected=None):
    if selected is None:
        selected = []

    print("\n   " + "  ".join(cols))

    for r in rows:
        print(r, end="  ")
        for c in cols:
            seat = r + c

            if seat in booked:
                print("XX", end=" ")
            elif seat in selected:
                print("[]", end=" ")
            else:
                print(seat, end=" ")
        print()


def select_seats(movie, time):
    all_seats = get_all_seats()
    booked = get_booked_seats(movie, time)
    selected = []

    while True:
        display_seats(booked, selected)

        print(f"\nSelected seats: {selected}")
        print(f"Max allowed without admin: {MAX_USER_TICKETS}")
        print("Type seat (e.g., D4) | 'done' | 'cancel'")

        choice = input("Select seat: ").strip().upper()

        if not choice:
            print("❌ Empty input")
            continue

        if choice == "DONE":
            if not selected:
                print("❌ Select at least one seat")
                continue

            # Admin check
            if len(selected) > MAX_USER_TICKETS:
                pwd = input("🔐 Admin password required: ")
                if pwd != ADMIN_PASSWORD:
                    print("❌ Wrong password. Limit is 6 seats.")
                    selected = []
                    continue

            return selected

        if choice == "CANCEL":
            return None

        if choice not in all_seats:
            print("❌ Invalid seat")
            continue

        if choice in booked:
            print("❌ Already booked")
            continue

        if choice in selected:
            print("⚠️ Already selected")
            continue

        selected.append(choice)


# ----------------------------
# SAVE BOOKING
# ----------------------------
def save_booking(city, theatre, movie, screen, time, seats):
    conn = connect()
    cursor = conn.cursor()

    booking_id = generate_booking_id()
    tickets = len(seats)

    price_per_ticket = screen_price.get(screen, 150)
    total_price = tickets * price_per_ticket

    cursor.execute("""
    INSERT INTO bookings(booking_id, city, theatre, movie, screen, time, tickets, seats)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (booking_id, city, theatre, movie, screen, time, tickets, ",".join(seats)))

    conn.commit()
    conn.close()

    booking_data = {
        "booking_id": booking_id,
        "city": city,
        "theatre": theatre,
        "movie": movie,
        "screen": screen,
        "time": time,
        "tickets": tickets,
        "seats": seats,
        "price_per_ticket": price_per_ticket,
        "total_price": total_price
    }

    json_path = os.path.join(DATA_PATH, "bookings.json")

    if os.path.exists(json_path):
        try:
            with open(json_path, "r", encoding="utf-8") as file:
                data = json.load(file)
        except:
            data = []
    else:
        data = []

    data.append(booking_data)

    with open(json_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    txt_path = os.path.join(DATA_PATH, "tickets.txt")

    with open(txt_path, "a", encoding="utf-8") as file:
        file.write("\n" + "=" * 40 + "\n")
        file.write(" MOVIE TICKET RECEIPT\n")
        file.write("=" * 40 + "\n")
        file.write(f"Booking ID : {booking_id}\n")
        file.write(f"City       : {city}\n")
        file.write(f"Theatre    : {theatre}\n")
        file.write(f"Movie      : {movie}\n")
        file.write(f"Screen     : {screen}\n")
        file.write(f"Time       : {time}\n")
        file.write(f"Seats      : {', '.join(seats)}\n")
        file.write(f"Price/Seat : ₹{price_per_ticket}\n")
        file.write(f"Total Price: ₹{total_price}\n")
        file.write("=" * 40 + "\n")

    print(f"\n✅ Booking Successful! ID: {booking_id}")
    print(f"💰 Total Amount: ₹{total_price}")

    log_info(f"Booking created: {booking_id} | {movie} | Seats: {seats} | Amount: {total_price}")


# ----------------------------
# VIEW BOOKINGS
# ----------------------------
def view_bookings():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM bookings")
    records = cursor.fetchall()
    conn.close()

    if not records:
        print("\nNo bookings found.")
        return

    print("\n--- Booking History ---")
    for row in records:
        print(f"{row[1]} | {row[2]} | {row[4]} | Seats: {row[8]}")


# ----------------------------
# SEARCH BOOKING 
# ----------------------------
def search_booking():
    keyword = input("Enter movie or city: ").strip().lower()

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM bookings
    WHERE lower(movie) LIKE ? OR lower(city) LIKE ?
    """, ('%' + keyword + '%', '%' + keyword + '%'))

    results = cursor.fetchall()
    conn.close()

    if not results:
        print("No results found.")
        log_error(f"Search failed: {keyword}")
        return

    print("\n🔍 Search Results:\n")

    for row in results:
        print("=" * 35)
        print(f"Booking ID : {row[1]}")
        print(f"City       : {row[2]}")
        print(f"Theatre    : {row[3]}")
        print(f"Movie      : {row[4]}")
        print(f"Screen     : {row[5]}")
        print(f"Time       : {row[6]}")
        print(f"Seats      : {row[8]}")
        print("=" * 35)

    log_info(f"Search performed: {keyword}")


# ----------------------------
# CANCEL BOOKING 
# ----------------------------
def cancel_booking():
    bid = input("Enter Booking ID: ").strip()

    conn = connect()
    cursor = conn.cursor()

    # Fetch booking first
    cursor.execute("SELECT * FROM bookings WHERE booking_id=?", (bid,))
    booking = cursor.fetchone()

    if not booking:
        print("❌ Booking not found")
        log_error(f"Cancel failed: {bid}")
        conn.close()
        return

    print("\nBooking Details:")
    print("=" * 35)
    print(f"Booking ID : {booking[1]}")
    print(f"Movie      : {booking[4]}")
    print(f"Seats      : {booking[8]}")
    print("=" * 35)

    confirm = input("Are you sure you want to cancel? (y/n): ").lower()

    if confirm != "y":
        print("❌ Cancel aborted")
        conn.close()
        return

    cursor.execute("DELETE FROM bookings WHERE booking_id=?", (bid,))
    conn.commit()
    conn.close()

    print("✅ Booking cancelled successfully")
    log_info(f"Booking cancelled: {bid}")