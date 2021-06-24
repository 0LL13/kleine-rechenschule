import random

from django.views.generic import TemplateView
from django.shortcuts import render
from .forms import AnswerForm


class Plus_in_10spacePageView(TemplateView):
    template_name = 'plus_in_10space.html'
    success_html = 'plus_in_10space_check.html'
    no_of_tasks = 3

    @classmethod
    def generate_plus10_tasks(self):
        """
        Generate tasks containing two addends with a sum less or equal 10.
        """
        task_list = []
        for _ in range(self.no_of_tasks):
            while True:
                x = random.randint(0, 9)
                y = random.randint(0, 9)
                result = x + y
                if result <= 10:
                    task_list.append((x, y, result))
                    break
        self.task_list = task_list
        return task_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # noqa
        context['task_list'] = self.generate_plus10_tasks()
        self.context = context
        return context

    def post(self, request):
        task_list = self.task_list
        no_of_tasks = self.no_of_tasks
        form = AnswerForm(request.POST)
        answers = form.clean_answers()
        print('answers', answers)
        answered_tasks = form.correct_answers(task_list, answers, no_of_tasks)

        return render(request,
                      self.success_html,
                      {'answered_tasks': answered_tasks}
                      )


class Plus_in_10space_checkPageView(TemplateView):
    template_name = 'plus_in_10space_check.html'


class Minus_in_10spacePageView(TemplateView):
    template_name = 'minus_in_10space.html'
    success_html = 'minus_in_10space_check.html'
    no_of_tasks = 3

    @classmethod
    def generate_minus10_tasks(self):
        """
        Generate tasks containing a minuend and a subtrahend with a difference
        higher or equal 0.
        """
        task_list = []
        for _ in range(self.no_of_tasks):
            while True:
                x = random.randint(0, 9)
                y = random.randint(0, 9)
                result = x - y
                if result >= 0:
                    task_list.append((x, y, result))
                    break
        self.task_list = task_list
        return task_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # noqa
        context['task_list'] = self.generate_minus10_tasks()
        self.context = context
        return context

    def post(self, request):
        task_list = self.task_list
        no_of_tasks = self.no_of_tasks
        form = AnswerForm(request.POST)
        answers = form.clean_answers()
        print('answers', answers)
        answered_tasks = form.correct_answers(task_list, answers, no_of_tasks)

        return render(request,
                      self.success_html,
                      {'answered_tasks': answered_tasks}
                      )


class Minus_in_10space_checkPageView(TemplateView):
    template_name = 'minus_in_10space_check.html'


class HomePageView(TemplateView):
    template_name = 'home.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'


class AufgabenPageView(TemplateView):
    template_name = 'aufgaben.html'


class TenSpacePageView(TemplateView):
    template_name = 'ten_space.html'


class ZwanzigerraumPageView(TemplateView):
    template_name = 'zwanzigerraum.html'


class HunderterraumPageView(TemplateView):
    template_name = 'hunderterraum.html'


class TausenderraumPageView(TemplateView):
    template_name = 'tausenderraum.html'


class Kleines1x1PageView(TemplateView):
    template_name = 'kleines1x1.html'


class Groszes1x1PageView(TemplateView):
    template_name = 'großes1x1.html'
