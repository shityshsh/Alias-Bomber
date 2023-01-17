from email.mime.text import MIMEText
import smtplib
from colorama import Fore, Style
import os
from threading import Thread
import time
from tools.functions import clear

emails_sent = 0
emails_failed = 0

def send_gmail_emails():
    sender_email = input("Your Email: ")
    password = input("Your Password: ")
    receiver_email = input("Target Email: ")
    message = (MIMEText(input("Message: ")))
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = input("What is the subject? ")
    num_input = input("Number Of Emails: ")
    num_emails = int(num_input)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    try:
        server.login(sender_email, password)
    except:
        print("Log In Failed, Please Check Your Credentials")
        exit()

    def send_email_gmail(sender_email, receiver_email, password, message):
        global emails_sent
        global emails_failed
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
            server.quit()
            print(Fore.LIGHTGREEN_EX + "Email Sent" + Style.RESET_ALL)
            emails_sent += 1
        except:
            print(Fore.LIGHTRED_EX + f"Email Failed" + Style.RESET_ALL)
            emails_failed += 1    
    threads = []
    for i in range(num_emails):
        thread = Thread(target=send_email_gmail, args=(sender_email, receiver_email, password, message))
        thread.start()
        time.sleep(1)
        threads.append(thread)

    for thread in threads:
        thread.join()

    print(f"""
    
    [{emails_sent}] Succesfull Emails

    [{emails_failed}] Failed Emails
    
    
    """)

    time.sleep(3)
    clear()
