import subprocess
import uuid
import requests
import re
import platform

class HWID:
    def __init__(self):
        self.hwid = None
        self.model_name = None
        self.serial_number = None
        self.proccesor = None
        self.version = None
        
    def get_hwid_mac(self):
        output = subprocess.check_output(['ioreg', '-rd1', '-c', 'IOPlatformExpertDevice']).decode()
        hwid = re.search("(?<=IOPlatformUUID\" = \")[^\"]*", output)
        serial_number = re.search("(?<=IOPlatformSerialNumber\" = \")[^\"]*", output)
        self.hwid = hwid.group()
        self.proccesor = platform.processor()
        self.version = platform.mac_ver()[0]
        self.serial_number = serial_number.group()
        return self.hwid, self.serial_number, self.version, self.proccesor

    def get_hwid_windows(self):
        self.hwid = str(uuid.getnode())
        return self.hwid
    
    def send_hwid(self):
        hwid_data = {
            'hwid': self.hwid,
            'proccesor': self.proccesor,
            'version': self.version,
            'serial_number': self.serial_number
        }
        url = "https://yourapi.com/api"
        response = requests.post(url, json=hwid_data)
        print(response.status_code)
