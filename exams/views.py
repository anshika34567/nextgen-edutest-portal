from django.shortcuts import render, redirect
from .models import Student


# Home Page
def home(request):
    return render(request, 'home.html')


# Login Page + Authentication
def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            student = Student.objects.get(email=email, password=password)
            return redirect('/dashboard/')
        except:
            return render(request, 'login.html', {'error': 'Invalid Email or Password'})

    return render(request, 'login.html')


# Register Page
def register(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        course = request.POST.get("course")

        Student.objects.create(
            name=name,
            email=email,
            password=password,
            course=course
        )

        return redirect('/login/')

    return render(request, 'register.html')


# Dashboard Page
def dashboard(request):
    return render(request, 'dashboard.html')

# Exam Page
from .models import Question

def exam(request):

    questions = Question.objects.all()
    if request.method == "POST":
    
        score = 0
        total = questions.count()

        for q in questions:

            selected = request.POST.get(str(q.id))

            if selected == q.correct_option:
                score += 1

        return render(request,'result.html',{'score':score,'total':total})

    return render(request,'exam.html',{'questions':questions})