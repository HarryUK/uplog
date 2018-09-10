import requests
import platform
import time
import datetime
import os

try:
    if platform == 'win32':
        def clearer():
            os.system('cls')
    else:
        def clearer():
            os.system('clear')

    iph = ''
    timeout = ''
    checker = ''
    while iph == '':
        clearer()
        iph = input('URL/IP (including http/https): ')
        iph = iph.lower()

    while checker == '' or checker != '1' and checker != '2':
        clearer()
        checker = input('Would you like outputs to be storred in a local text file?\n1) Yes\n2) No\nAnswer: ')

    while timeout == '' or timeout < 1:
        clearer()
        print('Your URL: ' + iph)
        if checker == '1':
            print('Log outputs are enabled')
        else:
            print('Log outputs are disabled')
        print('Reminder: Timeout must be 1 second or more')
        timeout = int(input('Timeout (seconds): '))



    def ready():
        clearer()
        if checker == '1':
            choutput = ' and we will place the outputs into files:\nDowntime: down.log\nUptime: up.log\n'
        else:
            choutput = ' and won\'t log the outputs into a file'
        print('Right, we will now start checking if ' + iph + ' is up every ' + str(timeout) + ' second/s' + choutput)
        time.sleep(2.5)
        print('3')
        time.sleep(1)
        print('2')
        time.sleep(1)
        print('1')
        time.sleep(1)
        print('Started')

    ready()


    def check():
        # We've started
        clearer()
        print('UpLog\nv0.1.0\nMade by Harry Chris\nResponses:')
        while True:
            r = requests.get(iph, timeout = timeout)
            time.sleep(timeout)
            if r.status_code == 200:
                print(iph + ' is running well :) // AT: ' + str(datetime.datetime.now()))
                if checker == '1':
                    print('This has been put into up.log\n')
                    with open('up.log', 'a') as myfile:
                        myfile.write(iph + '  was running well at: ' + str(datetime.datetime.now()) + '\n')
            else:
                print(iph + ' HAS FAILED :(! // AT: ' + str(datetime.datetime.now()))
                if checker == '1':
                    print('This has been put into down.log\n')
                    with open('down.log', 'a') as myfile:
                        myfile.write(iph + '  FAILED AT: ' + str(datetime.datetime.now()) + '\n')
    check()

except KeyboardInterrupt:
    clearer()
    print('Thanks for using UpLog!')
    print('If you enjoyed using UpLog please remember to give me good feedback')
    print('as it really does help :)')
    print('https://github.com/harryuk/uplog/')
    exit()

else:
    print('Unknown error occurred, please send me information of what you were doing when this error happened:')
    print('hcarrigan59@gmail.com')
    exit()
