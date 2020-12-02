import os, requests, sys, time, timeit
from threading import Thread
from colorama import init, Fore; init()

token = 'input github token here'

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
            if len(name) > 4 and response.status_code == 404:
                print(f'{Fore.GREEN}--> %s Available <--' % name)
                with open('useable.txt', 'a') as w:
                    w.write(f'{name} \n')
            else:                                               
                print(f'{Fore.RED}--> %s Unvailable <--' % name)
        except Exception:
            KeyboardInterrupt()
            print("Problem Occured")

print('|...|')
time.sleep(2)
print('|.....|')
time.sleep(2)
print('|.......|')
time.sleep(2)

threads = []

for i in range(thread_count):
    threads.append(Thread(target=check,args=[flow(name)[i]])) 
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

print('Check Done!')

sys.exit()







