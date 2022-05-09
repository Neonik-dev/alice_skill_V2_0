from alice_skill.config import *
import alice_skill.view.texts as texts


def make_response(text, tts=None, card=None, state=None, buttons=None):
    response = {
        "text": text,
        "tts": tts if tts else text
    }
    if buttons:
        response["buttons"] = buttons

    if card:
        response["card"] = card

    response = {
        "response": response,
        "version": '1.0'
    }

    if state:
        response[RESPONSE_STATE] = state

    return response


def button(title, payload=None, url=None, hide=False):
    button = {
        'title': title,
        'hide': hide,
    }

    if payload:
        button["payload"] = payload
    if url:
        button['url'] = url
    return button


def image(image_id, title=None, description=None, img_button=None):
    return {
        "image_id": image_id,
        "title": title,
        "description": description,
        "button": img_button
    }

def item(image_id=None, title=None, description=None, img_button=None):
    return {
        "image_id": image_id,
        "title": title,
        "description": description,
        "button": img_button
    }

def big_image(image_to_show):
    image_to_show['type'] = 'BigImage'
    return image_to_show


def items_list(content, header, footer=None, footer_button=None):
    return {
        "type": "ItemsList",
        "header": {
            "text": header,
        },
        "items": content,
        "footer": {
            "text": footer,
            "button": footer_button
        }
    }


def image_gallery(image_items):
    return {
        "type": "ImageGallery",
        "items": image_items
    }


def fallback_response(text=None, butt=None):
    if text:
        return make_response(text, buttons=butt)
    return make_response(texts.FALLBACK_TEXT, buttons=butt)