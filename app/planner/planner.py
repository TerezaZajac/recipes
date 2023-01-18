from django.db import models

# Create your models here.

class Tag:
    label = models.CharField(max_length=200)

class Course:
    title = models.CharField(max_length=200)
    label = models.ForeignKey(Tag, on_delete=models.CASCADE)

class Unit:
    unit = models.FloatField(default=0)

class Ingredience:
    name = models.CharField(max_length=200)

class Recipe:
    title = models.ForeignKey(Course, on_delete=models.CASCADE)
    label = models.ForeignKey(Tag, on_delete=models.CASCADE)
    ingredience = models.ForeignKey(Ingredience, on_delete=models.CASCADE)
    instruction = models.CharField(max_length=2000)

