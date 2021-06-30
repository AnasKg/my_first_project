from course import serializers
from course.serializers import BranchSerializer
import course
import random
from course.forms import BranchForm
from django.http.response import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from .models import Branch, Group, Student
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from django.contrib.auth.decorators import login_required

from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


def my_main_page(request):
    return render(request, 'course/my_page.html')


def branches_list(request):
    branches = Branch.objects.all()
    my_context = {'branches': branches, 'age': 20}
    return render(request, 'course/branches-list.html', context=my_context)


# Создание view на основе класса, используем готовый класс ListView
class BranchListView(ListView):
    # login_url = '/user/login/'
    # Указываем модель 
    model = Branch
    # Указываем шаблон(template)
    template_name = 'course/branches-list.html'
    # указываем название переменной в контексте(context), которая содержит список объектов
    # указанной модели, по умолчание значение context_object_name имеет 'object_list'
    context_object_name = 'branches'


def branch_detail(request, branch_id):
    branch = get_object_or_404(Branch, pk=branch_id)
    groups = Group.objects.filter(branch=branch)
    context = {'branch': branch, 'groups': groups}
    return render(request, 'course/branch-detail.html', context=context)


# Создание view на основе класса, используем готовый класс ListView
class BranchDetailView(DetailView):
    # Указываем модель
    model = Branch
    # Указываем шаблон(template)
    template_name = 'course/branch-detail.html'
    # указываем название переменной в контексте(context), которая содержит объект
    # указанной модели, по умолчание значение context_object_name имеет 'object'
    context_object_name = 'branch'
    # указываем название аргумента для id в url, по умолчанию pk
    pk_url_kwarg = 'branch_id'

    def get_context_data(self, **kwargs):
        # метод который получает context, который находится у родительского класса,
        # переопределяем(измененили, переделали) для добавления дополнительных конекстов
        context = super().get_context_data(**kwargs)
        # получаю группу данного филиала
        context['groups'] = Group.objects.filter(branch=self.object)
        return context

# декоратор login_required проверяет авторизован ли пользователь
@login_required
def branch_create(request):
    if request.method == "POST":
        form = BranchForm(request.POST, request.FILES)
        if form.is_valid():
            # commit=False чтоб не отправлять запрос в базу
            branch = form.save(commit=False)
            branch.creator = request.user
            branch.save()
            return redirect('branch_detail', branch_id=branch.id)
    else:
        form = BranchForm()

    return render(request, 'course/branch-create.html', {'form': form})


class BranchCreateView(CreateView):
    model = Branch
    fields = ['name', 'address', 'photo']
    template_name = 'course/branch-create.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.creator = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


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


class BranchUpdateView(LoginRequiredMixin, UpdateView):
    model = Branch
    fields = ['name', 'address', 'photo']
    template_name = 'course/branch-edit.html'
    pk_url_kwarg = 'branch_id'
    login_url = '/user/login/'


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
    courses = student.courses.all()
    my_context = {'student': student, 'courses': courses}
    return render(request, 'course/student-detail.html', context=my_context)


class StudentDetailView(DetailView):
    model = Student
    template_name = 'course/student-detail.html'
    context_object_name = 'student'
    pk_url_kwarg = 'student_id'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        student = self.object
        courses = student.courses.all()
        context['courses'] = courses
        return context




def student_random(request):
    students = Student.objects.all()
    random_student = random.choice(students)
    my_context = {'student': random_student}
    return render(request, 'course/student-detail.html', context=my_context)
