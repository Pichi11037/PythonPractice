from domain.User import User
from service.UserDAO import UserDAO
from logger_base import log

count = 0

while count == 0:
    option = input(
        '''
Menu:
1) Add user
2) List users
3) Update user
4) Delete user
5) Exit
'''
    )
    if option == '1':
        username = input('Username: ')
        pw1 = input('Password: ')
        pw2 = input('Confirm password: ')

        if pw1 == pw2:
            confirm = input(f'''Check data. Confirm? (y/n)
    Username: {username},
    password: {pw1}
    ''')
            
            if confirm.capitalize() == 'Y':
                newUser = User(username=username, password=pw1)
                insertUser = UserDAO.insert(newUser)
                log.debug(f'Users inserted: {insertUser}')
            else:
                log.debug('Insert cancelled...')

        else:
            log.error("Passwords don't match...")
            continue

    elif option == '2':
        for user in UserDAO.select():
            log.debug(user)
        
    elif option == '3':
        nId = input('Provide the id of the user you want to update: ')
        nUsername = input('New username: ')
        nPw1 = input('New password: ')
        nPw2 = input('Confirm new Password: ')

        if nPw1 == nPw2:
            updatedUser = User(id=nId, username=nUsername, password=nPw1)
            userUpdated = UserDAO.update(updatedUser)
            log.debug(f'Users updated: {userUpdated}')
        else:
            log.error("Passwords don't match...")
            continue
        
    elif option == '4':
        nId = input('Provide the ID of the user you want to delete: ')
        deletedUser = User(id=nId, username='', password='')
        userDeleted = UserDAO.delete(deletedUser)
        log.debug(f'Users deleted: {userDeleted}')
    elif option == '5':
        count = 1
    else:
        continue