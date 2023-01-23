from django.db import models

# Create your models here.

class Tag(models.Model):
    label = models.CharField(max_length=200)

    def __str__(self):
        return self.label

class Course(models.Model):
    title = models.CharField(max_length=200)
    label = models.ForeignKey(Tag, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Unit(models.Model):
    unit = models.FloatField(default=0)

    def __str__(self):
        return self.unit

class Ingredience(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.ForeignKey(Course, on_delete=models.CASCADE)
    label = models.ForeignKey(Tag, on_delete=models.CASCADE)
    ingredience = models.ForeignKey(Ingredience, on_delete=models.CASCADE)
    instruction = models.CharField(max_length=2000)

    def __str__(self):
        return self.title


