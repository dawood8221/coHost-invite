import os
os.system("pip install samimo")

import samino as aminofix
import threading,time
c=aminofix.Client()
c.sid_login("AnsiMSI6IG51bGwsICIwIjogMiwgIjMiOiAwLCAiMiI6ICJjMDFkYWU1ZC00YzFkLTQ2NDAtODgzNi05YzM0YTMxODc4NTAiLCAiNSI6IDE2NTk4MjE3NTYsICI0IjogIjM3LjIzNi4xMzYuNTAiLCAiNiI6IDEwMH267LTknAzHT9yiUEAfcbCABFv0LQ")
x1=c.get_from_link("http://aminoapps.com/p/j131lx")
x2=c.get_from_link("http://aminoapps.com/c/kings-of-manga")
s=aminofix.Local(comId=x2.comId)
so=aminofix.Local(comId=x1.comId)
on=s.get_online_users(start=0,size=100).userId
time.sleep(5)
def x():
	for i in range(100):so.chat_settings(chatId=x1.objectId,)
	print("end")
x()
