import colorama
from colorama import Fore as fore
import subprocess
import os
import hashlib
from cryptography.fernet import Fernet
from tkinter import filedialog


def clear():
    if os.name == "nt":  # Windows
        subprocess.run("cls", shell=True)
    else:  # Linux/macOS
        subprocess.run("clear", shell=True)

def logo():

    print(fore.MAGENTA + '''
██████╗░██████╗░░█████╗░██████╗░██╗░░░██╗██████╗░████████╗
██╔══██╗╚════██╗██╔══██╗██╔══██╗╚██╗░██╔╝██╔══██╗╚══██╔══╝
██║░░██║░█████╔╝██║░░╚═╝██████╔╝░╚████╔╝░██████╔╝░░░██║░░░
██║░░██║░╚═══██╗██║░░██╗██╔══██╗░░╚██╔╝░░██╔═══╝░░░░██║░░░
██████╔╝██████╔╝╚█████╔╝██║░░██║░░░██║░░░██║░░░░░░░░██║░░░
╚═════╝░╚═════╝░░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░░░░░░░╚═╝░░░''' + fore.RESET)

def OPs():
    print(fore.GREEN + "[01] Encrypt")
    print(fore.CYAN + "[02] Decrypt")
    print(fore.RED + "[00] Quit"+ fore.RESET)
    
    OP = input(fore.GREEN + ">_" + fore.RESET)
    if OP == '01' or OP == '1':
        encrypt()
    elif OP == '02' or OP == '2':
        decrypt()
    elif OP == '00' or OP == '0':
        quit()
    else:
        print(fore.RED + "Invalid Option" + fore.RESET)
        OPs()

def encrypt():
    O = input(fore.GREEN + "Generate Key? [Y/N] >_" + fore.RESET)
    if O.lower() == 'y':
        key = Fernet.generate_key()
        name = input(fore.GREEN + "Key name >_")
        folder = filedialog.askdirectory(title='key output')
        with open(f"{folder}/{name}.key", "wb") as key_file:
            key_file.write(key)
        print(fore.CYAN + f"🔑 Key in:: {folder}/{name}.key")
        print(fore.YELLOW + f"Generated key at: {key.decode()}")
    elif O.lower() == 'n':
        key = input(fore.GREEN + "Enter Key >_" + fore.RESET).encode()
    
    f = Fernet(key)
    msg = filedialog.askopenfilename(title='select file to crypt')
    
    with open(msg, "rb") as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(msg, "wb") as file:
        file.write(encrypted_data)
    print(fore.YELLOW + "📜 Cryptedddddd!!!!! >;3")
    input("Pres Enter")
    clear()
    logo()
    OPs()


def decrypt():
    O = input(fore.GREEN + "Do you have the key? [Y/N] >_" + fore.RESET)

    if O.lower() == 'y':
        key = input(fore.GREEN + "Enter the key >_" + fore.RESET).encode()
        try:
            f = Fernet(key)
            msg = filedialog.askopenfilename(title='Select the file to decrypt')
            with open(msg, "rb") as file:
                file_data = file.read()
            decrypted_data = f.decrypt(file_data)
            with open(msg, "wb") as file:
                file.write(decrypted_data)
            print(fore.YELLOW + "📜 Successfully decrypted!")
        except Exception as e:
            print(fore.RED + f"❌ Failed to decrypt with provided key: {e}")

    elif O.lower() == 'n':
        print(fore.CYAN + "🔍 You will now select a wordlist to try brute force...")
        list_path = filedialog.askopenfilename(title="Select a wordlist (one key per line)")
        with open(list_path, "r") as f:
            keys = [line.strip().encode() for line in f if line.strip()]

        msg = filedialog.askopenfilename(title='Select the file to decrypt')
        with open(msg, "rb") as file:
            encrypted_data = file.read()

        success = False
        for i, key in enumerate(keys, 1):
            try:
                f = Fernet(key)
                decrypted_data = f.decrypt(encrypted_data)
                with open(msg, "wb") as file:
                    file.write(decrypted_data)
                print(fore.GREEN + f"✅ Decryption successful with key #{i} -> {key.decode()}")
                success = True
                break
            except Exception:
                print(fore.RED + f"❌ Key #{i} failed.")

        if not success:
            print(fore.YELLOW + "All keys failed. Decryption unsuccessful.")

    else:
        print(fore.RED + "Invalid option.")
    
    input("Press Enter to return to menu...")
    clear()
    logo()
    OPs()

clear()
logo()
OPs()