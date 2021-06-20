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
        print('context:\n', context)
        self.context = context

        return context

    def post(self, request):
        form = AnswerForm(request.POST)
        print('Doing the post')
        print('form:', form)
        # print('form["answer"]:', form["answer"])
        print('form.is_valid():', form.is_valid())
        if form.is_valid():
            answers = form.cleaned_data
            print('answers:', answers)

        return render(request, self.success_html, {'form': form, 'answers': answers}) # noqa


class Plus_im_10er_checkPageView(ListView):
    template_name = 'plus_im_10er_check.html'

    def get_queryset(self, request):
        answer_list = request.POST.get('answers')
        tasks = request.POST.get('tasks')
        print("Now in plus_im_10er_check")
        return answer_list, tasks

    def post_list(request):
        answer_list = request.POST.get()
        return render(request, 'plus_im_10er.html', answer_list)


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
