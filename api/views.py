from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Question
from .serializer import QuestionSerializer
import json


@api_view(['GET', 'POST'])
def question(request):
    if request.method == 'GET':
        question = Question.objects.all()
        serializer = QuestionSerializer(question, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            stat = {'status':'your question has been saved successfully'}
            stat.update(serializer.data)
            return Response(stat, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def question_name(request,name):
    question = Question.objects.filter(name__iexact=name)
    if question:
        serializer = QuestionSerializer(question, many=True)
        return Response(serializer.data)
    else:
        return Response({'status':'no search results found'})

@api_view(['GET'])
def question_type(request,qtype):
    question = Question.objects.filter(qtype__iexact=qtype)
    if question:
        serializer = QuestionSerializer(question, many=True)
        return Response(serializer.data)
    else:
        return Response({'status':'no search results found'})

@api_view(['GET'])
def question_date(request,date):
    try:
        date,month,year = date.split('-')
    except:
        return Response({'status':'invalid date format please refer from /help/teacher'})
    question = Question.objects.filter(timestamp__year=year, 
                         timestamp__month=month, 
                         timestamp__day=date)
    if question:
        serializer = QuestionSerializer(question, many=True)
        return Response(serializer.data)
    else:
        return Response({'status':'no search results found'})

@api_view(['GET'])
def teacher_help(request):
    data = {
        'filter all question': {
            'url': '/',
            'method': 'get',
        },
        'filter question by date':{
            'url': '/date/{day-month-year}',
            'method': 'get',
            'example url': '/date/20-10-2020'
        },
        'fileter by student name':{
            'url': '/name/{name_of_student}',
            'method': 'get',
            'example url': '/name/naman'
        },
        'filter by type of question':{
            'url': 'type/{question_type}',
            'method':'get',
            'example':'/type/math'
        }
    }
    return Response(data)

@api_view(['GET'])
def student_help(request):
    data = {
        'url': "/",
        'method':'post',
        'fields': "['Name','Question_type','Question_image','Question_text']",
        'optional field': 'Question_image',
        'help text': 'Send the data by filling the details of corresponding fields in the body'
    }
    return Response(data)

@api_view(['GET'])
def all_help(request):
    data = {
        'student help':{
            'method':'get',
            'url':'/help/student'
        },
        'teacher help':{
            'method':'get',
            'url':'/help/teacher'
        }
    }
    return Response(data)
