from django.db import models
from django.contrib.auth.models import User

class todo(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    todo_name=models.CharField(max_length=1000)
    status=models.BooleanField(default=False)
    
    def _str_(self):
        return self.todo_name