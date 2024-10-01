from django.db import models
from django.utils import timezone
from datetime import timedelta

class School(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ClassGroup(models.Model):
    name = models.CharField(max_length=50)
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='classes')

    def __str__(self):
        return f'{self.name} - {self.school.name}'


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    class_group = models.ForeignKey(ClassGroup, on_delete=models.CASCADE, related_name='students')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Test(models.Model):
    name = models.CharField(max_length=100)
    class_group = models.ForeignKey(ClassGroup, on_delete=models.CASCADE, related_name='tests')
    max_score = models.IntegerField()
    duration = models.IntegerField(default=60)  # Длительность теста в минутах
    start_time = models.DateTimeField()  # Дата и время начала теста

    def __str__(self):
        return self.name



class Question(models.Model):
    text = models.TextField()
    score = models.IntegerField()  # Балл за вопрос в зависимости от сложности
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='questions')

    def __str__(self):
        return f'Question: {self.text} - Score: {self.score}'


class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    score = models.IntegerField()
    completion_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.student.first_name} {self.student.last_name} - {self.test.name} - Score: {self.score}'
