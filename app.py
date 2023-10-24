
command = ''
car_status = 'stop'

while command != 'quit':
    command = input(' ').lower()
    if command == 'help':
        print('''
            start - to start the car
            stop - to stop the car
            quit - to exit
        ''')
    elif command == 'start':
        print('Car started - ready to go')
    elif command =='stop' and car_status != 'stop':
        print('Car stopped')
    else:
        print('Invalid command')
else:
    print('Bye')
