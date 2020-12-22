from django.shortcuts import render
from .models import Profile
from django.http import HttpResponse
from django.template import loader
import pdfkit
# config = pdfkit.configuration(wkhtmltopdf=r"C:\Users\sgouldson.CASPIAN71\Documents\coding\udemy\django_course\CV_generator\wkhtmltopdf\bin")
import io
import os

# Create your views here.

def accept(request):
    if request.method == "POST":
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        phone = request.POST.get("phone", "")
        summary = request.POST.get("summary", "")
        degree = request.POST.get("degree", "")
        school = request.POST.get("school", "")
        university = request.POST.get("university", "")
        previous_work = request.POST.get("previous_work", "")
        skills = request.POST.get("skills", "")

        profile = Profile(name=name, email=email, phone=phone, summary=summary, degree=degree, school=school, university=university, previous_work=previous_work, skills=skills)
        profile.save()

    return render(request, 'pdf/accept.html')

def resume(request,id):
    user_profile = Profile.objects.get(pk=id)
    template = loader.get_template('pdf/resume.html')
    html = template.render({'user_profile':user_profile})
    options ={
        'page-size':'Letter',
        'encoding':"UTF-8",
    }

    config = pdfkit.configuration(wkhtmltopdf=r'C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe')

    pdf = pdfkit.from_string(html,False,options=options,configuration=config)
    response = HttpResponse(pdf,content_type='application/pdf')
    response['Content-Disposition'] ='attachment;filename=resume.pdf'

    return response

def list(request):
    profiles = Profile.objects.all()
    return render(request, 'pdf/list.html', {'profiles': profiles})