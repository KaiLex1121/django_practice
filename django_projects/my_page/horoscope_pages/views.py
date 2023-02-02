from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


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


def get_index(request):

    signs_names = tuple(get_signs())

    signs_with_html_tags = ''

    for sign in signs_names:
        redirect_url = reverse('horoscope_zodiac_sign', args=(sign,))
        signs_with_html_tags += f'<li> <a href="{redirect_url}"> {sign} </a> </li>'

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
