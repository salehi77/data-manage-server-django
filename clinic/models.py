from django.db import models


class ClinicModel(models.Model):
    clinicName = models.CharField(max_length=40)
    diagramModel = models.TextField(blank=True)
    diagramTree = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.clinicName
