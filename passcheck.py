import re
from colorama import Fore, Style, init
import pyfiglet
import requests
import os

init(autoreset=True)

def download_rockyou_file():
    url = 'https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt'
    response = requests.get(url)
    with open('rockyou.txt', 'wb') as file:
        file.write(response.content)

def is_password_in_rockyou(password):
    if not os.path.isfile('rockyou.txt'):
        download_rockyou_file()
    with open('rockyou.txt', 'r', encoding='latin-1') as file:
        for line in file:
            if password == line.strip():
                return True
    return False

def password_strength(password):
    length = len(password)
    complexity = 0
    suggestions = []
    
    if length >= 8:
        complexity += 1
    else:
        suggestions.append("🔸 " + Fore.YELLOW + "Make your password at least 8 characters long.")

    if re.search(r"[a-z]", password):
        complexity += 1
    else:
        suggestions.append("🔸 " + Fore.YELLOW + "Include at least one lowercase letter.")

    if re.search(r"[A-Z]", password):
        complexity += 1
    else:
        suggestions.append("🔸 " + Fore.YELLOW + "Include at least one uppercase letter.")

    if re.search(r"\d", password):
        complexity += 1
    else:
        suggestions.append("🔸 " + Fore.YELLOW + "Include at least one digit.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        complexity += 1
    else:
        suggestions.append("🔸 " + Fore.YELLOW + "Include at least one special character (e.g., !, @, #, $, etc.).")

    if re.search(r"(.)\1{2,}", password):
        complexity -= 1
        suggestions.append("🔸 " + Fore.YELLOW + "Avoid sequences of the same character (e.g., 'aaa').")

    if complexity == 0:
        strength = "Very Weak"
        color = Fore.RED
        emoji = "🔴"
    elif complexity == 1:
        strength = "Weak"
        color = Fore.RED
        emoji = "🟠"
    elif complexity == 2:
        strength = "Moderate"
        color = Fore.YELLOW
        emoji = "🟡"
    elif complexity == 3:
        strength = "Strong"
        color = Fore.GREEN
        emoji = "🟢"
    elif complexity == 4:
        strength = "Very Strong"
        color = Fore.GREEN
        emoji = "🟢"
    else:
        strength = "Excellent"
        color = Fore.CYAN
        emoji = "🔵"
    
    return f"{color}Password Strength: {strength} {emoji}", suggestions

def main():
    tool_name = "PassCheck"
    ascii_art = pyfiglet.figlet_format(tool_name, font="drpepper")
    colored_ascii = f"{Fore.BLUE}{Style.BRIGHT}{ascii_art}"
    print(colored_ascii + Fore.RED + " V-2.0\n")
    
    hackbit_website = "https://hackbit.org/"
    link_hackbit = f"\033]8;;{hackbit_website}\033\\hackbit.org\033]8;;\033\\"
    
    
    print(f"{Fore.GREEN}Created by {Style.BRIGHT}@0xSaikat{Style.RESET_ALL}{Fore.GREEN} and an official tool of {link_hackbit}.\n")
    
    while True:
        user_password = input(Fore.GREEN + "🔑 Enter your password to check its strength (or press 'q' to quit): " + Style.RESET_ALL)
        
        if user_password.lower() == 'q':
            print(Fore.CYAN + "Goodbye! 👋")
            break
        
        print()

        if is_password_in_rockyou(user_password):
            print(Fore.RED + "[+] " + Style.RESET_ALL + "Your password is weak and exposed on the internet...!")
            secure_choice = input(Fore.RED + "[+] " + Style.RESET_ALL + "Do you want to secure your password and make it strong (yes/no)? " + Style.RESET_ALL)
            if secure_choice.lower() == 'yes':
                print("\n🔸 Use a mix of uppercase and lowercase letters.")
                print("🔸 Include at least one digit.")
                print("🔸 Add special characters like !, @, #, $, etc.")
                print("🔸 Make your password at least 12 characters long.")
                print("🔸 Avoid using common words or easily guessable information.")
                print("🔸 Avoid using sequences of the same character.\n")
            else:
                print(Fore.CYAN + "Goodbye! 👋")
                break
        else:
            strength, suggestions = password_strength(user_password)
            print(Fore.RED + "[+] " + Style.RESET_ALL + "Your password is safe...!")
            print(strength + "\n")
            print(Fore.RED + "[+] " + Style.RESET_ALL + "Here are some recommendations to make a good password:")
            for suggestion in suggestions:
                print(suggestion)
            secure_choice = input(Fore.RED + "[+] " + Style.RESET_ALL + "Do you want to make the password more strong (yes/no)? " + Style.RESET_ALL)
            if secure_choice.lower() == 'yes':
                print("\n🔸 Use a mix of uppercase and lowercase letters.")
                print("🔸 Include at least one digit.")
                print("🔸 Add special characters like !, @, #, $, etc.")
                print("🔸 Make your password at least 12 characters long.")
                print("🔸 Avoid using common words or easily guessable information.")
                print("🔸 Avoid using sequences of the same character.\n")
            else:
                print(Fore.CYAN + "Goodbye! 👋")
                break

if __name__ == "__main__":
    main()
