import unittest
from flask import url_for
from app import app  # Імпортуємо ваш Flask-додаток


class FlaskAppTestCase(unittest.TestCase):

    def setUp(self):
        """Настроюємо тестовий клієнт перед кожним тестом"""
        self.app = app.test_client()
        self.app.testing = True  # Встановлюємо режим тестування

        self.app_context = app.test_request_context()
        # self.app_context.push()

    def test_main_route(self):
        """Тестуємо головний маршрут"""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)  # Перевіряємо статус-код
        self.assertIn(b'Hello, world!', response.data)  # Перевіряємо наявність тексту у відповіді

    def test_homepage(self):
        """Тестуємо домашню сторінку"""
        response = self.app.get('/homepage')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'This is your homepage :)', response.data)

    def test_greetings(self):
        """Тестуємо маршрут привітання"""
        response = self.app.get('/hi/John?age=30')

        with self.app_context:
            url_with_get_param = url_for("greetings", name="John", age=30)
            response = self.app.get(url_with_get_param)

        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome name=\'JOHN\' age=\'30\'!', response.data)

    def test_admin_redirect(self):
        """Тестуємо редирект на адміністратора"""
        response = self.app.get('/admin', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Welcome name='ADMINISTRATOR' age=None!", response.data)


if __name__ == '__main__':
    unittest.main()
