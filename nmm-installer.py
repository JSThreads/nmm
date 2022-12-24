import os
import sys

# Files organisation
# etc/nmm
# |-- nmm.py
# |-- config.json
# |-- /nginx-x.y.z
# |-- /modules

# Has to be run with admin permissions
os.system('apt update')
os.system('apt-get install -y nginx')
os.system('mkdir /etc/nmm')

if len(sys.argv) == 2 and sys.argv[1] == '--with-dep':
    # Install nginx dependencies
    # gcc make etc..
    os.system('apt install -y build-essential')
    # pcre library
    os.system('apt install -y libpcre3 libpcre3-dev')
    # zlib
    os.system('apt install -y zlib1g zlib1g-dev')

    # Installing wget to get other files
    os.system('apt install -y wget unzip tar')

    # OpenSSL
    os.system('wget https://www.openssl.org/source/openssl-1.1.1c.tar.gz --directory-prefix /etc/openssl')
    os.system('tar -xf /etc/openssl/openssl-1.1.1c.tar.gz -C /etc/openssl')
    os.system('rm /etc/openssl/openssl-1.1.1c.tar.gz')

    os.system('cd /etc/openssl/openssl-1.1.1c && ./config --prefix=/usr/local/ssl --openssldir=/usr/local/ssl shared zlib && make && make test && make install && cd /')

# Nginx source
# https://nginx.org/download/nginx-x.y.z

# Downloading the zip, extracting it and deleting the zip
# os.system('wget https://nginx.org/download/nginx-1.23.3.zip --directory-prefix /etc/nmm')
os.system('wget https://nginx.org/download/nginx-1.23.3.tar.gz --directory-prefix /etc/nmm')
# os.system('unzip /etc/nmm/nginx-1.23.3.zip -d /etc/nmm')
os.system('tar -xzvf /etc/nmm/nginx-1.23.3.tar.gz -C /etc/nmm')
# os.system('rm /etc/nmm/nginx-1.23.3.zip')
os.system('rm /etc/nmm/nginx-1.23.3.tar.gz')
