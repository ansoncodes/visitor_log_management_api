from django.db import models

# Create your models here.

class Visitor(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    purpose = models.CharField(max_length=250)
    check_in_time = models.DateTimeField(auto_now_add=True)
    check_out_time = models.DateTimeField(null = True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.phone}"