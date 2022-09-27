from asyncio import FastChildWatcher
import os;
from colorama import Fore, Back, Style
import time
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
print(f" Welcome to the game 😴")
end_game=False;
bids={}

while not end_game:
    name=input(f" What is your name? 😈:")
    amount=input(f" What's your bid? 💰:")
    bids[name]=amount;
    os.system('cls||clear')
    other_bid=input(f" Are there any other Bidders🤨? Type yes or no :")
    if other_bid.lower()=="no":
        end_game=True         

maxbid={"name":"","bid":0};   

def countdown():
    t=5
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
      
    print(f'{maxbid["name"]} won the bid with {maxbid["bid"]}$ 🥳 🍾')
  
for key in bids:
    bid=bids[key]
    if(int(bid)>int(maxbid["bid"])):
        maxbid["name"]=key
        maxbid["bid"]=bid

countdown();



#
