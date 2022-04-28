from word import Word
import logging
import os
import time

from word import words

FORMAT = '%(asctime)s %(levelname)s - %(message)s'
logging.basicConfig(level=logging.INFO, filename='log.log', filemode='a', format=FORMAT)

clear = lambda: os.system('cls')
points = 0
correct = []

print(len(words))

while points < len(words):
    clear()
    w = Word()
    if w.random_word in correct:
        w = Word()
    else:
        print('To play word again type "1" and press enter.')
        w.sey()
        user_input = input('Please type word:\n')
        

        while user_input == str(1):
            w.sey()
            user_input = input('Please type word:')

        if w.check(user_input):
            logging.info(f'{w.word()} - correct')
            points += 1
            correct.append(w.random_word)
            print('correct')
            time.sleep(1)
            
        else:
            logging.error(f'wrong | word:{w.word()} user input: {user_input}')
            print('wrong\n')
            print(f'Hint: {w.hint()}\n')
            time.sleep(1)
clear()
print('Congratulations you can spell all words!!! :)')
