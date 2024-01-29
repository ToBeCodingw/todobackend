from django.db import models

class Todo(models.Model):
    id = models.AutoField(primary_key=True)
    userid = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    done = models.BooleanField(default=False)
    regdate = models.DateTimeField(auto_now_add=True)
    moddate = models.DateTimeField(null=True)
