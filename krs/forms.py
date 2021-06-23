from django import forms
from django.core.exceptions import ValidationError


class AnswerForm(forms.Form):
    answer_1 = forms.IntegerField(label='answer', required=False)
    answer_2 = forms.IntegerField(label='answer', required=False)
    answer_3 = forms.IntegerField(label='answer', required=False)
    answer_4 = forms.IntegerField(label='answer', required=False)
    answer_5 = forms.IntegerField(label='answer', required=False)
    answer_6 = forms.IntegerField(label='answer', required=False)
    answer_7 = forms.IntegerField(label='answer', required=False)
    answer_8 = forms.IntegerField(label='answer', required=False)
    answer_9 = forms.IntegerField(label='answer', required=False)
    answer_10 = forms.IntegerField(label='answer', required=False)

    def clean_answers(self):
        if self.is_valid():
            answers = self.cleaned_data
            return answers
        raise ValidationError(message='Invalid value', code='invalid')

    def correct_answers(self, task_list, answers, no_of_tasks):
        total_correct_answers = 0
        answered_tasks = []

        # helper to get the form_field name
        index = 1

        for task in task_list:
            x, y, correct_result = task
            if index > no_of_tasks:
                break
            if answers[f'answer_{index}'] is None:
                answer = '?'
                answered_tasks.append((x, y, correct_result, answer,
                                       total_correct_answers))
                continue

            answer = int(answers[f'answer_{index}'])
            if answer == correct_result:
                total_correct_answers += 1
            answered_tasks.append((x, y, correct_result, answer,
                                   total_correct_answers))
            index += 1

        return answered_tasks
