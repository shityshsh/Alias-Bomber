import smtplib
import time
import curses
from colorama import Fore, Style
import subprocess
import multiprocessing
from multiprocessing.pool import ThreadPool
import threading
from threading import Thread
import sib_api_v3_sdk as sib
from hwid_logger import HWID
from email.mime.text import MIMEText
from tools.functions import clear, system
from modules.outlook import send_outlook_emails
from modules.gmail import send_gmail_emails
import os












def ascii():
    print( Fore.LIGHTRED_EX + f"""\
    

        
    
 
 

                                    _ _             ____                  _                      __ 
                              /\   | (_)           |  _ \                | |                    /_ |
                             /  \  | |_  __ _ ___  | |_) | ___  _ __ ___ | |__   ___ _ __  __   _| |
                            / /\ \ | | |/ _` / __| |  _ < / _ \| '_ ` _ \| '_ \ / _ \ '__| \ \ / / |
                           / ____ \| | | (_| \__ \ | |_) | (_) | | | | | | |_) |  __/ |     \ V /| |
                          /_/    \_\_|_|\__,_|___/ |____/ \___/|_| |_| |_|_.__/ \___|_|      \_/ |_|

                                                                           
                                          {Fore.RED + "  Coded By Alias -- github.com/aliasnoclip" + Style.RESET_ALL}                                              
                                                                                         
    
    """)



def display_menu():
    print( Fore.LIGHTRED_EX + """
    
    Alias Emailer v1 | Home | alias#9999
    
    [1] Gmail
    
    [2] Outlook
    
    """ + Style.RESET_ALL)

def handle_choice(choice):
    if choice == "1":
        send_gmail_emails()
        pass
    elif choice == "2":
        send_outlook_emails()
        pass
    elif choice == "3":
        # code for option 3 v2
        pass
    elif choice == "4":
                clear()
    elif choice == "5":
        print("Exiting...")
        exit()
    else:
        print("Invalid choice. Please try again.")
        time.sleep(2)
        clear()



while True:
    ascii()
    display_menu()
    choice = input("Enter your choice: ")
    handle_choice(choice)








   
