import datetime
import telepot
import math
from telepot.loop import MessageLoop
from time import sleep

now = datetime.datetime.now()
timestamp = ('Date: ' + str(now.day) + '/' + str(now.month) + '/' + str(now.year) + "\n" + 'Time: ' + str(now.hour) + ':' + str(now.minute) + ':' + str(now.second))

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    username = msg['from']['username']
    firstname = msg['from']['first_name']
 #   lastname = msg['from']['last_name']
    print (f"\n Received: {command}\n From: {chat_id}, {firstname}")

    if command == '/start':
        bot.sendMessage (chat_id, "Hello there, "+str(firstname)+"!")
    else:
        #bot.sendMessage(chat_id, (9999-+int(command))*(9999-+int(command)))
        
        #calls the method that does the math then returns that value as a response
        bot.sendMessage(chat_id, calculate(command)) 

#bot token
bot = telepot.Bot('')
MessageLoop(bot, handle).run_as_thread()

print (bot.getMe())
print ("\n"+'BOT_IS_ONLINE!' "\n" +(timestamp))

#added a method to handle the math
def calculate(number):
    return str(int(math.pow((9999-int(number)),2))

while 1:
    sleep(10) 
