import random
import os
import subprocess
import tempfile

import espeak
from pydub import AudioSegment
from pydub.playback import play


INTROS = ['yo yo yo', 'whats up homie its rapbot',
          'its ya boi rapbot', 'shout out to my homies from balmakewen intermediate',
          'Droppin this fire mix for room 15', 'what. what. what. crunk ain\'t dead']
OUTROS = ['Peace out homies', 'mike drop', 'laters boi', 'word to your motha']


def get_loop():
    loop_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'loops')
    loops = [os.path.join(loop_path, f) for f in os.listdir(loop_path) if os.path.isfile(
        os.path.join(loop_path, f))]
    return random.choice(loops)


def build_rap(tweet):
    intro = random.choice(INTROS)
    outro = random.choice(OUTROS) + ' ' + random.choice(OUTROS)
    return intro + tweet + outro


def rap(tweet):
    loop_file = get_loop()
    loop = AudioSegment.from_wav(loop_file)
    loop = loop * 5  # make the loops longer for long tweets
    rap_txt = build_rap(tweet)

    print('Mixin rap...')
    es = espeak.ESpeak(pitch=1, speed=180, word_gap=15, voice='en-us')
    es.save(rap_txt, 'rap.wav')
    rap = AudioSegment.from_wav('rap.wav')
    mix = rap.overlay(loop)
    normalized_mix = mix.apply_gain(-mix.max_dBFS)
    normalized_mix.export("mix.mp3", format="mp3")
    print('Rappin...')
    subprocess.Popen(['play', '-q', 'mix.mp3'])
