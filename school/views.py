from django.shortcuts import render, get_object_or_404, redirect

# models
from .models import *

# forms
from .forms import *
# others
from django.contrib.auth.decorators import login_required
from .decorators import *


# Create your views here.

def school_view(request, *args, **kwargs):
    grades = Grade.objects.all()
    context = {
        'grades': grades,
    }
    return render(request, 'pages/school.html', context)


# chapters

def chapters_list_view(request, grade_name, *args, **kwargs):
    grade_obj = get_object_or_404(Grade, name=grade_name)
    chapters = grade_obj.chapter_set.all()
    context = {
        'chapters': chapters,
        'grade': grade_obj
    }
    return render(request, 'school/chapters-list.html', context)


# numericals

@login_required
@admin_only
def numerical_create_view(request, grade_name, chapter_name, *args, **kwargs):
    grade_obj = get_object_or_404(Grade, name=grade_name)
    chapter_obj = get_object_or_404(Chapter, name=chapter_name)
    form = NumericalForm(request.POST or None, initial={'grade': grade_obj, 'chapter': chapter_obj})
    if form.is_valid():
        form.save()
        return redirect('../')
    context = {
        'form': form
    }
    return render(request, 'school/numerical-form.html', context)


@admin_only
@login_required
def numerical_edit_view(request, numerical_id, *args, **kwargs):
    numerical_obj = get_object_or_404(Numerical, id=numerical_id)
    form = NumericalForm(request.POST or None, instance=numerical_obj)
    if form.is_valid():
        form.save()
        return redirect('school:numericals-list')
    context = {
        'form': form,
    }
    return render(request, 'school/numerical-form.html', context)


@admin_only
@login_required
def numerical_delete_view(request, numerical_id, *args, **kwargs):
    numerical_obj = get_object_or_404(Numerical, id=numerical_id)
    if request.method == 'POST':
        numerical_obj.delete()
        return redirect('.../')
    context = {
        'delete_page': True
    }
    return render(request, 'school/numerical-form.html', context)


def numericals_list_view(request, chapter_name, *args, **kwargs):
    chapter_obj = get_object_or_404(Chapter, name=chapter_name)
    numericals = chapter_obj.numerical_set.all()
    grade_obj = chapter_obj.grade
    user = request.user
    user_group = user.groups.filter(name='admin')
    is_admin = None
    if user_group.exists():
        is_admin = True
    context = {
        'chapter': chapter_obj,
        'grade': grade_obj,
        'numericals': numericals,
        'is_admin': is_admin
    }
    return render(request, 'school/numericals-list.html', context)
