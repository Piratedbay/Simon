import os
import rich
from rich import print
import time

print("importing modules...........")
os.system("pip install rich")
print("Download this apk in order to have it ")
os.system("xdg-open https://utorrent.en.softonic.com/android/support/v/7.4.4")
os.system("clear")
print("contact me  if error occurs.......................")
print("You can support me for further projects by donating me.......")
print("Gorkhali Blood all over my veins. Yes NEPAL IS NEPAL NO ONE CAN HAVE IIT")
for i in range (100):
    print("GORKHALI")
time.sleep(3)
os.system("clear")
############################________________________________________________________________________________
print("==========================================")
print("CATEGORIES LIST")
print("""[1]movie     [2] Anime
[3] Song
""")
print('---------------------------------------------------------------------------------')
print ('WRITE CATEGORY ')
a = input("enter a category: ")
time.sleep(2)
print("---------------------------------------------------------------------------------")
if a== "1":
    b = input("Enter a movie name:   ")
    os.system('xdg-open https://www.1377x.to/search/'+b+"/1")
elif a == "2":
    c = input("enter a anime name:   ")
    os.system('xdg-open https://www.1377x.to/search/'+c+"/1")
elif a== "3":
    s = input("Enter a song name:   ")
    s1 = input ("Enter artist name of the song:")
    os.system("xdg-open https://google.com/ "+s+s1+" torrent magnet")
else:
    print("Enter a valid category all in small caps")
