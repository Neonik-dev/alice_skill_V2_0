import requests
import alice_skill.config as config
import json


def get_all_categories():
    request_url = config.url + "/api/dictionary/groups/all"
    response = requests.get(request_url).json()
    return response[:5]


def get_all_words_in_category(category_id):
    request_url = config.url + f"/api/dictionary/words/group/{category_id}"
    response = requests.get(request_url).json()
    return response[:10]


def get_n_random_words(count):
    request_url = config.url + f"/api/dictionary/words/random/{count}"
    response = requests.get(request_url).json()
    return response


def get_word(word_id):
    request_url = config.url + "/api/dictionary/words/all"
    response = requests.get(request_url).json()

    for word in response:
        if word_id == word["id"]:
            return word


def get_category(category_id):
    request_url = config.url + "/api/dictionary/groups/all"
    response = requests.get(request_url).json()

    for category in response:
        if category_id == category["id"]:
            return category
