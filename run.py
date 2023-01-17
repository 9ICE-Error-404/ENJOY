import os, platform, time

os.system('clear')

try:

    import requests

except:

    os.system('pip install requests')

os.system('git pull')

import requests

bit = platform.architecture()[0]

if bit == '64bit':

    print("\n\x1b[1;92m Congratulations ! Your Device Supported Tool")

    from BTC_SPD import main

    main()

elif bit == '32bit':

    print("\x1b[1;92m Your Mobile Not Supported This Tool")
