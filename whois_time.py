import re
from datetime import datetime
import smtplib

sender = input ("Enter sender email: ")
password = input("Enter password: ")
receiver = input("Enter receiver email: ")

with open("domain_out.txt", "r") as f:
    content = f.read()
pattern = "\d{4}[/.-]\w{2,3}[/.-]\d{2}|\d{8}|\d{1,2}[/.-]\w{1,3}[/.-]\d{4}|\w{1,4}[ ]\w{2,3}[ ]\d{4}"
dates = re.findall(pattern, content)


fmt = '%d/%B/%Y'
date_list = []
message_list = []

for date in dates:        
    
    if "-" in date:   
        try:          
            date = datetime.strptime(date, '%Y-%m-%d').strftime(fmt)
                   
        except ValueError:                         
            try:
                date = datetime.strptime(date, '%Y-%b-%d').strftime(fmt)
        
            except ValueError:
                try:
                    date = datetime.strptime(date, '%d-%b-%Y').strftime(fmt)           
        
                except ValueError:
                    date = datetime.strptime(date, '%d-%m-%Y').strftime(fmt)
                    
                    
    elif "." in date:                     
        try:
            date = datetime.strptime(date, '%Y.%m.%d').strftime(fmt)
            
        except ValueError:
            date = datetime.strptime(date, '%d.%m.%Y').strftime(fmt)
            
    elif " " in date:
        try:
            date = datetime.strptime(date, '%b %d %Y').strftime(fmt)
            
        except ValueError:
            try:
                date = datetime.strptime(date, '%dst %b %Y').strftime(fmt)
            except ValueError:
                try:
                    date = datetime.strptime(date, '%dnd %b %Y').strftime(fmt)
                except ValueError:
                    try:
                        date = datetime.strptime(date, '%drd %b %Y').strftime(fmt)
                    except ValueError:
                        try:
                            date = datetime.strptime(date, '%dth %b %Y').strftime(fmt)
                        except ValueError:
                            pass
    elif "/" in date:  
        try:
            date = datetime.strptime(date, '%d/%m/%Y').strftime(fmt)
    
        except ValueError:
            pass
    else:
        date = datetime.strptime(date, '%Y%m%d').strftime(fmt)
            
    date_list.append(date)

         
d1 = date_list
d2 = datetime.today().strftime(fmt)
d2 = datetime.strptime(d2, fmt)

domains = re.findall("([a-zA-Z]+(?:\.[a-zA-Z]+)+)\n.+(?=\d{4}[/.-]\w{2,3}[/.-]\d{2}|\d{8}|\d{1,2}[/.-]\w{1,3}[/.-]\d{4}|\w{1,4}[ ]\w{2,3}[ ]\d{4})", content)
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


    if 0 <= d <= 60: #give warning in 60 days
        
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


