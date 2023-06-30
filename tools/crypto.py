import hashlib
import getpass
import sys
import os
import platform

from core.config import BASE_DIR, MNGR

# hash password
def hash_password(password):
    for _ in range(len(password)):
        password = hashlib.sha256(password.encode('utf-8')).hexdigest()
    return password

# string xor
def xor(target, key):
    long_list = [ord(c) for c in target]
    short_list = [ord(c) for c in key]

    repeated_short_list = (short_list * (len(long_list) // len(short_list))) + short_list[:len(long_list) % len(short_list)]

    xor_result = [a ^ b for a, b in zip(long_list, repeated_short_list)]

    return ''.join(chr(c) for c in xor_result)

# load flag
def load_flag_with_password(key=None):
    if not key:
        key = getpass.getpass('Password: ')
    with open(BASE_DIR / 'data' / 'key', 'r') as f:
        hash = f.read()
    if hash_password(key) != hash:
        print('Wrong password')
        sys.exit(1)
    else:
        with open(BASE_DIR / 'data' / 'token', 'r') as f:
            flag = f.read()
        return xor(flag, key)
    

def load_flag_without_password():
    with open(BASE_DIR / 'data' / 'token', 'r') as f:
        return f.read()


def setup_with_password(flag: str):
    password = input('Password: ')
    
    xored_flag = xor(flag, password)

    with open(BASE_DIR / 'data' / 'token', 'w') as f:
        f.write(xored_flag)

    with open(BASE_DIR / 'data' / 'key', 'w') as f:
        f.write(hash_password(password))
    
    # test
    print("Testing encryption. Enter your password, and you should see the flag.")
    print(load_flag_with_password())
    input("Press enter to continue.")
    os.system("cls" if platform.system() == "Windows" else "clear")

    MNGR["config"]["password"] = "yes"


def setup_without_password(flag: str):
    with open(BASE_DIR / 'data' / 'token', 'w') as f:
        f.write(flag)
    
    # test
    print("Testing setup. You should see the flag.")
    print(open(BASE_DIR / 'data' / 'token', 'r').read())
    input("Press enter to continue.")
    os.system("cls" if platform.system() == "Windows" else "clear")

    MNGR["config"]["password"] = "no"


def setup():
    flag = input('Flag: ')

    choice = input('Do you want to use a password? [y/n] (default: y) :')
    if choice.lower()[0] == 'n':
        setup_without_password(flag)
    else:
        setup_with_password(flag)



def test_password(password=None):
    if not password:
        password = input('Password: ')
    with open(BASE_DIR / 'data' / 'key', 'r') as f:
        hash = f.read()
    if hash_password(password) != hash:
        print('Wrong password')
        sys.exit(1)
    else:
        print('Correct password')
        sys.exit(0)


