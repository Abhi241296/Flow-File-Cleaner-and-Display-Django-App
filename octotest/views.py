from django.shortcuts import render
from django.db.models import Q
from django.views.generic import TemplateView, ListView
from django.http import HttpResponse
from octotest.functions import handle_uploaded_file, clean_file, upload_data
from octotest.forms import FlowFile, CleanedData
from octotest.models import UploadCleanData

def index(request):
    #uploaded = False
    if request.method == "POST":
        Filetable = FlowFile(request.POST, request.FILES)
        if Filetable.is_valid():
            handle_uploaded_file(request.FILES['file'])
            clean_file(request.FILES['file'])
            model_instance = Filetable.save(commit=False)
            model_instance.save()
            #uploaded = True
            #return render(request, "upclean.html", {'form':ReadingData})
            return render(request,"home.html", {'alert_flag': True})
    
    else:
        Filetable = FlowFile()
        return render(request,"index.html",{'form':Filetable})

def upclean(request):
    if request.method == "POST":
        ReadingData = CleanedData(request.POST, request.FILES)
        if ReadingData.is_valid():
            upload_data(request.FILES['file'])
            #model_instance = ReadingData.save(commit=False)
            #model_instance.save()
            return render (request,"home.html", {'alert_flag': True})
    else:
        ReadingData = CleanedData()
        return render (request,"upclean.html", {'form':ReadingData})

class HomePageView(TemplateView):
    template_name = 'home.html'

class SearchView(TemplateView):
    template_name = 'search.html'

class SearchResults(ListView):
    model = UploadCleanData
    template_name = 'results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list =  UploadCleanData.objects.filter(
            Q(MPAN_Core__icontains=query)| Q(Meter_ID__icontains=query) | Q(Register_Reading__icontains=query)
        )
        return object_list