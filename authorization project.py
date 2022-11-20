logins = ['aziz']
passwords = ['Fall2022']
try_count = 5

enter = input("Log in or Registration: ").capitalize()
while enter != "Registration" and enter != "Log in":
    enter = input('Enter only "Registration" or "Log in": ').capitalize()
if enter == 'Registration':
    login = input('Create login: ')
    while login in logins:
        login = input('Login is already taken, try another one: ')
    logins.append(login)
    password = input('Create password: ')
    while len(password) < 8:
        password = input('Too short password. Password should be min 8 symbols: ')
    countchar = 0
    countnum = 0
    for i in password:
        if i.isalpha():
            countchar += 1
        elif i.isdigit():
            countnum += 1
    while countchar == 0 or countnum == 0:
        password = input('Password should consist of letters and digits: ')
        countchar = 0
        countnum = 0
        for i in password:
            if i.isalpha():
                countchar += 1
            elif i.isdigit():
                countnum += 1
            while len(password) < 8:
                password = input('Too short password. Password should be min 8 symbols: ')
    passwords.append(password)
    print("Congratulations! You've logged in successfully!")
elif enter == 'Log in':
    login = input('Enter your login: ')
    while login not in logins:
        login = input('Login does not exist. Re-enter, please: ')
    password = input('Enter your password: ')
    while password != passwords[logins.index(login)]:
        password = input('Incorrect password. Re-enter your password, please: ')
        try_count -= 1
        if try_count == 0:
            print("You have no attempts  left, try logging in later")
    print(f'Welcome {login}!')