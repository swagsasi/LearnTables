from pygame import mixer
import random
import time
import os
import cursor


os.system('cls')
table = [int(x) for x in input("Enter table(s) to learn: ").split()]
sp = int(input("Enter time to display each table: "))
os.system('cls')
q = []    #Questions to be asked
n = 1     #Cycles count
tarr = [] #[22, 23, 24, ... 98, 99]
#This array is generated to access table sound file
for tx in range(2,10):
	for ty in range(2,10):
		tarr.append(int("{}{}".format(tx,ty)))
cursor.hide()


def read(tx, ty, ans):
    file_no = tarr.index(int("{}{}".format(tx,ty))) + 1
    file_dir = os.getcwd()
    file_name = os.path.join(file_dir, 'tables',
                             "tables_{}.mp3".format(file_no))
    mixer.init()
    mixer.music.load(file_name)
    mixer.music.play()
    time.sleep(0.8)
    mixer.music.pause()
    time.sleep(sp)
    os.system('cls')
    print("{} X {} = {}".format(tx,ty,ans))
    mixer.music.unpause()



def refil():
 for x in table:
    for y in range(2, 10):
        q.append("{} X {}".format(x ,y))
        #q.append("{} X {}".format(y ,x))#
    #q.remove("{} X {}".format(x ,x))#

def ask():
    while(True):
        i = random.choice(range(len(q)))
        t = q[i]
        #time.sleep(sp)
        n = [int(i) for i in t.split() if i.isdigit()]
        ans = n[0]*n[1]
        #os.system('cls')
        print(t+" = ")
        read(n[0],n[1],ans)
        time.sleep(sp)
        q.pop(i)
        os.system('cls')

        
while(True):
  try:
      refil()
      ask()
      
  except IndexError:
      os.system('cls')
      print("Cycles Completed: {}".format(n))
      time.sleep(2)
      n = n + 1
      os.system('cls')
