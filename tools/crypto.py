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

# load token
def load_token_with_password(key=None):
    if not key:
        key = getpass.getpass('Password: ')
    with open(BASE_DIR / 'data' / 'key', 'r') as f:
        hash = f.read()
    if hash_password(key) != hash:
        print('Wrong password')
        sys.exit(1)
    else:
        with open(BASE_DIR / 'data' / 'token', 'r') as f:
            token = f.read()
        return xor(token, key)
    

def load_token_without_password():
    with open(BASE_DIR / 'data' / 'token', 'r') as f:
        return f.read()


def setup_with_password(token: str):
    password = input('Password: ')
    
    xored_token = xor(token, password)

    with open(BASE_DIR / 'data' / 'token', 'w') as f:
        f.write(xored_token)

    with open(BASE_DIR / 'data' / 'key', 'w') as f:
        f.write(hash_password(password))
    
    # test
    print("Testing encryption. Enter your password, you should see the correct token.")
    print(load_token_with_password())
    print("Token saved. You should now be able to run the bot with password.")
    

    MNGR["config"]["password"] = "yes"
    MNGR.save()


def setup_without_password(token: str):
    with open(BASE_DIR / 'data' / 'token', 'w') as f:
        f.write(token)

    print("Token saved. You should now be able to run the bot without password.")

    MNGR["config"]["password"] = "no"
    MNGR.save()


def setup():
    token = input('token: ')

    choice = input('Do you want to use a password? [y/n] (default: y) :')
    if choice.lower()[0] == 'n':
        print("Setting up without password.")
        setup_without_password(token)
    else:
        print("Setting up with password.")
        setup_with_password(token)



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


