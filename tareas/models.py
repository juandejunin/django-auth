# from email.policy import default
# from multiprocessing.spawn import import_main_path
# from ssl import create_default_context
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    create = models.DateField(auto_now_add=True)
    dateCompleted = models.DateField(null=True, blank=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

#usuario juanci contraseña 1234asdf

#cuando se utilice el modelo voy a utilizar un metodo self, esto nos permite elegir como se define la tarea en la vista del panel de administracion

    def __str__(self):
        return self.title + ' - by '+ self.user.username