import subprocess
import re
import tldextract
from data_if_loop import domain_lookup

with open("domain_list.txt") as f:
    domain_all = f.read().splitlines()

with open ("domain_out.txt", "w") as f:
    f.write("")

temp = []

for domain in domain_all:
    domain = tldextract.extract(domain)
    domain = "{}.{}".format(domain.domain, domain.suffix)
    domain_all = set(domain)
    if domain not in temp:
        temp.append(domain)

temp.remove('.') 

for domain in temp:
    
    print (domain)
    
    d = tldextract.extract(domain)
    d = "{}".format(d.suffix)
    temp = set(d)
  
    tld = domain_lookup(domain)
     
    def whois(ip,name):
        p = subprocess.Popen(['whois', ip], stdout=subprocess.PIPE)
        out, err = p.communicate()
        m = re.search(tld.get(name), out.decode('ISO-8859-9'))
        return m.group(1)
    
    def whois_server(ip,name):
        p = subprocess.Popen(['whois', ip], stdout=subprocess.PIPE)
        out, err = p.communicate()
        try:
            m = re.findall(tld.get(name), out.decode('ISO-8859-9'))
        except:
            m = re.findall(tld.get(name), out.decode('ISO-8859-9')).group(1)
        return m
    
    with open("domain_out.txt", "a") as f: 
        f.writelines(domain)
        f.writelines("\n")
        try:
            f.writelines(" " + whois(domain, "expiration_date") + "\n")
            f.writelines(" " + str(whois_server(domain, "name_servers")) + "\n")
            f.writelines(" " + whois(domain, "status") + "\n")
        except:
            f.writelines("\n")
        f.writelines("\n")
  
  
