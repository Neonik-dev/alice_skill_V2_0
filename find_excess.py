import random
import alice_skill.view.texts as texts
import alice_skill.view.keyboards as keyboards
import alice_skill.view.tts as tts
from alice_skill.view.texts import *
from alice_skill.uttils import *
import alice_skill.data as data
from random import choice


def start_find_excess():
    return make_response(BEGIN_PLAY_FIND_EXCESS, state={"screen": "begin_find_excess"},
                         buttons=[button("Начинаем", hide=True)])


def continue_find_excess(idd, payload):
    box = choice(data.excess)
    if payload.get("excess", None) == 1:
        head = "Все верно. Идем дальше"
    elif payload.get("excess", None) == 0:
        head = "Неверно, попробуй снова"
        for i in data.excess:
            if i["id"] == payload["id"]:
                box = i
                break
    elif idd:
        head = "Выберите ответ из кнопок, либо скажите 'остановись'"
        buttons = []
        for i in data.excess:
            if i["id"] == idd:
                box = i
                break

        for i in box["question"]:
            buttons.append(
                button(title=i, hide=True, payload={"excess": 1 if box["answer"] == i else 0, "id": box["id"]}))

        return make_response(text=head, state={"screen": "find_excess", "id": box["id"]}, buttons=buttons)
    else:
        head = "Выберите лишнее:"

    items = []
    buttons = []
    random.shuffle(box["question"])
    for i in box["question"]:
        items.append(item(description=i))
        buttons.append(button(title=i, hide=True, payload={"excess": 1 if box["answer"] == i else 0, "id": box["id"]}))

    return make_response(text=head, state={"screen": "find_excess", "id": box["id"]},
                         card=items_list(content=items, header=head), buttons=buttons)
