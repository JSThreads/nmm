import os
import sys

# Files organisation
# etc/nmm
# |-- nmm.py
# |-- config.json
# |-- /nginx-x.y.z
# |-- /modules

# Compilation steps
# Depencencies
# apt install -y build-essential
# apt install -y libpcre3 libpcre3-dev
# apt install -y zlib1g zlib1g-dev
# apt install -y wget unzip tar

# OpenSSL
# wget https://www.openssl.org/source/openssl-1.1.1c.tar.gz --directory-prefix /etc/openssl
# tar -xf /etc/openssl/openssl-1.1.1c.tar.gz -C /etc/openssl
# rm /etc/openssl/openssl-1.1.1c.tar.gz
# cd /etc/openssl/openssl-1.1.1c && ./config --prefix=/usr/local/ssl --openssldir=/usr/local/ssl shared zlib && make && make test && make install && cd /

# ============ # TEST # ============#

# Work directory : /usr/lib/nmm
#
# ================================= #
#         Update deb packages
# ================================= #
# Sources: 
# https://www.nginx.com/blog/harnessing-power-convenience-of-javascript-for-each-request-with-nginx-javascript-module#njs-oss-load%22
# https://onelinerhub.com/nginx/install-njs-nginx-javascript-module
""" 
apt install -y curl gnupg2 ca-certificates lsb-release debian-archive-keyring
curl https://nginx.org/keys/nginx_signing.key | gpg --dearmor | tee /usr/share/keyrings/nginx-archive-keyring.gpg >/dev/null
echo "deb [signed-by=/usr/share/keyrings/nginx-archive-keyring.gpg] http://nginx.org/packages/ubuntu `lsb_release -cs` nginx" | tee /etc/apt/sources.list.d/nginx.list
apt update
apt install -y nginx-module-njs
"""
# After the installation those lines need to be added to: /etc/nginx/nginx.conf
"""
load_module modules/ngx_http_js_module.so;
load_module modules/ngx_stream_js_module.so;
"""
# Finally reopen it and reload
"""
service nginx start
nginx -s reload
"""

# ============ # TEST # ============#

# Has to be run with admin permissions
os.system('apt update')
os.system('apt-get update')

# NMM
os.system('apt install -y build-essential')
os.system('apt install -y libpcre3 libpcre3-dev')
os.system('apt install -y zlib1g zlib1g-dev')
os.system('mkdir /etc/nmm')

if '--includes' in sys.argv:
    # nginx
    os.system('apt install -y wget systemctl')

if '--latest-nginx' in sys.argv:
    # change focal to bionic if ubuntu is < 20.04 
    os.system('echo \'deb [arch=amd64] http://nginx.org/packages/mainline/ubuntu/ focal nginx\ndeb-src http://nginx.org/packages/mainline/ubuntu/ focal nginx\' > /etc/apt/sources.list.d/nginx.list')

    # update signature
    os.system('wget http://nginx.org/keys/nginx_signing.key')
    os.system('apt-key add nginx_signing.key')

    # remove old nginx
    os.system('apt remove nginx nginx-common nginx-full nginx-core')

    # backup nginx configuration
    os.system('cp /etc/nginx/nginx.conf /etc/nginx/nginx.conf.bak')

    # install nginx
    os.system('apt install -y nginx')
elif '--install-nginx' in sys.argv:
    os.system('apt-get install -y nginx')

if '--add-service' in sys.argv:
    os.system('nginx -t')
    os.system('systemctl start nginx')
    os.system('systemctl enable nginx')
    os.system('systemctl status nginx')

