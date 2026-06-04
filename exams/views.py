from django.shortcuts import render, redirect
from .models import Student
from .models import Result
from .models import Exam
from .models import CheatingReport
from django.contrib.admin.views.decorators import staff_member_required

# Home Page
def home(request):
    return render(request, 'home.html')


# Login Page + Authentication
def login(request):

    if request.method == "POST":

        email = request.POST.get("email")
        password = request.POST.get("password")

        try:

            student = Student.objects.get(
                email=email,
                password=password
            )

            # Check if student is blocked
            if student.is_blocked:

                return render(
                    request,
                    'login.html',
                    {
                        'error':
                        'Your account has been blocked by the administrator.'
                    }
                )

            request.session['student_name'] = student.name
            request.session['student_id'] = student.id

            return redirect('/dashboard/')

        except Student.DoesNotExist:

            return render(
                request,
                'login.html',
                {
                    'error':
                    'Invalid Email or Password'
                }
            )

    return render(
        request,
        'login.html'
    )
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
    exams = Exam.objects.all()
    for exam in exams:
        exam.question_count = Question.objects.filter(exam=exam).count()
    return render(request, 'dashboard.html', {'exams': exams})
#profile page
def profile(request):

    student_name = request.session.get('student_name')

    student = Student.objects.get(
        name=student_name
    )

    results = Result.objects.filter(
        student_name=student_name
    ).order_by('date')

    scores = []
    labels = []

    for r in results:
        scores.append(r.score)
        labels.append(r.date.strftime("%d-%m"))

    return render(
        request,
        'profile.html',
        {
            'student': student,
            'scores': scores,
            'labels': labels,
            'total_exams': results.count()
        })

# Exam Page
from .models import Question

def exam(request, exam_id):

    exam = Exam.objects.get(id=exam_id)

    questions = Question.objects.filter(
        exam=exam
    ).order_by('?')

    if request.method == "POST":

        score = 0
        total = questions.count()

        review_data = []

        for q in questions:

            selected = request.POST.get(
                f"q{q.id}"
            )

            is_correct = (
                selected == q.correct_option
            )

            if is_correct:
                score += 1

            review_data.append({
                'question': q.question_text,
                'student_answer': selected,
                'correct_answer': q.correct_option,
                'is_correct': is_correct
            })

        student_name = request.session.get(
            'student_name',
            'Guest'
        )

        Result.objects.create(
            student_name=student_name,
            score=score,
            total=total
        )

        percentage = round(
            (score / total) * 100,
            2
        )

        return render(
            request,
            'result.html',
            {
                'score': score,
                'total': total,
                'percentage': percentage,
                'review_data': review_data
            }
        )

    return render(
        request,
        'exam.html',
        {
            'questions': questions,
            'exam': exam
        }
    )


#logout
from django.contrib.auth import logout

def logout_user(request):
    logout(request)
    return redirect('/')

#history
def history(request):
    
    student_name = request.session.get(
        'student_name'
    )

    results = Result.objects.filter(
        student_name=student_name
    ).order_by('-date')

    return render(
        request,
        "history.html",
        {"results":results}
    )

#leaderboard
def leaderboard(request):

    results = Result.objects.all().order_by('-score')[:10]

    return render(request, "leaderboard.html", {"results": results})



from django.db.models import Avg
@staff_member_required
def admin_dashboard(request):

    total_students = Student.objects.count()

    total_exams = Exam.objects.count()

    total_results = Result.objects.count()

    total_questions = Question.objects.count()

    cheating_cases = CheatingReport.objects.count()

    context = {

        'total_students':
        total_students,

        'total_exams':
        total_exams,

        'total_results':
        total_results,

        'total_questions':
        total_questions,

        'cheating_cases':
        cheating_cases
    }

    return render(
        request,
        'admin_dashboard.html',
        context
    )

