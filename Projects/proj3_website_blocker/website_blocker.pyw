import time
from datetime import datetime as dt

#hosts_temp = r"C:\Users\admin\Documents\GitHub\learning_py\Projects\proj3_website_blocker\hosts"
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
website_list = ["www.facebook.com","www.sistech.ca","facebook.com","sistech.ca"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,12) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,22):
#        print "Working hours..."
        with open(hosts_path,'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.seek(0,2)
                    file.write(redirect+" "+website+"\n")
    else:
        with open(hosts_path,'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
#        print "Outside business hours..."

    time.sleep(5)