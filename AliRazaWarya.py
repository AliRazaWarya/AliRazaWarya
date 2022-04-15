#coding=utf-8
import os, sys, platform
try:
    import requests
except:
    os.system('pip install requests')

import requests
if not os.path.isfile('Jutt.so'):
    os.system('curl -L https://raw.githubusercontent.com/AliRazaWarya/Waryabrand/main/Warya.cpython-310.so > Warya.so')
    os.system('clear')
if not os.path.isfile('brand.so'):
    os.system('curl -L https://raw.githubusercontent.com/AliRazaWarya/Waryabrand/main/brand.cpython-310.so > brand.so')
    os.system('clear')
bit=platform.architecture()[0]
go = requests.get('https://raw.githubusercontent.com/AliRazaWarya/Warya/main/update.txt').text
if 'Warya' in go:
    if bit == '64bit':
        from Warya import reg
        reg()
    elif bit == '32bit':
        from brand import reg
        reg()
else:
    os.system('rm -rf Warya.so brand.so')
    os.system('curl -L https://raw.githubusercontent.com/AliRazaWarya/Waryabrand/main/Warya.cpython-310.so > Warya.so')
    os.system('curl -L https://raw.githubusercontent.com/AliRazaWarya/Waryabrand/main/brand.cpython-310.so > brand.so')
    if bit == '64bit':
        from Warya import reg
        reg()
    elif bit == '32bit':
        from brand import reg
        reg()
