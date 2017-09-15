#
# =======================================+SCRIPT BY HANI LAMANI+==============================================
#
# ==========================================+date : 2017/09/06+===============================================
#
# ================================+contact : www.facebook.com/lamanihani+=====================================
#
# ====================================+github : www.github.com/lamanihani=====================================
#
# TNX TO : my GOD <3 , THE PROPHET MOHAMED <3 , 
#=============================================================================================================
import sys
import os
import time
os.system('clear')
def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(4. / 100)
slowprint("    \033[91mThe Easy")
def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0. / 100)
slowprint('''\033[1;31m \033[91m    
       __  ___                 ________                               
      /  |/  /___ ______      / ____/ /_  ____ _____  ____ ____  _____
     / /|_/ / __ `/ ___/_____/ /   / __ \/ __ `/ __ \/ __ `/ _ \/ ___/
    / /  / / /_/ / /__/_____/ /___/ / / / /_/ / / / / /_/ /  __/ /    
   /_/  /_/\__,_/\___/      \____/_/ /_/\__,_/_/ /_/\__, /\___/_/     
                                                   /____/\033[97m             
''')
def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(3. / 100)
slowprint("\t\t                                         \033[93mBy :Lamani Hani VEGETA-LFH\033[97m")
print(" ")
print("1- show the current MAC-ADDRESS")
print("")
print("2- change your MAC-ADDRESS Randomly")
print("")
print("3- change your MAC-ADDRESS Customly")
print("")
print("4- reset the original MAC-ADDRESS")
print(" ")
print("5- why change MAC-ADDRESS")
print("")
mohamed=input("\033[92m[?] \033[96mmake your choise ==>")
if mohamed==('1') :
            print(" ")
            print("\033[94m1 \033[97m- \033[91mwlan0 \033[97m( WIFI connexion)")
            print("\033[94m2 \033[97m- \033[91meth0 \033[97m( CABLE connection)")
            print(" ")
            lawla=input("   \033[95m[?] \033[97menter your \033[91mconnection type \033[97m:")
            if lawla==('1') :
                      slowprint("\033[97m")
                      os.system('macchanger -s wlan0')
                      print(" ")
                      alla=input('press any key to cuntinue')
                      os.system('clear') 
                      os.system('python3 mac.py')
            if lawla==('2') :
                       slowprint("\033[97m")
                       os.system('macchanger -s eth0')
                       print(" ")
                       allah=input('press any key to cuntinue')
                       os.system('clear')
                       os.system('python3 mac.py')

if mohamed==('2') :
               print(" ")
               print("\033[94m1 \033[97m- \033[91mwlan0 \033[97m( WIFI connexion)")
               print("\033[94m2 \033[97m- \033[91meth0 \033[97m( CABLE connection)")
               print(" ")
               deuxs=input("   \033[95m[?] \033[97menter your \033[91mconnection type \033[97m:")
               if deuxs==('2') :
                        slowprint("")
                        os.system('ifconfig eth0 down')
                        os.system('macchanger -r eth0')
                        os.system('ifconfig eth0 up')
                        print(" ")
                        hoho=input("press any key to cuntinue")
                        os.system('clear')
                        os.system('python3 mac.py')
               if deuxs==('1') :
                        slowprint("")
                        os.system('ifconfig wlan0 down')
                        os.system('macchanger -r wlan0')
                        os.system('ifconfig wlan0 up')
                        print(" ")
                        hoho=input("press any key to cuntinue")
                        os.system('clear')
                        os.system('python3 mac.py')

if mohamed==('4'): 
               print(" ")
               print("\033[94m1 \033[97m- \033[91mwlan0 \033[97m( WIFI connexion)")
               print("\033[94m2 \033[97m- \033[91meth0 \033[97m( CABLE connection)")
               print(" ")
               talta=input("   \033[95m[?] \033[97menter your \033[91mconnection type \033[97m:")
               if talta==('2') :
                        print(" ")
                        slowprint("\033[97m")
                        os.system('macchanger -p eth0')
                        print(" ") 
                        lopa=input("press any key to cuntinue ")
                        os.system('clear')
                        os.system('python3 mac.py')
               if talta==('1') : 
                        print(" ")
                        slowprint("\033[97m")
                        os.system('ifconfig wlan0 down')
                        os.system('macchanger -p wlan0')
                        os.system('ifconfig wlan0 up')
                        print(" ") 
                        lopa=input("press any key to cuntinue ")
                        os.system('clear')
                        os.system('python3 mac.py')


def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(8. / 100)

if mohamed==('5'): 
               print("\033[97m")
               slowprint(''' 
       [*] Static IP Assignment: Routers allow you to assign static IP addresses to your computers. When a device connects, it always receives a specific IP address if it has a matching MAC address

   [*] MAC Address Filtering: Networks can use MAC address filtering, only allowing devices with specific MAC addresses to connect to a network. This isn’t a great security tool because people can spoof their MAC addresses.
   
   [*] MAC Authentication: Some Internet service providers may require authentication with a MAC address and only allow a device with that MAC address to connect to the Internet. You may need to change your router or computer’s MAC address to connect.
 
   [*] Device Identification: Many airport Wi-Fi networks and other public Wi-Fi networks use a device’s MAC address to identify it. For example, an airport Wi-Fi network might offer a free 30 minutes and then ban your MAC address from receiving more Wi-Fi. Change your MAC address and you could get more Wi-Fi. (Free, limited Wi-Fi may also be tracked using browser cookies or an account system.)

   [*] Device Tracking: Because they’re unique, MAC addresses can be used to track you. When you walk around, your smartphone scans for nearby Wi-Fi networks and broadcasts its MAC address. A company named Renew London used trash bins in the city of London to track people’s movements around the city based on their MAC addresses. Apple’s iOS 8 will use a random MAC address each time it scans for nearby Wi-Fi networks to prevent this sort of tracking. 
                                                                                     Lamani-Hani

               ''')
def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(3. / 100)

if mohamed==('3'):
               print(" ")
               print("\033[94m1 \033[97m- \033[91mwlan0 \033[97m( WIFI connexion)")
               print("\033[94m2 \033[97m- \033[91meth0 \033[97m( CABLE connection)")
               print(" ")
               rabaa=input("   \033[95m[?] \033[97menter your \033[91mconnection type \033[97m:")
               if rabaa==('2') :
                        print(" ")
                        os.system('ifconfig eth0 down')
                        dire=input("\033[95m[?] \033[97menter THE NEW \033[92mMAC-ADDRESS \033[97m: ")
                        os.system('ifconfig eth0 down')
                        os.system('macchanger -m'+(dire)+' eth0')
                        os.system('ifconfig eth0 up')
                        print("done")
               if rabaa==('1') : 
                        os.system('ifconfig wlan0 down')
                        print(" ")
                        dire=input("\033[95m[?] \033[97menter THE NEW \033[92mMAC-ADDRESS \033[97m: ")
                        os.system('ifconfig wlan0 down')
                        os.system('macchanger -m'+(dire)+' wlan0')
                        os.system('ifconfig wlan0 up')
                        print("done")




