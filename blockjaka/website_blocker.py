import time
from datetime import datetime as dt
hosts_path=r"C:\Windows\System32\drivers\etc\hosts" #r 的母的是不要转移转义
hosts_temp="hosts"
redirect = "127.0.0.1"
website_list=["www.facebook.com","facebook.com","www.youtube.com","youtube.com","mail.ru","e.mail.ru","www.mail.ru"]
# we will use task scheduler,we also can use the third party tools
print("Hello, Sir ,My name is [Yaakov Robot], I am responsible for your daily work.\n")
while True:
    #add and remove the host file in a proper time
    if dt(dt.now().year,dt.now().month,dt.now().day,8) <dt.now() <dt(dt.now().year,dt.now().month,dt.now().day,16):
        print("Working Hours.....")
        with open(hosts_path,'r+') as file:
                content=file.read()
                for website in website_list:
                    if website in content:
                        pass
                    else:
                        file.write(redirect+" "+website+"\n")
    else:
        with open(hosts_path,'r+') as file:
            content=file.readlines()
            file.seek(0) # set the pointer to the first line
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)# checks for the line has or not the websites list and it will work
            file.truncate() # that means everyhthing gones below.
        print("Fun Hours......")
    time.sleep(5) #print every five seconds.
