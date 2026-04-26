from src.database import create_table, connect
from src.data import cities, theatres, movies, screens, timings, screen_price
from src.utils import header, menu, get_choice
from src.booking import (
    save_booking,
    view_bookings,
    search_booking,
    cancel_booking,
    select_seats
)
from src.logger import log_info


# ----------------------------
# DB INITIALIZATION
# ----------------------------
def init_database():
    create_table()

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT name FROM sqlite_master 
    WHERE type='table' AND name='bookings'
    """)

    table = cursor.fetchone()
    conn.close()

    if not table:
        print("❌ ERROR: bookings table not created!")
    else:
        print("✅ Database ready")


# ----------------------------
# BOOK TICKET
# ----------------------------
def book_ticket():
    header("BOOK TICKET")

    print("\nCity:")
    menu(cities)
    city = get_choice(cities)

    print("\nTheatre:")
    menu(theatres[city])
    theatre = get_choice(theatres[city])

    print("\nMovie:")
    menu(movies)
    movie = get_choice(movies)

   
    print("\nScreen:")
    for i, scr in enumerate(screens, 1):
        price = screen_price.get(scr, 150)
        print(f"{i}. {scr} (₹{price})")

    screen = get_choice(screens)

    print("\nTime:")
    menu(timings)
    time = get_choice(timings)

    seats = select_seats(movie, time)

    if seats is None:
        print("❌ Booking cancelled.")
        return

    save_booking(city, theatre, movie, screen, time, seats)


# ----------------------------
# MAIN MENU
# ----------------------------
def main():
    init_database()
    log_info("Application started")

    while True:
        header("MOVIE BOOKING SYSTEM")

        print("1. Book Ticket")
        print("2. View Bookings")
        print("3. Search Booking")
        print("4. Cancel Booking")
        print("5. Exit")

        choice = input("Enter choice (1-5): ").strip()

        if choice == "1":
            book_ticket()
        elif choice == "2":
            view_bookings()
        elif choice == "3":
            search_booking()
        elif choice == "4":
            cancel_booking()
        elif choice == "5":
            print("Goodbye 👋")
            log_info("Application exited")
            break
        else:
            print("❌ Invalid choice")


if __name__ == "__main__":
    main()