import requests,re,colorama
import os
import sys
colorama.init()
red = '\033[31m'
yellow = '\033[93m'
green = '\033[92m'
clear = '\033[0m'
bold = '\033[01m'
cyan = '\033[96m'
cy='\033[095m'
cya='\033[095m'
os.system("clear")
os.system("figlet U-danbaiwa")
print(green,"\t\t\tv1.0.0")
print("\n\n")
print(cyan," 1:-Hack Cctv Camera")
print("")
print(yellow,bold,"2:-Update Tool")
print("")
print(cy,bold,"3:-Exit")
print("\n")
cho=input(cya,bold,"Enter Option: ")      
if cho=="1":
   
   print("\n")
   print(red,"1:-France")
   print(green,"2:-South Africa")
   print(yellow,"3:-Saudi Arabia")
   print(cya,"4:-Germany")
   print(bold,"5:-Slovakia")
   print(cya,"6:-Crotia")
   print(green,"7:-Taiwan")
   print(red,"8:-Hungary")
   print(cya,"9:-Cyprus")
   print(yellow,"10:-Russian Federation")
   try:
     print()
     countries = ["US", "JP", "IT", "KR", "FR", "DE", "TW", "RU", "GB", "NL","-"]
     headers = {"User-Agent": "Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0"}

     num = int(input("OPTIONS : "))
     if num not in range(1, 10+1):
       raise IndexError

     country = countries[num-1]
     res = requests.get(
        f"https://www.insecam.org/en/bycountry/{country}", headers=headers
    )
     last_page = re.findall(r'pagenavigator\("\?page=", (\d+)', res.text)[0]

     for page in range(int(last_page)):
       res = requests.get(
            f"https://www.insecam.org/en/bycountry/{country}/?page={page}",
            headers=headers
        )
       find_ip = re.findall(r"http://\d+.\d+.\d+.\d+:\d+", res.text)
       for ip in find_ip:
         print("\033[1;31m", ip)
   
   except:
     pass
   finally:
     print("\033[1;37m")
     exit()
elif cho=="3":
  #print()
   os.system("clear")
   os.system("figlet U-danbaiwa")
   print(green,"\t\t\tv 1.0.0")
   print(cya,"\t\tcoded by U-danbaiwa")
   print("\n")
   print(yellow,bold,"\t*********************************************")
   print(cya,"CHOOSE PAGE FROM",yellow,"1",cya,"to",yellow," 5")
   print(bold,green,"\t*********************************************")
		 
   list=input(cya,"Enter Choice: ")
   if list=="1":
   os.system("clear")
   os.system("figlet CCTC-HACK")
   print(green,"\t\t\tv 1.0.0")
   print(cya,"\t\tcoded by U-danbaiwa")
   print(green,"CHOOSE\n")
   print(Yellow,bold,"1:-United States\n2:-Mexico\n3:-Moldova\n4:-Japan\n5:-Finland\n5:-Nicaragua\n6:-Italy\n7:-China\n8:-Malta\n9:-Korea\n10:-Chile")
			
