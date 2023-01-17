# Alias-Bomber v1
 Efficient and fast email bomber that utilizes multithreading and has a hwid logger that can connect to an API for auth.
 
## DISCLAIMER:THIS PROJECT IS FOR ACADEMIC PURPOSES ONLY. THE DEVELOPERS TAKE NO RESPONSIBILITY FOR ILLEGAL USAGE AND/OR POTENTIAL HARMS.

- Adding API Support + Proxies For v2
- Gmail collapses multiple emails sent within a certain amount of time, im working on a solution/adding multiple mail support.


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

## 2. hwid checker setup - for skids only


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


## 3. Getting Gmail App Key

`
Go To Your Gmail --> Manage Google Your Account ---> Security Sigining In With Gmail ---> Enable 2FA ---> Repeat The First 3 Steps Then Click "App Passwords" and create your key.
`

# Tips

- Use email subjects and phrases that spam filters haven't already learned to defend against.

- Use a aged gmail account, protonmail and outlook hit the spam folder quicker.

- Verify your outlook with a phone number before sending out emails with it or it will get locked instantly



## License:
MIT
