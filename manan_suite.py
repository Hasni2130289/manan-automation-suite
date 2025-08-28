import os
import getpass

# Constants
USERNAME = "manan"
PASSWORD = "manan"

# Clear screen function
def clear_screen():
    os.system("clear" if os.name == "posix" else "cls")

# Banner function
def banner():
    print("\n" + "="*60)
    print("          \033[1m\033[95mMANAN AUTOMATION\033[0m")  # Bold + Purple
    print("="*60 + "\n")

# Menu
def main_menu():
    while True:
        print("1. SEO Helper")
        print("2. Thumbnail Helper")
        print("3. Social Post Generator")
        print("4. Scheduler")
        print("5. Exit")
        choice = input("\nSelect option: ")

        if choice == "1":
            print("\n[SEO Helper running...]\n")
        elif choice == "2":
            print("\n[Thumbnail Helper running...]\n")
        elif choice == "3":
            print("\n[Social Post Generator running...]\n")
        elif choice == "4":
            print("\n[Scheduler running...]\n")
        elif choice == "5":
            print("\nExiting... Goodbye!\n")
            break
        else:
            print("\n❌ Invalid option, try again!\n")

# Main
if __name__ == "__main__":
    clear_screen()
    banner()
    u = input("Username: ")
    p = getpass.getpass("Password: ")
    if u == USERNAME and p == PASSWORD:
        clear_screen()
        banner()
        main_menu()
    else:
        print("❌ Wrong username or password!")            break
        else: 
            print("Invalid choice!")

if __name__ == "__main__":
    clear_screen()
    banner()
    u = input("Username: ")
    p = getpass.getpass("Password: ")
    if u == USERNAME and p == PASSWORD:
        clear_screen()
        main_menu()
    else:
        print("❌ Wrong username or
