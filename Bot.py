import json
import wikipedia
print("Welcome Mr.")
while(True):
    with open('data.json') as file:
        json_data=json.load(file)
    i=input('You: ').lower()
    for key in json_data.keys():
        if key in i:
            try:
                print("Bot:",json_data[key][i])
                break
            except: 
                try:
                    print("Bot:",wikipedia.summary(i,sentences=1))
                    break
                except:
                    print("Bot: Sorry I don't understand, what do you want's to say?")
                    break
    else:
        print("Bot: Sorry I don't understand, what do you want's to say?") 
    file.close() 