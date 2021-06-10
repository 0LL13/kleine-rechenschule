# krs/views.py
import random
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.shortcuts import render
from .forms import ResultForm


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


class Plus_im_10erPageView(TemplateView):
    form_class = ResultForm
    template_name = 'plus_im_10er.html'
    success_html = 'plus_im_10er_check.html'

    def tasks(self):
        task_list = []
        for i in range(10):
            while True:
                x = random.randint(0, 9)
                y = random.randint(0, 9)
                z = x + y
                if z <= 10:
                    task_list.append((x, y, z))
                    break
        return task_list

    def get_context_data(self, **kwargs):
        context = super(Plus_im_10erPageView, self).get_context_data(**kwargs)  # noqa
        task_list = self.tasks()
        context['tasks'] = task_list
        self.context = context

        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(self.success_html)

        return render(request, self.template_name, {'form': form})


class Plus_im_10er_checkPageView(TemplateView):
    template_name = 'plus_im_10er_check.html'

    def get_context_data(self, **kwargs):
        context = super(Plus_im_10er_checkPageView, self).get_context_data(**kwargs)  # noqa
        answer_list = context['answer_list']
        task_list = context['task_list']
        return answer_list, task_list
