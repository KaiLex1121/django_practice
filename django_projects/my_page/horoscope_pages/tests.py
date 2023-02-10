from django.test import TestCase
from . import views


class TestHoroscope(TestCase):

    SIGNS = views.get_signs()

    def test_signs_views(self):

        signs = self.SIGNS

        for sign in signs:

            sign_desc = signs[sign]

            response = self.client.get(f'/horoscope/{sign}/')

            self.assertEqual(response.status_code, 200)

            self.assertIn(sign_desc, response.content.decode())

    def test_signs_redirects(self):

        signs = tuple(self.SIGNS)

        for num, sign in enumerate(signs, start=1):
            response = self.client.get(f'/horoscope/{num}/')
            self.assertEqual(response.status_code, 302)
            self.assertEqual(response.url, f'/horoscope/{sign}/')
