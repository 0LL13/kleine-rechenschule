# from random import random
# from collections import defaultdict
from django import forms


class AnswerForm(forms.Form):
    answer = forms.CharField(label='answer', required=False)


# class AnswerForm(forms.Form):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.label_suffix = ""
#
#     calcs = "3 + 5 = "
#     answer = forms.CharField(label=calcs, max_length=2)
#

# class PlusCalcsForm(forms.Form):
#
#     def generate_plus_calcs(self):
#         # https://docs.python.org/3/library/collections.html
#         d = defaultdict(int)
#         calcs_w_results = list()
#         for i in range(10):
#             while True:
#                 x = random.randint(0, 9)
#                 y = random.randint(0, 9)
#                 point = (x, y)
#                 z = x + y
#                 d[x] += 1
#                 d[y] += 1
#                 if z <= 10:
#                     if d[x] <= 3 and d[y] <= 3:
#                         calcs_w_results.append((point, z))
#                         break
#                     else:
#                         d[x] -= 1
#                         d[y] -= 1
#
#         return calcs_w_results
#
#     def __init__(self, *args, **kwargs):
#         super(PlusCalcs, self).__init__(*args, **kwargs)
#         calcs = self.generate_plus_calcs()
#         for i, calc in enumerate(calcs):
#             problem = 'calc[0][0] + calc[0][1] = '
#             self.fields[i] = forms.CharField(label=problem)
