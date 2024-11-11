version = 1.1

import os
import keyboard
import requests
import json
from prettytable import PrettyTable
from colorama import Fore, Style

os.system("cls" if os.name == "nt" else "clear")

if os.name != "nt":
    print("You must be using Windows 11/10 to run this program.")
    print("Press any key to continue...", end="", flush=True)
    keyboard.read_event()
    exit()
    
    
os.system("title Phantom Locator")    
    
def locate(ip):
    try:
        ip_response = requests.get(f"http://ip-api.com/json/{ip}")
        ip_data = json.loads(ip_response.text)
        
        table = PrettyTable(["Category", "Value"])
        
        table.add_row(["Country", f"{ip_data['country']} ({ip_data['countryCode']})"])
        table.add_row(["Region", f"{ip_data['regionName']} ({ip_data['region']})"])
        table.add_row(["City", ip_data["city"]])
        table.add_row(["ZIP Code", ip_data["zip"]])
        table.add_row(["Latitude", ip_data["lat"]])
        table.add_row(["Longitude", ip_data["lon"]])
        table.add_row(["Timezone", ip_data["timezone"]])
        table.add_row(["Internet Service Provider", ip_data["isp"]])
        table.add_row(["Organization", ip_data["org"]])
        table.add_row(["Autonomous System", ip_data["as"]])
         
        faded = ""
        red = 40
        lines = str(table).splitlines()  # Convert table to string before splitting

        for i, line in enumerate(lines):
            faded += f"\033[38;2;{red};0;220m{line}\033[0m"
            if red < 255:
                red += 15
                if red > 255:
                    red = 255
            if i < len(lines) - 1:
                faded += "\n"
        
        if ip == "":
            ip = "yourself"
        
        print(f"{Fore.MAGENTA}IP Info for: {ip}{Style.RESET_ALL}\n{faded}\n")
    except Exception as e:
        print(f"An unknown error occurred ({e})")
        exit()
    
while True:
    text = f"""
                         ____  _                 _                    _                    _             
                        |  _ \\| |__   __ _ _ __ | |_ ___  _ __ ___   | |    ___   ___ __ _| |_ ___  _ __  
                        | |_) | '_ \\ / _` | '_ \\| __/ _ \\| '_ ` _ \\  | |   / _ \\ / __/ _` | __/ _ \\| '__|
                        |  __/| | | | (_| | | | | || (_) | | | | | | | |__| (_) | (_| (_| | || (_) | |   
                        |_|   |_| |_|\\__,_|_| |_|\\__\\___/|_| |_| |_| |_____\\___/ \\___\\__,_|\\__\\___/|_| v{version}
                        by: Phantom Services                      
                        
                        ╔═════════════════════════════╗
                        ║   1. Geolocate IP Address   ║
                        ║   2. Exit                   ║
                        ╠═════════════════════════════╝
                        ║
                        ╚═> """

    # Make text purple gradient
    os.system("")
    faded = ""
    red = 40
    lines = text.splitlines()

    for i, line in enumerate(lines):
        faded += f"\033[38;2;{red};0;220m{line}\033[0m"
        if not red == 255:
            red += 15
            if red > 255:
                red = 255
        if i < len(lines) - 1:
            faded += "\n"
        
    print(faded, end="")

    option = input()
    if option == "1":
        os.system("cls")
        ip_address = input(f"{Fore.MAGENTA}Enter an IP address: {Style.RESET_ALL}")
        os.system("cls")
        locate(ip_address)
        break
    elif option == "2":
        exit()
    else:
        os.system("cls")
    
input("Press enter to continue...")
