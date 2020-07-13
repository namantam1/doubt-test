from rest_framework.serializers import HyperlinkedModelSerializer
from rest_framework import serializers
from .models import Question

class QuestionSerializer(HyperlinkedModelSerializer):
    Date_and_time = serializers.DateTimeField(format="%d-%m-%Y %H:%M",required=False,source='timestamp')
    Name = serializers.CharField(source='name')
    Question_type = serializers.CharField(source='qtype')
    Question_image = serializers.ImageField(source='image',required=False)
    Question_text = serializers.CharField(source='question')
    class Meta:
        model = Question
        fields = ['Date_and_time','Name','Question_type','Question_image','Question_text']