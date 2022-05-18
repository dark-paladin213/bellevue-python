import os 


def friends_0():
    filePath = '/Users/Corey/Documents/GitHub/bellevue-python/'
    fileName = 'friends.txt'
    completePath = filePath+fileName

    os.path.isfile(fileName) 
    os.path.isdir(filePath) 
    os.path.exists(completePath) 
    print('Complete Path',completePath)
    print('\n')

    name_0 = input('Name: ')
    phone_0 = input('Phone number: ')
    address_0 = input('Address: ')
    print('\n')
    with open(completePath, 'a') as fileHandle: 
        fileHandle.write(f'\nName:{name_0}, Phone number:{phone_0}, Adress:{address_0}')
    with open(completePath, 'r') as fileHandle: 
        data = fileHandle.read() 
        print(data)

def family_0():
    filePath = '/Users/Corey/Documents/GitHub/bellevue-python/'
    fileName = 'family.txt'
    completePath = filePath+fileName

    os.path.isfile(fileName) 
    os.path.isdir(filePath) 
    os.path.exists(completePath) 
    print('Complete Path',completePath)
    print('\n')

    name_0 = input('Name: ')
    phone_0 = input('Phone number: ')
    address_0 = input('Address: ')
    print('\n')
    with open(completePath, 'a') as fileHandle: 
        fileHandle.write(f'\nName:{name_0}, Phone number:{phone_0}, Adress:{address_0}')
    with open(completePath, 'r') as fileHandle: 
        data = fileHandle.read() 
        print(data)

def work_0():
    filePath = '/Users/Corey/Documents/GitHub/bellevue-python/'
    fileName = 'work.txt'
    completePath = filePath+fileName

    os.path.isfile(fileName) 
    os.path.isdir(filePath) 
    os.path.exists(completePath) 
    print('Complete Path',completePath)
    print('\n')

    name_0 = input('Name: ')
    phone_0 = input('Phone number: ')
    address_0 = input('Address: ')
    print('\n')
    with open(completePath, 'a') as fileHandle: 
        fileHandle.write(f'\nName:{name_0}, Phone number:{phone_0}, Adress:{address_0}')
    with open(completePath, 'r') as fileHandle: 
        data = fileHandle.read() 
        print(data)

def welcomestate():
    print('''\tHello you are going to add your name, address and phone\n\tto one of the three directories below\n''')
    directories = ['friends', 'family', 'work']
    for directory in directories:
        print(directory)
        print('\n')

def userinput():
    options = input('friends press 1, family press 2, work press 3: ')
    if options == '1':
        friends_0()
    elif options == '2':
        family_0()
    elif options == '3':
        work_0()
    else:
        print('Please press 1, 2 or 3')


addanother = 'yes'
while addanother == 'yes':
    welcomestate()
    userinput()
    
    print('Do you want to add another name? (yes or no)')
    addanother = input('yes/no: ')
    if addanother == 'yes':
        continue
    if addanother == 'no':
        print('Thank you.')
    else:
        print('Please type yes or no')
        addanother = input('yes/no: ')
    continue




