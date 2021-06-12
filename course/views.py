from django.shortcuts import render
from django.http import HttpResponse
from .models import Branch, Group, Student


def my_main_page(request):
    my_context = {
        'name': 'ITC',
        'my_list': [1,2,3,4,5]
    }
    return render(request, 'course/my_page.html', context=my_context)


def branches_list(request):
    branches = Branch.objects.all()
    my_context = {'branches': branches}
    return render(request, 'course/branches-list.html', context=my_context)


def branch_detail(request, branch_id):
    branch = Branch.objects.get(id=branch_id)
    groups = Group.objects.filter(branch=branch)
    context = {'branch': branch, 'groups': groups}
    return render(request, 'course/branch-detail.html', context=context)


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
