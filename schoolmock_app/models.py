from django.db import models
from django.utils import timezone

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



class TeacherInput(models.Model):
    language = models.TextField(max_length=255)
    difficulty = models.TextField(max_length=255)
    subject_name = models.TextField(max_length=255)
    class_name = models.IntegerField()
    quarter = models.TextField(max_length=255)
    information = models.TextField(max_length=500)

    def __str__(self):
        return f'{self.class_name} {self.subject_name} {self.quarter}'


# Renamed Question model related to TeacherInput
class TeacherQuestion(models.Model):
    category = models.ForeignKey(TeacherInput, on_delete=models.CASCADE, related_name="questions")
    theme = models.CharField(max_length=255)
    question_level = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.category} {self.theme}'


class Option(models.Model):
    question = models.ForeignKey(TeacherQuestion, on_delete=models.CASCADE, related_name='options')  # Updated to use TeacherQuestion
    answer = models.CharField(max_length=100)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.answer