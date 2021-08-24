import data


def domain_lookup(domain):    
    
    if domain.endswith("com"):
        tld = data.com
    elif domain.endswith("ist"):
        tld = data.com
    elif domain.endswith("istanbul"):
        tld = data.com
    elif domain.endswith("ac.uk"):
        tld = data.ac_uk
    elif domain.endswith("am"):
        tld = data.am
    elif domain.endswith("amsterdam"):
        tld = data.amsterdam
    elif domain.endswith("ar"):
        tld = data.ar
    elif domain.endswith("at"):
        tld = data.at
    elif domain.endswith("au"):
        tld = data.au
    elif domain.endswith("aw"):
        tld = data.aw
    elif domain.endswith("bank"):
        tld = data.bank
    elif domain.endswith("be"):
        tld = data.be
    elif domain.endswith("biz"):
        tld = data.biz
    elif domain.endswith("br"):
        tld = data.br
    elif domain.endswith("by"):
        tld = data.by
    elif domain.endswith("ca"):
        tld = data.ca
    elif domain.endswith("cc"):
        tld = data.cc
    elif domain.endswith("cl"):
        tld = data.cl
    elif domain.endswith("club"):
        tld = data.club
    elif domain.endswith("cn"):
        tld = data.cn
    elif domain.endswith("co"):
        tld = data.co
    elif domain.endswith("com.au"):
        tld = data.com_au
    elif domain.endswith("com.tr"):
        tld = data.com_tr
    elif domain.endswith("tr"):
        tld = data.com_tr
    elif domain.endswith("co.il"):
        tld = data.co_il
    elif domain.endswith("courses"):
        tld = data.courses
    elif domain.endswith("cr"):
        tld = data.cr
    elif domain.endswith("cz"):
        tld = data.cz
    elif domain.endswith("de"):
        tld = data.de
    elif domain.endswith("download"):
        tld = data.download
    elif domain.endswith("edu"):
        tld = data.edu
    elif domain.endswith("education"):
        tld = data.education
    elif domain.endswith("eu"):
        tld = data.eu
    elif domain.endswith("fi"):
        tld = data.fi
    elif domain.endswith("fm"):
        tld = data.fm
    elif domain.endswith("fr"):
        tld = data.fr
    elif domain.endswith("flr"):
        tld = data.frl
    elif domain.endswith("game"):
        tld = data.game
    elif domain.endswith("global"):
        tld = data.global_
    elif domain.endswith("hk"):
        tld = data.hk
    elif domain.endswith("id"):
        tld = data.id_
    elif domain.endswith("ie"):
        tld = data.ie
    elif domain.endswith("im"):
        tld = data.im
    elif domain.endswith("in"):
        tld = data.in_
    elif domain.endswith("info"):
        tld = data.info
    elif domain.endswith("ink"):
        tld = data.ink    
    elif domain.endswith("io"):
        tld = data.io
    elif domain.endswith("ir"):
        tld = data.ir
    elif domain.endswith("is"):
        tld = data.is_
    elif domain.endswith("it"):
        tld = data.it
    elif domain.endswith("kr"):
        tld = data.kr
    elif domain.endswith("kz"):
        tld = data.kz
    elif domain.endswith("link"):
        tld = data.link
    elif domain.endswith("lt"):
        tld = data.lt
    elif domain.endswith("lv"):
        tld = data.lv
    elif domain.endswith("ml"):
        tld = data.me
    elif domain.endswith("mobi"):
        tld = data.mobi
    elif domain.endswith("mx"):
        tld = data.mx
    elif domain.endswith("name"):
        tld = data.name
    elif domain.endswith("net"):
        tld = data.net
    elif domain.endswith("ninja"):
        tld = data.ninja
    elif domain.endswith("nl"):
        tld = data.nl
    elif domain.endswith("nu"):
        tld = data.nu
    elif domain.endswith("nyc"):
        tld = data.nyc
    elif domain.endswith("nz"):
        tld = data.nz
    elif domain.endswith("online"):
        tld = data.online
    elif domain.endswith("org"):
        tld = data.org
    elif domain.endswith("pe"):
        tld = data.pe
    elif domain.endswith("pharmacy"):
        tld = data.pharmacy
    elif domain.endswith("pl"):
        tld = data.pl
    elif domain.endswith("press"):
        tld = data.press
    elif domain.endswith("pro"):
        tld = data.pro
    elif domain.endswith("pt"):
        tld = data.pt
    elif domain.endswith("pub"):
        tld = data.pub
    elif domain.endswith("pw"):
        tld = data.pw
    elif domain.endswith("rest"):
        tld = data.rest
    elif domain.endswith("ru"):
        tld = data.ru
    elif domain.endswith("ru.rf"):
        tld = data.ru_rf
    elif domain.endswith("sale"):
        tld = data.sale
    elif domain.endswith("security"):
        tld = data.security
    elif domain.endswith("sh"):
        tld = data.sh
    elif domain.endswith("site"):
        tld = data.site
    elif domain.endswith("se"):
        tld = data.se
    elif domain.endswith("space"):
        tld = data.space
    elif domain.endswith("store"):
        tld = data.store
    elif domain.endswith("study"):
        tld = data.study
    elif domain.endswith("tech"):
        tld = data.tech
    elif domain.endswith("tel"):
        tld = data.tel
    elif domain.endswith("theatre"):
        tld = data.theatre
    elif domain.endswith("tickets"):
        tld = data.tickets
    elif domain.endswith("trade"):
        tld = data.trade
    elif domain.endswith("tv"):
        tld = data.tv
    elif domain.endswith("ua"):
        tld = data.ua
    elif domain.endswith("uk"):
        tld = data.uk
    elif domain.endswith("us"):
        tld = data.us
    elif domain.endswith("uz"):
        tld = data.uz
    elif domain.endswith("video"):
        tld = data.video
    elif domain.endswith("website"):
        tld = data.website
    elif domain.endswith("wiki"):
        tld = data.wiki
    elif domain.endswith("work"):
        tld = data.work
    elif domain.endswith("xyz"):
        tld = data.xyz
    elif domain.endswith("za"):
        tld = data.za
    return tld