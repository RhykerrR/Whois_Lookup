import re

status_list = []

with open("domain_out.txt", "r") as f:
    content = f.read()   
pattern = "^([a-zA-Z]+(?:\.[a-zA-Z]+)+).*$\n.+\n.+.\n.(.+)"
check = re.findall(pattern, content, re.MULTILINE)

for i in check:
    (domain, status) = i  
    if not status.startswith("ok"):
        print (domain.rstrip() + " --> " + status)
