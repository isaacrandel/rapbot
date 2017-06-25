import random
import os
import tempfile

import espeak
from pydub import AudioSegment
from pydub.playback import play

INTROS = ['yo yo yo', 'wassup homie its rapbot', 'its ya boi rapbot']
OUTROS = ['Peace out homies', 'mic drop', 'laters boi']

def get_loop():
    from os import listdir
    from os.path import isfile, join
    loop_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'loops')
    loops = [os.path.join(loop_path, f) for f in listdir(loop_path) if isfile(join(loop_path, f))]
    return random.choice(loops)

def build_rap(tweet):
    intro = random.choice(INTROS)
    outro = random.choice(OUTROS)
    return intro + tweet + outro


def rap(tweet):
    loop_file = get_loop()
    loop = AudioSegment.from_wav(loop_file)
    rap_txt = build_rap(tweet)

    es = espeak.ESpeak(pitch=1)
    with tempfile.TemporaryDirectory() as tmpdir:
        es.save(rap_txt, 'rap.wav')
        rap = AudioSegment.from_wav('rap.wav')
        mix = loop.overlay(rap)
        play(mix)