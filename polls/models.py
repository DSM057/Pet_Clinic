from django.db import models
from django.contrib.auth.models import User


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField('Імя',max_length=25)
    surname = models.CharField('Прізвище', max_length=35)
    number = models.CharField('Номер',max_length=10)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Кліент'
        verbose_name = 'Кліента'
        ordering = ['name']

class TypeAnimal(models.Model):
    animals = ((None, 'Виберіть тип тварини'), ('cat', 'Кішка'), ('dog', 'Собака'), ('hare', 'Заєц'), ('shinshila', 'Шиншила'))
    animal = models.CharField(max_length=20, choices=animals)
    def __str__(self):
        return self.animal

    class Meta:
        verbose_name_plural = 'Тваринки'
        verbose_name = 'Тваринка'
        ordering = ['animal']

class ClientAnimal(models.Model):
    age = models.CharField('Вік тваринки',max_length=3)
    description = models.TextField('Опис тваринки')
    client = models.ForeignKey(Client,on_delete=models.PROTECT)
    typeanimal = models.ForeignKey(TypeAnimal, on_delete=models.PROTECT)

    def __str__(self):
        return self.age

    class Meta:
        verbose_name_plural = 'Тваринка клієнта'
        verbose_name = 'Тваринка клієнта'
        ordering = ['typeanimal']

class Booking(models.Model):
    time = models.CharField('Час прийому',max_length=20)
    date = models.DateTimeField('Дата')
    client = models.ForeignKey(Client,on_delete=models.PROTECT , null=True, blank=True)


    def __str__(self):
        return self.time

    class Meta:
        verbose_name_plural = 'Запис на прийом'
        verbose_name = 'Запис на прийом'



