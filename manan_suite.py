import getpass
import time
from datetime import datetime
import os

# Simple login system
USERNAME = "manan"
PASSWORD = "manan"

def clear_screen():
    os.system("clear")  # Termux/Unix clear screen

def banner():
    print("\n" + "="*60)
    print(" " * 15 + "\033[1m\033[95mMANAN AUTOMATION\033[0m")  # Bold + Center + Purple
    print("="*60 + "\n")

def seo_helper():
    topic = input("Enter your video topic: ")
    title = f"{topic} | Best Tips & Tricks 2025"
    description = f"Learn all about {topic}! 🔥\nSubscribe for more!\n#Shorts #{topic.replace(' ', '')}"
    tags = [topic, f"{topic} 2025", "viral", "trending"]
    print("\n[SEO Helper Output]")
    print("Title:", title)
    print("Description:", description)
    print("Tags:", ", ".join(tags))

def thumbnail_helper():
    topic = input("Enter thumbnail topic: ")
    print(f"\nThumbnail idea generated for: {topic}")
    print("➡ Big Bold Title, Bright Colors, 1-2 words only!")

def social_post_helper():
    link = input("Enter your YouTube link: ")
    print("\n[Social Post]")
    print(f"🔥 Check this out: {link}\n#MananAutomation #YouTube")

def scheduler():
    post = input("Write your post: ")
    delay = int(input("Enter delay in seconds: "))
    print(f"\nScheduled! Your post will show after {delay} sec...")
    time.sleep(delay)
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {post}")

def main_menu():
    while True:
        banner()
        print("1. SEO Helper")
        print("2. Thumbnail Helper")
        print("3. Social Post Generator")
        print("4. Scheduler")
        print("5. Exit")
        choice = input("\nSelect option: ")
        if choice == "1": 
            seo_helper()
        elif choice == "2": 
            thumbnail_helper()
        elif choice == "3": 
            social_post_helper()
        elif choice == "4": 
            scheduler()
        elif choice == "5": 
            break
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
        print("❌ Wrong username or password!")if __name__ == "__main__":
    u = input("Username: ")
    p = getpass.getpass("Password: ")
    if u == USERNAME and p == PASSWORD:
        main_menu()
    else:
        print("❌ Wrong username or password!")
