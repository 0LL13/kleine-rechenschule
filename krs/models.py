# import random
from django.db import models


class PlusTaskModel(models.Model):
    x = models.IntegerField(default=3)
    y = models.IntegerField(default=5)
    res = models.IntegerField(default=8)
    task = models.CharField(max_length=10, default=f"{x} + {y} = ")


#     while True:
#         x = random.randint(0, 9)
#         y = random.randint(0, 9)
#         z = x + y
#         point = [x, y, z]
#         if z <= 10:
#             break
#
#     question = f"{x} + {y} = "
#     result = f"{z}"
#     task = (question, result)
#     answer = models.CharField(max_length=2)
