import re
import socket


dns_list = []

with open("domain_out.txt", "r") as f:
    content = f.read()
pattern = "((?:[A-Z0-9]+(?:-[A-Z0-9]+)*\.)+[A-Z]{2,})"
check = re.findall(pattern, content, re.MULTILINE)
for i in check:    
    if i not in dns_list:
        dns_list.append(i)       


for i in dns_list:
    try:
        addr = socket.gethostbyname(i)
        print (str(i) + " --> " + str(addr))
    except:
        print (str(i) + " --> No info")



