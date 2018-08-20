from django.shortcuts import render

# Create your views here.

from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect

def login(request):
    #return HttpResponse("请登录")
    #f = open('templates/login.html','r',encoding='utf-8')
    #data = f.read()
    #f.close()
    #return HttpResponse(data)
    error_msg = ''
    if request.method == "POST":
        user = request.POST.get('user',None)
        pwd = request.POST.get('pwd', None)
        if user == "root" and pwd =="123":
            return redirect('/home')
        else:
            error_msg = "用户名或密码错误！"
    return render(request ,'login.html',{'error_msg':error_msg})

def home(request):
    return render(request,'home.html')

def register(request):
    if request.method == 'GET':
        return render(request,'register.html')
    elif request.method == 'POST':
        u = request.POST.get('user')
        p = request.POST.get('pwd')
        v = request.POST.get('gender')
        if u =='root' and p =='123':
            return render(request,'home.html')
    else:
        return redirect('/regisrter')

