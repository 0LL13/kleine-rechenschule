# krs/tests.py
# -*- coding: utf-8 -*-
from django.test import SimpleTestCase
# from django.urls import reverse


class SimpleTests(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        assert response.status_code == 200

    def test_about_page_status_code(self):
        response = self.client.get('/about/')
        assert response.status_code == 200

    def test_aufgaben_page_status_code(self):
        response = self.client.get('/aufgaben/')
        assert response.status_code == 200

    def test_zehnerraum_page_status_code(self):
        response = self.client.get('/zehnerraum/')
        assert response.status_code == 200

    def test_zwanzigerraum_page_status_code(self):
        response = self.client.get('/zwanzigerraum/')
        assert response.status_code == 200

    def test_hunderterraum_page_status_code(self):
        response = self.client.get('/hunderterraum/')
        assert response.status_code == 200

    def test_tausenderraum_page_status_code(self):
        response = self.client.get('/tausenderraum/')
        assert response.status_code == 200

    def test_kleines1x1_page_status_code(self):
        response = self.client.get('/kleines1x1/')
        assert response.status_code == 200

    def test_groszes1x1_page_status_code(self):
        response = self.client.get('/großes1x1/')
        assert response.status_code == 200

    def test_plus_im_10er_page_status_code(self):
        response = self.client.get('/plus_im_10er/')
        assert response.status_code == 200

    def test_plus_im_10er_check_page_status_code(self):
        response = self.client.get('/plus_im_10er_check/')
        assert response.status_code == 200

    def test_plus_im_10er_post_method(self):
        answers = {'answer_1': 3, 'answer_2': 7, 'answer_3': 6}
        tasks = [(0, 3, 3, 3, 1), (5, 1, 6, 7, 1), (4, 2, 6, 6, 2)]
        response = self.client.post(('/plus_im_10er/'),
                                    {'tasks': tasks, 'answers': answers})  # noqa
        self.assertContains(response, "Antworten prüfen")
        self.assertContains(response('answers'), (4, 2, 6, 6, 2))
