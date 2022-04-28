from word import Word
import logging

from word import words

FORMAT = '%(asctime)s %(levelname)s - %(message)s'
logging.basicConfig(level=logging.INFO, filename='log.log', filemode='a', format=FORMAT)

points = 0
correct = []

while points < len(words):

    w = Word()
    if w.random_word in correct:
        w = Word()
    else:
        w.sey()
        print('To play word again type "1" and press enter.')
        user_input = input('Please type word:')

        while user_input == str(1):
            w.sey()
            user_input = input('Please type word:')

        if w.check(user_input):
            logging.info(f'{w.word()} - correct')
            points += 1
            correct.append(w.random_word)
            print('correct')
        else:
            logging.error(f'wrong | word:{w.word()} user input: {user_input}')
            print('wrong')

print('Congratulations you can spell all words!!! :)')
