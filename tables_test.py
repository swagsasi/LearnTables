import random
import time
import os
import cursor
import re

table = [int(x) for x in input("Enter table(s) to test: ").split()]
os.system('cls')
q = []  #Questions to be asked
n = 1   #Cycles count
wrongs = 0
begin = time.time()
        

def refill():
 for x in table:
    for y in range(2, 10):
        q.append("{} X {}".format(x ,y))
        q.append("{} X {}".format(y ,x))#
    q.remove("{} X {}".format(x ,x))#
        
def incorrect():
          cursor.hide()
          print("Incorrect")
          global wrongs
          wrongs = wrongs + 1
          time.sleep(0.5)
          os.system('cls')
          cursor.show()
          
def ask():
    while(True):
        i = random.choice(range(len(q)))
        t = q[i]
        ans = input("{} = ".format(t)).strip()
        n = [int(i) for i in t.split() if i.isdigit()]
        if(ans==''):
            incorrect()
            continue
        if (n[0]*n[1] == int(ans)):
            q.pop(i)
            os.system('cls')
            continue
        else:
            incorrect()

while(True):
  try:
      refill()
      ask()
  except IndexError:
      cursor.hide()
      os.system('cls')
      till = time.time() - begin
      print("Cycles Completed: {}/3".format(n))
      print("Wrongs: {}".format(wrongs))
      print("")
      print("Time passed: {0:.1f}s".format(till))
      if n == 3 and till < 90 and len(table) == 1 and wrongs == 0:
          print("Congratulations!")
      time.sleep(5)
      n = n + 1
      os.system('cls')
      cursor.show()
