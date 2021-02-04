#libraries 
import requests, re, colorama
import os
import sys
#import urrlib
#import httplib
#import urrlib2
#import json
import time
#import scan
#colours requered
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
cho=input("Enter Option: ")      
if cho=="1":
  os.system("clear")
  os.system("figlet U-danbaiwa")
  print(green,"\t\t\tv 1.0.0")
  print(cya,"\t\tcoded by U-danbaiwa")
  print("\n")
  print(yellow,bold,"\t*********************************************")
  print(cya,"CHOOSE PAGE FROM",yellow,"1",cya,"to",yellow," 5")
  print(bold,green,"\t*********************************************")
  print("")
  list=input("Enter Choice: ")
  
  if list=="1":
    os.system("clear")
    os.system("figlet CCTC-HACK")
    print(green,"\t\t\tv 1.0.0")
    print(cya,"\t\tcoded by U-danbaiwa")
    print(green,"CHOOSE\n")
    print(yellow,bold,"1:-United States\n2:-Mexico\n3:-Moldova\n4:-Japan\n5:-Finland\n5:-Nicaragua\n6:-Italy\n7:-China\n8:-Malta\n9:-Korea\n10:-Chile")
    try:
    
      countries= ["US", "JP", "IT", "KR", "FR", "DE", "TW", "RU", "GB", "NL","-"]
      headers = {"User-Agent": "Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0"}
      num= int(input("Enter Country: "))
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
        
  elif list=="2":
    os.system("clear")
    os.system("figlet CCTV-HACK")
    print(green,"\t\t\tv 1.0.0")
    print(cya,"\t\tcoded by U-danbaiwa")
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
      coun= ["CZ", "TR", "AT", "CH", "ES", "CA", "SE", "IL", "PL", "IR","-"]
      headers = {"User-Agent": "Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0"}
      num= int(input("Choose Country: "))
      if num not in range(1, 10+1):
      	raise IndexError
      country= coun[num-1]
      res= requests.get(f"https://www.insecam.org/en/bycountry/{country}", headers=headers)
      last_page = re.findall(r'pagenavigator\("\?page=", (\d+)', res.text)[0]
      for page in range(int(last_page)):
         res= requests.get(f"https://www.insecam.org/en/bycountry/{country}/?page={page}",headers=headers)
         find_ip = re.findall(r"http://\d+.\d+.\d+.\d+:\d+", res.text)
         for ip in find_ip:
            print('\033[096m',"CCTV IP HACKED==>","\033[92m",'\033[01m',ip,green,"ACCESS GRANTED")
    except:
      pass
    finally:
      print("\033[1;37m")
      exit() 
    	        
  if list=="3":
    os.system("clear")
    os.system("figlet CCTV-HACK")
    print(green,"\t\t\tv 1.0.0")
    print(cya,"\t\tcoded by U-danbaiwa")
    print("\n")
    print(red,"1:-Ireland")
    print(green,"2:-Pakistan")
    print(yellow,"3:-United Kingdom")
    print(cya,"4:-Egypt")
    print(bold,"5:-Netherland")
    print(cya,"6:-Thailand")
    print(green,"7:-Khazakhstan")
    print(red,"8:-Czeck Republic")
    print(cya,"9:-Ukraine")
    print(yellow,"10:-Kuwait")
    print("")
    try:
      countries= ["NO", "RO", "IN", "VN", "BE", "BR", "BG", "ID", "DK", "AR","-"]
      headers= {"User-Agent": "Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0"}

      num = int(input("Choose Country: "))
      if num not in range(1, 10+1):
      	raise IndexError
      country = countries[num-1]
      res= requests.get(f"https://www.insecam.org/en/bycountry/{country}", headers=headers)
      last_page2= re.findall(r'pagenavigator\("\?page=", (\d+)', res.text)[0]
      for page in range(int(last_page2)):
        res= requests.get(f"https://www.insecam.org/en/bycountry/{country}/?page={page}",headers=headers)
       	find_ip = re.findall(r"http://\d+.\+.\d+.\d+:\d+", res.text)
        for ip in find_ip:
          print('\033[096m',"CCTV IP HACKED==>","\033[92m",'\033[01m',ip,green,"ACCESS GRANTED")
    except:
      pass
    finally:
      print("\033[1;37m")
      exit()             
  if list=="4":
    os.system("clear")
    os.system("figlet CCTV-HACK")
    print(green,"\t\t\tv 1.0.0")
    print(cya,"\t\tcoded by U-danbaiwa")
    print("\n")
    print(red,"1:-Turkey")
    print(green,"2:-Serbia")
    print(yellow,"3:-Venezuela")
    print(cya,"4:-Austria")
    print(bold,"5:-Honkong")
    print(cya,"6:-Geogeia")
    print(green,"7:-Switzerland")
    print(red,"8:-greece")
    print(cya,"9:-montenegro")
    print(yellow,"10:-Spain")
    print(red,"11:-Portugal")
    print(green,"12:-El Salvador")
    print(yellow,"13:-Canada")
    print(cya,"14:-Latvia")
    print(bold,"15:-Luxembourg")
    print(cya,"16:-Sweden")
    print(green,"17:-Singapore")
    print(red,"18:-Curacao")
    print(cya,"19:-Israel")
    print(yellow,"20:-Iceland")
    print(cya,"21:-Puerto Rico")
    print(green,"22:-iran")
    print(red,"23:-Malaysia")
    print(cya,"24:-Costa Rica")
    print(yellow,"25:-Poland")
    print(red,"26:-Colombia")
    print(green,"27:-Belarus")
    print(yellow,"28:-india")
    print(cya,"29:-Tunisia")
    print(bold,"30:-Albania")
    print(cya,"31:-Norway")
    print(green,"32:-Estonia")
    print(red,"33:-Liechtenstein")
    print(cya,"34:-domania")
    print(yellow,"35:-Dominican Republic")
    print(cya,"36:-Bosnia And Herzegovia")
    print(green,"37:-Viet Nam")
    print(red,"38:-Sloveania")
    print(cya,"39:-Paraguay")
    print(yellow,"40:-Belgium")
    print(cya,"41:-Ecuador")
    print(green,"42:-Philippines")
    print(red,"43:-Brazil")
    print(cya,"44:-Lithuania")
    print(yellow,"45:-Faroe Islands")
    print(red,"46:-Bulgaria")
    print(green,"47:-Palestinian")
    print(yellow,"48:-Guatemala")
    print(cya,"49:-Indonesia")
    print(bold,"50:-New Zealand")
    print(cya,"51:-Nepal")
    print(green,"52:-Bangladeh")
    print(red,"53:-denmark")
    print(cya,"54:-peru")
    print(yellow,"55:-Argentina")
		    
    try:
     print()
     countries3= ["MX", "FI", "CN", "CL", "ZA", "SK", "HU", "IE", "EG", "TH",
                 "UA", "RS", "HK", "GR", "PT", "LV", "SG", "IS", "MY", "CO",
                 "TN", "EE", "DO", "SI", "EC", "LT", "PS", "NZ", "BD", "PA",
                 "MD", "NI", "MT", "IT", "SA", "HR", "CY", "PK", "AE", "KZ",
                 "KW", "VE", "GE", "ME", "SV", "LU", "CW", "PR", "CR", "BY",
                 "AL", "LI", "BA", "PY", "PH", "FO", "GT", "NP", "PE", "UY","-"]
     headers= {"User-Agent": "Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0"}
     num= int(input("Choose Country: "))
     if num not in range(1, 55+1):
      raise IndexError
     country = countries3[num-1]
     res= requests.get(f"https://www.insecam.org/en/bycountry/{country}", headers=headers)
     last_page3= re.findall(r'pagenavigator\("\?page=", (\d+)', res.text)[0]

     for page in range(int(last_page3)):
       res= requests.get(f"https://www.insecam.org/en/bycountry/{country}/?page={page}",headers=headers)
       find_ip = re.findall(r"http://\d+.\d+.\d+.\d+:\d+", res.text)
       for ip in find_ip:
         print('\033[096m',"CCTV IP HACKED==>","\033[92m",'\033[01m',ip,green,"ACCESS GRANTED")		      
			
    except:
      pass
    finally:
      print("\033[1;37m")
      exit()
elif cho=="2":
	os.system("clear")
	os.system("figlet U-danbaiwa")
	print("please wait...")
	os.system("cd /data/data/com.termux/files/home")
	os.system("pkg update -y")
	os.system("pkg install -y git")
	os.system("pkg install python2")
	os.system("cd /data/data/com.termux/files/home && git clone https://github.com/U-danbaiwa/cctv-hacking.git")
	os.system("cd /data/data/com.termux/files/home")
	print(cya+"\t=====COMPLETE INSTALL THANK YOU=====")
if cho=="3":
   time.sleep(3)
   print(red,"see you letter!!!")
   os.system("exit")
else:
   print("Wrong Command")
   


