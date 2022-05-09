import alice_skill.view.texts as texts
import alice_skill.view.keyboards as keyboards
import alice_skill.view.tts as tts
import alice_skill.data as data
from alice_skill.uttils import *
import random


def start_proverb():
    return make_response(texts.START_PROVERB, state={"proverb": "start"}, buttons=[button("Начинаем", hide=True)])


def play_proverb(idd, payload):
    head = "Выберите продолжение."
    box = random.choice(data.proverb)
    if payload.get("answer_proverb") == 1:
        head = "Отлично получилось."
    elif payload.get("answer_proverb") == 0:
        head = "Вам стоит подумать еще."
        for i in data.proverb:
            if i["id"] == payload["id"]:
                box = i
                break
    elif idd:
        head = "Выберите ответ из кнопок, либо скажите 'остановись'"
        for i in data.proverb:
            if i["id"] == idd:
                box = i
                break

        buttons = []
        for i in box["choice"]:
            buttons.append(
                button(title=i, hide=True, payload={"answer_proverb": 1 if box["answer"] == i else 0, "id": box["id"]}))

    items = []
    buttons = []
    items.append(item(title=box["question"], description=" "))

    random.shuffle(box["choice"])
    for i in box["choice"]:
        items.append(item(description=i))
        buttons.append(
            button(title=i, hide=True, payload={"answer_proverb": 1 if box["answer"] == i else 0, "id": box["id"]}))

    return make_response(text=head, state={"proverb": "play", "id": box["id"]},
                         card=items_list(content=items, header=head), buttons=buttons)
