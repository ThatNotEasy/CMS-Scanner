# Author: Pari Malam

import os
import requests
import urllib3
import sys
import random
from sys import stdout
from multiprocessing.dummy import Pool
from colorama import Fore, init
from requests.packages.urllib3.exceptions import InsecureRequestWarning
delete_warning = urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
init(autoreset=True)

FR = Fore.RED
FC = Fore.CYAN
FY = Fore.YELLOW
FW = Fore.WHITE
FG = Fore.GREEN

MEOW = 'Results'

if not os.path.exists(MEOW):
    os.mkdir(MEOW)

def banners():
    os.system('clear' if os.name == 'posix' else 'cls')
    stdout.write("                                                                                         \n")
    stdout.write(""+Fore.LIGHTRED_EX +"██████╗ ██████╗  █████╗  ██████╗  ██████╗ ███╗   ██╗███████╗ ██████╗ ██████╗  ██████╗███████╗   ██╗ ██████╗ \n")
    stdout.write(""+Fore.LIGHTRED_EX +"██╔══██╗██╔══██╗██╔══██╗██╔════╝ ██╔═══██╗████╗  ██║██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔════╝   ██║██╔═══██╗\n")
    stdout.write(""+Fore.LIGHTRED_EX +"██║  ██║██████╔╝███████║██║  ███╗██║   ██║██╔██╗ ██║█████╗  ██║   ██║██████╔╝██║     █████╗     ██║██║   ██║\n")
    stdout.write(""+Fore.LIGHTRED_EX +"██║  ██║██╔══██╗██╔══██║██║   ██║██║   ██║██║╚██╗██║██╔══╝  ██║   ██║██╔══██╗██║     ██╔══╝     ██║██║   ██║\n")
    stdout.write(""+Fore.LIGHTRED_EX +"██║  ██║██╔══██╗██╔══██║██║   ██║██║   ██║██║╚██╗██║██╔══╝  ██║   ██║██╔══██╗██║     ██╔══╝     ██║██║   ██║\n")
    stdout.write(""+Fore.LIGHTRED_EX +"██████╔╝██║  ██║██║  ██║╚██████╔╝╚██████╔╝██║ ╚████║██║     ╚██████╔╝██║  ██║╚██████╗███████╗██╗██║╚██████╔╝\n")
    stdout.write(""+Fore.LIGHTRED_EX +"╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚══════╝╚═╝╚═╝ ╚═════╝ \n")
    stdout.write(""+Fore.YELLOW +"═════════════╦═════════════════════════════════╦════════════════════════════════════════════════════════════\n")
    stdout.write(""+Fore.YELLOW   +"╔════════════╩═════════════════════════════════╩═════════════════════════════╗\n")
    stdout.write(""+Fore.YELLOW   +"║ \x1b[38;2;255;20;147m• "+Fore.GREEN+"AUTHOR             "+Fore.RED+"    |"+Fore.LIGHTWHITE_EX+"   PARI MALAM                                    "+Fore.YELLOW+"║\n")
    stdout.write(""+Fore.YELLOW   +"║ \x1b[38;2;255;20;147m• "+Fore.GREEN+"GITHUB             "+Fore.RED+"    |"+Fore.LIGHTWHITE_EX+"   GITHUB.COM/PARI-MALAM                         "+Fore.YELLOW+"║\n")
    stdout.write(""+Fore.YELLOW   +"╔════════════════════════════════════════════════════════════════════════════╝\n")
    stdout.write(""+Fore.YELLOW   +"║ \x1b[38;2;255;20;147m• "+Fore.GREEN+"OFFICIAL FORUM     "+Fore.RED+"    |"+Fore.LIGHTWHITE_EX+"   DRAGONFORCE.IO                                "+Fore.YELLOW+"║\n")
    stdout.write(""+Fore.YELLOW   +"║ \x1b[38;2;255;20;147m• "+Fore.GREEN+"OFFICIAL TELEGRAM  "+Fore.RED+"    |"+Fore.LIGHTWHITE_EX+"   TELEGRAM.ME/DRAGONFORCEIO                     "+Fore.YELLOW+"║\n")
    stdout.write(""+Fore.YELLOW   +"╚════════════════════════════════════════════════════════════════════════════╝\n") 
    print(f"{FY}[CMS-Scanner] - {FG}Perform With CMS Detection")
banners()


MEOWING = 'Depth/User-Agents.txt'

with open(MEOWING, 'r') as f:
    user_agents = [line.strip() for line in f.readlines()]

headers = {
    'User-Agent': random.choice(user_agents),
    'Content-type': '*/*',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive'
}

print(f"\n{FR}• {FY}Wordpress    {FR}• {FY}Joomla        {FR}• {FY}Laravel      \n{FR}• {FY}Opencart     {FR}• {FY}Drupal        {FR}• {FY}Prestashop\n{FR}• {FY}Magento      {FR}• {FY}vBulletin     {FR}• {FY}OsCommerce     {FR}• {FY}GIT-CONFIG")
filename = input(f"\n{Fore.RED}[+] {Fore.YELLOW}IP/DOMAIN LIST: {Fore.WHITE}")
try:
    targets = [i.strip() for i in open(filename, mode='r+', encoding='utf-8').readlines()]
except FileNotFoundError:
    sys.exit(f'{Fore.RED}[!] Bro? Whutt are you doin? File Not Found! {filename}')

def scan(url):
    parimalam(url)

def cms_wordpress(url):
    try:
        meow = url + "/xmlrpc.php?rsd"
        get_source = requests.get(meow, headers=headers, timeout=15).text
        if 'WordPress' in get_source:
            print(f'{FY}[CMS-Scanner] - {FW}{url} - {FG}[Wordpress!]')
            open(f'{MEOW}/Wordpress.txt', 'a').write(url + '\n')
        else:
            print(f'{FY}[CMS-Scanner] - {FW}{url} - {FR}[Not Found!]')
    except:
        pass

def cms_joomla(url):
    try:
        meow = url + "/language/en-GB/en-GB.xml"
        get_source = requests.get(meow, headers=headers, timeout=15).text
        if 'Joomla! Project' in get_source:
            print(f'{FY}[CMS-Scanner] - {FW}{url} - {FG}[Joomla!]')
            open(f'{MEOW}/Joomla.txt', 'a').write(url + '\n')
        else:
            print(f'{FY}[CMS-Scanner] - {FW}{url} - {FR}[Not Found!]')
    except:
        pass

def cms_laravel(url):
    try:
        meow = url + "/.env"
        get_source = requests.get(url, headers=headers, timeout=15).cookies
        get_sources = requests.get(meow, headers=headers, timeout=15).text
        if 'X-XSRF-TOKEN' in get_source and 'XSRF-TOKEN' in get_source:
            print(f'{FY}[CMS-Scanner] - {FW}{url} - {FG}[Laravel!]')
            open(f'{MEOW}/Laravel.txt', 'a').write(url + '\n')
        elif 'DB_HOST' in get_sources:
            print(f'{FY}[CMS-Scanner] - {FW}{url} - {FG}[Laravel!]')
            open(f'{MEOW}/Laravel.txt', 'a').write(url + '\n')
        else:
            print(f'{FY}[CMS-Scanner] - {FW}{url} - {FR}[Not Found!]')
    except:
        pass

def cms_opencart(url):
    try:
        get_source = requests.get(url, headers=headers, timeout=15).text
        if '/index.php?route=' in get_source:
            print(f'{FY}[CMS-Scanner] - {FW}{url} - {FG}[Opencart!]')
            open(f'{MEOW}/Opencart.txt', 'a').write(url + '\n')
        else:
            print(f'{FY}[CMS-Scanner] - {FW}{url} - {FR}[Not Found!]')
    except:
        pass

def cms_drupal(url):
    try:
        meow = url + "/sites/default"
        get_source = requests.get(url, headers=headers, timeout=15).text
        if 'sites/default' in get_source:
            print(f'{FY}[CMS-Scanner] - {FW}{url} - {FG}[Drupal!]')
            open(f'{MEOW}/Drupal.txt', 'a').write(url + '\n')
        else:
            print(f'{FY}[CMS-Scanner] - {FW}{url} - {FR}[Not Found!]')
    except:
        pass

def cms_prestashop(url):
    try:
        get_source = requests.get(url, headers=headers, timeout=15).text
        if 'content="PrestaShop"' in get_source:
            print(f'{FY}[CMS-Scanner] - {FW}{url} - {FG}[Prestashop!]')
            open(f'{MEOW}/Prestashop.txt', 'a').write(url + '\n')
        else:
            print(f'{FY}[CMS-Scanner] - {FW}{url} - {FR}[Not Found!]')
    except:
        pass

def cms_magento(url):
    try:
        meow = url + "/index.php/admin/index/"
        get_source = requests.get(meow, headers=headers, timeout=15).text
        if 'Magento' in get_source:
            print(f'{FY}[CMS-Scanner] - {FW}{url} - {FG}[Magento!]')
            open(f'{MEOW}/Magento.txt', 'a').write(url + '\n')
        else:
            print(f'{FY}[CMS-Scanner] - {FW}{url} - {FR}[Not Found!]')
    except:
        pass

def cms_vbulletin(url):
    try:
        get_source = requests.get(url, headers=headers, timeout=15).text
        if 'meta name="generator" content="vBulletin' in get_source:
            print(f'{FY}[CMS-Scanner] - {FW}{url} - {FG}[vBulletin!]')
            open(f'{MEOW}/vBulletin.txt', 'a').write(url + '\n')
        else:
            print(f'{FY}[CMS-Scanner] - {FW}{url} - {FR}[Not Found!]')
    except:
        pass

def cms_oscommerce(url):
    try:
        get_source = requests.get(url, headers=headers, timeout=15).text
        if 'osCommerce' in get_source:
            print(f'{FY}[CMS-Scanner] - {FW}{url} - {FG}[OsCommerce!]')
            open(f'{MEOW}/osCommerce.txt', 'a').write(url + '\n')
        else:
            print(f'{FY}[CMS-Scanner] - {FW}{url} - {FR}[Not Found!]')
    except:
        pass

def git_config(url):
    try:
        meow = url + "/.git/config"
        get_source = requests.get(meow, headers=headers, timeout=15).text
        if 'repositoryformatversion' in get_source:
            print(f'{FY}[CMS-Scanner] - {FW}{url} - {FG}[GIT Found!]')
            open(f'{MEOW}/GIT-CONFIG.txt', 'a').write(url + '\n')
        else:
            print(f'{FY}[CMS-Scanner] - {FW}{url} - {FR}[Not Found!]')
    except:
        pass

def parimalam(url):
    cms_wordpress(url)
    cms_joomla(url)
    cms_laravel(url)
    cms_opencart(url)
    cms_drupal(url)
    cms_prestashop(url)
    cms_magento(url)
    cms_vbulletin(url)
    cms_oscommerce(url)
    git_config(url)

if __name__ == '__main__':
    try:
        with Pool(50) as p:
            p.map(scan, targets)
    except KeyboardInterrupt:
        print(f"{FR}[BYE BITCH!]")