
users = {}
status = ""

def displayMenu():
    newstatus = input("Are you registered user? y/n?: ")
    if newstatus == 'y':
        oldUser()
    elif newstatus == 'n':
        newUser()
    else:
        pass

def newUser():
    createLogin = input('Create log in name: ')

    if createLogin in users:
        print('\nLogin name already exist!\n')

    else:
        createPassw = input('Create new password: ')
        users[createLogin] = createPassw
        print('\nUser created\n')

def oldUser():
    login = input('Enter your login name: ')
    passw = input('Enter your password: ')

    if login in users and users[login] == passw:
        print('\nLogin successful!\n')

    else:
        print("\nUser doesn't exist or wrong password!\n")

while status != 'q':
    displayMenu()