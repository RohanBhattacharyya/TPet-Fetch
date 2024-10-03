#compile using github actions
from colorama import Fore, Back, Style
import sys
import shutil
import re
import json
import platform
import socket
import cpuinfo
import wcwidth
import os
n = len(sys.argv)
import random
import datetime
# ANSI escape sequences regex pattern
ansi_escape = re.compile(r'\x1b\[([0-9]+)(;[0-9]+)*m')


total_memory, used_memory, free_memory = map(
    int, os.popen('free -t -m').readlines()[-1].split()[1:])
path_to_check = "/"
storage = shutil.disk_usage(path_to_check)


hunger_thresh = 600
bedtime = 21
try:
    f = open('~/tpdata.json',"r")
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









def preprocess_line(line: str, term_width: int) -> str:
    visible_length = 0
    result = ""
    i = 0
    
    while i < len(line):
        # Check for ANSI escape sequences
        match = ansi_escape.match(line, i)
        if match:
            # Append the entire ANSI sequence to the result
            result += match.group(0)
            # Skip the entire ANSI sequence
            i = match.end()
        else:
            # Get the character width using wcwidth
            char_width = wcwidth.wcwidth(line[i])
            
            # If adding this character exceeds terminal width, break
            if visible_length + char_width > term_width:
                break
            
            # Add the character to the result
            result += line[i]
            # Increment visible length by the width of the character
            visible_length += char_width
            i += 1
    
    return result

def printl(text: str):
    # Get the width of the terminal window
    term_width = shutil.get_terminal_size().columns
    
    # Split the text into lines
    lines = text.splitlines()
    
    for line in lines:
        # Preprocess the line to fit the terminal width
        processed_line = preprocess_line(line, term_width)
        # Print the truncated line
        print(processed_line+Style.RESET_ALL)

# Example complex usage


# Sample data functions for testing
def get_sys_icon()->str:

    system = platform.freedesktop_os_release()['ID']
    # printl(system)
    match system:
        case "debian":
            return '\uf306'.encode('utf-16', 'surrogatepass').decode('utf-16')
        case "fedora":
            return '\uf30a'.encode('utf-16', 'surrogatepass').decode('utf-16')
        case "arch":
            return '\udb82\udcc7'.encode('utf-16', 'surrogatepass').decode('utf-16')
        case _:
            return '\udb80\udf79'.encode('utf-16', 'surrogatepass').decode('utf-16')

responses = ["*sigh* bored","hmm...","stop wurking","play wif me pwease","*content*","huh","well well well","hello there","hi","wsp","*cough*","r u gonna do something?","im your only frend","...","u shuld touch grass"]
sleeping_responses = ["ZZZ","*dreams of sneks*","don't distrub *snores*","*yawn* go to slep pls"]
hungry_responses = ["fuud...","give foods","nibbles pls?","sneks","-snack","im hungry","could you bring sneks?","i'd like to eat pls"]
snack_responses = ["MMM!","tanks!","yumm!","more...?","SNECKS!","*burp*","you bring sneks? gud!"]
full_responses = ["can't eat..", "too ful","pls no more...","im done","*spits out*"]
line1 = f"{Style.BRIGHT}{Fore.YELLOW}{os.getlogin()}{Fore.RED}@{Fore.BLUE}{socket.gethostname()}{Style.RESET_ALL}"
line2 = f"{Style.BRIGHT}{Fore.MAGENTA}{get_sys_icon()}{Style.RESET_ALL}  {Fore.GREEN}{platform.freedesktop_os_release()['NAME']}{Style.RESET_ALL}"
line3 = f"{Style.BRIGHT}{Fore.MAGENTA}{'\uf0f4'.encode('utf-16', 'surrogatepass').decode('utf-16')}{Style.RESET_ALL}  {Fore.GREEN}{os.popen('uptime -p').read()[:-1]}{Style.RESET_ALL}"
line4 = f"{Style.BRIGHT}{Fore.MAGENTA}{'\uf4bc'.encode('utf-16', 'surrogatepass').decode('utf-16')}{Style.RESET_ALL}  {Fore.GREEN}{cpuinfo.get_cpu_info()['brand_raw']}{Style.RESET_ALL}"
line5 = f"{Style.BRIGHT}{Fore.MAGENTA}{'\uefc5'.encode('utf-16', 'surrogatepass').decode('utf-16')}{Style.RESET_ALL}  {Fore.GREEN}{round((used_memory/total_memory) * 100, 2)}% ( {round(used_memory/1000,1)} GB / {round(free_memory/1000,1)} GB )"
line6 = f"{Style.BRIGHT}{Fore.MAGENTA}{'\uf0c7'.encode('utf-16', 'surrogatepass').decode('utf-16')}{Style.RESET_ALL}  {Fore.GREEN}{round((storage[1]/storage[0])*100,2)}% ( {round(storage[1]/1000000000,1)} GB / {round(storage[0]/1000000000,1)} GB )"
if len(sys.argv)>=2:

    if sys.argv[1]=="-display" and len(sys.argv)==2:
        if sleep_check():
            printl(f"""
             {line1}
   {Fore.MAGENTA}(\\{Style.RESET_ALL}__{Fore.MAGENTA}/){Style.RESET_ALL}     {line2}
   ( -_-)     {line3}
   / > >\\     {line4}
              {line5}
              {line6}

   {Style.BRIGHT}{sleeping_responses[random.randint(0,len(sleeping_responses)-1)]}
            """)
        elif hunger_check():
            printl(f"""
             {line1}
   {Fore.MAGENTA}(\\{Style.RESET_ALL}__{Fore.MAGENTA}/){Style.RESET_ALL}     {line2}
   ( o_o)     {line3}
   / > <\\     {line4}
              {line5}
              {line6}

   {Style.BRIGHT}{hungry_responses[random.randint(0,len(hungry_responses)-1)]}
                """)
        else:
            printl(f"""
             {line1}
   {Fore.MAGENTA}(\\{Style.RESET_ALL}__{Fore.MAGENTA}/){Style.RESET_ALL}     {line2}
   ( ._.)     {line3}
   / > <\\     {line4}
              {line5}
              {line6}

   {Style.BRIGHT}{responses[random.randint(0,len(responses)-1)]}
                """)

    elif sys.argv[1]=="-snack" and len(sys.argv)==2:
        if sleep_check():
            printl(f"""
             {line1}
   {Fore.MAGENTA}(\\{Style.RESET_ALL}__{Fore.MAGENTA}/){Style.RESET_ALL}     {line2}
   ( -_-)     {line3}
   / > >\\     {line4}
              {line5}
              {line6}

   {Style.BRIGHT}{sleeping_responses[random.randint(0,len(sleeping_responses)-1)]}
                """)
        elif hunger_check():
            printl(f"""
             {line1}
   {Fore.MAGENTA}(\\{Style.RESET_ALL}__{Fore.MAGENTA}/){Style.RESET_ALL}     {line2}
   ( ^_^)     {line3}
   / > <\\     {line4}
              {line5}
              {line6}

   {Style.BRIGHT}{snack_responses[random.randint(0,len(snack_responses)-1)]}
                """)
            feed()
        else:
            printl(f"""
             {line1}
   {Fore.MAGENTA}(\\{Style.RESET_ALL}__{Fore.MAGENTA}/){Style.RESET_ALL}     {line2}
   ( {Fore.GREEN}@_@{Style.RESET_ALL})     {line3}
   / > <\\     {line4}
              {line5}
              {line6}

   {Style.BRIGHT}{full_responses[random.randint(0,len(full_responses)-1)]}
                """)
    else:
        help()
else:
    help()
f = open("~/tpdata.json","w")
f.write(json.dumps(stats, indent = 4))
f.close()
