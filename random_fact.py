import alice_skill.view.texts as texts
import alice_skill.view.keyboards as keyboards
import alice_skill.view.tts as tts
from alice_skill.uttils import *
import alice_skill.data as data
from random import choice


def send_random_fact(buttons=None):
    fact = choice(data.facts)
    return make_response(text=fact, buttons=buttons)
