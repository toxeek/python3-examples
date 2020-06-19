#!/usr/bin/env python3
#- * -coding: utf - 8 - * -#

# USAGE: python3 chk-connectivity.py
#
# it will check some urls passed in a listm that we yield from,
# some are unresilvable domains, others are, all in the outputs
#


import urllib.request
import urllib.error
import re
import time

__version__ = '1.0.1'# Sem 

#globals
my_global_dict = dict()

# generator,for fun
def internet_conn(urls):
    yield from urls

urls = ["https://www.google.com", "https://aws.ajndfbmazon.com", "https://docs.python.org", "https://githukijajb.com"]

my_gen_urls = internet_conn(urls)
def check_conn(gen_list):
    ret_code = dict()
    for u in list(my_gen_urls):
        print(f"[+] checking connectivity to {u} ..")
        try: 
            ret_code[u] = urllib.request.urlopen(u, timeout = 3).getcode()
            if re.match("\d{3}", str(ret_code[u])):
                my_global_dict[u] = 'ok'
        except urllib.error.URLError as e:
            my_global_dict[u] = 'err'
            # print(f)
            print(f"[+] domain name {u} not resolvable, please check again the URL ...")
            pass
        except urllib.error.HTTPError as f:
            my_global_dict[u] = 'err'
            # print(e)
            print(f"[+] you may need auth to connect to {u}, or exotic HTTP error happened.. retry..")
            pass
    if 'ok' in my_global_dict.values() and 'err' in my_global_dict.values():
        print("[+] looks like we can connect to the Internet, but some url/s failed on resolution/connectivity")
        for k,v in my_global_dict.items():
            if 'err' in v:
                print(f"{k} : had connectivity/resolution problems.")                  
    elif 'err' not in my_global_dict.values():
        print("[+] we have connectivity to the Internet, no errors connecting or resolving urls ..")
    else:
        pass
if __name__ == '__main__':
    check_conn(my_gen_urls)
