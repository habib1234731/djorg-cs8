from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4
class Note(models.Model):
    id = models.UUIDField(primary_key=True, default = uuid4, editable=False)
    #Todo: Add user/author who created it
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    #Todo: Tagging system or categories
    category = models.CharField(max_length=20)

class PersonalNote(Note):
    user = models.ForeignKey(User,on_delete=models.CASCADE)