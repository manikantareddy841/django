from django.shortcuts import render
from .models import feedbackdata
from .forms import feedbackform
from django.http.response import HttpResponse

def feedback_view(request):
    if request.method=='GET':
        fform=feedbackform()
        feedbacks=feedbackdata.objects.all()
        return render(request,'feedback.html',{'abcd':fform,'feedbacks':feedbacks})
    else:
        fform=feedbackform(request.POST)
        if fform.is_valid():
            name1=request.POST.get('name')
            rating1=request.POST.get('rating')
            feedback1=request.POST.get('feedback')
            data=feedbackdata(
                name=name1,
                rating=rating1,
                feedback=feedback1
            )
            data.save()
            fform=feedbackform()
            feedbacks=feedbackdata.objects.all()
            return render(request,'feedback.html',{'abcd':fform,'feedbacks':feedbacks})
        else:
            return HttpResponse('user missed data')

# Create your views here.
