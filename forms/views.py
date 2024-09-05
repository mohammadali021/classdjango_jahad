from django.http import HttpResponse
from django.shortcuts import render

from forms.models import FormModel
from django.contrib import messages


def index(request):
    if request.method == 'POST':
        data = request.POST
        alldata = FormModel.objects.all()

        # for i in alldata:
        #     if request.POST['content'] in i.content:
        #         return HttpResponse('تکراریه')
        #     else:
        FormModel.objects.create(title=data['title'], content=data['content'])

    return render(request, "forms/Forms.html", context={'data': FormModel.objects.all()})

def viewoky(request):
    return render(request, "forms/index.html")
# Create your views here.
