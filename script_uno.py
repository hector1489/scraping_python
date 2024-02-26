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

machine_noob = "noob-1"
exists_noob = False

for a in final_machines:
    if a == machine_noob:
        exists_noob= True
        break

color_green = Fore.GREEN
color_yellow = Fore.YELLOW

if exists_noob == True:
    print("\n" +  color_green + "there are no new machines")
else:
    print("\n" + color_yellow + "New machine!")



