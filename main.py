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
from hwid_checker import HWID














print(Fore.RED + f"""\
    
 
  ______   __  __                            _______                           __                                               __   
 /      \ /  |/  |                          /       \                         /  |                                            _/  |  
/$$$$$$  |$$ |$$/   ______    _______       $$$$$$$  |  ______   _____  ____  $$ |____    ______    ______         __     __ / $$ |  
$$ |__$$ |$$ |/  | /      \  /       |      $$ |__$$ | /      \ /     \/    \ $$      \  /      \  /      \       /  \   /  |$$$$ |  
$$    $$ |$$ |$$ | $$$$$$  |/$$$$$$$/       $$    $$< /$$$$$$  |$$$$$$ $$$$  |$$$$$$$  |/$$$$$$  |/$$$$$$  |      $$  \ /$$/   $$ |  
$$$$$$$$ |$$ |$$ | /    $$ |$$      \       $$$$$$$  |$$ |  $$ |$$ | $$ | $$ |$$ |  $$ |$$    $$ |$$ |  $$/        $$  /$$/    $$ |  
$$ |  $$ |$$ |$$ |/$$$$$$$ | $$$$$$  |      $$ |__$$ |$$ \__$$ |$$ | $$ | $$ |$$ |__$$ |$$$$$$$$/ $$ |              $$ $$/    _$$ |_ 
$$ |  $$ |$$ |$$ |$$    $$ |/     $$/       $$    $$/ $$    $$/ $$ | $$ | $$ |$$    $$/ $$       |$$ |               $$$/    / $$   |
$$/   $$/ $$/ $$/  $$$$$$$/ $$$$$$$/        $$$$$$$/   $$$$$$/  $$/  $$/  $$/ $$$$$$$/   $$$$$$$/ $$/                 $/     $$$$$$/ 
                                                                                                                                     
                                                                                                                                     
                                                                                                                                     


                                          {Fore.BLUE + "  Coded By Alias -- github.com/aliasnoclip" + Style.RESET_ALL}                                              
                                                                                         
""" + Style.RESET_ALL)




sender_email = ""
receiver_email = ""
password = ""
message = "IDJFHDID PEBVGYJC GGWGFBFI HUOKB"
num_emails = 1
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender_email, password)

def send_email(sender_email, receiver_email, password, message):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
        server.quit()
        print("email sent")
    except:
        print("error sending email")    
threads = []
for i in range(num_emails):
    thread = Thread(target=send_email, args=(sender_email, receiver_email, password, message))
    thread.start()
    time.sleep(1)
    threads.append(thread)

for thread in threads:
    thread.join()

print("All emails sent to "+receiver_email)

   
