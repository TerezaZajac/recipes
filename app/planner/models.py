from django.db import models

# Create your models here.

class Tag(models.Model):
    label = models.CharField(max_length=200)

class Course(models.Model):
    title = models.CharField(max_length=200)
    label = models.ForeignKey(Tag, on_delete=models.CASCADE)

class Unit(models.Model):
    unit = models.FloatField(default=0)

class Ingredience(models.Model):
    name = models.CharField(max_length=200)

class Recipe(models.Model):
    title = models.ForeignKey(Course, on_delete=models.CASCADE)
    label = models.ForeignKey(Tag, on_delete=models.CASCADE)
    ingredience = models.ForeignKey(Ingredience, on_delete=models.CASCADE)
    instruction = models.CharField(max_length=2000)


