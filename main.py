import requests
from colorama import Fore
from pyfiglet import Figlet
from rainbowtext import text


def logo():
    banner = Figlet(font="doom").renderText("Eyecon")
    print(text(banner))
    print(Fore.RED + "[*] Powered by Root of Cyber")
    print(text( "[+] Created by Mr.Cyb3rGhost"))
    print(Fore.LIGHTMAGENTA_EX + "[-] Number Lookup version: 2.0")
    print(Fore.YELLOW + "╼" * 60)
    
def main():
    number = (input(Fore.GREEN+"[*] Enter a Number: "))

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
        'Connection': 'Keep-Alive',
        'Accept': 'application/json',
        'e-auth-v': 'e1',
        'e-auth': 'dd4190a9-e11e-453d-86ea-2246ddfbd393',
        'e-auth-c': '41',
        'e-auth-k': 'PgdtSBeR0MumR7fO',
        'accept-charset': 'UTF-8',
        'content-type': 'application/x-www-form-urlencoded; charset=utf-8',
    }

    params = {
        'cli': f'88{number}',
        'lang': 'en',
        'is_callerid': 'true',
        'is_ic': 'true',
        'cv': 'vc_530_vn_4.0.530_a',
        'requestApi': 'URLconnection',
        'source': 'MenifaFragment',
    }

    response = requests.get('https://api.eyecon-app.com/app/getnames.jsp', params=params, headers=headers)
    if response.status_code == 200:
        res_data= response.json()
        print(Fore.GREEN+"[+] Name:", res_data[0]['name'])
    else:
        print(Fore.RED+"[-] Error: ", response.status_code)
    

logo()
main()
