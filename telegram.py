
# coding: utf-8

# In[2]:

import telepot, time, serial
ser = serial.Serial('COM3',9600)

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    
    
    if content_type == 'text':
        command = msg['text']
        print 'Got Command: ' + command
        
        if '/hello' in command:
            bot.sendMessage(chat_id,"Hello, any commands for today?")
			
        if 'on' in command.lower().split(' '):
			ser.write(b'Y')
			bot.sendMessage(chat_id,'Led ON')
			
        if 'off' in command.lower().split(' '):
		    ser.write(b'N')
		    bot.sendMessage(chat_id,'Led OFF')
            
            
bot = telepot.Bot("277041505:AAGksFIYH4iM411uDu-9it7PZtieJSNAJc0")


bot.message_loop(handle)

while 1:
    time.sleep(20)

