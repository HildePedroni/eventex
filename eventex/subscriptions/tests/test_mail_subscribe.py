from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Hildebrando Pedroni', cpf='12345678901',
                    email='hilde.pedroni@gmail.com', phone='19-99759-7552')
        self.response = self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_sbscription_email_from(self):
        expect = 'contato@eventex.com'
        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com', 'hilde.pedroni@gmail.com']
        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            'Hildebrando Pedroni',
            '12345678901',
            'hilde.pedroni@gmail.com',
            '19-99759-7552',
        ]
        
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
