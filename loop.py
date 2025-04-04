import requests
from parse_scouting_data import main
from os import system, remove
import time
from glob import glob
from datetime import datetime
import pytz

while True:
    # check if current time is between 8am and 8pm EST
    est = pytz.timezone('US/Eastern')
    current_time = datetime.now(est)
    current_hour = current_time.hour

    if current_hour >= 8 and current_hour < 20:
        print("Script can only run outside of 8am-8pm EST")
        time.sleep(60*60)
        continue

    system("git pull")
    # download the data
    # clear old html reports
    for i in glob('team_pages/*.html'):
        remove(i)
    try:
        #    generate the new html reports
        main()
    except:
        print("waiting first data drop")
        time.sleep(15 * 60)
        continue
    # make use of git to automatically update the report
    # if their are no changes it will not commit anything
    system("git add .")
    system("git commit -m 'updated report'")
    system("git push")
    time.sleep(30 * 60) # minute



