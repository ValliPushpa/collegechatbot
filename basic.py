"""


"""
" Importing predefined packages"
import random
from datetime import datetime

"importing user define packages"

from location import location
from founder import college
from branch import branch
from hostel import hostel

"Introducing chat bot to the user.."

def self_intro():
   response=[ "Hey Human...!!! I am Jolly. i will help you know Details about your college.","Hello..!!!. This is Jolly How can i help you to know college details ?."," I am jolly, I am here too help you to know college details. "]
   return random.choice(response)
'Whishing user according to time...'
def get_time():
    current_time = datetime.now()
    wish="GOOD MORNING..!!!!"
    if current_time.hour<=17:
        wish="GOOD AFTERNOON...!!!!"
    elif current_time.hour<=22:
        wish="GOOD EVENING...!!!"
    else:
        wish ="ITS TOOO LATE MAN...!!!"
    return wish

'Greeting to user '
def welcome(name):
    messages=["It's Pleasure to meet you"," Nice to meet you "," I'm gald to meet you"]
    return random.choice(messages)

'Display the menu...'
def showmenu():
    print("what you want to know...")
    print("__________________________")
    print("1.Location of college")
    print("2.About college")
    print("3.Branch")
    print("4.Hostel")
    print("5.exit")
    print("________________________________")
    try:
        return int(input("Enter your choice[1-5] : "))
    except:
        print("only Enter  choice from 1 to 4")
        return 0
        
'Functionality of chat bot..'      
def bot():
        print(self_intro())
        print(get_time())
        name=input("Please Enter your Name :")
        print(welcome(name))
       # print(get_time())
        choice=showmenu()

        while choice !=5:
            if(choice==1):
                print(location())
            elif choice==2  :
                print(college())
            elif choice==3:
                print('1.ECE','2.CSE','3.EEE','4.MECH','5.CIVIL','6.IT', sep='\n')
                print("Enter your choice")
                c=(int(input()))
                print(branch(c))
            elif choice==4:
                print("AC or Non AC")
                
                print(hostel(input()))
            elif choice>=5:
                print("I can't understand... sorry")
            else: 
                return 0
            choice=showmenu()
bot()
print('Have a Nice Day....!!!!!!','keep Smiling(*_*)','Thank you ....[^..^]',sep='\n')

            





