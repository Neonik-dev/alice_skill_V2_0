import alice_skill.view.texts as texts
import alice_skill.view.keyboards as keyboards
import alice_skill.view.tts as tts
from alice_skill.uttils import *
import alice_skill.data as data
import alice_skill.api_work as api


def chose_category():
    all_categories = api.get_all_categories()
    items = []
    for category in all_categories:
        items.append(item(title=category["name_origin"], description=category["name_rus"],
                          img_button=button(category["name_origin"], payload={"category_button": category["id"]})))
    return make_response(text="",
                         tts=texts.CHOOSE_CATEGORY,
                         card=items_list(content=items,
                                         header=texts.CHOOSE_CATEGORY))


def learn_words_by_num(category, step):
    all_word = api.get_all_words_in_category(category)
    if len(all_word) <= step:
        return make_response(
            text=texts.CONGRATS_LERN
        )
    word = all_word[step]
    return make_response(
        text=texts.WORD_TEMPALTE.format(
            word=word["word_original"],
            translate=word["word_rus"]),
        tts=tts.WORD_TEMPALTE.format(
            word=word["word_original"],
            translate=word["word_rus"]),
        state={'active_skill': "learn_words",
               "step": step + 1,
               "category": category}
    )

