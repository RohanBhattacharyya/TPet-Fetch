from colorama import Fore, Back, Style
import sys
import json
import platform
import socket
import os
n = len(sys.argv)
import random
import datetime


responses = ["*sigh* bored","hmm...","stop wurking","play wif me pwease","*content*","huh","well well well","hello there","hi","wsp","*cough*","r u gonna do something?","im your only frend","...","u shuld touch grass"]
sleeping_responses = ["ZZZ","*dreams of sneks*","don't distrub *snores*","*yawn* go to slep pls"]
hungry_responses = ["fuud...","give foods","nibbles pls?","sneks","-snack","im hungry","could you bring sneks?","i'd like to eat pls"]
snack_responses = ["MMM!","tanks!","yumm!","more...?","SNECKS!","*burp*","you bring sneks? gud!"]
full_responses = ["can't eat..", "too ful","pls no more...","im done","*spits out*"]
hunger_thresh = 600
bedtime = 21
try:
	f = open('data.json',"r")
	content = f.read()
	f.close()
except:
	content = ""



if content:
	stats = json.loads(content)
else:	
	# print("File is empty")
	stats = {

		"hungry": False,
		"timewhenlastfed": datetime.datetime.now().timestamp(),
		"is_sleeping": False
	}

def get_sys_icon()->str:

	system = platform.freedesktop_os_release()['ID']
	# print(system)
	match system:
		case "debian":
			return '\uf306'.encode('utf-16', 'surrogatepass').decode('utf-16')
		case "fedora":
			return '\uf30a'.encode('utf-16', 'surrogatepass').decode('utf-16')
		case "arch":
			return '\udb82\udcc7'.encode('utf-16', 'surrogatepass').decode('utf-16')
		case _:
			return '\udb80\udf79'.encode('utf-16', 'surrogatepass').decode('utf-16')

	
# print(stats)

def help()->None:
	print(f"""
		{Style.BRIGHT}Usage:{Style.RESET_ALL}
		 -display: Shows pet in terminal
		 -snack: Gives pet snack
		""")
def hunger_check()->bool:
	if stats["hungry"]==False and datetime.datetime.now().timestamp()-stats["timewhenlastfed"]>=hunger_thresh:
		stats["hungry"]=True
	return stats["hungry"]
def sleep_check()->bool:
	if int(datetime.datetime.now().strftime("%H"))>=bedtime:
		return True
	else:
		return False
def feed()->None:
	if stats["hungry"]==True:
		stats["hungry"]=False
		stats["timewhenlastfed"]=datetime.datetime.now().timestamp()

line1 = f"{Style.BRIGHT}{Fore.YELLOW}{os.getlogin()}{Fore.RED}@{Fore.BLUE}{socket.gethostname()}{Style.RESET_ALL}"
line2 = f"{Style.BRIGHT}{Fore.MAGENTA}{get_sys_icon()}{Style.RESET_ALL}  {Fore.GREEN}{platform.freedesktop_os_release()['NAME']}{Style.RESET_ALL}"
line3 = f"{Style.BRIGHT}{Fore.MAGENTA}{'\uf0f4'.encode('utf-16', 'surrogatepass').decode('utf-16')}{Style.RESET_ALL}  {Fore.GREEN}{os.popen('uptime -p').read()[:-1]}{Style.RESET_ALL}"

if len(sys.argv)>=2:

	if sys.argv[1]=="-display" and len(sys.argv)==2:
		if sleep_check():
			print(f"""
   {Fore.MAGENTA}(\\{Style.RESET_ALL}__{Fore.MAGENTA}/){Style.RESET_ALL}	{line1}
   ( -_-)	{line2}
   / > >\\	{line3}

   {Style.BRIGHT}{sleeping_responses[random.randint(0,len(sleeping_responses)-1)]}
			""")
		elif hunger_check():
			print(f"""
   {Fore.MAGENTA}(\\{Style.RESET_ALL}__{Fore.MAGENTA}/){Style.RESET_ALL}	{line1}
   ( o_o)	{line2}
   / > <\\	{line3}

   {Style.BRIGHT}{hungry_responses[random.randint(0,len(hungry_responses)-1)]}
				""")
		else:
			print(f"""
   {Fore.MAGENTA}(\\{Style.RESET_ALL}__{Fore.MAGENTA}/){Style.RESET_ALL}	{line1}
   ( ._.)	{line2}
   / > <\\	{line3}

   {Style.BRIGHT}{responses[random.randint(0,len(responses)-1)]}
				""")

	elif sys.argv[1]=="-snack" and len(sys.argv)==2:
		if sleep_check():
			print(f"""
   {Fore.MAGENTA}(\\{Style.RESET_ALL}__{Fore.MAGENTA}/){Style.RESET_ALL}	{line1}
   ( -_-)	{line2}
   / > >\\	{line3}

   {Style.BRIGHT}{sleeping_responses[random.randint(0,len(sleeping_responses)-1)]}
				""")
		elif hunger_check():
			print(f"""
   {Fore.MAGENTA}(\\{Style.RESET_ALL}__{Fore.MAGENTA}/){Style.RESET_ALL}	{line1}
   ( ^_^)	{line2}
   / > <\\	{line3}

   {Style.BRIGHT}{snack_responses[random.randint(0,len(snack_responses)-1)]}
				""")
			feed()
		else:
			print(f"""
   {Fore.MAGENTA}(\\{Style.RESET_ALL}__{Fore.MAGENTA}/){Style.RESET_ALL}	{line1}
   ( {Fore.GREEN}@_@{Style.RESET_ALL})	{line2}
   / > <\\	{line3}

   {Style.BRIGHT}{full_responses[random.randint(0,len(full_responses)-1)]}
				""")
	else:
		help()
else:
	help()
f = open("data.json","w")
f.write(json.dumps(stats, indent = 4))
f.close()
# print(stats)
# print(datetime.datetime.now().timestamp())