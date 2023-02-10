from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from datetime import datetime, date


def get_signs() -> dict:

    signs = {
        "aries": "Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).",
        "taurus": "Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).",
        "gemini": "Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).",
        "cancer": "Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).",
        "leo": "Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).",
        "virgo": "Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).",
        "libra": "Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).",
        "scorpio": "Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).",
        "sagittarius": "Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).",
        "capricorn": "Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).",
        "aquarius": "Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).",
        "pisces": "Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта)."
    }

    return signs


def get_signs_elements():

    zodiac_elements = {
        'fire': ['aries', 'leo', 'sagittarius'],
        'earth': ['taurus', 'virgo', 'capricorn'],
        'air': ['gemini', 'libra', 'aquarius'],
        'water': ['cancer', 'scorpio', 'pisces']
    }

    return zodiac_elements


def get_zodiac_dates():

    zodiac_dates = {
        1:  {'capricorn': (1, 20),   'aquarius': (21, 31)},
        2:  {'aquarius': (1, 19),    'pisces': (20, 29)},
        3:  {'pisces': (1, 20),      'aries': (21, 31)},
        4:  {'aries': (1, 20),       'taurus': (21, 30)},
        5:  {'taurus': (1, 21),      'gemini': (22, 31)},
        6:  {'gemini':  (1, 21),     'cancer': (22, 30)},
        7:  {'cancer':  (1, 22),     'leo': (23, 31)},
        8:  {'leo': (1, 21),         'virgo': (22, 31)},
        9:  {'virgo': (1, 22),       'libra': (23, 30)},
        10: {'libra': (1, 23),       'scorpio': (24, 31)},
        11: {'scorpio': (1, 22),     'sagittarius': (23, 30)},
        12: {'sagittarius': (1, 22), 'capricorn': (23, 31)}
    }

    return zodiac_dates


def get_sign_by_date(request, day, month):

    zodiac_dates = get_zodiac_dates()

    if month in zodiac_dates:
        signs_in_month = zodiac_dates[month]

        for sign, sign_date in signs_in_month.items():

            if day in range(sign_date[0], sign_date[1]+1):

                redirect_url = reverse('horoscope_zodiac_sign', args=(sign,))
                break

    return HttpResponseRedirect(redirect_url)


def get_type_page(request):

    elements_types = tuple(get_signs_elements())

    elements_with_html_tags = ''

    for element in elements_types:

        redirect_url = reverse('signs_by_element', args=(element,))

        elements_with_html_tags += f'<li> <a href="{redirect_url}"> {element.capitalize()} </a> </li>'

    response = f'<ul> {elements_with_html_tags} </ul>'

    return HttpResponse(response)


def get_signs_by_elements(request, element):

    signs_elements = get_signs_elements()

    if element in signs_elements:

        signs_by_element = signs_elements[element]

        elements_with_html_tags = ''

        for sign in signs_by_element:

            redirect_url = reverse('horoscope_zodiac_sign', args=(sign,))

            elements_with_html_tags += f'<li> <a href="{redirect_url}"> {sign.capitalize()} </a> </li>'

        response = f'<ul> {elements_with_html_tags} </ul>'

        return HttpResponse(response)

    else:
        return HttpResponseNotFound(f'Элемента {element} не существует')


def get_index(request):

    signs_names = tuple(get_signs())

    signs_with_html_tags = ''

    for sign in signs_names:
        redirect_url = reverse('horoscope_zodiac_sign', args=(sign,))
        signs_with_html_tags += f'<li> <a href="{redirect_url}"> {sign.title()} </a> </li>'

    response = f'<ol> {signs_with_html_tags} </ol>'

    return HttpResponse(response)


def get_zodiac_sign(request, zodiac_sign: str):

    signs = get_signs()

    response = signs.get(zodiac_sign.lower(), None)

    if response:
        return HttpResponse(response)
    return HttpResponseNotFound(f"Неизвестный знак зодиака {zodiac_sign}")


def get_zodiac_sign_by_num(request, zodiac_number: int):

    signs = get_signs()

    if 1 <= zodiac_number <= len(signs):
        sign_by_number = tuple(signs)[zodiac_number-1]
        redirected_url = reverse('horoscope_zodiac_sign', args=(sign_by_number,))
        response = HttpResponseRedirect(redirected_url)
    else:
        response = HttpResponseNotFound(f'Знака с номером {zodiac_number} нет')

    return response
