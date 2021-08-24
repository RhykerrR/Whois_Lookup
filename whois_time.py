import re
from datetime import datetime
import smtplib

sender = input ("Enter sender email: ")
password = input("Enter password: ")
receiver = input("Enter receiver email: ")



with open("domain_out.txt", "r") as f:
    content = f.read()
pattern = "\d{4}[/-]\w{2,3}[/-]\d{2}"
dates = re.findall(pattern, content)

fmt = '%d/%B/%Y'
list = []
message_list = []

for date in dates:        
    if "-" in date:               
        try:          
            date = datetime.strptime(date, '%Y-%m-%d').strftime(fmt)
                   
        except ValueError:                      
            
            date = datetime.strptime(date, '%Y-%b-%d').strftime(fmt)
            
    list.append(date)
          
d1 = list
d2 = datetime.today().strftime(fmt)
d2 = datetime.strptime(d2, fmt)

domains = re.findall(".*\s\s(?=\d{4}[/-]\w{2,3}[/-]\d{2})", content)
domains = map(lambda s: s.strip(), domains)
main_list = [' '.join(x) for x in zip(domains,d1)] 


for i in main_list:
    i = i.split()
    for a in i:
        try:
            a = datetime.strptime(a, fmt)
            d = ((a-d2).days)
            
        except ValueError:
            None


    if 0 <= d <= 60: #gives warning in 60 days
        
        message_list.append("Domain " + i.pop(0) + " is getting timed out in " + i.pop() + ". Only " + str(d) + " days left.") 
        


message_list.append("These are all the domains that are getting timed out in 60 days!")
message = ' \n\n'.join([str(item) for item in message_list])


server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()
server.login(sender, password)
server.sendmail(sender, receiver, message)
 
server.quit()

print ("Email sent!")




