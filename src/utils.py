def header(title):
    print("\n" + "=" * 50)
    print(title.center(50))
    print("=" * 50)


def menu(options):
    for i, opt in enumerate(options, 1):
        print(f"{i}. {opt}")


def get_choice(options):
    while True:
        try:
            choice = int(input("Enter choice: "))
            if 1 <= choice <= len(options):
                return options[choice - 1]
            else:
                print("❌ Invalid choice. Try again.")
        except ValueError:
            print("❌ Enter a valid number.")



def get_ticket_count(max_limit=6):
    while True:
        try:
            count = int(input(f"Enter number of tickets (max {max_limit}): "))
            if count <= 0:
                print("❌ Must be greater than 0.")
            elif count > max_limit:
                print(f"⚠️ Max allowed is {max_limit}. Admin required for more.")
            else:
                return count
        except ValueError:
            print("❌ Enter a valid number.")



def confirm_action(message="Confirm? (y/n): "):
    while True:
        choice = input(message).lower()
        if choice in ["y", "yes"]:
            return True
        elif choice in ["n", "no"]:
            return False
        else:
            print("❌ Enter y/n only.")



def safe_input(prompt):
    value = input(prompt).strip()
    return value if value else None