from cryptography.fernet import Fernet

#for generating key:
'''def write_key():
        key = Fernet.generate_key()
            with open("key.key", "wb") as key_file:
                key_file.write(key)
# write_key()'''

#for reading password:
def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

master_pwd = input("Enter your master password: ")
key = load_key() + master_pwd.encode()
fer = Fernet(key)

def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user , passw = data.split("|")
            print("User:",user,"Password:",fer.decrypt(passw.encode()))

def add():
    username = input("Username: ")
    pwd = input("Password: ")
    
    with open('passwords.txt', 'a') as f:
        encypted_data = fer.encrypt(pwd.encode())
        f.write(username + "|" + encypted_data.decode() + "\n")




while True:
    mode = input("Want to add or view?(a/v)\nwant to quit?press q: ")
    if mode == "a":
        add()
    elif mode == "v":
        view()
    elif mode == "q":
        break
    else:
        print("Invalid mode!")
        continue