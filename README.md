# Alias-Bomber v1
 Efficient and fast email bomber that utilizes multithreading and has a hwid logger that can connect to an API for auth.
 
## DISCLAIMER:THIS PROJECT IS FOR ACADEMIC PURPOSES ONLY. THE DEVELOPERS TAKE NO RESPONSIBILITY FOR ILLEGAL USAGE AND/OR POTENTIAL HARMS.

## Requirements
- Python 3.10+
- Basic Programming Knowledge

## Installation

## 1. Clone The Repo

You can either clone it or download the zip.
```
git clone https://github.com/aliasnoclip/Alias-Bomber.git
cd Alias-bomber
```

## 2. hwid checker setup


In ```hwid_checker.py``` find the ```send_hwid()``` function and edit it to your liking. I'm not going to tell you how to make an API (You should already know) but make sure your api is able to take whatever parameters you sent in the ```hwid_data``` variable

## Example: 
```
data = {
def send_hwid(self):
        #params
        hwid_data = {
            'hwid': self.hwid,
            'proccesor': self.proccesor,
            'version': self.version,
            'serial_number': self.serial_number
        }
        url = "https://yourapi.com/api"
        response = requests.post(url, json=hwid_data)
        print(response.status_code)
}
```

- If you aren't interested in using an API then you can just delete it

## 3. Bomber Setup


Inside of ```main.py``` change the variables like ```password, sender_email and reciever_email``` to your preference. If you'd like to make it more automated, you can put something like ```password = input("enter a password ")``` so you don't have to go into the code base to change it all the time.

# Tips

- If you want to prevent your emails from entering the spam folder, using proxies and or increase the cooldown in the ```main.py``` file.

- Use email subjects and phrases that spam filters haven't already learned to defend against.

- Use a aged gmail account, protonmail and outlook hit the spam folder quicker.






## License:
MIT
