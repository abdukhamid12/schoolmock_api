from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.utils import timezone
from datetime import timedelta
from .models import School, ClassGroup, Student, Test, Question, Result
from .serializers import SchoolSerializer, ClassGroupSerializer, StudentSerializer, TestSerializer, QuestionSerializer, ResultSerializer

# ViewSet для школ
class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer


# ViewSet для классов
class ClassGroupViewSet(viewsets.ModelViewSet):
    queryset = ClassGroup.objects.all()
    serializer_class = ClassGroupSerializer


# ViewSet для учеников
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


# ViewSet для тестов
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.utils import timezone
from datetime import timedelta
from .models import School, ClassGroup, Student, Test, Question, Result
from .serializers import SchoolSerializer, ClassGroupSerializer, StudentSerializer, TestSerializer, QuestionSerializer, ResultSerializer

class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

    @action(detail=True, methods=['post'])
    def start_test(self, request, pk=None):
        test = self.get_object()
        student_id = request.data.get('student_id')

        try:
            student = Student.objects.get(id=student_id)
        except Student.DoesNotExist:
            return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)

        # Проверяем, что текущее время не раньше времени начала теста
        current_time = timezone.now()
        if current_time < test.start_time:
            return Response({'error': 'Test has not started yet. Please wait until the start time.'}, status=status.HTTP_400_BAD_REQUEST)

        # Если время начала теста пришло, устанавливаем время начала и окончания
        start_time = timezone.now()
        end_time = start_time + timedelta(minutes=test.duration)

        return Response({
            'message': f'Test started for {student.first_name} {student.last_name}',
            'start_time': start_time,
            'end_time': end_time
        }, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def submit_test(self, request, pk=None):
        test = self.get_object()
        student_id = request.data.get('student_id')
        score = request.data.get('score')

        try:
            student = Student.objects.get(id=student_id)
        except Student.DoesNotExist:
            return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)

        result = Result.objects.create(student=student, test=test, score=score)
        result.save()

        return Response({'message': 'Test submitted', 'result_id': result.id}, status=status.HTTP_200_OK)



# ViewSet для вопросов
class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


# ViewSet для результатов теста
class ResultViewSet(viewsets.ModelViewSet):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer

    # Экшн для начала теста с таймером
    @action(detail=True, methods=['post'])
    def start_test(self, request, pk=None):
        test = self.get_object()
        student_id = request.data.get('student_id')

        try:
            student = Student.objects.get(id=student_id)
        except Student.DoesNotExist:
            return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)

        start_time = timezone.now()
        end_time = start_time + timedelta(minutes=test.duration)

        return Response({
            'message': f'Test started for {student.first_name} {student.last_name}',
            'start_time': start_time,
            'end_time': end_time
        }, status=status.HTTP_200_OK)

    # Экшн для завершения теста и сохранения результата
    @action(detail=True, methods=['post'])
    def submit_test(self, request, pk=None):
        test = self.get_object()
        student_id = request.data.get('student_id')
        score = request.data.get('score')

        try:
            student = Student.objects.get(id=student_id)
        except Student.DoesNotExist:
            return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)

        result = Result.objects.create(student=student, test=test, score=score)
        result.save()

        return Response({'message': 'Test submitted', 'result_id': result.id}, status=status.HTTP_200_OK)

# front views

def home(request):
    return render(request, 'schoolmock_front/index.html')

def write_id(request):
    return render(request, 'schoolmock_front/write_id.html')

def waiting_page(request):
    return render(request, 'schoolmock_front/waiting.html')