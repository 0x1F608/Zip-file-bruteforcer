import zipfile
import math
import os
import concurrent.futures
from datetime import datetime
from colorama import Fore
from pystyle import *


def title(args):
    if args:
        os.system(f"title Zip brutalizer [~] Made with love by HannahHaven [~] {args}")
    else:
        os.system("title Zip brutalizer [~] Made with love by HannahHaven")

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

ascii_art = """ _____   ________     __               __        ___                
/__  /  /  _/ __ \   / /_  _______  __/ /_____ _/ (_)___  ___  _____
  / /   / // /_/ /  / __ \/ ___/ / / / __/ __ `/ / /_  / / _ \/ ___/
 / /___/ // ____/  / /_/ / /  / /_/ / /_/ /_/ / / / / /_/  __/ /    
/____/___/_/      /_.___/_/   \__,_/\__/\__,_/_/_/ /___/\___/_/   

"""




line_count = 0
clear()
status = "Status - Idle"
title(status)
print(Colorate.Horizontal(Colors.blue_to_cyan, ascii_art))  
print("")
zip_file_name = input(f"{Fore.YELLOW}[!]{Fore.RESET} Zip file name [name.zip]: ")
wordlist_file = input(f"{Fore.YELLOW}[!]{Fore.RESET} Wordlist: ")

print("")

status = "Status - Cracking"
title(status)
try:
    num_threads = 100000000000
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        with open(wordlist_file, 'r') as wordlist:
            starttime = datetime.now()
            with zipfile.ZipFile(zip_file_name, 'r') as zip_file:
                for line in wordlist:
                    password = line.strip()
                    line_count += 1
                    try:
                        zip_file.extractall(pwd=password.encode('utf-8'))
                        time_taken = datetime.now() - starttime
                        time_taken_truncated = math.trunc(time_taken.total_seconds())
                        print("")
                        print("[-]~~~~~~~~~~~~~~~~~~~~~~~~~~~~[-]")
                        print("")
                        print(f"{Fore.GREEN}[+]{Fore.RESET} Hash found on line {line_count}")
                        print(f"{Fore.GREEN}[+]{Fore.RESET} Password: {password}")
                        print(f"{Fore.GREEN}[+]{Fore.RESET} Time taken: {time_taken_truncated}s")
                        print("")
                        print("[-]~~~~~~~~~~~~~~~~~~~~~~~~~~~~[-]")

                        status = f"Status - Cracked in {time_taken_truncated}s"
                        title(status)
                        break
                    except Exception as e:
                        print(f"{Fore.RED}[-]{Fore.RESET} Incorrect password: {password} | {line_count}")
                else:
                    status = "Status - Failed to crack"
                    title(status)
                    print(f"{Fore.YELLOW}[!]{Fore.RESET} Password not found in the wordlist.")
except Exception as e:
    print(f"{Fore.YELLOW}[!]{Fore.RESET} A fatal error occured | {e}")
input(Center.XCenter("\nPress enter to end..."))