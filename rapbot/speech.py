import random
import os
import tempfile

import espeak
from pydub import AudioSegment
from pydub.playback import play


INTROS = ['yo yo yo', 'whats up homie its rapbot',
          'its ya boi rapbot', 'shout out to my homies from balmakewen intermediate',
          'Droppin this fire mix for room 15', 'what. what. what. crunk ain\'t dead']
OUTROS = ['Peace out homies', 'mic drop', 'laters boi', 'word to your motha']


def get_loop():
    loop_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'loops')
    loops = [os.path.join(loop_path, f) for f in os.listdir(loop_path) if os.path.isfile(
        os.path.join(loop_path, f))]
    return random.choice(loops)


def build_rap(tweet):
    intro = random.choice(INTROS)
    outro = random.choice(OUTROS)
    return intro + tweet + outro


def rap(tweet):
    loop_file = get_loop()
    loop = AudioSegment.from_wav(loop_file)
    loop = loop * 3  # make the loops longer for long tweets
    rap_txt = build_rap(tweet)

    es = espeak.ESpeak(pitch=1)
    with tempfile.TemporaryDirectory() as tmpdir:
        es.save(rap_txt, 'rap.wav')
        rap = AudioSegment.from_wav('rap.wav')
        mix = rap.overlay(loop)
        play(mix)