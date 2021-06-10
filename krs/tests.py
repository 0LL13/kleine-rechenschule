# krs/tests.py
# -*- coding: utf-8 -*-
from django.test import SimpleTestCase


class SimpleTests(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        assert response.status_code == 200

    def test_about_page_status_code(self):
        response = self.client.get('/about/')
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
