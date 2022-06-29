import datetime
import pywhatkit as pwk
import pandas as pd
import pyautogui as pg
# 2015 5 6 8 53 40
# print("Time = %s:%s" % (time.hour, time.minute))

        

name= input('enter file name\n')
data=pd.read_csv ( name+".csv")
df=pd.DataFrame(data)
thislist = []
k = pg.position()

co=0
for index,col in df.iterrows():  
    no=col['phonenumber']
    co+=1
    if(no=='closed'):
            print("skip casuse of temp closed status")
    else:
            now = datetime.datetime.now()
            name=col['name']
            if now.minute>=58 :
                hr=now.hour+1
                mm=now.minute+2
                pwk.sendwhatmsg("+91"+no, "Hi testbads", hr, mm,15)
                pg.click(k.x,k.y)
                pg.keyDown('enter')
                pg.press("enter")
                thislist.append(name+" "+"sent")
            else:
                    hr=now.hour
                    mm=now.minute+1
                    pwk.sendwhatmsg("+91"+no, "Hi test12badhs", hr, mm,15)
                    pg.click(k.x,k.y)
                    pg.keyDown('enter')
                    pg.press("enter")
                    thislist.append(name+" "+"sent")

print("report\n")
tot=len(thislist)
re=str(tot)+"/"+str(co)
print(re)
#print("Time = %s:%s" % (time.hour, time.minute+1))

# pwk.sendwhatmsg("+919747830754", "Hi test1", hr, mm,10)
# pwk.sendwhatmsg("+919747830754", "Hi test2", hr, mm,10)
