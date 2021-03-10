from django import forms
from octotest.models import FlowFileForm, CleanedDataForm

class FlowFile(forms.ModelForm):
    class Meta:
        model = FlowFileForm
        fields = "__all__"

class CleanedData(forms.ModelForm):
    class Meta:
        model = CleanedDataForm
        fields = ['file']