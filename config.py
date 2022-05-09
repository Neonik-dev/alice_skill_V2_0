REQUEST_STATE = "session"
RESPONSE_STATE = "session_state"
url = "http://tatarinteam.ru"


class IntentsNames:
    gallery = "galery"
    items_list = "items_list"
    big_image = "big_image"
    send_fact = "send_fact"
    tatar_rules = "tatar_rules"
    find_excess = "find_excess"
    lets_lern = "lets_lern"
    stop = "stop"
    start_play = "start_play"
    skills = "skills"
    tell_phraseology = "tell_phraseology"
    pronunciation = "pronunciation"


skills = [
    {"title": "Игра найди лишнее слово",
     "description": "Интересная игра на перевод слов и выявление закономерностей",
     "image": None,
     "button": "Найди лишнее"},

    {"title": "Учить слова",
     "description": "Ты сможешь прослушать произношение татарских слов",
     "image": None,
     "button": "Учить слова"},

    {"title": "Интересные факты",
     "description": "Расскажу что нибудь интересное про татарский язык",
     "image": None,
     "button": "Влияние татарского языка на русский",
     "payload": {"fact": 1}},

    {"title": "Продолжи пословицу",
     "description": "Игра для прокачки своего перевода и для поплнения пословиц в свой запас",
     "image": None,
     "button": "Продолжи пословицу"},

     {'title': "Узнай слово по произношению",
      "description": "Алиса произнесет слово, а вы скажите перевод",
      "image": None,
      "button": "Узнай слово"},
]
