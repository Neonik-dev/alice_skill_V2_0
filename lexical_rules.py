import alice_skill.view.texts as texts
import alice_skill.view.keyboards as keyboards
import alice_skill.view.tts as tts
from alice_skill.config import IntentsNames
from alice_skill.uttils import *

FACE_IMAGE = "965417/44bcf1db546ac9ce9d62"
PADEG_IMAGE = "937455/923a33aa22c61bba5509"
MAIN_WORD = "997614/4cb673ffffff369c605a"
PRILAGATEL = "1030494/e2bcc0b7f703bc93d643"


def about_rules(event):
    intent = event["request"]["nlu"]["intents"][IntentsNames.tatar_rules]
    slot = intent["slots"]["rules"]["value"]

    if slot == "rule":
        items = [
            item(
                title="Лицо",
                description="Расскажу о склонении татарских слов в лицах",
                image_id=FACE_IMAGE,
                img_button=button(title="Лица", payload={"rule": "face"})
            ),
            item(
                title="Падеж",
                description="Расскажу про сколонение татарских слов в разные падежи",
                image_id=PADEG_IMAGE,
                img_button=button(title="Падеж", payload={"rule": "case"})
            ),
            item(
                title="Правило сравнительных степеней",
                description="Покажу как правильно ставить в сравнительные степени",
                image_id=PRILAGATEL,
                img_button=button(title="Правило сравнительных степеней", payload={"rule": "prilagatel"})
            ),
            item(
                title="Множественное число существительных",
                description="Покажу как правильно ставить во множественное число существительные",
                image_id=MAIN_WORD,
                img_button=button(title="Множественное число существительных", payload={"rule": "main_word"})
            ),
        ]
        return make_response(text=texts.ALL_RULES_TEXT, card=items_list(content=items, header="Правила"))
    elif slot == "face":
        return make_response(text="Расскажу о склонении татарских слов в лицах",
                             card=image_gallery(
                                 [item(image_id=FACE_IMAGE, title="Расскажу о склонении татарских слов в лицах")]))
    elif slot == "case":
        return make_response(text="Расскажу о склонении татарских слов в падежах", card=image_gallery(
            [item(image_id=FACE_IMAGE, title="Расскажу о склонении татарских слов в лицах")]))
    elif slot == "main_word":
        return make_response(text="Покажу как правильно ставить во множественное число существительные", card=image_gallery(
            [item(image_id=MAIN_WORD, title="Покажу как правильно ставить во множественное число существительные")]))
    elif slot == "prilagatel":
        return make_response(text="Покажу как правильно ставить в сравнительные степени", card=image_gallery(
            [item(image_id=PRILAGATEL, title="Покажу как правильно ставить в сравнительные степени")]))
    else:
        return fallback_response()
