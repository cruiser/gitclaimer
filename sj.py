import shutil, os, sys, requests, getpass, time
from os import system
from datetime import date
from threading import Thread
from colorama import init, Fore; init()


width = shutil.get_terminal_size().columns


def ui():
    print()
    print(f'                {Fore.MAGENTA}joker{Fore.MAGENTA}[{Fore.RED}DEV{Fore.MAGENTA}]'.center(width))
    print()
    print(f"                                    {Fore.GREEN}Created by {Fore.GREEN}e{Fore.YELLOW}m{Fore.CYAN}e{Fore.BLUE}r{Fore.RED}y{Fore.MAGENTA}{Fore.BLACK}#0831".center(width))

ui()

counter = 0
now = date.today()
user = str(getpass.getuser())

nope = False

def info():
    print()
    print(f"{Fore.CYAN}It is currently: {now} \n".center(width))
    print(f"You are currently logged in as: {user} \n".center(width))
    print()
    print(f'{Fore.YELLOW}This application is against Github TOS if used for monetary gain, I am not responsible for its use.'.center(width))
    print(f'            {Fore.YELLOW}Please wait while we {Fore.GREEN}CONNECT{Fore.YELLOW} you to the GITHUB servers'.center(width))
    
        
info()

time.sleep(5)
print('You can get your API key from https://github.com/settings/tokens/\n'.center(width))
print('Paste API Key into token.txt, if not a tragic malfunction will occur\n'.center(width))
time.sleep(3)

token = open('token.txt', 'r', encoding='UTF-8').read()

headers = {'Authorization': f'token {token}'}

thread_count = 50

name = open('names.txt', 'r', encoding='UTF-8').read().splitlines()


def flow(control):
    return[control[i::thread_count]for i in range(thread_count)] 

def check(names):
    for name in names:
        try:
            data = {'url': 'https://github.com/'}
            response = requests.get('https://github.com/%s' % name, headers=headers, json=data)
            if len(name) > 4 and response.status_code == 404: #only uses names with more than 4 characters, 404 means not found. If its not found, its not taken.
                print(f'{Fore.GREEN}--> {Fore.CYAN}%s {Fore.GREEN}Available <--' % name)
                with open('useable.txt', 'a') as w: #writes usernames that are available to this file
                    w.write(f'{name} \n')# ^
            else:                                               
                print(f'{Fore.RED}--> {Fore.CYAN}%s {Fore.RED}Unvailable <--' % name)
        except Exception:
            KeyboardInterrupt() #Ctrl + C
            print("Problem Occured")


threads = []

for i in range(thread_count):
    threads.append(Thread(target=check,args=[flow(name)[i]])) 
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

print(f'{Fore.BLUE}Check Done enjoy your names!\n')
print(f"{Fore.BLUE}Remember, there is a curse filter on github, all words used in the website wont be available, ex) {Fore.RED}input, code, method, admin, {Fore.BLUE}etc\n")

def remove():
    sad = input(f"{Fore.CYAN}Would you like me to clear your 'useable.txt' file? (y) or (n)").lower()
    if sad == 'y':
        file1 = open("useable.txt", 'r+')
        file1.truncate(0)
        file1.close()
        print(f'{Fore.BLUE}Clearing file...'.center(width))
        print(f'{Fore.BLUE} See me soon!'.center(width))
        time.sleep(1)
        sys.exit()
    else:
        pass
        

remove()

print()

def save():
    happy = input(f"{Fore.CYAN}Would you like me to copy your 'useable.txt' file to another file? (y) or (n) \n").lower()
    if happy == 'y':
        print(f'{Fore.BLUE}Copying file to copy.txt...'.center(width))
        shutil.copy2('useable.txt', 'copy.txt')
        print('Thank you for using Project Joker')
        time.sleep(2)
    else:
        print(f'{Fore.BLUE}See you soon {user}'.center(width))
        print(f'{Fore.BLUE}Thank you for using Project Joker'.center(width))
        time.sleep(4)
        sys.exit()

save()


    




