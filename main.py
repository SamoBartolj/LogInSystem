print('''Hello and welcome to SuperCoolProgram.
Beafore you continue you need to log in.
If you don have account please sign in.''')
signin_or_login = input('Type log in or sign in: ')


if signin_or_login == 'sign in':
    username = input('Enter your username: ')
    email = input('Enter your email: \n')
    password1 = input('Enter your password: \n')
    password2 = input('Enter your password again: \n')
    informations = [username, email, password1]

    if password1 == password2:
        text_file = open("Accounts.text", "w")
        text_file.writelines(informations)
        text_file.close()
        print('You successfully created an account.')


else:
    pass


if signin_or_login == 'log in':
    print('yao')

else:
    print('haoo')