import re
from colorama import Fore
import requests

website = "https://www.vulnhub.com/"
result = requests.get(website)
content = result.text

pattern = r"/entry/[\w-]*"
repeated_machines = re.findall(pattern, str(content))
no_duplicates = list(set(repeated_machines))

final_machines = []

for i in no_duplicates:
    machines_name = i.replace("/entry/", "")
    final_machines.append(machines_name)
    print(machines_name)

###########################

maquina_noob = "noob-1"
existe_noob = False

for a in final_machines:
    if a == maquina_noob:
        existe_noob= True
        break

color_green = Fore.GREEN
color_yellow = Fore.YELLOW

if existe_noob == True:
    print("\n" +  color_green + "there are no new machines")
else:
    print("\n" + color_yellow + "New machine!")



