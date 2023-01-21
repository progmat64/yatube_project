from django.db import models

# Create your models here.
# models.py
'''
class Contact(models.Model):
    # К полю name подключаем валидатор, проверяющий, что поле не пустое.
    name = models.CharField(max_length=100, validators=[validate_not_empty])
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    # К полю body тоже подключаем валидатор, проверяющий, что поле не пустое.
    body = models.TextField(validators=[validate_not_empty])
    is_answered = models.BooleanField(default=False)
'''