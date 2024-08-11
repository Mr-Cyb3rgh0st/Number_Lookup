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
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
        "accept": "application/json",
        "e-auth-v": "e1",
        "e-auth": "345eb9cc-3c68-415e-82ae-f41882255d01",                   
        "e-auth-c": "33",
        "e-auth-k": "PgdtSBeR0MumR7fO",
        "accept-charset": "UTF-8",
        "content-type": "application/x-www-form-urlencoded; charset=utf-8",
        "Host": "api.eyecon-app.com",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip"
    }

    url = f"https://api.eyecon-app.com/app/getnames.jsp?cli=88{number}&lang=en&is_callerid=true&is_ic=true&cv=vc_510_vn_4.0.510_a&requestApi=okHttp&source=MenifaFragment"
    response = requests.get(url, headers=headers)

    print(Fore.GREEN+"[+] Name:", response.content.decode('utf-8').split('"name":"')[1].split('","')[0])

logo()
main()