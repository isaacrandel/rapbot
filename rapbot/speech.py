import random

import espeak

INTROS = ['yo yo yo', 'wassup homie its rapbot', 'its ya boi rapbot']
OUTROS = ['Peace out homies', 'mic drop', 'laters boi']


def build_rap(tweet):
    intro = random.choice(INTROS)
    outro = random.choice(OUTROS)
    return intro + tweet + outro


def rap(tweet):
    rap = build_rap(tweet)

    es = espeak.ESpeak(pitch=1)
    es.say(rap)
