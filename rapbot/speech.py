import random

import pyttsx

INTROS = ['yo yo yo', 'wassup homie its rapbot', 'its ya boi rapbot']
OUTROS = ['Peace out homies', 'mic drop', 'laters boi']

def build_rap(tweet):
    intro = random.choice(INTROS)
    outro = random.choice(OUTROS)
    return intro + tweet + outro

def rap(tweet):
    engine = pyttsx.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 40)
    
    rap = build_rap(tweet)
    engine.say(rap)
    engine.runAndWait()
    