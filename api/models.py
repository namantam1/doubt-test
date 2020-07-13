from django.db import models

# Create your models here.
class Question(models.Model):
    name = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now=True)
    qtype = models.TextField()
    question = models.TextField()
    image = models.ImageField(upload_to='question_images')
