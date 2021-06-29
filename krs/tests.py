# krs/tests.py
# -*- coding: utf-8 -*-

from django.test import SimpleTestCase
from django.core.exceptions import ValidationError
from django.test import Client
from .forms import AnswerForm
from .views import Plus_Minus_in_10spacePageView


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

    def test_ten_space_page_status_code(self):
        response = self.client.get('/ten_space/')
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

    def test_plus_in_10space_page_status_code(self):
        response = self.client.get('/plus_in_10space/')
        assert response.status_code == 200

    def test_plus_in_10space_check_page_status_code(self):
        response = self.client.get('/plus_in_10space_check/')
        assert response.status_code == 200

    def test_minus_in_10space_page_status_code(self):
        response = self.client.get('/minus_in_10space/')
        assert response.status_code == 200

    def test_minus_in_10space_check_page_status_code(self):
        response = self.client.get('/minus_in_10space_check/')
        assert response.status_code == 200


class AnswerFormTest(SimpleTestCase):
    def test_AnswerForm_clean_answers(self):
        form = AnswerForm()

        with self.assertRaises(ValidationError):
            form.clean_answers()

    def test_AnswerForm_correct_answers(self):
        no_of_tasks = 3
        op = " + "
        answers = {'answer_1': 3, 'answer_2': 5, 'answer_3': 6}
        task_list = [(0, 3, op, 3), (5, 1, op, 6), (4, 2, op, 6)]

        form = AnswerForm()
        answered_tasks = form.correct_answers(task_list, answers, no_of_tasks)
        assert answered_tasks[no_of_tasks - 1][5] == 2

    def test_AnswerForm_correct_answers_break_bc_index_greater_no_of_tasks(self):  # noqa
        no_of_tasks = 0
        op = " + "
        answers = {'answer_1': 3, 'answer_2': 5, 'answer_3': 6}
        task_list = [(0, 3, op, 3), (5, 1, op, 6), (4, 2, op, 6)]

        form = AnswerForm()
        answered_tasks = form.correct_answers(task_list, answers, no_of_tasks)
        assert answered_tasks == []


class Plus_in_10spaceTests(SimpleTestCase):
    def test_plus_in_10space_post_method(self):
        answers = {'answer_1': 3, 'answer_2': 7, 'answer_3': 6}
        op = " + "
        tasks = [(0, 3, op, 3), (5, 1, op, 6), (4, 2, op, 6)]
        data = {'task_list': tasks, 'answers': answers}
        response = self.client.post(('/plus_in_10space/'), data)
        assert response.status_code == 200
        self.assertContains(response, "Antworten prüfen")

    def test_plus_in_10space_post_method_wo_tasks(self):
        c = Client()
        with self.assertRaises(AttributeError):
            c.post(('/plus_in_10space/'), [])


class Minus_in_10spaceTests(SimpleTestCase):
    def test_minus_in_10space_post_method(self):
        answers = {'answer_1': 3, 'answer_2': 7, 'answer_3': 6}
        op = " - "
        tasks = [(0, 3, op, 3), (5, 1, op, 6), (4, 2, op, 6)]
        data = {'task_list': tasks, 'answers': answers}
        response = self.client.post(('/minus_in_10space/'), data)
        assert response.status_code == 200
        self.assertContains(response, "Antworten prüfen")

    def test_minus_in_10space_post_method_wo_tasks(self):
        c = Client()
        with self.assertRaises(AttributeError):
            c.post(('/minus_in_10space/'), [])


class Plus_Minus_in_10spaceTests(SimpleTestCase):
    view = Plus_Minus_in_10spacePageView()

    def test_plus_minus_in_10space_get_context_data(self):
        context = self.view.get_context_data()
        assert 'task_list' in context

    def test_plus_minus_in_10space_post_method(self):
        answers = {'answer_1': 3, 'answer_2': 7, 'answer_3': 6}
        op = "operation"
        task_list = [(0, 3, op, 3), (5, 1, op, 6), (4, 2, op, 6)]
        data = {'task_list': task_list, 'answers': answers}
        response = self.client.post(('/plus_minus_in_10space/'), data)
        assert response.status_code == 200
        self.assertContains(response, "Antworten prüfen")

    def test_plus_minus_in_10space_post_method_wo_tasks(self):
        c = Client()
        with self.assertRaises(AttributeError):
            c.post(('/plus_minus_in_10space/'), [])
