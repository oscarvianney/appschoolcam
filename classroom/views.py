from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

from classroom.models import Course, Category, Grade, Classes, Matiere

from classroom.forms import NewCourseForm
from authy.models import Profile


# Create your views here.

@login_required
def index(request):
    user = request.user
    course = Course.objects.filter(enrolled=user)

    context = {
        'course': course
    }
    return render(request, 'index.html', context)


def get_classes(request):
    classes = Classes.objects.all()

    context = {
        'classes': classes
    }
    return render(request, 'classroom/classes.html', context)



def get_matieres(request, class_slug):
    user = request.user.profile.user_statut
    classe = get_object_or_404(Classes, slug=class_slug)
    matieres = Matiere.objects.filter(classes=classe)
    if user != "6eme":
        return HttpResponseForbidden()
    else:
        user == "6eme"
    context = {
        'matieres': matieres
    }
    return render(request, 'classroom/matiere.html', context)


def Categories(request, matiere_slug):
    matiere = get_object_or_404(Matiere, slug=matiere_slug)
    categories = Category.objects.filter(matiere=matiere)

    context = {
        'categories': categories
    }
    return render(request, 'classroom/categories.html', context)


def CategoryCourses(request, cat_slug):
    category = get_object_or_404(Category, slug=cat_slug)
    courses = Course.objects.filter(category=category)

    context = {
        'category': category,
        'courses': courses,
    }
    return render(request, 'classroom/categorycourses.html', context)


def NewCourse(request):
    user = request.user
    if request.method == 'POST':
        form = NewCourseForm(request.POST, request.FILES)
        if form.is_valid():
            picture = form.cleaned_data.get('picture')
            title = form.cleaned_data.get('title')
            description = form.cleaned_data.get('description')
            category = form.cleaned_data.get('category')
            syllabus = form.cleaned_data.get('syllabus')
            Course.objects.create(picture=picture, title=title, description=description, category=category,
                                  syllabus=syllabus, user=user)
            return redirect('my-courses')
    else:
        form = NewCourseForm()

    context = {
        'form': form,
    }

    return render(request, 'classroom/newcourse.html', context)


@login_required
def CourseDetail(request, course_id):
    user = request.user
    course = get_object_or_404(Course, id=course_id)
    teacher_mode = False

    if user == course.user:
        teacher_mode = True

    context = {
        'course': course,
        'teacher_mode': teacher_mode,
    }

    return render(request, 'classroom/course.html', context)


@login_required
def Enroll(request, course_id):
    user = request.user
    course = get_object_or_404(Course, id=course_id)
    if user.profile.user_type == 'student':
        course.enrolled.add(user)
    context = {
        'course': course
    }
    return render(request, 'classroom/course.html', context)


@login_required
def DeleteCourse(request, course_id):
    user = request.user
    course = get_object_or_404(Course, id=course_id)

    if user != course.user:
        return HttpResponseForbidden()
    else:
        course.delete()
    return redirect('my-courses')


@login_required
def EditCourse(request, course_id):
    user = request.user
    course = get_object_or_404(Course, id=course_id)

    if user != course.user:
        return HttpResponseForbidden()

    else:
        if request.method == 'POST':
            form = NewCourseForm(request.POST, request.FILES, instance=course)
            if form.is_valid():
                course.picture = form.cleaned_data.get('picture')
                course.title = form.cleaned_data.get('title')
                course.description = form.cleaned_data.get('description')
                course.category = form.cleaned_data.get('category')
                course.syllabus = form.cleaned_data.get('syllabus')
                course.save()
                return redirect('my-courses')
        else:
            form = NewCourseForm(instance=course)

    context = {
        'form': form,
        'course': course
    }

    return render(request, 'classroom/editcourse.html', context)


def MyCourses(request):
    user = request.user
    courses = Course.objects.filter(user=user)

    context = {
        'courses': courses
    }

    return render(request, 'classroom/mycourses.html', context)


def Submissions(request, course_id):
    user = request.user
    course = get_object_or_404(Course, id=course_id)
    grades = Grade.objects.filter(course=course, submission__user=user)
    context = {
        'grades': grades,
        'course': course
    }
    return render(request, 'classroom/submissions.html', context)


def StudentSubmissions(request, course_id):
    user = request.user
    course = get_object_or_404(Course, id=course_id)
    grades = Grade.objects.filter(course=course)
    context = {
        'course': course,
        'grades': grades,
    }
    return render(request, 'classroom/studentgrades.html', context)


def GradeSubmission(request, course_id, grade_id):
    user = request.user
    course = get_object_or_404(Course, id=course_id)
    grade = get_object_or_404(Grade, id=grade_id)

    if user != course.user:
        return HttpResponseForbidden()
    else:
        if request.method == 'POST':
            points = request.POST.get('points')
            grade.points = points
            grade.status = 'graded'
            grade.graded_by = user
            grade.save()
            return redirect('student-submissions', course_id=course_id)
    context = {
        'course': course,
        'grade': grade,
    }

    return render(request, 'classroom/gradesubmission.html', context)
