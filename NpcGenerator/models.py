from django.db import models


# Create your models here.
class Race(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Class(models.Model):
    name = models.CharField(max_length=200)
    race = models.ManyToManyField(Race)

    def __str__(self):
        return self.name


class Subclass(models.Model):
    name = models.CharField(max_length=200)
    klasa = models.ManyToManyField(Class)

    def __str__(self):
        return self.name


# class FinalModel(models.Model):
#     race = models.ForeignKey(Race, on_delete=models.CASCADE)
#     hero_class = models.ForeignKey(Class, on_delete=models.CASCADE)
#     Subclass = models.ForeignKey(Subclass, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return f'{self.race} {self.hero_class} {self.Subclass}'
