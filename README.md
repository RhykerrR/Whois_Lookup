# Whois_Lookup
Python scripts that gives some useful information about the domains we want. This script makes use of regex a lot. We take all the regex info from data.py.
## whois_main
Reads domains from the domain_list.txt and pastes expiration date, name server and status of those domains to domain_out.txt.
## whois_time
Reads expiration date from the domain_out.txt and sends an email to our entered email.
## whois_dns
Reads name server from the domain_out.txt and prints them with their corresponded ip.
## whois_status
Reads status from the domain_out.txt and prints them.


### Usage
>$ sudo apt install whois

Our code makes use of subprocess.popen to query whois
### Support
Linux / Python 3.X
