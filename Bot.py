import json
import wikipedia
import time
dic={}
print('Welcome Sir,',end=" ")
wish_time=time.ctime().split()[3].split(':')[0]
if wish_time <'12':
    print('Good Morning!')
elif wish_time>='12' and wish_time<'18':
    print('Good Afternoon!')
else:
    print('Good Evening!')
while(True):
    with open('data.json') as file:
        json_data=json.load(file)
    i=input('You1: ').lower()
    a=0
    while a==0:
        for key in json_data.keys():
            if key in i:
                try:
                    print("Bot:",json_data[key][i])
                    break
                except:
                    if i in dic.values():
                        print(dic)
                        break 
                    try:
                        print("Bot:",wikipedia.summary(i,sentences=1))
                        break
                    except:
                        print("Bot: Sorry I don't understand, what do you want's to say?1")
                        break
        else:
            print("Bot: Sorry I don't understand, what do you want's to say?2") 
        file.close()
        try:
            statements=json_data[key][i].split('\n')[1]
            i=input('You2: ').lower()
            if "And who are you?" in statements:
                statements='who is me'
                if i.split().__len__()==4:
                    i='You are '+i.split()[3]+'.'
                elif i.split().__len__()==3:
                    i='You are '+i.split()[2]+'.'
                elif i.split().__len__()==2:
                    i='You are '+i.split()[1]+'.'
                elif i.split().__len__()==1:
                    i='You are '+i.split()[0]+'.'
                print('Welcome '+i.split()[2]+"! (^_^)")
                dic.update({statements:i})    
        except:
            a=a+1