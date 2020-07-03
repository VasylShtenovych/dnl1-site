from django.db import models
from teachers.models import Lesson as LessonList, Teacher
import datetime


class ClassSchedule(models.Model):
    class_title = models.CharField('Клас', max_length=5)

    objects = models.Manager()

    def __str__(self):
        return self.class_title

    class Meta:
        verbose_name = 'Розклад класу'
        verbose_name_plural = 'Розклади класів'

WEEKDAYS = (
        ('Mo', 'Понеділок'),
        ('Tu', 'Вівторок'),
        ('We', 'Середа'),
        ('Th', 'Четвер'),
        ('Fr', 'П\'ятниця'),
    )
class ClassLesson(models.Model):

    LESSONINDEXES = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
    )
    day = models.CharField(
        'День',
        max_length=2,
        choices=WEEKDAYS,
        blank=True,
        null=True
    )
    index = models.CharField(
        'Номер уроку',
        max_length=1,
        choices=LESSONINDEXES,
        blank=True,
        null=True
    )
    title = models.ForeignKey(LessonList, on_delete=models.CASCADE)
    class_consisting = models.ForeignKey(ClassSchedule, on_delete=models.CASCADE)
    lesson_teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.title.title
