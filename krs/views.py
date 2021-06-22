import random

# from typing import Any
from django.views.generic import TemplateView
from django.shortcuts import render
from .forms import AnswerForm


class Plus_im_10erPageView(TemplateView):
    template_name = 'plus_im_10er.html'
    success_html = 'plus_im_10er_check.html'
    no_of_tasks = 3

#     def __init__(self, **kwargs: Any) -> None:
#         super().__init__(**kwargs)
#         self.tasks = generate_plus10_tasks(no_of_tasks=self.no_of_tasks)

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
        print('task_list after get_context_data:\n', self.task_list)
        self.context = context
        return context

    def post(self, request):
        form = AnswerForm(request.POST)
        answered_tasks = []
        print('Doing the post')

        if form.is_valid():
            answers = form.cleaned_data
            total_correct_answers = 0

            # helper to get the form_field name
            index = 1

            for task in self.task_list:
                if index > self.no_of_tasks:
                    break
                # TBD: form.fields.items()
                answer = int(answers[f'answer_{index}'])
                print(f'answer_{index} in post: ', answer)
                print('task in post: ', task)
                x, y, correct_result = task
                print('x, y, correct_result: ', x, y, correct_result)
                if answer == correct_result:
                    total_correct_answers += 1
                answered_tasks.append((x, y, correct_result, answer,
                                       total_correct_answers))  # noqa
                print('answered_tasks: ', answered_tasks)
                index += 1

        return render(request,
                      self.success_html,
                      {'answered_tasks': answered_tasks}
                      )


class Plus_im_10er_checkPageView(TemplateView):
    template_name = 'plus_im_10er_check.html'


class HomePageView(TemplateView):
    template_name = 'home.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'


class AufgabenPageView(TemplateView):
    template_name = 'aufgaben.html'


class ZehnerraumPageView(TemplateView):
    template_name = 'zehnerraum.html'


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
