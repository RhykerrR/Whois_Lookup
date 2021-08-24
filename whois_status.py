import re


status_list = []

with open("domain_out.txt", "r") as f:
    content = f.read()   
pattern = "([a-z0-9].+[a-z0-9]+.\s\s)(?:[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}.|[0-9]{4}-[a-zA-Z0-9]{2,3}-[0-9]{2}) (?:(?:(?:[A-z0-9]+(?:-[A-z0-9]+)*\.)+[A-z]{2,})) ([a-zA-Z]+\s[a-zA-Z]+://(?:[a-zA-Z]+(?:\.[a-zA-Z]+)+)/[a-zA-Z]+#[a-zA-Z]+)"
check = re.findall(pattern, content, re.MULTILINE)

for i in check:
    (domain, status) = i    
    if not status.startswith("ok"):
        print (domain.rstrip() + " --> " + status)
