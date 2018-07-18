from django.shortcuts import render
from .models import Category,Permission,Employee
from django.shortcuts import redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

@login_required(login_url='/logins/')
def index(request):
    return render(request,'permission/index.html')

def logins(request):
    return render(request,'permission/login.html')

def logouts(request):
    logout(request)
    return redirect('/')

def next_view(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('/')
    else:
        return redirect('/logins/')

def category_list(request):
    permission = True;
    if not request.user.username.endswith('admin'):
        permission = False;
    if request.method == 'POST':
        category_name = request.POST.get('category_name')
        category_note = request.POST.get('category_note')
        categorys = Category(name=category_name,note=category_note)
        categorys.save()
        return redirect('/category/')
    category = Category.objects.all()
    return render(request,'permission/category_list.html',{'category':category,'permission':permission})

@login_required(login_url='/logins/')
def input_category(request):
    return render(request,'permission/input_category.html')

def permission_list(request):
    if request.method == 'POST':
        employee = Employee.objects.get(number=request.POST.get('employee'))

        start = request.POST.get('start_date')
        end = request.POST.get('end_date')

        category = Category.objects.get(name=request.POST.get('category'))

        reason = request.POST.get('reason')
        permission = Permission(employee=employee,start=start,end=end,category=category,reason=reason)
        permission.save()
        return redirect('/permission/')

    permission = Permission.objects.all()
    return render(request,'permission/permission_list.html',{'permission':permission})

def input_permission(request):
    employee = Employee.objects.all()
    category = Category.objects.all()

    return render(request,'permission/input_permission.html',{'category':category,'employee':employee})

def delete_permission(request,id):
    del_permission = Permission.objects.get(id=id)
    del_permission.delete()
    return redirect('/permission/')