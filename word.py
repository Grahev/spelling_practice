import pyttsx3
import random


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

words = []
f = open('words.txt', 'r')
for x in f:
    x =x.strip()
    words.append(x)

class Word:
    def __init__(self):
        self.random_word = random.choice(words)
    
    def word(self):
        return self.random_word

    def sey(self):
        engine.say(self.random_word)
        engine.runAndWait()

    def print(self):
        print(self.random_word)

    def check(self, user_input):
        if self.random_word == user_input:
            return True
        else:
            return False

    def hint(self):
        masked =  self.random_word[0:2] + len(self.random_word[:-2])*"_"
        return masked
