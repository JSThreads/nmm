import os
import sys

if len(sys.argv) == 2 and (sys.argv[1] == 'install' or sys.argv[1] == 'i'):
    # Install dependences
    os.system('apt install wget')
    os.system('apt install tar')

    # Install Nginx
    os.system('wget https://nginx.org/download/nginx-1.11.5.tar.gz')
    os.system('tar -xzvf nginx-1.11.5.tar.gz')
    print(f'\u001b[32m✔ Successfully installed the dependencies\u001b[0m')
elif len(sys.argv) == 3 and (sys.argv[1] == 'install' or sys.argv[1] == 'i'):
    # install module 
    pass
elif len(sys.argv) == 3 and sys.argv[1] == 'uninstall':
    # uninstall module 
    pass
elif len(sys.argv) == 2 and sys.argv[1] == 'list':
    # list module 
    pass
elif len(sys.argv) > 1:
    print(f'\u001b[31m❌ The {sys.argv[1]} subcommand doesn\'t exists\u001b[0m')
else:
    print(f'\u001b[31m❌ You need to precise a subcommand\u001b[0m')
