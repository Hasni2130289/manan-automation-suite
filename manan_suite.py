#!/usr/bin/env python3
import os
import getpass
import shutil
import time

# Config
USERNAME = "manan"
PASSWORD = "manan"
BANNER_TEXT = "MANAN AUTOMATION"
FIGLET_FONT = "slant"   # looks large; change to "standard" or "big" if you want

# Try importing pyfiglet
try:
    from pyfiglet import Figlet, figlet_format
except Exception:
    print("Missing dependency: pyfiglet not installed. Run: pip install pyfiglet")
    raise SystemExit(1)

def clear_screen():
    os.system("clear" if os.name == "posix" else "cls")

def centered_figlet(text, font=FIGLET_FONT):
    # make ascii-art with pyfiglet and center lines to terminal width
    f = Figlet(font=font)
    art = f.renderText(text).rstrip("\n")
    cols = shutil.get_terminal_size((80, 20)).columns
    lines = art.splitlines()
    centered = "\n".join(line.center(cols) for line in lines)
    return centered

def show_banner_only():
    clear_screen()
    art = centered_figlet(BANNER_TEXT)
    print(art)

def show_banner_with_login_prompt():
    show_banner_only()
    print()  # small spacing
    # Put username/password prompt under the banner (center the prompt)
    cols = shutil.get_terminal_size((80,20)).columns
    user_prompt = "Username: "
    pass_prompt = "Password: "
    # center prompt labels (but input will appear after prompt)
    print(user_prompt.rjust((cols//2) + len(user_prompt)//2), end="")
    u = input().strip()
    print(pass_prompt.rjust((cols//2) + len(pass_prompt)//2), end="")
    p = getpass.getpass("")
    return u, p

def main_menu():
    while True:
        clear_screen()
        # show smaller banner on menu too (optional)
        print(centered_figlet(BANNER_TEXT, font="standard"))
        print("-"*40)
        print("1) SEO Helper")
        print("2) Thumbnail Helper")
        print("3) Social Post Generator")
        print("4) Scheduler (demo)")
        print("5) Exit")
        choice = input("\nSelect option: ").strip()
        if choice == "1":
            topic = input("Enter your video topic: ").strip()
            title = f"{topic} | Best Tips & Tricks 2025"
            desc = f"Learn about {topic}! Subscribe for more. #MananAutomation"
            print("\n[SEO Output]")
            print("Title:", title)
            print("Description:", desc)
            input("\nPress Enter to return to menu...")
        elif choice == "2":
            topic = input("Enter thumbnail title (short): ").strip()
            print("\nThumbnail idea: BIG TEXT | 1-2 WORDS | High contrast")
            input("\nPress Enter to return to menu...")
        elif choice == "3":
            link = input("Enter your video URL: ").strip()
            print("\nSocial post (ready):")
            print(f"Watch now: {link} \n#MananAutomation")
            input("\nPress Enter to return to menu...")
        elif choice == "4":
            post = input("Write the post text: ").strip()
            delay = input("Delay seconds before demo-post (enter 0 to post now): ").strip()
            try:
                sec = int(delay)
            except:
                sec = 0
            print(f"\nScheduled demo: posting after {sec} second(s)...")
            time.sleep(sec)
            print(f"Posted: {post}")
            input("\nPress Enter to return to menu...")
        elif choice == "5":
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid choice. Try again.")
            time.sleep(1)

def main():
    # 1) Show big centered banner only (no other header)
    clear_screen()
    print(centered_figlet(BANNER_TEXT, font=FIGLET_FONT))
    # 2) Then username/password prompts appear under it
    cols = shutil.get_terminal_size((80,20)).columns
    # simple centered prompts
    u = input("Username: ".center(cols//2))
    p = getpass.getpass("Password: ".center(cols//2))
    if u == USERNAME and p == PASSWORD:
        # on successful login, clear screen then show menu
        clear_screen()
        main_menu()
    else:
        print("\n❌ Wrong username or password!")
        time.sleep(1)

if __name__ == "__main__":
    main()
