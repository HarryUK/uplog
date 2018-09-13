import requests
import platform
import time
import datetime
import os

ex = requests.exceptions
try:

    if platform == 'win32':
        def clearer():
            os.system('cls')
    else:
        def clearer():
            os.system('clear')
    iph = ''
    tout = ''
    checker = ''
    while iph == '':
        clearer()
        iph = input('URL/IP (including http/https): ')
        iph = iph.lower()

    while checker == '' or checker != '1' and checker != '2':
        clearer()
        checker = input('Would you like outputs to be storred in a local text file?\n1) Yes\n2) No\nAnswer: ')

    while tout == '' or tout < 1:
        clearer()
        print('Your URL: ' + iph)
        if checker == '1':
            print('Log outputs are enabled')
        else:
            print('Log outputs are disabled')
        print('Reminder: Timeout must be 1 second or more')
        tout = int(input('Timeout (seconds): '))



    def ready():
        clearer()
        if checker == '1':
            choutput = ' and we will place the outputs into files:\nDowntime: down.log\nUptime: up.log\n'
        else:
            choutput = ' and won\'t log the outputs into a file'
        print('Right, we will now start checking if ' + iph + ' is up every ' + str(tout) + ' second/s' + choutput)
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
            r = requests.get(iph, timeout = tout)
            time.sleep(tout)
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
    print('You\'ve now exited UpLog')
    print('Thanks for using UpLog!')
    print('If you enjoyed using UpLog please remember to give me good feedback')
    print('as it really does help :)')
    print('https://github.com/harryuk/uplog/')
    exit()

except (ex.MissingSchema, ex.InvalidSchema):
    clearer()
    print('You forgot the schema or inserted an invalid schema, Use http:// or https:// in front of your URL')
    exit()

except ex.NewConnectionError:
    clearer()
    print('Could not connect to address')
    print('Remember http:// or http:// in front of your URL')
    exit()

except ex.InvalidURL:
    clearer()
    print('Your URL was invalid')
    print('If you used an IPv6 address remember to wrap it in [] for example:')
    print('https://[1111:1111:1:1111:1111:1111:1111:1111]')
    exit()

except ex.TooManyRedirects:
    clearer()
    print('You were redirected too many times')
    exit()

except ex.InvalidHeader:
    clearer()
    print('')
    exit()

except (ex.Timeout, ex.ReadTimeout):
    clearer()
    print('A timeout occurred, this meant the site didn\'t respond in the time you set.')

except:
    clearer()
    print('Unknown error occurred, please send me information of what you were doing when this error happened:')
    print('hcarrigan59@gmail.com')
    exit()

else:
    clearer()
    print('Unknown error occurred, please send me information of what you were doing when this error happened:')
    print('hcarrigan59@gmail.com')
    exit()
