from django.contrib import admin
from .models import FlowFileForm, CleanedDataForm, UploadCleanData

class FlowAdmin(admin.ModelAdmin):
    list_display = ("file",)

class CleanAdmin(admin.ModelAdmin):
    list_display = ("file",)

class UploadAdmin(admin.ModelAdmin):
    list_display = ("MPAN_Core", "BSC_Validation_Status", "Meter_ID", "Reading_Type", "Meter_Register_ID", "Reading_Date_Time", "Register_Reading", "Meter_Reading_Flag", "Reading_Method", "file",)

admin.site.register(FlowFileForm, FlowAdmin)
admin.site.register(CleanedDataForm, CleanAdmin)
admin.site.register(UploadCleanData, UploadAdmin)