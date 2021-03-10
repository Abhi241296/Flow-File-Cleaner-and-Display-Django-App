from django.db import models
from django.core.validators import RegexValidator
from datetime import datetime

class FlowFileForm(models.Model):
    file = models.FileField(upload_to = 'Files/')

    class Meta:
        db_table = "Filetable"
    
    def __str__(self):
        return self.file

class CleanedDataForm(models.Model):
    file = models.FileField(upload_to = 'Files/')

    class Meta:
        db_table = "ReadingData"
    
    def __str__(self):
        return self.file

class UploadCleanData(models.Model):
    objects = models.Manager()
    MPAN_Core = models.CharField(max_length=13)#, validators=[RegexValidator(r'^\d{1,10}$')])
    BSC_Validation_Status = models.CharField(max_length=1)
    Meter_ID = models.CharField(max_length=10)
    Reading_Type = models.CharField(max_length=1)
    Meter_Register_ID = models.CharField(max_length=2)
    Reading_Date_Time = models.DateTimeField(null=True, blank=True)
    Register_Reading = models.CharField(max_length=10)
    Meter_Reading_Flag = models.CharField(max_length=1)
    Reading_Method = models.CharField(max_length=1)
    file = models.FileField()

    class Meta:
        db_table = "UsageData"

    def __str__(self):
        return self.MPAN_Core

