

import random
import re
import numpy as np
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]
word = random.choice(word_list)
lst = []

for i in word:
    lst.append("_")

print(lst)
counter = 0
lives = 7

# while lives != 0 or counter != len(word):  
#     letter = input("Guess a letter: ")
#     if letter not in word:
#         print(stages[lives-1])
#         lives -= 1
#         if lives==0:
#             print("YOU LOSE THE GAME!!")
#             counter= len(word)
#     else:
#         for index, i in enumerate(word.lower()):
#             if (i == letter.lower() and lst[index] == "_"):
#                 lst[index] = i
#                 counter += 1
#                 if(counter== len(word)):
#                     print("You Won the Game!")
#                     lives=0
#         print(' '.join(lst))


#################

while lives != 0 or counter != len(word):
    letter = input("Guess a letter: ")
    if letter not in word:
        print(stages[lives-1])
        lives -= 1
        if lives==0:
            print("YOU LOSE THE GAME!!")
            counter= len(word)
    else:
        indices_object = re.finditer(pattern=letter, string=word.lower())
        indices = [index.start() for index in indices_object]
        lst= np.asarray(lst)
        lst[indices]=letter   # a is found 3 time this will replace a all the times
        counter+=len(indices)
        if(counter== len(word)):
         print("You Won the Game!")
         lives=0
        print(' '.join(lst))



########













    # for index, i in enumerate(word.lower()):
    #     print(letter.lower())
    #     print(lst[index])
    #     if (i == letter.lower() and lst[index] == "_"):
    #         lst[index] = i
    #         counter += 1
    #         print(counter)
    #     else:
    #         print(stages[lives-1])
    #         lives -= 1
    #         print(lives)
    #         if (lives == 0):
    #             counter = len(word)
    #             print("You Lose")
    #             break



# endOfGame=False
# while not endOfGame:
#     letter = input("Guess a letter: ")
#     for index, i in enumerate(word.lower()):
#         if (i == letter.lower() and lst[index]=="_"):
#             lst[index] = i
#     print(lst)
#     if "_" not in lst:
#         endOfGame= True
# print("You won")
