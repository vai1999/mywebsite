import email
from urllib import request
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
# from django.core.mail import send_mail,get_connection


def home(req):
    return render(req, 'home.html')


def about(req):
    return render(req, "about.html")


def course(req):
    return render(req, "course.html")


def gallery(req):
    return render(req, "gallery.html")


def contact(req):
    return render(req, "contact.html")


def ragist(req):
    return render(req, "ragist.html")


def ragistTask(req):
    from . models import Student
    # from django.core.mail import EmailMessage
    # email = EmailMessage('Hello', 'World', to=['rishimahobiya199@gmail.com'])
    # email.send()
    ob = Student()
    ob.fname = req.GET.get("fname")
    ob.lname = req.GET.get("lname")
    ob.email = req.GET.get("email")
    ob.password = req.GET.get("password")
    ob.mob = req.GET.get("mob")
    ob.save()
   
    return redirect("/firstapp/login")


def login(req):
    return render(req, "login.html")


def loginTask(req):
    global email
    global password
    email = req.GET.get("email")
    password = req.GET.get("password")
    from firstapp.models import Student
    db = Student.objects.all()
    for i in db:
          # if role==i.role:
            if email == email:
                if password == password:
                    return redirect("/firstapp/student")
                else:
                    return redirect("/login")
            else:
                return HttpResponse("Please Select right role")
    else:
            return redirect("/registration")


def db(req):
    from firstapp.models import Student
    rec = Student.objects.filter(email=email)
    return render(req, "db.html", {'rec': rec})


def student(req):
    from firstapp.models import Student
    rec = Student.objects.filter(email=email)
    return render(req, 'student.html', {'rec': rec})


def faculty(req):
    from firstapp.models import Faculty
    rec = Faculty.objects.filter(email=email)
    return render(req, 'faculty.html', {'rec': rec})


def updateStudent(req):
    from . models import Student
    id = req.GET.get("id")
    ob = Student.objects.get(id=id)
    ob.fname = req.GET.get("fname")
    ob.lname = req.GET.get("lname")
    ob.email = req.GET.get("email")
    ob.password = req.GET.get("Password")
    ob.mob = req.GET.get("mob")
    ob.save()

    return render(request, "markSheet.html")


def markSheet(request):
    from firstapp.models import Student
    rec = Student.objects.filter(email=email)
    if request.method == "POST":
        s1 = eval(request.POST.get('subject1'))
        s2 = eval(request.POST.get('subject2'))
        s3 = eval(request.POST.get('subject3'))
        s4 = eval(request.POST.get('subject4'))
        s5 = eval(request.POST.get('subject5'))
        t = s1+s2+s3+s4+s5
        p = t*100/500
        if p >= 60:
            d = "First Div"
        elif p >= 48:
            d = "Second Div"
        elif p >= 35:
            d = "Fail"
        data = {
            'total': t,
            'per': p,
            'div': d,
            's1': s1,
            's2': s2,
            's3': s3,
            's4': s4,
            's5': s5
        }
        return render(request, "markSheet.html", data)
    return render(request, "markSheet.html")


# Create your views here.
