import requests
from parse_scouting_data import main
from os import system, remove
import time
from glob import glob
from datetime import datetime
import pytz

# where the data is hosted
from_url = "https://wsform.com/wp-content/uploads/2021/04/day.csv"

# check if current time is between 8am and 8pm EST
est = pytz.timezone('US/Eastern')
current_time = datetime.now(est)
current_hour = current_time.hour

if current_hour >= 8 and current_hour < 20:
    print("Script can only run outside of 8am-8pm EST")
    exit()


# download the data
response = requests.get(from_url)
with open('_VScouterData.csv', 'wb') as f:
    f.write(response.content)

# clear old html reports
for i in glob('team_pages/*.html'):
    remove(i)

# pull the latest changes
# this allows us to update formulas without needing to access this machine
system("git pull")

# generate the new html reports
main()

# make use of git to automatically update the report
# if their are no changes it will not commit anything
system("git add .")
system("git commit -m 'updated report'")
system("git push")



