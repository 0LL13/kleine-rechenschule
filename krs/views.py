# krs/views.py
import random
# from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, ListView
from django.shortcuts import render
from .forms import AnswerForm


class Plus_im_10erPageView(TemplateView):
    form_class = AnswerForm
    template_name = 'plus_im_10er.html'
    success_html = 'plus_im_10er_check.html'
    task_list = []

    @classmethod
    def tasks(self):
        task_list = []
        for i in range(3):
            while True:
                x = random.randint(0, 9)
                y = random.randint(0, 9)
                z = x + y
                if z <= 10:
                    task_list.append((x, y, z))
                    break
        self.task_list = task_list
        return task_list

    def get_context_data(self, **kwargs):
        context = super(Plus_im_10erPageView, self).get_context_data(**kwargs)  # noqa
        task_list = self.tasks()
        context['tasks'] = task_list
        print('task_list after get_context_data:\n', task_list)
        self.context = context

        return context

    def post(self, request):
        form = AnswerForm(request.POST)
        tasks_w_answers = list()
        print('Doing the post')
        print('self.task_list:', self.task_list)
        print('form.is_valid():', form.is_valid())
        if form.is_valid():
            answers = form.cleaned_data
            tasks = self.task_list
            index = 1
            counter = 0
            for task in tasks:
                print('task in post:', task)
                answer = int(answers[f'answer_{index}'])
                print('answer:', answer)
                x, y, z = task
                if z == answer:
                    counter += 1
                task_new = (*task, answer, counter)
                print('task_new:', task_new)
                tasks_w_answers.append(task_new)
                index += 1

        return render(request, self.success_html, {'form': form,
                                                   'answers': answers,
                                                   'tasks': tasks_w_answers}) # noqa


class Plus_im_10er_checkPageView(ListView):
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
