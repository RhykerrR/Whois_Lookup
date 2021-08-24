

com = {


    'domain_name':                r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':                r'Registrant\s*Organi(?:s|z)ation:\s?(.+)',
    'registrant_country':       r'Registrant Country:\s?(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':            r'Registry Expiry Date:\s?(.+)',
    'updated_date':                r'Updated Date:\s?(.+)',

    'name_servers':                r'Name Server:\s*(.+)\s*',
    'status':                    r'Status:\s?(.+)',
    'emails':                    r'[\w.-]+@[\w.-]+\.[\w]{2,4}',
}

ac_uk = {
    
    
    'domain_name':                r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':                r'Registrant\s*Organi(?:s|z)ation:\s?(.+)',
    'registrant_country':       r'Registrant Country:\s?(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':            r'Registry Expiry Date:\s?(.+)',
    'updated_date':                r'Updated Date:\s?(.+)',

    'name_servers':                r'Name Server:\s*(.+)\s*',
    'status':                    r'Status:\s?(.+)',
    'emails':                    r'[\w.-]+@[\w.-]+\.[\w]{2,4}',
    
    'registrant':               r'Registrant:\n\s*(.+)',

    'creation_date':            r'Registered on:\s*(.+)',
    'expiration_date':          r'Expiry date:\s*(.+)',
    'updated_date':             r'Last updated:\s*(.+)',

    'name_servers':             r'Name Servers:\s*(.+)\s*',
    'status':                   r'Registration status:\n\s*(.+)',

    'domain_name':              r'Domain:\n\s?(.+)',

    'owner':                    r'Domain Owner:\n\s?(.+)',
    'registrar':                r'Registered By:\n\s?(.+)',
    'registrant':               r'Registered Contact:\n\s*(.+)',
    'expiration_date':          r'Renewal date:\n\s*(.+)',

    'updated_date':             r'Entry updated:\n\s*(.+)',
    'creation_date':            r'Entry created:\n\s?(.+)',
    'name_servers':             r'Servers:\s*(.+)\t\n\s*(.+)\t\n',

}

am = {
    'domain_name':              r'Domain name:\s+(.+)',
    'status':                   r'Status:\s(.+)',

    'registrar':                r'Registrar:\s+(.+)',
    'registrant':               r'Registrant:\s+(.+)',
    'registrant_country':       r'Registrant:\n.+\n.+\n.+\n\s+(.+)',

    'creation_date':            r'Registered:\s+(.+)',
    'expiration_date':          r'Expires:\s+(.+)',
    'updated_date':             r'Last modified:\s+(.+)',

    'name_servers':             r'DNS servers.*:\n(?:\s+(\S+)\n)(?:\s+(\S+)\n)?(?:\s+(\S+)\n)?(?:\s+(\S+)\n)\n?',
}

amsterdam = {
    
    'domain_name':                r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':                r'Registrant\s*Organi(?:s|z)ation:\s?(.+)',
    'registrant_country':       r'Registrant Country:\s?(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':            r'Registry Expiry Date:\s?(.+)',
    'updated_date':                r'Updated Date:\s?(.+)',

    'name_servers':                r'Name Server:\s*(.+)\s*',
    'status':                    r'Status:\s?(.+)',
    'emails':                    r'[\w.-]+@[\w.-]+\.[\w]{2,4}',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':               r'Registrant Organization:\s?(.+)',

    'updated_date':             r'Updated Date:\s?(.+)',
    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':          r'Registry Expiry Date:\s?(.+)',

    'name_servers':             r'Name Server:\s*(.+)',
    'status':                   r'Domain Status:\s*(.+)',
}

ar = {
    
    'domain_name':                r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':                r'Registrant\s*Organi(?:s|z)ation:\s?(.+)',
    'registrant_country':       r'Registrant Country:\s?(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':            r'Registry Expiry Date:\s?(.+)',
    'updated_date':                r'Updated Date:\s?(.+)',

    'name_servers':                r'Name Server:\s*(.+)\s*',
    'status':                    r'Status:\s?(.+)',
    'emails':                    r'[\w.-]+@[\w.-]+\.[\w]{2,4}',

    'domain_name':              r'domain\s*:\s?(.+)',

    'registrar':                r'registrar:\s?(.+)',

    'creation_date':            r'registered:\s?(.+)',
    'expiration_date':          r'expire:\s?(.+)',
    'updated_date':             r'changed\s*:\s?(.+)',

    'name_servers':             r'nserver:\s*(.+)\s*',
}

at = {
    
    'domain_name':                r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':                r'Registrant\s*Organi(?:s|z)ation:\s?(.+)',
    'registrant_country':       r'Registrant Country:\s?(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':            r'Registry Expiry Date:\s?(.+)',
    'updated_date':                r'Updated Date:\s?(.+)',

    'name_servers':                r'Name Server:\s*(.+)\s*',
    'status':                    r'Status:\s?(.+)',
    'emails':                    r'[\w.-]+@[\w.-]+\.[\w]{2,4}',

    'domain_name':              r'domain:\s?(.+)',

    'updated_date':             r'changed:\s?(.+)',

    'name_servers':             r'nserver:\s*(.+)',
}

au = {
   
    'domain_name':                r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':                r'Registrant\s*Organi(?:s|z)ation:\s?(.+)',
    'registrant_country':       r'Registrant Country:\s?(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':            r'Registry Expiry Date:\s?(.+)',
    'updated_date':                r'Updated Date:\s?(.+)',

    'name_servers':                r'Name Server:\s*(.+)\s*',
    'status':                    r'Status:\s?(.+)',
    'emails':                    r'[\w.-]+@[\w.-]+\.[\w]{2,4}',

    'registrar':                r'Registrar Name:\s?(.+)',

    'updated_date':             r'Last Modified:\s?(.+)'
}

aw = {
    'domain_name':                r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':                r'Registrant\s*Organi(?:s|z)ation:\s?(.+)',
    'registrant_country':       r'Registrant Country:\s?(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':            r'Registry Expiry Date:\s?(.+)',
    'updated_date':                r'Updated Date:\s?(.+)',

    'name_servers':                    r'Name Server:\s*(.+)\s*',
    'status':                    r'Status:\s?(.+)',
    'emails':                    r'[\w.-]+@[\w.-]+\.[\w]{2,4}',

    'expiration_date':          None,
    'registrant_country':       None,

    'domain_name':              r'Domain name:\s?(.+)',
    'name_servers':             (
        r'''(?x:
            Domain\ nameservers:[ \t]*\n
            (?:[ \t]+) (\S+) (?:[ \t]+\S+)? \n       # ns1.tld.nl [A?]
            (?:(?:[ \t]+) (\S+) (?:[ \t]+\S+)? \n)?  # opt-ns2.tld.nl [A?]
            (?:(?:[ \t]+) (\S+) (?:[ \t]+\S+)? \n)?  # opt-ns2.tld.nl [AAAA?]
            (?:(?:[ \t]+) (\S+) (?:[ \t]+\S+)? \n)?  # opt-ns3.tld.nl [A?]
            (?:(?:[ \t]+) (\S+) (?:[ \t]+\S+)? \n)?  # opt-ns3.tld.nl [AAAA?]
            (?:(?:[ \t]+) (\S+) (?:[ \t]+\S+)? \n)?  # opt-ns4.tld.nl [A?]
            (?:(?:[ \t]+) (\S+) (?:[ \t]+\S+)? \n)?  # opt-ns4.tld.nl [AAAA?]
            (?:(?:[ \t]+) (\S+) (?:[ \t]+\S+)? \n)?  # opt-ns5.tld.nl [A?]
            (?:(?:[ \t]+) (\S+) (?:[ \t]+\S+)? \n)?  # opt-ns5.tld.nl [AAAA?]
            # Don't check for final LF; there might be even more records..
        )'''),
    'reseller':                 r'Reseller:\s?(.+)',
    'abuse_contact':            r'Abuse Contact:\s?(.+)',
}

bank = {
    'domain_name':                r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':                r'Registrant\s*Organi(?:s|z)ation:\s?(.+)',
    'registrant_country':       r'Registrant Country:\s?(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':            r'Registry Expiry Date:\s?(.+)',
    'updated_date':                r'Updated Date:\s?(.+)',

    'name_servers':                r'Name Server:\s*(.+)\s*',
    'status':                    r'Status:\s?(.+)',
    'emails':                    r'[\w.-]+@[\w.-]+\.[\w]{2,4}',

    'domain_name':              r'Domain Name:\s?(.+)',
    'registrar':                r'Registrar:\s*(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':          r'Registry Expiry Date:\s?(.+)',
    'updated_date':             r'Updated Date:\s?(.+)',
}

be = {
     'domain_name':                r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':                r'Registrant\s*Organi(?:s|z)ation:\s?(.+)',
    'registrant_country':       r'Registrant Country:\s?(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':            r'Registry Expiry Date:\s?(.+)',
    'updated_date':                r'Updated Date:\s?(.+)',

    'name_servers':                r'Name Server:\s*(.+)\s*',
    'status':                    r'Status:\s?(.+)',
    'emails':                    r'[\w.-]+@[\w.-]+\.[\w]{2,4}',

    'registrant':               r'Registrant:\n\s*(.+)',

    'creation_date':            r'Registered on:\s*(.+)',
    'expiration_date':          r'Expiry date:\s*(.+)',
    'updated_date':             r'Last updated:\s*(.+)',

    'name_servers':             r'Name Servers:\s*(.+)\s*',
    'status':                   r'Registration status:\n\s*(.+)',

    'registrar':                r'\nREGISTRAR:\s*(.+)\n',

    'creation_date':            r'\ncreated:\s*(.+)\n',
    'updated_date':             r'\nlast modified:\s*(.+)\n',
    'expiration_date':          r'\noption expiration date:\s*(.+)\n',

    'name_servers':             r'\nnameservers:\s*(.+)\n\s*(.+)\n',
    'status':                   r'\nStatus:\n\s*(.+)',

    'domain_name':              r'\nDomain:\s*(.+)',

    'registrar':                r'Company Name:\n?(.+)',

    'creation_date':            r'Registered:\s*(.+)\n',

    'status':                   r'Status:\s?(.+)',
}

biz = {
    'domain_name':                r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':                r'Registrant\s*Organi(?:s|z)ation:\s?(.+)',
    'registrant_country':       r'Registrant Country:\s?(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':            r'Registry Expiry Date:\s?(.+)',
    'updated_date':                r'Updated Date:\s?(.+)',

    'name_servers':                r'Name Server:\s*(.+)\s*',
    'status':                    r'Status:\s?(.+)',
    'emails':                    r'[\w.-]+@[\w.-]+\.[\w]{2,4}',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':               r'Registrant Organization:\s?(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':          r'Registry Expiry Date:\s?(.+)',
    'updated_date':             r'Updated Date:\s?(.+)',

    'status':                   None,
}

br = {
    'domain_name':                r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':                r'Registrant\s*Organi(?:s|z)ation:\s?(.+)',
    'registrant_country':       r'Registrant Country:\s?(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':            r'Registry Expiry Date:\s?(.+)',
    'updated_date':                r'Updated Date:\s?(.+)',

    'name_servers':                r'Name Server:\s*(.+)\s*',
    'status':                    r'Status:\s?(.+)',
    'emails':                    r'[\w.-]+@[\w.-]+\.[\w]{2,4}',

    'domain_name':              r'domain:\s?(.+)',

    'registrar':                'nic.br',
    'registrant':               None,
    'owner':                    r'owner:\s?(.+)',

    'creation_date':            r'created:\s?(.+)',
    'expiration_date':          r'expires:\s?(.+)',
    'updated_date':             r'changed:\s?(.+)',

    'name_servers':             r'nserver:\s*(.+)',
    'status':                   r'status:\s?(.+)',
}

by = {
    'domain_name':                r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':                r'Registrant\s*Organi(?:s|z)ation:\s?(.+)',
    'registrant_country':       r'Registrant Country:\s?(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':            r'Registry Expiry Date:\s?(.+)',
    'updated_date':                r'Updated Date:\s?(.+)',

    'name_servers':                r'Name Server:\s*(.+)\s*',
    'status':                    r'Status:\s?(.+)',
    'emails':                    r'[\w.-]+@[\w.-]+\.[\w]{2,4}',

    'domain_name':              r'Domain Name:\s*(.+)',
    'registrar':                r'\nRegistrar:\s*(.+)',
    'registrant':               r'\nOrg:\s*(.+)',
    'registrant_country':       r'\nCountry:\s*(.+)',

    'creation_date':            r'\nCreation Date:\s*(.+)',
    'expiration_date':          r'\nExpiration Date:\s*(.+)',
    'updated_date':             r'\nUpdated Date:\s*(.+)',

    'name_servers':             r'\nName Server:\s*(.+)',
}

ca = {
    'domain_name':                r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':                r'Registrant\s*Organi(?:s|z)ation:\s?(.+)',
    'registrant_country':       r'Registrant Country:\s?(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':            r'Registry Expiry Date:\s?(.+)',
    'updated_date':                r'Updated Date:\s?(.+)',

    'name_servers':                r'Name Server:\s*(.+)\s*',
    'status':                    r'Status:\s?(.+)',
    'emails':                    r'[\w.-]+@[\w.-]+\.[\w]{2,4}',
}

cc = {
    'domain_name':                r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':                r'Registrant\s*Organi(?:s|z)ation:\s?(.+)',
    'registrant_country':       r'Registrant Country:\s?(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':            r'Registry Expiry Date:\s?(.+)',
    'updated_date':                r'Updated Date:\s?(.+)',

    'name_servers':                r'Name Server:\s*(.+)\s*',
    'status':                    r'Status:\s?(.+)',
    'emails':                    r'[\w.-]+@[\w.-]+\.[\w]{2,4}',

    'domain_name':              r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s*(.+)',
    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':          r'Registry Expiry Date:\s?(.+)',

    'updated_date':             r'Updated Date:\s?(.+)',
    'status':                   r'Status:\s?(.+)',
}

cl = {
    'domain_name':                r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':                r'Registrant\s*Organi(?:s|z)ation:\s?(.+)',
    'registrant_country':       r'Registrant Country:\s?(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':            r'Registry Expiry Date:\s?(.+)',
    'updated_date':                r'Updated Date:\s?(.+)',

    'name_servers':                r'Name Server:\s*(.+)\s*',
    'status':                    r'Status:\s?(.+)',
    'emails':                    r'[\w.-]+@[\w.-]+\.[\w]{2,4}',

    'registrar':                'nic.cl',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':              r'Expiration Date:\s?(.+)',

    'name_servers':             r'Name Server:\s*(.+)\s*',
}

club = {
    'domain_name':                r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':                r'Registrant\s*Organi(?:s|z)ation:\s?(.+)',
    'registrant_country':       r'Registrant Country:\s?(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':            r'Registry Expiry Date:\s?(.+)',
    'updated_date':                r'Updated Date:\s?(.+)',

    'name_servers':                r'Name Server:\s*(.+)\s*',
    'status':                    r'Status:\s?(.+)',
    'emails':                    r'[\w.-]+@[\w.-]+\.[\w]{2,4}',
}

cn = {
    'domain_name':                r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':                r'Registrant\s*Organi(?:s|z)ation:\s?(.+)',
    'registrant_country':       r'Registrant Country:\s?(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':            r'Registry Expiry Date:\s?(.+)',
    'updated_date':                r'Updated Date:\s?(.+)',

    'name_servers':                r'Name Server:\s*(.+)\s*',
    'status':                    r'Status:\s?(.+)',
    'emails':                    r'[\w.-]+@[\w.-]+\.[\w]{2,4}',

    'registrar':                r'Sponsoring Registrar:\s?(.+)',
    'registrant':               r'Registrant:\s?(.+)',

    'creation_date':            r'Registration Time:\s?(.+)',
    'expiration_date':          r'Expiration Time:\s?(.+)',
}

co = {
    'domain_name':                r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':                r'Registrant\s*Organi(?:s|z)ation:\s?(.+)',
    'registrant_country':       r'Registrant Country:\s?(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':            r'Registry Expiry Date:\s?(.+)',
    'updated_date':                r'Updated Date:\s?(.+)',

    'name_servers':                r'Name Server:\s*(.+)\s*',
    'status':                    r'Status:\s?(.+)',
    'emails':                    r'[\w.-]+@[\w.-]+\.[\w]{2,4}',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':               r'Registrant Organization:\s?(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':          r'Registry Expiry Date:\s?(.+)',
    'updated_date':             r'Updated Date:\s?(.+)',

    'status':                   None,
    'status':                   r'Status:\s?(.+)',
}

com_au = {
    'domain_name':                r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':                r'Registrant\s*Organi(?:s|z)ation:\s?(.+)',
    'registrant_country':       r'Registrant Country:\s?(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':            r'Registry Expiry Date:\s?(.+)',
    'updated_date':                r'Updated Date:\s?(.+)',

    'name_servers':                r'Name Server:\s*(.+)\s*',
    'status':                    r'Status:\s?(.+)',
    'emails':                    r'[\w.-]+@[\w.-]+\.[\w]{2,4}',

    'registrar':                r'Registrar Name:\s?(.+)',

    'updated_date':             r'Last Modified:\s?(.+)'
}

com_tr = {
    'domain_name':                r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':                r'Registrant\s*Organi(?:s|z)ation:\s?(.+)',
    'registrant_country':       r'Registrant Country:\s?(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':            r'Registry Expiry Date:\s?(.+)',
    'updated_date':                r'Updated Date:\s?(.+)',

    'name_servers':                r'Name Server:\s*(.+)\s*',
    'status':                    r'Status:\s?(.+)',
    'emails':                    r'[\w.-]+@[\w.-]+\.[\w]{2,4}',

    'domain_name':          r'\*\* Domain Name:\s?(.+)',

    'registrar':            r'Organization Name\s+:\s?(.+)',
    'registrant':           r'\*\* Registrant:\s+?(.+)',
    'registrant_country':   None,

    'creation_date':        r'Created on..............:\s?(.+).',
    'expiration_date':      r'Expires on..............:\s?(.+).',
    'updated_date':         None,

    'name_servers':         r'\*\* Domain Servers:\n(?:(\S+)\n)(?:(\S+)\n)?(?:(\S+)\n)?(?:(\S+)\n)?(?:(\S+)\n)?(?:(\S+)\n)\n?',
    'status':               None,
}

co_il = {
    'domain_name':                r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':                r'Registrant\s*Organi(?:s|z)ation:\s?(.+)',
    'registrant_country':       r'Registrant Country:\s?(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':            r'Registry Expiry Date:\s?(.+)',
    'updated_date':                r'Updated Date:\s?(.+)',

    'name_servers':                r'Name Server:\s*(.+)\s*',
    'status':                    r'Status:\s?(.+)',
    'emails':                    r'[\w.-]+@[\w.-]+\.[\w]{2,4}',

    'domain_name':              r'domain:\s*(.+)',
    'registrar':                r'registrar name:\s*(.+)',
    'registrant':               None,
    'registrant_country':       None,

    'creation_date':            None,
    'expiration_date':          r'validity:\s*(.+)',
    'updated_date':             None,

    'name_servers':             r'nserver:\s*(.+)',
    'status':                   r'status:\s*(.+)',
}


courses = {
    'domain_name':                r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':                r'Registrant\s*Organi(?:s|z)ation:\s?(.+)',
    'registrant_country':       r'Registrant Country:\s?(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':            r'Registry Expiry Date:\s?(.+)',
    'updated_date':                r'Updated Date:\s?(.+)',

    'name_servers':                r'Name Server:\s*(.+)\s*',
    'status':                    r'Status:\s?(.+)',
    'emails':                    r'[\w.-]+@[\w.-]+\.[\w]{2,4}',
}

cr = {
    'domain_name':                r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':                r'Registrant\s*Organi(?:s|z)ation:\s?(.+)',
    'registrant_country':       r'Registrant Country:\s?(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':            r'Registry Expiry Date:\s?(.+)',
    'updated_date':                r'Updated Date:\s?(.+)',

    'name_servers':                r'Name Server:\s*(.+)\s*',
    'status':                    r'Status:\s?(.+)',
    'emails':                    r'[\w.-]+@[\w.-]+\.[\w]{2,4}',

    'domain_name':              r'domain:\s?(.+)',
    'registrar':                r'registrar:\s?(.+)',
    'registrant':               r'registrant:\s?(.+)',
    'registrant_country':       None,

    'creation_date':            r'registered:\s?(.+)',
    'expiration_date':          r'expire:\s?(.+)',
    'updated_date':             r'changed:\s?(.+)',

    'name_servers':             r'nserver:\s*(.+) ',
    'status':                   r'status:\s*(.+)',
}

cz = {
    'domain_name':                r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':                r'Registrant\s*Organi(?:s|z)ation:\s?(.+)',
    'registrant_country':       r'Registrant Country:\s?(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':            r'Registry Expiry Date:\s?(.+)',
    'updated_date':                r'Updated Date:\s?(.+)',

    'name_servers':                r'Name Server:\s*(.+)\s*',
    'status':                    r'Status:\s?(.+)',
    'emails':                    r'[\w.-]+@[\w.-]+\.[\w]{2,4}',

    'domain_name':              r'domain:\s?(.+)',
    'registrar':                r'registrar:\s?(.+)',
    'registrant':               r'registrant:\s?(.+)',
    'registrant_country':       None,

    'creation_date':            r'registered:\s?(.+)',
    'expiration_date':          r'expire:\s?(.+)',
    'updated_date':             r'changed:\s?(.+)',

    'name_servers':             r'nserver:\s*(.+) ',
    'status':                   r'status:\s*(.+)',
}

de = {
    'domain_name':                r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':                r'Registrant\s*Organi(?:s|z)ation:\s?(.+)',
    'registrant_country':       r'Registrant Country:\s?(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':            r'Registry Expiry Date:\s?(.+)',
    'updated_date':                r'Updated Date:\s?(.+)',

    'name_servers':                r'Name Server:\s*(.+)\s*',
    'status':                    r'Status:\s?(.+)',
    'emails':                    r'[\w.-]+@[\w.-]+\.[\w]{2,4}',

    'domain_name':              r'\ndomain:\s*(.+)',

    'updated_date':             r'\nChanged:\s?(.+)',

    'name_servers':             r'Nserver:\s*(.+)',
}

download = {
    'domain_name':                r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':                r'Registrant\s*Organi(?:s|z)ation:\s?(.+)',
    'registrant_country':       r'Registrant Country:\s?(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':            r'Registry Expiry Date:\s?(.+)',
    'updated_date':                r'Updated Date:\s?(.+)',

    'name_servers':                r'Name Server:\s*(.+)\s*',
    'status':                    r'Status:\s?(.+)',
    'emails':                    r'[\w.-]+@[\w.-]+\.[\w]{2,4}',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':               r'Registrant Organization:\s?(.+)',

    'updated_date':             r'Updated Date:\s?(.+)',
    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':          r'Registry Expiry Date:\s?(.+)',

    'name_servers':             r'Name Server:\s*(.+)',
    'status':                   r'Domain Status:\s*(.+)',

    'name_servers':             r'Name Server:\s*(.+)\r',
    'status':                   r'Domain Status:\s*([a-zA-z]+)',
}


edu = {
    'domain_name':                r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':                r'Registrant\s*Organi(?:s|z)ation:\s?(.+)',
    'registrant_country':       r'Registrant Country:\s?(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':            r'Registry Expiry Date:\s?(.+)',
    'updated_date':                r'Updated Date:\s?(.+)',

    'name_servers':                r'Name Server:\s*(.+)\s*',
    'status':                    r'Status:\s?(.+)',
    'emails':                    r'[\w.-]+@[\w.-]+\.[\w]{2,4}',

    'registrant':               r'Registrant:\s*(.+)',

    'creation_date':            r'Domain record activated:\s?(.+)',
    'updated_date':             r'Domain record last updated:\s?(.+)',
    'expiration_date':          r'Domain expires:\s?(.+)',

    'name_servers':             r'Name Servers:\s?\t(.+)\n\t(.+)\n',
}


education = {
    # GANDI SAS
    'domain_name':                r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':                r'Registrant\s*Organi(?:s|z)ation:\s?(.+)',
    'registrant_country':       r'Registrant Country:\s?(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':            r'Registry Expiry Date:\s?(.+)',
    'updated_date':                r'Updated Date:\s?(.+)',

    'name_servers':                r'Name Server:\s*(.+)\s*',
    'status':                    r'Status:\s?(.+)',
    'emails':                    r'[\w.-]+@[\w.-]+\.[\w]{2,4}',

    'registrant':               r'Registrant Organization:\s?(.+)',

    'expiration_date':          r'Registrar Registration Expiration Date:\s?(.+)',

    'status':                   r'Domain Status:\s?(.+)',
}


eu = {
    'domain_name':                r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':                r'Registrant\s*Organi(?:s|z)ation:\s?(.+)',
    'registrant_country':       r'Registrant Country:\s?(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':            r'Registry Expiry Date:\s?(.+)',
    'updated_date':                r'Updated Date:\s?(.+)',

    'name_servers':                r'Name Server:\s*(.+)\s*',
    'status':                    r'Status:\s?(.+)',
    'emails':                    r'[\w.-]+@[\w.-]+\.[\w]{2,4}',

    'registrar':                r'Name:\s?(.+)',

    'domain_name':              r'\nDomain:\s*(.+)',

    'name_servers':             r'Name servers:\n(?:\s+(\S+)\n)(?:\s+(\S+)\n)?(?:\s+(\S+)\n)?(?:\s+(\S+)\n)?(?:\s+(\S+)\n)?(?:\s+(\S+)\n)\n?',
}


fi = {
    'extend': None,

    'domain_name':              r'domain\.+:\s?(.+)',

    'registrar':                r'registrar\.+:\s?(.+)',

    'registrant_country':       None,

    'creation_date':            r'created\.+:\s?(.+)',
    'expiration_date':          r'expires\.+:\s?(.+)',
    'updated_date':             r'modified\.+:\s?(.+)',

    'name_servers':             r'nserver\.+:\s*(.+)',
    'status':                   r'status\.+:\s?(.+)',
}

fm = {
    'domain_name':                r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':                r'Registrant\s*Organi(?:s|z)ation:\s?(.+)',
    'registrant_country':       r'Registrant Country:\s?(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':            r'Registry Expiry Date:\s?(.+)',
    'updated_date':                r'Updated Date:\s?(.+)',

    'name_servers':                r'Name Server:\s*(.+)\s*',
    'status':                    r'Status:\s?(.+)',
    'emails':                    r'[\w.-]+@[\w.-]+\.[\w]{2,4}',
}


fr = {
    'domain_name':                r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':                r'Registrant\s*Organi(?:s|z)ation:\s?(.+)',
    'registrant_country':       r'Registrant Country:\s?(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':            r'Registry Expiry Date:\s?(.+)',
    'updated_date':                r'Updated Date:\s?(.+)',

    'name_servers':                r'Name Server:\s*(.+)\s*',
    'status':                    r'Status:\s?(.+)',
    'emails':                    r'[\w.-]+@[\w.-]+\.[\w]{2,4}',

    'domain_name':              r'domain:\s?(.+)',
    'registrar':                r'registrar:\s*(.+)',
    'registrant':               r'contact:\s?(.+)',

    'creation_date':            r'created:\s?(.+)',
    'expiration_date':          r'Expiry Date:\s?(.+)',
    'updated_date':             r'last-update:\s?(.+)',

    'name_servers':             r'nserver:\s*(.+)',
    'status':                   r'status:\s?(.+)',
}

frl = {
    'domain_name':                r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':                r'Registrant\s*Organi(?:s|z)ation:\s?(.+)',
    'registrant_country':       r'Registrant Country:\s?(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':            r'Registry Expiry Date:\s?(.+)',
    'updated_date':                r'Updated Date:\s?(.+)',

    'name_servers':                r'Name Server:\s*(.+)\s*',
    'status':                    r'Status:\s?(.+)',
    'emails':                    r'[\w.-]+@[\w.-]+\.[\w]{2,4}',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':               r'Registrant Organization:\s?(.+)',

    'updated_date':             r'Updated Date:\s?(.+)',
    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':          r'Registry Expiry Date:\s?(.+)',

    'name_servers':             r'Name Server:\s*(.+)',
    'status':                   r'Domain Status:\s*(.+)',
}

game = {
    'domain_name':                r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':                r'Registrant\s*Organi(?:s|z)ation:\s?(.+)',
    'registrant_country':       r'Registrant Country:\s?(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':            r'Registry Expiry Date:\s?(.+)',
    'updated_date':                r'Updated Date:\s?(.+)',

    'name_servers':                r'Name Server:\s*(.+)\s*',
    'status':                    r'Status:\s?(.+)',
    'emails':                    r'[\w.-]+@[\w.-]+\.[\w]{2,4}',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':               r'Registrant Organization:\s?(.+)',

    'updated_date':             r'Updated Date:\s?(.+)',
    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':          r'Registry Expiry Date:\s?(.+)',

    'name_servers':             r'Name Server:\s*(.+)',
    'status':                   r'Domain Status:\s*(.+)',
}

global_ = {
    'domain_name':                r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':                r'Registrant\s*Organi(?:s|z)ation:\s?(.+)',
    'registrant_country':       r'Registrant Country:\s?(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':            r'Registry Expiry Date:\s?(.+)',
    'updated_date':                r'Updated Date:\s?(.+)',

    'name_servers':                r'Name Server:\s*(.+)\s*',
    'status':                    r'Status:\s?(.+)',
    'emails':                    r'[\w.-]+@[\w.-]+\.[\w]{2,4}',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':               r'Registrant Organization:\s?(.+)',

    'updated_date':             r'Updated Date:\s?(.+)',
    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':          r'Registry Expiry Date:\s?(.+)',

    'name_servers':             r'Name Server:\s*(.+)',
    'status':                   r'Domain Status:\s*(.+)',

    'name_servers': r'Name Server: (.+)',
}

hk = {
    'domain_name':                r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':                r'Registrant\s*Organi(?:s|z)ation:\s?(.+)',
    'registrant_country':       r'Registrant Country:\s?(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':            r'Registry Expiry Date:\s?(.+)',
    'updated_date':                r'Updated Date:\s?(.+)',

    'name_servers':                r'Name Server:\s*(.+)\s*',
    'status':                    r'Status:\s?(.+)',
    'emails':                    r'[\w.-]+@[\w.-]+\.[\w]{2,4}',

    'domain_name':                r'Domain Name:\s+(.+)',

    'registrar':                r'Registrar Name:\s?(.+)',
    'registrant':                r'Company English Name.*:\s?(.+)',
    'registrant_country':       None,

    'creation_date':            r'Domain Name Commencement Date:\s?(.+)',
    'expiration_date':            r'Expiry Date:\s?(.+)',
    'updated_date':                None,

    'name_servers':                r'Name Servers Information:\n\n(?:(\S+)\n)(?:(\S+)\n)(?:(\S+)\n)?(?:(\S+)\n)?\n?',
    'status':                    None,
}

id_ = {
    'domain_name':                r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':                r'Registrant\s*Organi(?:s|z)ation:\s?(.+)',
    'registrant_country':       r'Registrant Country:\s?(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':            r'Registry Expiry Date:\s?(.+)',
    'updated_date':                r'Updated Date:\s?(.+)',

    'name_servers':                r'Name Server:\s*(.+)\s*',
    'status':                    r'Status:\s?(.+)',
    'emails':                    r'[\w.-]+@[\w.-]+\.[\w]{2,4}',

    'registrar':                r'Sponsoring Registrar Organization:\s?(.+)',

    'creation_date':            r'Created On:\s?(.+)',
    'expiration_date':          r'Expiration Date:\s?(.+)',
    'updated_date':             r'Last Updated On:\s?(.+)$',
}

ie = {
    'domain_name':                r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':                r'Registrant\s*Organi(?:s|z)ation:\s?(.+)',
    'registrant_country':       r'Registrant Country:\s?(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':            r'Registry Expiry Date:\s?(.+)',
    'updated_date':                r'Updated Date:\s?(.+)',

    'name_servers':                r'Name Server:\s*(.+)\s*',
    'status':                    r'Status:\s?(.+)',
    'emails':                    r'[\w.-]+@[\w.-]+\.[\w]{2,4}',
}

im = {
    'domain_name':              r'Domain Name:\s+(.+)',
    'status':                   None,

    'registrar':                None,
    'registrant_country':       None,

    'creation_date':            '',
    'expiration_date':          r'Expiry Date:\s?(.+)',
    'updated_date':             '',

    'name_servers':             r'Name Server:(.+)',
}

in_ = {
    'domain_name':                r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':                r'Registrant\s*Organi(?:s|z)ation:\s?(.+)',
    'registrant_country':       r'Registrant Country:\s?(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':            r'Registry Expiry Date:\s?(.+)',
    'updated_date':                r'Updated Date:\s?(.+)',

    'name_servers':                r'Name Server:\s*(.+)\s*',
    'status':                    r'Status:\s?(.+)',
    'emails':                    r'[\w.-]+@[\w.-]+\.[\w]{2,4}',
}

info = {
    'domain_name':                r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':                r'Registrant\s*Organi(?:s|z)ation:\s?(.+)',
    'registrant_country':       r'Registrant Country:\s?(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':            r'Registry Expiry Date:\s?(.+)',
    'updated_date':                r'Updated Date:\s?(.+)',

    'name_servers':                r'Name Server:\s*(.+)\s*',
    'status':                    r'Status:\s?(.+)',
    'emails':                    r'[\w.-]+@[\w.-]+\.[\w]{2,4}',
}

ink = {
    'domain_name':                r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':                r'Registrant\s*Organi(?:s|z)ation:\s?(.+)',
    'registrant_country':       r'Registrant Country:\s?(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':            r'Registry Expiry Date:\s?(.+)',
    'updated_date':                r'Updated Date:\s?(.+)',

    'name_servers':                r'Name Server:\s*(.+)\s*',
    'status':                    r'Status:\s?(.+)',
    'emails':                    r'[\w.-]+@[\w.-]+\.[\w]{2,4}',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':               r'Registrant Organization:\s?(.+)',

    'updated_date':             r'Updated Date:\s?(.+)',
    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':          r'Registry Expiry Date:\s?(.+)',

    'name_servers':             r'Name Server:\s*(.+)',
    'status':                   r'Domain Status:\s*(.+)',
}

io = {
    'domain_name':                r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':                r'Registrant\s*Organi(?:s|z)ation:\s?(.+)',
    'registrant_country':       r'Registrant Country:\s?(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':            r'Registry Expiry Date:\s?(.+)',
    'updated_date':                r'Updated Date:\s?(.+)',

    'name_servers':                r'Name Server:\s*(.+)\s*',
    'status':                    r'Status:\s?(.+)',
    'emails':                    r'[\w.-]+@[\w.-]+\.[\w]{2,4}',

    'expiration_date':          r'\nRegistry Expiry Date:\s?(.+)',
}


ir = {
    'extend': None,

    'domain_name':              r'domain:\s?(.+)',
    'registrar':                'nic.ir',

    'registrant_country':       None,

    'creation_date':            None,
    'status':                   None,

    'expiration_date':          r'expire-date:\s?(.+)',
    'updated_date':             r'last-updated:\s?(.+)',

    'name_servers':             r'nserver:\s*(.+)\s*',
}


is_ = {
    'domain_name':              r'domain:\s?(.+)',

    'registrar':                None,
    'registrant':               r'registrant:\s?(.+)',
    'registrant_country':       None,

    'creation_date':            r'created:\s?(.+)',
    'expiration_date':          r'expires:\s?(.+)',
    'updated_date':             None,

    'name_servers':             r'nserver:\s?(.+)',
    'status':                   None,
    'emails':                   r'[\w.-]+@[\w.-]+\.[\w]{2,4}',
}


it = {
    'domain_name':                r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':                r'Registrant\s*Organi(?:s|z)ation:\s?(.+)',
    'registrant_country':       r'Registrant Country:\s?(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':            r'Registry Expiry Date:\s?(.+)',
    'updated_date':                r'Updated Date:\s?(.+)',

    'name_servers':                r'Name Server:\s*(.+)\s*',
    'status':                    r'Status:\s?(.+)',
    'emails':                    r'[\w.-]+@[\w.-]+\.[\w]{2,4}',

    'domain_name':              r'Domain:\s?(.+)',
    'registrar':                r'Registrar\s*Organization:\s*(.+)',
    'registrant':               r'Registrant\s*Organization:\s*(.+)',

    'creation_date':            r'Created:\s?(.+)',
    'expiration_date':          r'Expire Date:\s?(.+)',
    'updated_date':             r'Last Update:\s?(.+)',

    'name_servers':             r'Nameservers\s?(.+)\s?(.+)\s?(.+)\s?(.+)',
    'status':                   r'Status:\s?(.+)',
}


kr = {
    'domain_name':                r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':                r'Registrant\s*Organi(?:s|z)ation:\s?(.+)',
    'registrant_country':       r'Registrant Country:\s?(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':            r'Registry Expiry Date:\s?(.+)',
    'updated_date':                r'Updated Date:\s?(.+)',

    'name_servers':                r'Name Server:\s*(.+)\s*',
    'status':                    r'Status:\s?(.+)',
    'emails':                    r'[\w.-]+@[\w.-]+\.[\w]{2,4}',

    'domain_name':              r'Domain Name\s*:\s?(.+)',

    'registrar':                r'Authorized Agency\s*:\s*(.+)',
    'registrant':               r'Registrant\s*:\s*(.+)',

    'creation_date':            r'Registered Date\s*:\s?(.+)',
    'expiration_date':          r'Expiration Date\s*:\s?(.+)',
    'updated_date':             r'Last Updated Date\s*:\s?(.+)',

    'status':                   r'status\s*:\s?(.+)',
}


kz = {
    'extend': None,

    'domain_name':              r'Domain name\.+:\s(.+)',

    'registrar':                r'Current Registar:\s(.+)',
    'registrant_country':       r'Country\.+:\s?(.+)',

    'expiration_date':          None,
    'creation_date':            r'Domain created:\s(.+)',
    'updated_date':             r'Last modified :\s(.+)',

    'name_servers':             r'server.*:\s(.+)',
    'status':                   r'Domain status :\s?(.+)',
}

link = {
    'domain_name':                r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':                r'Registrant\s*Organi(?:s|z)ation:\s?(.+)',
    'registrant_country':       r'Registrant Country:\s?(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':            r'Registry Expiry Date:\s?(.+)',
    'updated_date':                r'Updated Date:\s?(.+)',

    'name_servers':                r'Name Server:\s*(.+)\s*',
    'status':                    r'Status:\s?(.+)',
    'emails':                    r'[\w.-]+@[\w.-]+\.[\w]{2,4}',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':               r'Registrant Organization:\s?(.+)',

    'updated_date':             r'Updated Date:\s?(.+)',
    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':          r'Registry Expiry Date:\s?(.+)',

    'name_servers':             r'Name Server:\s*(.+)',
    'status':                   r'Domain Status:\s*(.+)',
}

lt = {
    'domain_name':                r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':                r'Registrant\s*Organi(?:s|z)ation:\s?(.+)',
    'registrant_country':       r'Registrant Country:\s?(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':            r'Registry Expiry Date:\s?(.+)',
    'updated_date':                r'Updated Date:\s?(.+)',

    'name_servers':                r'Name Server:\s*(.+)\s*',
    'status':                    r'Status:\s?(.+)',
    'emails':                    r'[\w.-]+@[\w.-]+\.[\w]{2,4}',

    'domain_name':              r'Domain:\s?(.+)',

    'creation_date':            r'Registered:\s?(.+)',
    'expiration_date':          r'Expires:\s?(.+)',

    'name_servers':             r'Nameserver:\s*(.+)\s*',
    'status':                   r'\nStatus:\s?(.+)',
}

lv = {
    'domain_name':                r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':                r'Registrant\s*Organi(?:s|z)ation:\s?(.+)',
    'registrant_country':       r'Registrant Country:\s?(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':            r'Registry Expiry Date:\s?(.+)',
    'updated_date':                r'Updated Date:\s?(.+)',

    'name_servers':                r'Name Server:\s*(.+)\s*',
    'status':                    r'Status:\s?(.+)',
    'emails':                    r'[\w.-]+@[\w.-]+\.[\w]{2,4}',

    'domain_name':              r'\ndomain:\s*(.+)',

    'creation_date':            r'\ncreated:\s*(.+)',
    'expiration_date':          r'\npaid-till:\s*(.+)',

    'name_servers':             r'\nnserver:\s*(.+)',
    'status':                   r'\nstate:\s*(.+)',

    'creation_date':            r'Registered:\s*(.+)\n',
    'updated_date':             r'Changed:\s*(.+)\n',

    'status':                   r'Status:\s?(.+)',
}

me = {
    'domain_name':                r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':                r'Registrant\s*Organi(?:s|z)ation:\s?(.+)',
    'registrant_country':       r'Registrant Country:\s?(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':            r'Registry Expiry Date:\s?(.+)',
    'updated_date':                r'Updated Date:\s?(.+)',

    'name_servers':                r'Name Server:\s*(.+)\s*',
    'status':                    r'Status:\s?(.+)',
    'emails':                    r'[\w.-]+@[\w.-]+\.[\w]{2,4}',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':               r'Registrant Organization:\s?(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':          r'Registry Expiry Date:\s?(.+)',
    'updated_date':             r'Updated Date:\s?(.+)',

    'status':                   None,

    'creation_date':            r'Domain Create Date:\s?(.+)',
    'expiration_date':          r'Domain Expiration Date:\s?(.+)',
    'updated_date':             r'Domain Last Updated Date:\s?(.+)',

    'name_servers':             r'Nameservers:\s?(.+)',
    'status':                   r'Domain Status:\s?(.+)',
}

ml = {
    'domain_name':                r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':                r'Registrant\s*Organi(?:s|z)ation:\s?(.+)',
    'registrant_country':       r'Registrant Country:\s?(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':            r'Registry Expiry Date:\s?(.+)',
    'updated_date':                r'Updated Date:\s?(.+)',

    'name_servers':                r'Name Server:\s*(.+)\s*',
    'status':                    r'Status:\s?(.+)',
    'emails':                    r'[\w.-]+@[\w.-]+\.[\w]{2,4}',

    'domain_name':              r'Domain name:\s*([^(i|\n)]+)',

    'registrar':                r'(?<=Owner contact:\s)[\s\S]*?Organization:(.*)',
    'registrant_country':       r'(?<=Owner contact:\s)[\s\S]*?Country:(.*)',
    'registrant':               r'(?<=Owner contact:\s)[\s\S]*?Name:(.*)',

    'creation_date':            r'Domain registered: *(.+)',
    'expiration_date':          r'Record will expire on: *(.+)',

    'name_servers':             r'Domain Nameservers:\s*(.+)\n\s*(.+)\n',

    'emails':                   r'[\w.-]+@[\w.-]+\.[\w]{2,4}',
}

mobi = {
    'domain_name':                r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':                r'Registrant\s*Organi(?:s|z)ation:\s?(.+)',
    'registrant_country':       r'Registrant Country:\s?(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':            r'Registry Expiry Date:\s?(.+)',
    'updated_date':                r'Updated Date:\s?(.+)',

    'name_servers':                r'Name Server:\s*(.+)\s*',
    'status':                    r'Status:\s?(.+)',
    'emails':                    r'[\w.-]+@[\w.-]+\.[\w]{2,4}',

    'expiration_date':          r'\nRegistry Expiry Date:\s?(.+)',
    'updated_date':             r'\nUpdated Date:\s?(.+)',
}


mx = {
    'domain_name':              r'Domain Name:\s?(.+)',

    'registrant':               r'Registrant:\n\s*(.+)',
    'registrar':                r'Registrar:\s?(.+)',

    'creation_date':            r'Created On:\s?(.+)',
    'expiration_date':          r'Expiration Date:\s?(.+)',
    'updated_date':             r'Last Updated On:\s?(.+)',

    'name_servers':             r'\sDNS:\s*(.+)',
}


name = {
    'domain_name':                r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':                r'Registrant\s*Organi(?:s|z)ation:\s?(.+)',
    'registrant_country':       r'Registrant Country:\s?(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':            r'Registry Expiry Date:\s?(.+)',
    'updated_date':                r'Updated Date:\s?(.+)',

    'name_servers':                r'Name Server:\s*(.+)\s*',
    'status':                    r'Status:\s?(.+)',
    'emails':                    r'[\w.-]+@[\w.-]+\.[\w]{2,4}',

    'status':                   r'Domain Status:\s?(.+)',
}

net = {
    'domain_name':                r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':                r'Registrant\s*Organi(?:s|z)ation:\s?(.+)',
    'registrant_country':       r'Registrant Country:\s?(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':            r'Registry Expiry Date:\s?(.+)',
    'updated_date':                r'Updated Date:\s?(.+)',

    'name_servers':                r'Name Server:\s*(.+)\s*',
    'status':                    r'Status:\s?(.+)',
    'emails':                    r'[\w.-]+@[\w.-]+\.[\w]{2,4}',
}


ninja = {
    'domain_name':                r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':                r'Registrant\s*Organi(?:s|z)ation:\s?(.+)',
    'registrant_country':       r'Registrant Country:\s?(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':            r'Registry Expiry Date:\s?(.+)',
    'updated_date':                r'Updated Date:\s?(.+)',

    'name_servers':                r'Name Server:\s*(.+)\s*',
    'status':                    r'Status:\s?(.+)',
    'emails':                    r'[\w.-]+@[\w.-]+\.[\w]{2,4}',

    'registrant':               r'Registrant Organization:\s?(.+)',

    'expiration_date':          r'Registrar Registration Expiration Date:\s?(.+)',

    'status':                   r'Domain Status:\s?(.+)',
}

nl = {
    'domain_name':                r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':                r'Registrant\s*Organi(?:s|z)ation:\s?(.+)',
    'registrant_country':       r'Registrant Country:\s?(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':            r'Registry Expiry Date:\s?(.+)',
    'updated_date':                r'Updated Date:\s?(.+)',

    'name_servers':                r'Name Server:\s*(.+)\s*',
    'status':                    r'Status:\s?(.+)',
    'emails':                    r'[\w.-]+@[\w.-]+\.[\w]{2,4}',

    'expiration_date':          None,
    'registrant_country':       None,

    'domain_name':              r'Domain name:\s?(.+)',
    'name_servers':             (
        r'''(?x:
            Domain\ nameservers:[ \t]*\n
            (?:[ \t]+) (\S+) (?:[ \t]+\S+)? \n       # ns1.tld.nl [A?]
            (?:(?:[ \t]+) (\S+) (?:[ \t]+\S+)? \n)?  # opt-ns2.tld.nl [A?]
            (?:(?:[ \t]+) (\S+) (?:[ \t]+\S+)? \n)?  # opt-ns2.tld.nl [AAAA?]
            (?:(?:[ \t]+) (\S+) (?:[ \t]+\S+)? \n)?  # opt-ns3.tld.nl [A?]
            (?:(?:[ \t]+) (\S+) (?:[ \t]+\S+)? \n)?  # opt-ns3.tld.nl [AAAA?]
            (?:(?:[ \t]+) (\S+) (?:[ \t]+\S+)? \n)?  # opt-ns4.tld.nl [A?]
            (?:(?:[ \t]+) (\S+) (?:[ \t]+\S+)? \n)?  # opt-ns4.tld.nl [AAAA?]
            (?:(?:[ \t]+) (\S+) (?:[ \t]+\S+)? \n)?  # opt-ns5.tld.nl [A?]
            (?:(?:[ \t]+) (\S+) (?:[ \t]+\S+)? \n)?  # opt-ns5.tld.nl [AAAA?]
            # Don't check for final LF; there might be even more records..
        )'''),
    'reseller':                 r'Reseller:\s?(.+)',
    'abuse_contact':            r'Abuse Contact:\s?(.+)',
}


nu = {
    'domain_name':              r'domain:\s?(.+)',

    'registrar':                r'registrar:\s?(.+)',

    'registrant_country':       None,

    'creation_date':            r'created:\s?(.+)',
    'expiration_date':          r'expires:\s?(.+)',
    'updated_date':             r'modified:\s?(.+)',

    'name_servers':             r'nserver:\s*(.+)',
    'status':                   r'status:\s?(.+)',
}


nyc = {
    'domain_name':                r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':                r'Registrant\s*Organi(?:s|z)ation:\s?(.+)',
    'registrant_country':       r'Registrant Country:\s?(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':            r'Registry Expiry Date:\s?(.+)',
    'updated_date':                r'Updated Date:\s?(.+)',

    'name_servers':                r'Name Server:\s*(.+)\s*',
    'status':                    r'Status:\s?(.+)',
    'emails':                    r'[\w.-]+@[\w.-]+\.[\w]{2,4}',

    'domain_name':              r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s*(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':          r'Registry Expiry Date:\s?(.+)',
    'updated_date':             r'Updated Date:\s?(.+)',

    'status':                   r'Status:\s?(.+)',
}


nz = {
    'extend': None,

    'domain_name':              r'domain_name:\s?(.+)',
    'registrar':                r'registrar_name:\s?(.+)',
    'registrant':               r'registrant_contact_name:\s?(.+)',
    'registrant_country':       None,

    'creation_date':            r'domain_dateregistered:\s?(.+)',
    'expiration_date':          r'domain_datebilleduntil:\s?(.+)',
    'updated_date':             r'domain_datelastmodified:\s?(.+)',

    'name_servers':             r'ns_name_[0-9]{2}:\s?(.+)',
    'status':                   r'query_status:\s?(.+)',
    'emails':                   r'[\w.-]+@[\w.-]+\.[\w]{2,4}',
}


online = {
    'domain_name':                r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':                r'Registrant\s*Organi(?:s|z)ation:\s?(.+)',
    'registrant_country':       r'Registrant Country:\s?(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':            r'Registry Expiry Date:\s?(.+)',
    'updated_date':                r'Updated Date:\s?(.+)',

    'name_servers':                r'Name Server:\s*(.+)\s*',
    'status':                    r'Status:\s?(.+)',
    'emails':                    r'[\w.-]+@[\w.-]+\.[\w]{2,4}',

    'domain_name':              r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s*(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':          r'Registry Expiry Date:\s?(.+)',
    'updated_date':             r'Updated Date:\s?(.+)',

    'status':                   r'Status:\s?(.+)',
}

org = {
    'domain_name':                r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':                r'Registrant\s*Organi(?:s|z)ation:\s?(.+)',
    'registrant_country':       r'Registrant Country:\s?(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':            r'Registry Expiry Date:\s?(.+)',
    'updated_date':                r'Updated Date:\s?(.+)',

    'name_servers':                r'Name Server:\s*(.+)\s*',
    'status':                    r'Status:\s?(.+)',
    'emails':                    r'[\w.-]+@[\w.-]+\.[\w]{2,4}',

    'expiration_date':          r'\nRegistry Expiry Date:\s?(.+)',
    'updated_date':             r'\nLast Updated On:\s?(.+)',

    'name_servers':             r'Name Server:\s?(.+)\s*',
}

pe = {
    'domain_name':                r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':                r'Registrant\s*Organi(?:s|z)ation:\s?(.+)',
    'registrant_country':       r'Registrant Country:\s?(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':            r'Registry Expiry Date:\s?(.+)',
    'updated_date':                r'Updated Date:\s?(.+)',

    'name_servers':                r'Name Server:\s*(.+)\s*',
    'status':                    r'Status:\s?(.+)',
    'emails':                    r'[\w.-]+@[\w.-]+\.[\w]{2,4}',

    'registrant':                r'Registrant Name:\s?(.+)',

    'admin':                    r'Admin Name:\s?(.+)',
}

pharmacy = {
    'domain_name':                r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':                r'Registrant\s*Organi(?:s|z)ation:\s?(.+)',
    'registrant_country':       r'Registrant Country:\s?(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':            r'Registry Expiry Date:\s?(.+)',
    'updated_date':                r'Updated Date:\s?(.+)',

    'name_servers':                r'Name Server:\s*(.+)\s*',
    'status':                    r'Status:\s?(.+)',
    'emails':                    r'[\w.-]+@[\w.-]+\.[\w]{2,4}',

    'domain_name':              r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s*(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':          r'Registry Expiry Date:\s?(.+)',
    'updated_date':             r'Updated Date:\s?(.+)',

    'status':                   r'status:\s?(.+)',
}

pl = {
    'domain_name':                r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':                r'Registrant\s*Organi(?:s|z)ation:\s?(.+)',
    'registrant_country':       r'Registrant Country:\s?(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':            r'Registry Expiry Date:\s?(.+)',
    'updated_date':                r'Updated Date:\s?(.+)',

    'name_servers':                r'Name Server:\s*(.+)\s*',
    'status':                    r'Status:\s?(.+)',
    'emails':                    r'[\w.-]+@[\w.-]+\.[\w]{2,4}',

    'registrant':               r'Registrant:\n\s*(.+)',

    'creation_date':            r'Registered on:\s*(.+)',
    'expiration_date':          r'Expiry date:\s*(.+)',
    'updated_date':             r'Last updated:\s*(.+)',

    'name_servers':             r'Name Servers:\s*(.+)\s*',
    'status':                   r'Registration status:\n\s*(.+)',

    'registrar':                r'\nREGISTRAR:\s*(.+)\n',

    'creation_date':            r'\ncreated:\s*(.+)\n',
    'updated_date':             r'\nlast modified:\s*(.+)\n',
    'expiration_date':          r'\noption expiration date:\s*(.+)\n',

    'name_servers':             r'\nnameservers:\s*(.+)\n\s*(.+)\n',
    'status':                   r'\nStatus:\n\s*(.+)',
}


press = {
    'domain_name':                r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':                r'Registrant\s*Organi(?:s|z)ation:\s?(.+)',
    'registrant_country':       r'Registrant Country:\s?(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':            r'Registry Expiry Date:\s?(.+)',
    'updated_date':                r'Updated Date:\s?(.+)',

    'name_servers':                r'Name Server:\s*(.+)\s*',
    'status':                    r'Status:\s?(.+)',
    'emails':                    r'[\w.-]+@[\w.-]+\.[\w]{2,4}',

    'domain_name':              r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s*(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':          r'Registry Expiry Date:\s?(.+)',
    'updated_date':             r'Updated Date:\s?(.+)',

    'status':                   r'Status:\s?(.+)',
}

pro = {
    'domain_name':                r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':                r'Registrant\s*Organi(?:s|z)ation:\s?(.+)',
    'registrant_country':       r'Registrant Country:\s?(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':            r'Registry Expiry Date:\s?(.+)',
    'updated_date':                r'Updated Date:\s?(.+)',

    'name_servers':                r'Name Server:\s*(.+)\s*',
    'status':                    r'Status:\s?(.+)',
    'emails':                    r'[\w.-]+@[\w.-]+\.[\w]{2,4}',
}

pt = {
    'domain_name':                r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':                r'Registrant\s*Organi(?:s|z)ation:\s?(.+)',
    'registrant_country':       r'Registrant Country:\s?(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':            r'Registry Expiry Date:\s?(.+)',
    'updated_date':                r'Updated Date:\s?(.+)',

    'name_servers':                r'Name Server:\s*(.+)\s*',
    'status':                    r'Status:\s?(.+)',
    'emails':                    r'[\w.-]+@[\w.-]+\.[\w]{2,4}',

    'domain_name':              r'Domain:\s?(.+)',

    'registrar':                None,

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':          r'Expiration Date:\s?(.+)',
    'updated_date':             None,

    'name_servers':             r'Name Server:\s*(.+)',
    'status':                   r'Domain Status:\s?(.+)',
}

pub = {
    'domain_name':                r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':                r'Registrant\s*Organi(?:s|z)ation:\s?(.+)',
    'registrant_country':       r'Registrant Country:\s?(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':            r'Registry Expiry Date:\s?(.+)',
    'updated_date':                r'Updated Date:\s?(.+)',

    'name_servers':                r'Name Server:\s*(.+)\s*',
    'status':                    r'Status:\s?(.+)',
    'emails':                    r'[\w.-]+@[\w.-]+\.[\w]{2,4}',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':               r'Registrant Organization:\s?(.+)',

    'updated_date':             r'Updated Date:\s?(.+)',
    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':          r'Registry Expiry Date:\s?(.+)',

    'name_servers':             r'Name Server:\s*(.+)',
    'status':                   r'Domain Status:\s*(.+)',
}

pw = {
    'domain_name':                r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':                r'Registrant\s*Organi(?:s|z)ation:\s?(.+)',
    'registrant_country':       r'Registrant Country:\s?(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':            r'Registry Expiry Date:\s?(.+)',
    'updated_date':                r'Updated Date:\s?(.+)',

    'name_servers':                r'Name Server:\s*(.+)\s*',
    'status':                    r'Status:\s?(.+)',
    'emails':                    r'[\w.-]+@[\w.-]+\.[\w]{2,4}',

    'domain_name':              r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s*(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':          r'Registry Expiry Date:\s?(.+)',
    'updated_date':             r'Updated Date:\s?(.+)',

    'status':                   r'Status:\s?(.+)',
}

rest = {
    'domain_name':                r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':                r'Registrant\s*Organi(?:s|z)ation:\s?(.+)',
    'registrant_country':       r'Registrant Country:\s?(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':            r'Registry Expiry Date:\s?(.+)',
    'updated_date':                r'Updated Date:\s?(.+)',

    'name_servers':                r'Name Server:\s*(.+)\s*',
    'status':                    r'Status:\s?(.+)',
    'emails':                    r'[\w.-]+@[\w.-]+\.[\w]{2,4}',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':               r'Registrant Organization:\s?(.+)',

    'updated_date':             r'Updated Date:\s?(.+)',
    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':          r'Registry Expiry Date:\s?(.+)',

    'name_servers':             r'Name Server:\s*(.+)',
    'status':                   r'Domain Status:\s*(.+)',

    'status':                   r'Domain Status:\s*(.+)',
}

ru = {
    'domain_name':                r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':                r'Registrant\s*Organi(?:s|z)ation:\s?(.+)',
    'registrant_country':       r'Registrant Country:\s?(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':            r'Registry Expiry Date:\s?(.+)',
    'updated_date':                r'Updated Date:\s?(.+)',

    'name_servers':                r'Name Server:\s*(.+)\s*',
    'status':                    r'Status:\s?(.+)',
    'emails':                    r'[\w.-]+@[\w.-]+\.[\w]{2,4}',

    'domain_name':              r'\ndomain:\s*(.+)',

    'creation_date':            r'\ncreated:\s*(.+)',
    'expiration_date':          r'\npaid-till:\s*(.+)',

    'name_servers':             r'\nnserver:\s*(.+)',
    'status':                   r'\nstate:\s*(.+)',
}

ru_rf = {
    'domain_name':                r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':                r'Registrant\s*Organi(?:s|z)ation:\s?(.+)',
    'registrant_country':       r'Registrant Country:\s?(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':            r'Registry Expiry Date:\s?(.+)',
    'updated_date':                r'Updated Date:\s?(.+)',

    'name_servers':                r'Name Server:\s*(.+)\s*',
    'status':                    r'Status:\s?(.+)',
    'emails':                    r'[\w.-]+@[\w.-]+\.[\w]{2,4}',

    'domain_name':              r'\ndomain:\s*(.+)',

    'creation_date':            r'\ncreated:\s*(.+)',
    'expiration_date':          r'\npaid-till:\s*(.+)',

    'name_servers':             r'\nnserver:\s*(.+)',
    'status':                   r'\nstate:\s*(.+)',
}

sale = {
    'domain_name':                r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':                r'Registrant\s*Organi(?:s|z)ation:\s?(.+)',
    'registrant_country':       r'Registrant Country:\s?(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':            r'Registry Expiry Date:\s?(.+)',
    'updated_date':                r'Updated Date:\s?(.+)',

    'name_servers':                r'Name Server:\s*(.+)\s*',
    'status':                    r'Status:\s?(.+)',
    'emails':                    r'[\w.-]+@[\w.-]+\.[\w]{2,4}',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':               r'Registrant Organization:\s?(.+)',

    'updated_date':             r'Updated Date:\s?(.+)',
    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':          r'Registry Expiry Date:\s?(.+)',

    'name_servers':             r'Name Server:\s*(.+)',
    'status':                   r'Domain Status:\s*(.+)',
}

security = {
    'domain_name':                r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':                r'Registrant\s*Organi(?:s|z)ation:\s?(.+)',
    'registrant_country':       r'Registrant Country:\s?(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':            r'Registry Expiry Date:\s?(.+)',
    'updated_date':                r'Updated Date:\s?(.+)',

    'name_servers':                r'Name Server:\s*(.+)\s*',
    'status':                    r'Status:\s?(.+)',
    'emails':                    r'[\w.-]+@[\w.-]+\.[\w]{2,4}',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':               r'Registrant Organization:\s?(.+)',

    'updated_date':             r'Updated Date:\s?(.+)',
    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':          r'Registry Expiry Date:\s?(.+)',

    'name_servers':             r'Name Server:\s*(.+)',
    'status':                   r'Domain Status:\s*(.+)',
}

sh = {
    'domain_name':                r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':                r'Registrant\s*Organi(?:s|z)ation:\s?(.+)',
    'registrant_country':       r'Registrant Country:\s?(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':            r'Registry Expiry Date:\s?(.+)',
    'updated_date':                r'Updated Date:\s?(.+)',

    'name_servers':                r'Name Server:\s*(.+)\s*',
    'status':                    r'Status:\s?(.+)',
    'emails':                    r'[\w.-]+@[\w.-]+\.[\w]{2,4}',
    
    'registrant':              r'\nRegistrant Organization:\s?(.+)',

    'expiration_date':         r'\nRegistry Expiry Date:\s*(.+)',

    'status':                  r'\nDomain Status:\s?(.+)',
}

site = {
    'domain_name':                r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':                r'Registrant\s*Organi(?:s|z)ation:\s?(.+)',
    'registrant_country':       r'Registrant Country:\s?(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':            r'Registry Expiry Date:\s?(.+)',
    'updated_date':                r'Updated Date:\s?(.+)',

    'name_servers':                r'Name Server:\s*(.+)\s*',
    'status':                    r'Status:\s?(.+)',
    'emails':                    r'[\w.-]+@[\w.-]+\.[\w]{2,4}',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':               r'Registrant Organization:\s?(.+)',

    'updated_date':             r'Updated Date:\s?(.+)',
    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':          r'Registry Expiry Date:\s?(.+)',

    'name_servers':             r'Name Server:\s*(.+)',
    'status':                   r'Domain Status:\s*(.+)',
}

se = {
    'extend': None,

    'domain_name':              r'domain:\s?(.+)',

    'registrar':                r'registrar:\s?(.+)',

    'registrant_country':       None,

    'creation_date':            r'created:\s?(.+)',
    'expiration_date':          r'expires:\s?(.+)',
    'updated_date':             r'modified:\s?(.+)',

    'name_servers':             r'nserver:\s*(.+)',
    'status':                   r'status:\s?(.+)',
}

space = {
    'domain_name':                r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':                r'Registrant\s*Organi(?:s|z)ation:\s?(.+)',
    'registrant_country':       r'Registrant Country:\s?(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':            r'Registry Expiry Date:\s?(.+)',
    'updated_date':                r'Updated Date:\s?(.+)',

    'name_servers':                r'Name Server:\s*(.+)\s*',
    'status':                    r'Status:\s?(.+)',
    'emails':                    r'[\w.-]+@[\w.-]+\.[\w]{2,4}',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':               r'Registrant Organization:\s?(.+)',

    'updated_date':             r'Updated Date:\s?(.+)',
    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':          r'Registry Expiry Date:\s?(.+)',

    'name_servers':             r'Name Server:\s*(.+)',
    'status':                   r'Domain Status:\s*(.+)',
}

store = {
    'domain_name':                r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':                r'Registrant\s*Organi(?:s|z)ation:\s?(.+)',
    'registrant_country':       r'Registrant Country:\s?(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':            r'Registry Expiry Date:\s?(.+)',
    'updated_date':                r'Updated Date:\s?(.+)',

    'name_servers':                r'Name Server:\s*(.+)\s*',
    'status':                    r'Status:\s?(.+)',
    'emails':                    r'[\w.-]+@[\w.-]+\.[\w]{2,4}',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':               r'Registrant Organization:\s?(.+)',

    'updated_date':             r'Updated Date:\s?(.+)',
    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':          r'Registry Expiry Date:\s?(.+)',

    'name_servers':             r'Name Server:\s*(.+)',
    'status':                   r'Domain Status:\s*(.+)',
}

study = {
    'domain_name':                r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':                r'Registrant\s*Organi(?:s|z)ation:\s?(.+)',
    'registrant_country':       r'Registrant Country:\s?(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':            r'Registry Expiry Date:\s?(.+)',
    'updated_date':                r'Updated Date:\s?(.+)',

    'name_servers':                r'Name Server:\s*(.+)\s*',
    'status':                    r'Status:\s?(.+)',
    'emails':                    r'[\w.-]+@[\w.-]+\.[\w]{2,4}',
}

tech = {
    'domain_name':                r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':                r'Registrant\s*Organi(?:s|z)ation:\s?(.+)',
    'registrant_country':       r'Registrant Country:\s?(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':            r'Registry Expiry Date:\s?(.+)',
    'updated_date':                r'Updated Date:\s?(.+)',

    'name_servers':                r'Name Server:\s*(.+)\s*',
    'status':                    r'Status:\s?(.+)',
    'emails':                    r'[\w.-]+@[\w.-]+\.[\w]{2,4}',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':               r'Registrant Organization:\s?(.+)',

    'updated_date':             r'Updated Date:\s?(.+)',
    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':          r'Registry Expiry Date:\s?(.+)',

    'name_servers':             r'Name Server:\s*(.+)',
    'status':                   r'Domain Status:\s*(.+)',
}


tel = {
    'domain_name':                r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':                r'Registrant\s*Organi(?:s|z)ation:\s?(.+)',
    'registrant_country':       r'Registrant Country:\s?(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':            r'Registry Expiry Date:\s?(.+)',
    'updated_date':                r'Updated Date:\s?(.+)',

    'name_servers':                r'Name Server:\s*(.+)\s*',
    'status':                    r'Status:\s?(.+)',
    'emails':                    r'[\w.-]+@[\w.-]+\.[\w]{2,4}',

    'domain_name':              r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s*(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':          r'\nRegistry Expiry Date:\s?(.+)',
    'updated_date':             r'Updated Date:\s?(.+)',

    'status':                   r'Status:\s?(.+)',
}

theatre = {
    'domain_name':                r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':                r'Registrant\s*Organi(?:s|z)ation:\s?(.+)',
    'registrant_country':       r'Registrant Country:\s?(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':            r'Registry Expiry Date:\s?(.+)',
    'updated_date':                r'Updated Date:\s?(.+)',

    'name_servers':                r'Name Server:\s*(.+)\s*',
    'status':                    r'Status:\s?(.+)',
    'emails':                    r'[\w.-]+@[\w.-]+\.[\w]{2,4}',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':               r'Registrant Organization:\s?(.+)',

    'updated_date':             r'Updated Date:\s?(.+)',
    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':          r'Registry Expiry Date:\s?(.+)',

    'name_servers':             r'Name Server:\s*(.+)',
    'status':                   r'Domain Status:\s*(.+)',
}

tickets = {
    'domain_name':                r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':                r'Registrant\s*Organi(?:s|z)ation:\s?(.+)',
    'registrant_country':       r'Registrant Country:\s?(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':            r'Registry Expiry Date:\s?(.+)',
    'updated_date':                r'Updated Date:\s?(.+)',

    'name_servers':                r'Name Server:\s*(.+)\s*',
    'status':                    r'Status:\s?(.+)',
    'emails':                    r'[\w.-]+@[\w.-]+\.[\w]{2,4}',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':               r'Registrant Organization:\s?(.+)',

    'updated_date':             r'Updated Date:\s?(.+)',
    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':          r'Registry Expiry Date:\s?(.+)',

    'name_servers':             r'Name Server:\s*(.+)',
    'status':                   r'Domain Status:\s*(.+)',
}

trade = {
    'domain_name':                r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':                r'Registrant\s*Organi(?:s|z)ation:\s?(.+)',
    'registrant_country':       r'Registrant Country:\s?(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':            r'Registry Expiry Date:\s?(.+)',
    'updated_date':                r'Updated Date:\s?(.+)',

    'name_servers':                r'Name Server:\s*(.+)\s*',
    'status':                    r'Status:\s?(.+)',
    'emails':                    r'[\w.-]+@[\w.-]+\.[\w]{2,4}',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':               r'Registrant Organization:\s?(.+)',

    'updated_date':             r'Updated Date:\s?(.+)',
    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':          r'Registry Expiry Date:\s?(.+)',

    'name_servers':             r'Name Server:\s*(.+)',
    'status':                   r'Domain Status:\s*(.+)',
}

tv = {
    'domain_name':                r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':                r'Registrant\s*Organi(?:s|z)ation:\s?(.+)',
    'registrant_country':       r'Registrant Country:\s?(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':            r'Registry Expiry Date:\s?(.+)',
    'updated_date':                r'Updated Date:\s?(.+)',

    'name_servers':                r'Name Server:\s*(.+)\s*',
    'status':                    r'Status:\s?(.+)',
    'emails':                    r'[\w.-]+@[\w.-]+\.[\w]{2,4}',

    'domain_name':              r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s*(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':          r'Registry Expiry Date:\s?(.+)',
    'updated_date':             r'Updated Date:\s?(.+)',

    'status':                   r'Status:\s?(.+)',
}

ua = {
   'domain_name':                r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':                r'Registrant\s*Organi(?:s|z)ation:\s?(.+)',
    'registrant_country':       r'Registrant Country:\s?(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':            r'Registry Expiry Date:\s?(.+)',
    'updated_date':                r'Updated Date:\s?(.+)',

    'name_servers':                r'Name Server:\s*(.+)\s*',
    'status':                    r'Status:\s?(.+)',
    'emails':                    r'[\w.-]+@[\w.-]+\.[\w]{2,4}',

    'domain_name':              r'\ndomain:\s*(.+)',

    'registrar':                r'\nregistrar:\s*(.+)',
    'registrant_country':       r'\ncountry:\s*(.+)',

    'creation_date':            r'\ncreated:\s*(.+)',
    'expiration_date':          r'\nexpires:\s*(.+)',
    'updated_date':             r'\nmodified:\s*(.+)',

    'name_servers':             r'\nnserver:\s*(.+)',
    'status':                   r'\nstatus:\s*(.+)',
}

uk = {
    'domain_name':                r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':                r'Registrant\s*Organi(?:s|z)ation:\s?(.+)',
    'registrant_country':       r'Registrant Country:\s?(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':            r'Registry Expiry Date:\s?(.+)',
    'updated_date':                r'Updated Date:\s?(.+)',

    'name_servers':                r'Name Server:\s*(.+)\s*',
    'status':                    r'Status:\s?(.+)',
    'emails':                    r'[\w.-]+@[\w.-]+\.[\w]{2,4}',

    'registrant':               r'Registrant:\n\s*(.+)',

    'creation_date':            r'Registered on:\s*(.+)',
    'expiration_date':          r'Expiry date:\s*(.+)',
    'updated_date':             r'Last updated:\s*(.+)',

    'name_servers':             r'Name Servers:\s*(.+)\s*',
    'status':                   r'Registration status:\n\s*(.+)',
}

us = {
    'domain_name':                r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':                r'Registrant\s*Organi(?:s|z)ation:\s?(.+)',
    'registrant_country':       r'Registrant Country:\s?(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':            r'Registry Expiry Date:\s?(.+)',
    'updated_date':                r'Updated Date:\s?(.+)',

    'name_servers':                r'Name Server:\s*(.+)\s*',
    'status':                    r'Status:\s?(.+)',
    'emails':                    r'[\w.-]+@[\w.-]+\.[\w]{2,4}',

    'status':                   r'Domain Status:\s?(.+)',
}

uz = {
    'domain_name':                r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':                r'Registrant\s*Organi(?:s|z)ation:\s?(.+)',
    'registrant_country':       r'Registrant Country:\s?(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':            r'Registry Expiry Date:\s?(.+)',
    'updated_date':                r'Updated Date:\s?(.+)',

    'name_servers':                r'Name Server:\s*(.+)\s*',
    'status':                    r'Status:\s?(.+)',
    'emails':                    r'[\w.-]+@[\w.-]+\.[\w]{2,4}',

    'domain_name':              r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s*(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':          r'Expiration Date:\s?(.+)',
    'updated_date':             r'Updated Date:\s?(.+)',

    'status':                   r'Status:\s?(.+)',
}

video = {
    'domain_name':                r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':                r'Registrant\s*Organi(?:s|z)ation:\s?(.+)',
    'registrant_country':       r'Registrant Country:\s?(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':            r'Registry Expiry Date:\s?(.+)',
    'updated_date':                r'Updated Date:\s?(.+)',

    'name_servers':                r'Name Server:\s*(.+)\s*',
    'status':                    r'Status:\s?(.+)',
    'emails':                    r'[\w.-]+@[\w.-]+\.[\w]{2,4}',

    'expiration_date':          r'\nRegistry Expiry Date:\s?(.+)',
    'updated_date':             r'\nUpdated Date:\s?(.+)',
}

website = {
    'domain_name':                r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':                r'Registrant\s*Organi(?:s|z)ation:\s?(.+)',
    'registrant_country':       r'Registrant Country:\s?(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':            r'Registry Expiry Date:\s?(.+)',
    'updated_date':                r'Updated Date:\s?(.+)',

    'name_servers':                r'Name Server:\s*(.+)\s*',
    'status':                    r'Status:\s?(.+)',
    'emails':                    r'[\w.-]+@[\w.-]+\.[\w]{2,4}',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':               r'Registrant Organization:\s?(.+)',

    'updated_date':             r'Updated Date:\s?(.+)',
    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':          r'Registry Expiry Date:\s?(.+)',

    'name_servers':             r'Name Server:\s*(.+)',
    'status':                   r'Domain Status:\s*(.+)',
}

wiki = {
    'domain_name':                r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':                r'Registrant\s*Organi(?:s|z)ation:\s?(.+)',
    'registrant_country':       r'Registrant Country:\s?(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':            r'Registry Expiry Date:\s?(.+)',
    'updated_date':                r'Updated Date:\s?(.+)',

    'name_servers':                r'Name Server:\s*(.+)\s*',
    'status':                    r'Status:\s?(.+)',
    'emails':                    r'[\w.-]+@[\w.-]+\.[\w]{2,4}',

    'domain_name':              r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s*(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':          r'Registry Expiry Date:\s?(.+)',
    'updated_date':             r'Updated Date:\s?(.+)',

    'status':                   r'Status:\s?(.+)',
}

work = {
    'domain_name':                r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':                r'Registrant\s*Organi(?:s|z)ation:\s?(.+)',
    'registrant_country':       r'Registrant Country:\s?(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':            r'Registry Expiry Date:\s?(.+)',
    'updated_date':                r'Updated Date:\s?(.+)',

    'name_servers':                r'Name Server:\s*(.+)\s*',
    'status':                    r'Status:\s?(.+)',
    'emails':                    r'[\w.-]+@[\w.-]+\.[\w]{2,4}',

    'domain_name':              r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s*(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':          r'Registry Expiry Date:\s?(.+)',
    'updated_date':             r'Updated Date:\s?(.+)',
}

xyz = {
    'domain_name':                r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':                r'Registrant\s*Organi(?:s|z)ation:\s?(.+)',
    'registrant_country':       r'Registrant Country:\s?(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':            r'Registry Expiry Date:\s?(.+)',
    'updated_date':                r'Updated Date:\s?(.+)',

    'name_servers':                r'Name Server:\s*(.+)\s*',
    'status':                    r'Status:\s?(.+)',
    'emails':                    r'[\w.-]+@[\w.-]+\.[\w]{2,4}',

    'domain_name':              r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s*(.+)',
    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':          r'\nRegistry Expiry Date:\s?(.+)',
    'updated_date':             r'Updated Date:\s?(.+)',
    'status':                   r'Status:\s?(.+)',
}

za = {
    'domain_name':                r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':                r'Registrant\s*Organi(?:s|z)ation:\s?(.+)',
    'registrant_country':       r'Registrant Country:\s?(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':            r'Registry Expiry Date:\s?(.+)',
    'updated_date':                r'Updated Date:\s?(.+)',

    'name_servers':                r'Name Server:\s*(.+)\s*',
    'status':                    r'Status:\s?(.+)',
    'emails':                    r'[\w.-]+@[\w.-]+\.[\w]{2,4}',
}


    