from course.forms import BranchForm
from django.http.response import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from .models import Branch, Group, Student


def my_main_page(request):
    return render(request, 'course/my_page.html')


def branches_list(request):
    branches = Branch.objects.all()
    my_context = {'branches': branches}
    return render(request, 'course/branches-list.html', context=my_context)


def branch_detail(request, branch_id):
    branch = get_object_or_404(Branch, pk=branch_id)
    groups = Group.objects.filter(branch=branch)
    context = {'branch': branch, 'groups': groups}
    return render(request, 'course/branch-detail.html', context=context)


def branch_create(request):
    if request.method == "POST":
        form = BranchForm(request.POST)
        if form.is_valid():
            branch = form.save()
            return redirect('branch_detail', branch_id=branch.id)
    else:
        form = BranchForm()

    return render(request, 'course/branch-create.html', {'form': form})


def branch_edit(request, branch_id):
    # Получить объект или если не существует то вывести ошибку 404 
    branch = get_object_or_404(Branch, pk=branch_id)
    # Проверяем метод запроса, если POST то обновляем наши данные
    if request.method == "POST":
        # используем django form(BranchForm), для проверки полученных данных
        # Полученные данные находятся request.POST 
        form = BranchForm(request.POST, instance=branch)
        # Проверяем валидна(все ли данные введены правильно) ли наша форма
        if form.is_valid():
            # Сохраняем изменения в БД
            branch = form.save()
            # Перенаправляем пользователя к подробрной информации филиала
            return redirect('branch_detail', branch_id=branch.id)
    else:
        # Если не POST запрос, то открываем форму для редактирования
        form = BranchForm(instance=branch)
    
    return render(request, 'course/branch-edit.html', {'form': form})


def group_list(request):
    groups = Group.objects.all()
    my_context = {'groups': groups}
    return render(request, 'course/groups.html', context=my_context)


def group_detail(request, group_id):
    group = Group.objects.get(id=group_id)
    students = Student.objects.filter(group=group)
    context = {'group': group, 'students': students}
    return render(request, 'course/group-detail.html', context=context)


def student_list(request):
    students = Student.objects.all()
    my_context = {'students': students}
    return render(request, 'course/students.html', context=my_context)


def student_detail(request, student_id):
    student = Student.objects.get(id=student_id)
    my_context = {'student': student}
    return render(request, 'course/student-detail.html', context=my_context)
