from alice_skill import config
from alice_skill.uttils import *
import alice_skill.random_fact as random_fact
import alice_skill.find_excess as find_excess
import alice_skill.lexical_rules as lexical_rules
import alice_skill.complete_proverb as complete_proverb
import alice_skill.lern_words as lern_words
import alice_skill.listen_pronunciation as listen_pronunciation


def handler(event, context):
    intents = event["request"].get("nlu", {}).get('intents', [])
    state = event.get('state').get(REQUEST_STATE, {})
    payload = event["request"].get('payload', {})

    if event["session"]['new']:
        return start()
    elif IntentsNames.stop in intents:
        return make_response(text=texts.STOPED, buttons=[button(title="Помощь", hide=True)])
    # пейлоады
    elif payload.get("fact", None):
        return random_fact.send_random_fact(buttons=[button(title="Ещё", hide=True, payload={"fact": 1})])
    elif payload.get("category_button", None) is not None:
        return lern_words.learn_words_by_num(payload["category_button"], 0)
    # статусы
    elif state.get("pronunciation", None):
        return listen_pronunciation.learn_words()
    elif state.get('active_skill', None):
        if state['active_skill'] == "learn_words":
            return lern_words.learn_words_by_num(state["category"], state["step"])

    elif state.get("screen", None) == "begin_find_excess":
        if IntentsNames.start_play in intents:
            return find_excess.continue_find_excess(idd=state.get("id", None), payload=payload)
        else:
            return fallback_response('Вы вышли из мини-игры "лишнее слово". Теперь вы в главном меню',
                                     butt=[button(title="Помощь", hide=True)])
    elif state.get("screen", None) == "find_excess":
        return find_excess.continue_find_excess(idd=state.get("id", None), payload=payload)

    elif state.get("proverb", None) == "start":
        if IntentsNames.start_play in intents:
            return complete_proverb.play_proverb(idd=state.get("id", None), payload=payload)
        else:
            return fallback_response('Вы вышли из мини-игры "лишнее слово". Теперь вы в главном меню',
                                     butt=[button(title="Помощь", hide=True)])
    elif state.get("proverb") == "play":
        return complete_proverb.play_proverb(idd=state.get("id", None), payload=payload)

    # интенты
    elif IntentsNames.tell_phraseology in intents:
        return complete_proverb.start_proverb()
    elif IntentsNames.send_fact in intents:
        return random_fact.send_random_fact(buttons=[button(title="Ещё", hide=True, payload={"fact": 1})])
    elif IntentsNames.lets_lern in intents:
        return lern_words.chose_category()
    elif IntentsNames.tatar_rules in intents:
        return lexical_rules.about_rules(event)
    elif IntentsNames.find_excess in intents:
        return find_excess.start_find_excess()
    elif IntentsNames.skills in intents:
        return get_skills()
    elif IntentsNames.pronunciation in intents:
        return listen_pronunciation.start()
    else:
        return fallback_response(butt=[button(title="Помощь", hide=True)])


def start():
    return make_response(texts.WELCOME, buttons=[button(title="Помощь", hide=True)])


def get_skills():
    items = []
    for skill in config.skills:
        items.append(item(
            title=skill["title"],
            description=skill["description"],
            img_button=button(title=skill["button"])
        ))
    return make_response(text=texts.I_CAN, card=items_list(header=texts.I_CAN, content=items))
