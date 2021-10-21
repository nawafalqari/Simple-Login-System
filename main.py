from pymongo import MongoClient
from bson.objectid import ObjectId


print('Welcome To My App')
print('If this is your first time here type "register", or "login" if you have an account')

url = '' # Mongo db url
client = MongoClient(url)
users_info = client.users.users_info

done = True

isLoggedIn = False
username = None
password = None
name = None

while done:
    command = input('> ').strip()

    if command.startswith(('quit', 'exit')):
        done = False
    elif command == 'register':
        if isLoggedIn == True:
            print('You can not use this command while you are logged in.')
        else:
            print('What is your name')
            name = input('Name: ')
            print()
            print('Enter a username')
            regUsername = input('username: ').strip()
            print()
            print('Enter a password')
            regPassword = input('password: ')
            print()
            if users_info.count_documents({'username': regUsername}) != 0:
                print('Username is already used, try different one')
            elif len(regPassword) < 3:
                print('Week password')
            else:
                users_info.insert_one({'name': name, 'username': regUsername, 'password': regPassword})
                print('You have registed sucessfully')
                print('login using "login" command')
    elif command == 'login':
        if isLoggedIn == True:
            print('You are already logged in')
            print('use "logout" command')
        else:
            loginUsrname = input('username: ')
            loginPassword = input('password: ')
            
            if loginUsrname == '' or loginPassword == '':
                print('Something is missing')
            else:
                result = users_info.find_one({'username': loginUsrname, 'password': loginPassword})
                
                if not result:
                    print('username or password is invalid')
                else:
                    isLoggedIn = True
                    username = result['username']
                    password = result['password']
                    name = result['name']

                    print()
                    print('Welcome {}'.format(result['name']))
                    print('You have logged in sucessfully')
        
    elif command == 'logout':
        if isLoggedIn == False:
            print('You are not logged in')
        else:
            logout = False
            while not logout:
                areusure = input('Are you sure? ("yes"/"no"): ').lower().strip()
                if areusure == 'yes':
                    isLoggedIn = False
                    username = None
                    password = None
                    name = None

                    logout = True
                elif areusure == 'no':
                    logout = True
                else:
                    print('invalid answer')

    elif command == 'what is my name':
        if isLoggedIn == False:
            print('You should login in first to use this command')
            print('To login use "login" command')
        else:
            print(name)
